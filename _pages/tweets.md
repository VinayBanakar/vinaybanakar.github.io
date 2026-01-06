---
layout: page
permalink: /tweets/
title: Unposted Tweets
---
<style>
  body {
    background-color: #fafaf8;
  }
  .post-title {
    display: block !important;
    text-align: center;
    width: 100%;
  }
  .tweets-list {
    list-style: none;
    padding: 0;
    margin: 28px auto;
    max-width: 720px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .tweets-list li {
    background: #ffffff;
    border: 1px solid #e5e1d7;
    border-radius: 12px 14px 16px 12px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.03);
    padding: 14px 16px 16px;
    position: relative;
    transition: transform 120ms ease, box-shadow 120ms ease, border-color 120ms ease;
  }
  .tweets-list li:nth-child(3n) {
    border-radius: 18px 10px 14px 24px;
  }
  .tweets-list li:nth-child(4n) {
    border-radius: 10px 18px 22px 12px;
  }
  .tweets-list li:nth-child(5n) {
    border-radius: 20px 14px 12px 14px;
  }
  .tweets-list li:hover {
    transform: translateY(-1px);
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.05);
    border-color: #d8d2c3;
  }
  .tweets-list li em {
    display: block;
    font-style: normal;
    font-weight: 600;
    font-size: 0.82rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: #7f7a70;
    margin: 0 0 6px 0;
  }
  .tweets-list li > a[href^="#"] {
    position: absolute;
    top: 10px;
    right: 12px;
    text-decoration: none;
    color: #b1aa9c;
    font-weight: 700;
    font-size: 0.95rem;
    opacity: 0;
    transition: opacity 120ms ease, color 120ms ease;
  }
  .tweets-list li:hover > a[href^="#"] {
    opacity: 1;
    color: #7f7a70;
  }
  .tweets-list li {
    font-size: 1rem;
    line-height: 1.6;
    color: #1f1c17;
  }
</style>

<p style="text-align: center;">If you’re nodding or fuming, send me an <a href="mailto:vin@cs.wisc.edu">email</a>. I like both :)</p>

- <a id="jan-6-2026-a"></a> [#](#jan-6-2026-a) *Jan 6 2026* AI coding agents are great for avoiding atachment to ideas. The longer you spend time coding something, the more attached you get to the implementation. The coding agents could help fail faster, making failures more acceptable.
- <a id="jan-6-2026-b"></a> [#](#jan-6-2026-b) *Jan 6 2026* In biology, there are two ways to explain something. Mechanical or evolutionary. Evolutionary understanding is deeper. We often ignore the "evoluationary" pressures that shaped system designs of computers. Should one have apply this lens when designing systems?
- <a id="jan-1-2026"></a> [#](#jan-1-2026) *Jan 1 2026* There are more royalty today than ever before in human history. Yet, we think of royalty as a thing of the past. Royalty have the luxury of ignorance of the system around them.
- <a id="dec-27-2025-a"></a> [#](#dec-27-2025-a) *Dec 27 2025* LLMs model language about reality and not the reality itself.
- <a id="dec-27-2025-b"></a> [#](#dec-27-2025-b) *Dec 27 2025* If humans have been shaped so thoroughly by language that most never access raw experience (birth, death, awe -- something that can't be labeled) anyway, is the difference between human cognition and LLM cognition smaller than we'd like to believe?
{: .tweets-list}
