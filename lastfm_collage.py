#!/usr/bin/env python3
import math
import os
import sys
from io import BytesIO
from typing import List, Optional

import requests
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

API_URL = "https://ws.audioscrobbler.com/2.0/"
OUTPUT_PATH = "assets/img/lastfm-collage.jpg"
WIDTH = 1200
HEIGHT = 1200
TILE_SIZE = 300
PERIOD = "7day"
LAYOUT = "topleft"
JPEG_QUALITY = 100
TIMEOUT_SECS = 20


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required env var: {name}")
    return value


def fetch_top_albums(
    session: requests.Session,
    user: str,
    api_key: str,
    period: str,
    needed: int,
) -> list:
    albums = []
    page = 1
    page_size = min(1000, max(50, int(needed * 1.5)))
    while len(albums) < needed:
        params = {
            "method": "user.gettopalbums",
            "format": "json",
            "user": user,
            "api_key": api_key,
            "period": period,
            "limit": page_size,
            "page": page,
        }
        response = session.get(API_URL, params=params, timeout=TIMEOUT_SECS)
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            raise RuntimeError(f"Last.fm error {data.get('error')}: {data.get('message')}")

        payload = data.get("topalbums", {})
        albums.extend(payload.get("album", []))
        attr = payload.get("@attr", {})
        try:
            total_pages = int(attr.get("totalPages", 0))
        except (TypeError, ValueError):
            total_pages = 0

        if total_pages and page >= total_pages:
            break
        page += 1

    return albums


def pick_image_url(album: dict) -> str:
    for image in reversed(album.get("image", [])):
        url = image.get("#text")
        if url:
            return url
    return ""


def download_tile(session: requests.Session, url: str) -> Optional[Image.Image]:
    try:
        response = session.get(url, timeout=TIMEOUT_SECS)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        return img.convert("RGB").resize((TILE_SIZE, TILE_SIZE), resample=Image.LANCZOS)
    except Exception:
        return None


def build_collage(tiles: List[Image.Image], rows: int, cols: int) -> Image.Image:
    canvas = Image.new("RGB", (WIDTH, HEIGHT))
    x_offset = int(-(TILE_SIZE * cols - WIDTH) / 2)
    y_offset = int(-(TILE_SIZE * rows - HEIGHT) / 2)

    if LAYOUT != "topleft":
        raise RuntimeError(f"Unsupported layout: {LAYOUT}")

    i = 0
    for row in range(rows):
        for col in range(cols):
            canvas.paste(tiles[i], (x_offset + col * TILE_SIZE, y_offset + row * TILE_SIZE))
            i += 1

    return canvas


def main() -> int:
    user = require_env("LASTFM_USER")
    api_key = require_env("LASTFM_API_KEY")

    cols = math.ceil(WIDTH / TILE_SIZE)
    rows = math.ceil(HEIGHT / TILE_SIZE)
    needed = rows * cols

    session = requests.Session()
    session.headers.update({"User-Agent": "vinaybanakar-lastfm-collage/1.0"})

    albums = fetch_top_albums(session, user, api_key, PERIOD, needed)
    if len(albums) < needed:
        raise RuntimeError("Not enough albums returned to fill the collage")

    tiles: List[Image.Image] = []
    for album in albums:
        if len(tiles) >= needed:
            break
        url = pick_image_url(album)
        if not url:
            continue
        tile = download_tile(session, url)
        if tile is None:
            continue
        tiles.append(tile)

    if len(tiles) < needed:
        raise RuntimeError("Not enough album images could be downloaded")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    collage = build_collage(tiles, rows, cols)
    collage.save(OUTPUT_PATH, "JPEG", quality=JPEG_QUALITY, subsampling=0)
    print(f"Saved collage to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
