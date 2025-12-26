#!/usr/bin/env python3
"""
Generate a Jekyll _data JSON file from a public Google Photos *shared album* link.

- Input:  Google Photos shared album URL (photos.app.goo.gl/...)
- Output: JSON like:
  {
    "album_url": "...",
    "generated_at": "...",
    "photos": [
      {"id": "...", "thumb": "...", "full": "...", "width": 1234, "height": 567},
      ...
    ]
  }

This is an unofficial scraper (Google Photos has no official "grid embed" for shared albums).

# To force update the photos grid
python3 gphotos_album_to_json.py \ 
  "https://photos.app.goo.gl/h2bCHWHXuAM6n65J7" \
  "_data/my_album.json"
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from typing import Any, Dict, List, Optional, Set, Tuple
from urllib.request import Request, urlopen


# Matches AF_initDataCallback blobs that contain JSON-ish data we can parse.
AF_RE = re.compile(
    r"AF_initDataCallback\(\{.*?data:(.*?),\s*sideChannel:.*?\}\);",
    re.DOTALL,
)

LH3_HOST_SNIPPET = "lh3.googleusercontent.com"

# Common end-of-url sizing tokens seen on lh3 URLs (not exhaustive, but helpful).
# We'll strip any trailing "=w123-h456-c" or "=s123" etc and then apply our own "=wNNNN".
SIZE_SUFFIX_RE = re.compile(r"=[^/?#]*$")


def fetch_html(url: str, timeout: int = 30) -> str:
    req = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; JekyllGalleryBot/1.0)",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    return data.decode("utf-8", errors="replace")


def try_parse_callback_data(html: str) -> List[Any]:
    """Return a list of parsed JSON 'data' blobs from AF_initDataCallback."""
    blobs: List[Any] = []
    for m in AF_RE.finditer(html):
        raw = m.group(1).strip()
        try:
            blobs.append(json.loads(raw))
        except Exception:
            # Some blobs may not be valid JSON; ignore and keep going.
            continue
    return blobs


def make_sized(url: str, width: int) -> str:
    """
    Make a "sized" lh3 URL by removing any trailing size suffix and appending '=w{width}'.
    This keeps thumbnails light and makes the lightbox view sharp.

    Example:
      https://lh3.../ABC=w400-h300-c  -> https://lh3.../ABC=w2400
    """
    # Remove the final "=..." token if present (common in lh3 image links)
    base = SIZE_SUFFIX_RE.sub("", url)
    return f"{base}=w{width}"


def extract_images(obj: Any, thumb_w: int, full_w: int) -> List[Dict[str, Any]]:
    """
    Recursively find image-like entries.
    Looks for lists like:
      [<id:str>, [<url:str>, <width:int>, <height:int>, ...], ...]
    where url contains lh3.googleusercontent.com
    """
    found: List[Dict[str, Any]] = []
    seen: Set[Tuple[Optional[str], str]] = set()

    def walk(x: Any) -> None:
        if isinstance(x, list):
            # Candidate match
            if (
                len(x) >= 2
                and isinstance(x[0], str)
                and isinstance(x[1], list)
                and len(x[1]) >= 1
                and isinstance(x[1][0], str)
                and LH3_HOST_SNIPPET in x[1][0]
            ):
                img_id = x[0]
                url = x[1][0]

                width = (
                    int(x[1][1])
                    if len(x[1]) > 1 and isinstance(x[1][1], (int, float))
                    else None
                )
                height = (
                    int(x[1][2])
                    if len(x[1]) > 2 and isinstance(x[1][2], (int, float))
                    else None
                )

                key = (img_id, url)
                if key not in seen:
                    seen.add(key)
                    found.append(
                        {
                            "id": img_id,
                            # use our controlled sizes for better UX
                            "thumb": make_sized(url, thumb_w),
                            "full": make_sized(url, full_w),
                            # keep original-ish dims if available
                            "width": width,
                            "height": height,
                            # keep original URL too (sometimes handy)
                            "url": url,
                        }
                    )

            for item in x:
                walk(item)

        elif isinstance(x, dict):
            for v in x.values():
                walk(v)

    walk(obj)
    return found


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Scrape a public Google Photos shared album and write a Jekyll-friendly JSON file."
    )
    ap.add_argument("album_url", help="Google Photos shared album URL (photos.app.goo.gl/...)")
    ap.add_argument("output_json", help="Output path, e.g. _data/my_album.json")
    ap.add_argument("--timeout", type=int, default=30, help="HTTP timeout seconds (default: 30)")
    ap.add_argument("--thumb", type=int, default=600, help="Thumbnail width (default: 600)")
    ap.add_argument("--full", type=int, default=2400, help="Full view width (default: 2400)")
    args = ap.parse_args()

    html = fetch_html(args.album_url, timeout=args.timeout)
    blobs = try_parse_callback_data(html)

    if not blobs:
        print(
            "ERROR: Could not find any parseable AF_initDataCallback data in the album page.\n"
            "       Make sure the album link is publicly accessible (link sharing on).",
            file=sys.stderr,
        )
        return 2

    photos: List[Dict[str, Any]] = []
    for b in blobs:
        photos.extend(extract_images(b, thumb_w=args.thumb, full_w=args.full))

    # De-dupe by original URL while preserving order
    seen_urls: Set[str] = set()
    deduped: List[Dict[str, Any]] = []
    for p in photos:
        u = p.get("url")
        if isinstance(u, str) and u not in seen_urls:
            seen_urls.add(u)
            deduped.append(p)

    out = {
        "album_url": args.album_url,
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "photos": deduped,
    }

    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(deduped)} photos to {args.output_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())