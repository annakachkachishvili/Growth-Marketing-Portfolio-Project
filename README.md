# Growth Marketing Portfolio Project

## Overview

This repository documents the setup process for the required project environment using Cursor, GitHub, Claude Code, and Codex.

The main goal of this stage was not just completing installation steps, but making sure the environment, integrations, and onboarding flows were actually working before moving further into the workflow.

> This README covers **Step 1 — Setup** (below) and **Step 2 — Research Project: AI-Powered SEO Content Production** (further down).

---

## Tools Installed

* Cursor IDE
* GitHub
* Claude Code extension
* Codex extension

---

## Steps Completed

* Installed Cursor
* Connected GitHub to Cursor
* Installed Claude Code and Codex extensions
* Tested onboarding and authentication flows
* Created a public GitHub repository
* Created and documented this README

---

## Issues Encountered

### GitHub Integration

Cursor temporarily returned a rate-limit/authentication issue during GitHub connection. After checking that the issue was platform-side rather than account-related, I retried the connection and confirmed successful integration.

### Claude Code Authentication

Claude Code installed successfully, but authentication required a Claude Pro/Max subscription or API access. Instead of treating it as a blocker, I documented the limitation and continued with the remaining setup.

### Unexpected Hardware Issue

Near the end of the process, my laptop became unusable before the final submission stage. Since the setup work had already been completed earlier, I switched to another machine, logged back into my accounts, and finished the repository/documentation work there instead of restarting the process from scratch.

---

## Notes

I approached the setup in layers rather than rushing directly into repository work. First, I got familiar with the tools, workflows, onboarding flows, and overall environment (YouTube, ChatGPT), configured and tested the environment itself, then moved to documentation once the workflow was stable.

This process was also a good reminder that most setup problems are easier to solve once you isolate whether the issue is:
* local,
* account-related,
* or platform-side.

---
---

# Step 2 — Research Project: AI-Powered SEO Content Production

## Why this topic

I chose **AI-powered SEO content production** out of the eight options. 100Hires is an AI ATS, and businesses like it grow primarily through SEO content — blog articles, comparison pages, alternative pages, and landing pages. The role itself centers on producing that content with AI tools. So this topic is not adjacent to the business; it *is* the growth engine.

I deliberately chose the most business-aligned and most demanding of the eight options rather than the easiest one, because it is also the highest-leverage thing to learn for this work.

## Who I collected, and why these experts

I selected **10 practitioners** — people who actually run agencies, build tools, or lead in-house content, not names pulled from a "top 10" listicle. I filtered for three things:

1. **Genuine practitioner proof** — they show their own results (dashboards, case studies, live experiments).
2. **Close alignment** to AI-powered SEO *content production* specifically.
3. **Collectability** — each has an active, official LinkedIn or YouTube presence I can actually collect from.

All three archetypes from the brief are represented (LinkedIn authors, YouTube creators, podcast hosts), and together they span the full production pipeline: production at scale, content optimization, frameworks, workflows, and content quality/judgment.

The full annotated list with links is in **[`/research/sources.md`](research/sources.md)**.

| #  | Expert           | Collect from        | Focus                                       |
|----|------------------|---------------------|---------------------------------------------|
| 1  | Jake Ward        | LinkedIn            | Programmatic SEO + AI content at scale      |
| 2  | Jesse Cunningham | YouTube             | AI content production at scale              |
| 3  | Kevin Indig      | LinkedIn            | AI-search strategy & visibility measurement |
| 4  | Ryan Law         | LinkedIn            | AI content process + Claude Code            |
| 5  | Koray T. Gübür   | LinkedIn            | Semantic SEO + AI agents                    |
| 6  | Julian Goldie    | YouTube             | AI content & automation workflows           |
| 7  | Gael Breton      | LinkedIn            | AI workflows (and a healthy skeptic)        |
| 8  | Steve Toth       | LinkedIn            | Content frameworks + AI search              |
| 9  | Aleyda Solis     | LinkedIn            | AI search optimization                      |
| 10 | Lily Ray         | LinkedIn / YouTube  | Content quality, E-E-A-T, AI search         |

**Collection split:** 8 from LinkedIn (Ward, Indig, Law, Koray, Gael, Toth, Aleyda, Ray) · 2 from YouTube (Cunningham, Goldie) — using both collection methods the brief asks for. The YouTube set was deliberately narrowed: I verified each channel's live uploads (June 2026) and kept only creators who are both recent *and* on-topic for AI-SEO content; experts whose YouTube had gone stale or off-topic are collected from LinkedIn, where they remain active.

## Repository structure

```
/research
  ├── sources.md              # the 10 experts: links, dates, annotations
  ├── linkedin-posts/         # collected posts, organized by author
  ├── youtube-transcripts/    # collected transcripts, organized by author/video
  └── other/                  # articles, newsletters, slides, extra materials
/scripts
  └── fetch_youtube_transcripts.py   # pulls transcripts via the Supadata API
```

## How content was collected

* **YouTube transcripts** — pulled programmatically with the **Supadata API** via `scripts/fetch_youtube_transcripts.py`. The script fetches each transcript and saves it as Markdown under `research/youtube-transcripts/<author>/`, formatted into timestamped paragraphs. Each file opens with a **"Key points" synthesis** (my own notes distilling the tactics, with a skeptical caveat where the video is a sales pitch), followed by the verbatim transcript as the source. See `research/youtube-transcripts/README.md` for the index.
* **LinkedIn posts** — collected manually from each author's recent public posts (last ~3 months). LinkedIn requires authentication and its terms forbid automated scraping, so manual collection is the compliant route the brief explicitly allows.

Commits are made incrementally as material is gathered, so the history reflects steady progress rather than one final dump.

## What's next

This collected material is the raw input for turning the research into a structured, original **AI-SEO content playbook** in a later step.
