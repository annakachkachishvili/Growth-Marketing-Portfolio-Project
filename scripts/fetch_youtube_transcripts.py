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
        # "https://www.youtube.com/watch?v=XXXXXXXXXXX",
    ],
    "koray-tugberk-gubur": [
        # "https://www.youtube.com/watch?v=XXXXXXXXXXX",
    ],
    "julian-goldie": [
        # "https://www.youtube.com/watch?v=XXXXXXXXXXX",
    ],
    "gael-breton-authority-hacker": [
        # "https://www.youtube.com/watch?v=XXXXXXXXXXX",
    ],
    "aleyda-solis-crawling-mondays": [
        # "https://www.youtube.com/watch?v=XXXXXXXXXXX",
    ],
}


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", text)[:80] or "video"


def fetch_transcript(video_url: str) -> dict:
    """Call Supadata and return {'text': ..., 'title': ...}."""
    resp = requests.get(
        API_URL,
        params={"url": video_url, "text": "true"},   # text=true => plain text
        headers={"x-api-key": API_KEY},
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()

    # Supadata returns the plain transcript in "content" when text=true.
    # Fall back to joining segments if the shape is different.
    text = data.get("content")
    if not text and isinstance(data.get("transcript"), list):
        text = " ".join(seg.get("text", "") for seg in data["transcript"])
    if not text and isinstance(data.get("content"), list):
        text = " ".join(seg.get("text", "") for seg in data["content"])
    return {"text": text or "", "title": data.get("title", "")}


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

            if not result["text"]:
                print(f"  ! No transcript returned for {url}")
                continue

            title = result["title"] or url.split("=")[-1]
            fname = author_dir / f"{slugify(title)}.md"
            fname.write_text(
                f"# {title}\n\n"
                f"- **Author:** {author}\n"
                f"- **Source:** {url}\n"
                f"- **Collected:** {time.strftime('%Y-%m-%d')}\n"
                f"- **Method:** Supadata YouTube Transcript API\n\n"
                f"---\n\n{result['text']}\n",
                encoding="utf-8",
            )
            done += 1
            print(f"  ✓ {author}: {fname.name}")
            time.sleep(2.2)  # stay under 5 requests / 10 seconds

    print(f"\nDone. Saved {done}/{total} transcript(s) to {OUT_DIR}")


if __name__ == "__main__":
    main()
