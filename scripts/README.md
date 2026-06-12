# Scripts

Two small Python tools I wrote to collect YouTube material programmatically via the **[Supadata](https://supadata.ai) API** (free tier: 100 credits/month, `x-api-key` auth, rate-limited to 5 requests / 10 seconds).

## Setup

```bash
pip3 install requests
export SUPADATA_API_KEY="your_key_here"   # never hard-coded; read from the environment
```

The key is read from an environment variable on purpose — it is never committed (see `.gitignore`).

## `list_latest_videos.py`

Lists each channel's most recent uploads (title + date + URL) so I could pick the strongest, most *recent* videos rather than guessing. It calls Supadata's `youtube/channel/videos` endpoint (returns latest-first video IDs), then looks up each video's metadata, and writes a summary to `latest-videos-found.md` (gitignored — it's a scratch file, not a deliverable).

```bash
python3 scripts/list_latest_videos.py
```

I used this to confirm which channels were actually active before collecting — which is how I caught that two experts' channels were stale (newest upload 5–9 months old) and moved their collection to LinkedIn.

## `fetch_youtube_transcripts.py`

Fetches transcripts for a chosen list of videos via Supadata's `youtube/transcript` endpoint and saves each as Markdown under `research/youtube-transcripts/<author>/`.

```bash
python3 scripts/fetch_youtube_transcripts.py
```

Notes on the implementation:
- The transcript API returns **segments** (`{text, offset, duration}`), which the script groups into ~30-second paragraphs prefixed with a `[mm:ss]` timestamp for readability.
- Calls use the `videoId` parameter (the combo I verified works) and a 2.2s delay between requests to stay under the rate limit.
- A small `TITLES` map gives each output file a human-readable filename.
- After the script runs, I add a **"Key points" synthesis** to the top of each transcript by hand — clearly labelled as my own notes, with the transcript (lightly corrected for obvious transcription errors) preserved below as the source.

## Why two collection methods

YouTube transcripts are collected via API (above). **LinkedIn posts are collected through the browser** — navigating each author's public activity feed in a logged-in session and extracting the post text directly from the page. This is a lightweight, assisted approach rather than bulk automated scraping, which LinkedIn's terms prohibit (and which is why there's no LinkedIn scraper script here).
