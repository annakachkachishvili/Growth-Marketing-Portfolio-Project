#!/usr/bin/env python3
"""
fetch_youtube_transcripts.py
Collect YouTube transcripts for the AI-SEO research project using the Supadata API.

WHAT IT DOES
  - Reads the VIDEOS list below (author -> list of YouTube video URLs)
  - Calls the Supadata transcript API for each video
  - Saves each transcript as Markdown in ../research/youtube-transcripts/<author>/

SETUP
  1. Get a free Supadata API key: https://supadata.ai  (free tier = 100 credits/month, no card)
  2. Put your key in an environment variable so it's never hard-coded:
        macOS/Linux:   export SUPADATA_API_KEY="your_key_here"
  3. Install the one dependency:
        pip3 install requests
  4. Fill in the VIDEOS list with the real video URLs you picked (last ~3 months).
  5. Run it:
        python3 fetch_youtube_transcripts.py

Docs: https://docs.supadata.ai/youtube/get-transcript
Rate limit: 5 requests / 10 seconds (the script sleeps to stay under it).
"""

import os
import re
import sys
import time
import pathlib
import requests

API_KEY = os.environ.get("SUPADATA_API_KEY")
API_URL = "https://api.supadata.ai/v1/youtube/transcript"

# Output goes into the repo's research folder (one level up from /scripts).
OUT_DIR = pathlib.Path(__file__).resolve().parent.parent / "research" / "youtube-transcripts"

# ---------------------------------------------------------------------------
# FILL THIS IN. For each author, paste the YouTube URLs of the recent videos
# (last ~3 months) you want transcripts for. 3-5 strong videos each is plenty.
# ---------------------------------------------------------------------------
VIDEOS = {
    "jesse-cunningham": [
        "https://www.youtube.com/watch?v=O9Ys-6ArGVs",  # Ranking on Google AI Overviews & ChatGPT on Autopilot
        "https://www.youtube.com/watch?v=qX0Hme7J9P4",  # The 5-AI System to Make Money w/ SEO Online
        "https://www.youtube.com/watch?v=XxTY7LFEliQ",  # Using ChatGPT "SUPER" Mode (API grounded data)
    ],
    "julian-goldie": [
        "https://www.youtube.com/watch?v=YSYjs3L3MMU",  # How I Run My Entire SEO From One Dashboard
        "https://www.youtube.com/watch?v=nTyLa_zavfs",  # Get ChatGPT to Recommend Any Product Over Competitors (GEO)
        "https://www.youtube.com/watch?v=8NAjD6HcHzk",  # How to Rank #1 with Claude Fable 5 AI SEO
    ],
    # Koray, Aleyda, and Gael are collected from LinkedIn instead — their YouTube
    # channels are stale (Koray 9mo, Aleyda 5mo) or off-topic for AI-SEO content.
}

# Nice filenames (the transcript API doesn't return titles).
TITLES = {
    "O9Ys-6ArGVs": "Ranking on Google AI Overviews and ChatGPT on Autopilot",
    "qX0Hme7J9P4": "The 5-AI System to Make Money with SEO Online",
    "XxTY7LFEliQ": "Using ChatGPT SUPER Mode with API Grounded Data",
    "YSYjs3L3MMU": "How I Run My Entire SEO From One Dashboard",
    "nTyLa_zavfs": "Get ChatGPT to Recommend Any Product Over Competitors",
    "8NAjD6HcHzk": "How to Rank Number 1 with Claude Fable 5 AI SEO",
}


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", text)[:80] or "video"


def extract_video_id(url: str) -> str:
    m = re.search(r"[?&]v=([\w-]+)", url) or re.search(r"youtu\.be/([\w-]+)", url)
    return m.group(1) if m else url


def fetch_transcript(video_url: str) -> dict:
    """Call Supadata and return {'text': ..., 'title': ...}."""
    vid = extract_video_id(video_url)
    resp = requests.get(
        API_URL,
        params={"videoId": vid},   # proven combo; do NOT add text=true (causes 503)
        headers={"x-api-key": API_KEY},
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()

    # Supadata returns "content" as a list of {text, offset(ms), duration} segments.
    content = data.get("content")
    segments = content if isinstance(content, list) else []
    return {"segments": segments, "title": data.get("title", "")}


def _mmss(ms: int) -> str:
    s = int(ms / 1000)
    return f"{s // 60:02d}:{s % 60:02d}"


def format_transcript(segments: list, group_seconds: int = 30) -> str:
    """Group caption segments into ~group_seconds paragraphs, each prefixed with a timestamp."""
    paragraphs = []
    cur, cur_start = [], None
    for seg in segments:
        off = seg.get("offset", 0)
        if cur_start is None:
            cur_start = off
        cur.append((seg.get("text", "") or "").strip())
        if off - cur_start >= group_seconds * 1000:
            paragraphs.append((cur_start, " ".join(t for t in cur if t)))
            cur, cur_start = [], None
    if cur:
        paragraphs.append((cur_start or 0, " ".join(t for t in cur if t)))
    return "\n\n".join(f"**[{_mmss(start)}]** {text}" for start, text in paragraphs)


def main():
    if not API_KEY:
        sys.exit("ERROR: set your key first ->  export SUPADATA_API_KEY=\"your_key\"")

    total = sum(len(v) for v in VIDEOS.values())
    if total == 0:
        sys.exit("Nothing to do: add some video URLs to the VIDEOS list first.")

    print(f"Fetching {total} transcript(s)...\n")
    done = 0
    for author, urls in VIDEOS.items():
        if not urls:
            continue
        author_dir = OUT_DIR / author
        author_dir.mkdir(parents=True, exist_ok=True)

        for url in urls:
            try:
                result = fetch_transcript(url)
            except Exception as e:  # noqa: BLE001
                print(f"  ! FAILED {url}: {e}")
                continue

            if not result["segments"]:
                print(f"  ! No transcript returned for {url}")
                continue

            title = TITLES.get(extract_video_id(url)) or result["title"] or url.split("=")[-1]
            body = format_transcript(result["segments"])
            fname = author_dir / f"{slugify(title)}.md"
            fname.write_text(
                f"# {title}\n\n"
                f"- **Author:** {author}\n"
                f"- **Source:** {url}\n"
                f"- **Collected:** {time.strftime('%Y-%m-%d')}\n"
                f"- **Method:** Supadata YouTube Transcript API\n"
                f"- *Auto-generated transcript, formatted into timestamped paragraphs for readability. "
                f"Transcription artifacts (e.g. \"GBT\" for GPT) are verbatim from the auto-captions.*\n\n"
                f"---\n\n"
                f"## Transcript\n\n{body}\n",
                encoding="utf-8",
            )
            done += 1
            print(f"  ✓ {author}: {fname.name}")
            time.sleep(2.2)  # stay under 5 requests / 10 seconds

    print(f"\nDone. Saved {done}/{total} transcript(s) to {OUT_DIR}")


if __name__ == "__main__":
    main()
