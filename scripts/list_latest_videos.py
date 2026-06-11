#!/usr/bin/env python3
"""
list_latest_videos.py
List each channel's most recent videos (title + date + URL) using the Supadata API,
so we can pick the strongest, most recent ones for transcript collection.

WHAT IT DOES
  - For each channel below, asks Supadata for the latest video IDs (newest first)
  - Looks up each video's title + upload date
  - Writes a summary to ../latest-videos-found.md  (this file is gitignored)

SETUP
  export SUPADATA_API_KEY="your_key_here"
  pip3 install requests
  python3 scripts/list_latest_videos.py

Note on credits: free tier = 100 credits/month. This run uses roughly
(1 + PER_CHANNEL) calls per channel. With PER_CHANNEL=6 and 5 channels that's ~35.
Run it once; then we'll spend the rest on transcripts.
"""

import os
import sys
import time
import pathlib
import requests

API_KEY = os.environ.get("SUPADATA_API_KEY")
BASE = "https://api.supadata.ai/v1/youtube"
PER_CHANNEL = 6  # how many recent videos to list per channel

OUT_FILE = pathlib.Path(__file__).resolve().parent.parent / "latest-videos-found.md"

# author_key -> channel handle/URL (Supadata accepts handle, URL, or channel ID)
CHANNELS = {
    "Jesse Cunningham": "https://www.youtube.com/@jessecunninghamv",
    "Koray Tuğberk Gübür": "https://www.youtube.com/@TopicalAuthority",
    "Julian Goldie": "https://www.youtube.com/@JulianGoldieSEO",
    "Gael Breton (Authority Hacker)": "https://www.youtube.com/@AuthorityHacker",
    "Aleyda Solis (Crawling Mondays)": "https://www.youtube.com/c/crawlingmondaysbyaleyda",
}


def get(url, params):
    r = requests.get(url, params=params, headers={"x-api-key": API_KEY}, timeout=60)
    r.raise_for_status()
    return r.json()


def latest_video_ids(channel_id, limit):
    data = get(f"{BASE}/channel/videos", {"id": channel_id, "type": "video", "limit": limit})
    # response: {"videoIds": [...], "shortIds": [...], "liveIds": [...]}
    ids = data.get("videoIds") or data.get("videoIDs") or []
    return ids[:limit]


def video_meta(video_id):
    data = get(f"{BASE}/video", {"id": video_id})
    title = data.get("title") or "(no title)"
    # date field name can vary; try a few
    date = (data.get("uploadDate") or data.get("publishedDate")
            or data.get("published") or data.get("date") or "")
    duration = data.get("duration") or ""
    return title, str(date)[:10], duration


def main():
    if not API_KEY:
        sys.exit('ERROR: run  export SUPADATA_API_KEY="your_key"  first')

    lines = ["# Latest videos found (newest first)\n",
             f"_Generated {time.strftime('%Y-%m-%d %H:%M')}_\n"]
    for author, channel in CHANNELS.items():
        print(f"\n=== {author} ===")
        lines.append(f"\n## {author}\nChannel: {channel}\n")
        try:
            ids = latest_video_ids(channel, PER_CHANNEL)
        except Exception as e:  # noqa: BLE001
            print(f"  ! channel list failed: {e}")
            lines.append(f"- (could not list videos: {e})\n")
            continue

        for vid in ids:
            url = f"https://www.youtube.com/watch?v={vid}"
            try:
                title, date, dur = video_meta(vid)
            except Exception as e:  # noqa: BLE001
                title, date, dur = "(metadata failed)", "", ""
            print(f"  {date}  {title}")
            lines.append(f"- **{date}** — {title}  \n  {url}\n")
            time.sleep(2.2)  # stay under rate limit

    OUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nSaved -> {OUT_FILE}")


if __name__ == "__main__":
    main()
