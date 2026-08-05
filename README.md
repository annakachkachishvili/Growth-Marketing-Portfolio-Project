# Growth Marketing Portfolio Project

## Overview

This repository documents the setup process for the required project environment using Cursor, GitHub, Claude Code, and Codex.

The main goal of this stage was not just completing installation steps, but making sure the environment, integrations, and onboarding flows were actually working before moving further into the workflow.

> This README covers **Step 1 — Setup** (below), **Step 2 — Research Project: AI-Powered SEO Content Production** (further down), and **Step 3 — the Playbook**, which lives in **[`PLAYBOOK.md`](PLAYBOOK.md)**.

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

The full annotated list with links is in **[`/research/sources.md`](research/sources.md)**, and exactly *how* I sourced, scored and verified these experts (and who I cut) is documented in **[`/research/methodology.md`](research/methodology.md)**.

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

## Repository map

```
README.md                         # this file (Step 1 setup + Step 2 research + Step 3 pointer)
PLAYBOOK.md                       # Step 3: the AI-SEO content playbook built from this research
/research
  ├── sources.md                  # the 10 experts: roles, links, annotations
  ├── methodology.md              # how I sourced, scored & verified them (+ who I cut)
  ├── key-themes.md               # my synthesis: cross-cutting patterns → playbook outline
  ├── linkedin-posts/             # collected posts by author (8 experts) + index
  ├── youtube-transcripts/        # collected transcripts by author (2 experts) + index
  └── other/
        ├── articles/              # collected long-form articles, organized per author (captures)
        ├── expert-owned-content.md # experts' blogs/newsletters/guides (deeper than their posts)
        └── key-studies.md          # primary data/studies/patents the experts cite
/scripts
  ├── fetch_youtube_transcripts.py  # pulls transcripts via the Supadata API
  ├── list_latest_videos.py         # lists a channel's recent uploads via the API
  └── README.md                     # how the scripts + API work
```

**Where to start:** [`methodology.md`](research/methodology.md) (how the experts were chosen) → [`sources.md`](research/sources.md) (the list) → [`key-themes.md`](research/key-themes.md) (what the material adds up to).

## How content was collected

* **YouTube transcripts** — pulled programmatically with the **Supadata API** via `scripts/fetch_youtube_transcripts.py`. The script fetches each transcript and saves it as Markdown under `research/youtube-transcripts/<author>/`, formatted into timestamped paragraphs. Each file opens with a **"Key points" synthesis** (my own notes distilling the tactics, with a skeptical caveat where the video is a sales pitch), followed by the verbatim transcript as the source. See `research/youtube-transcripts/README.md` for the index.
* **LinkedIn posts** — collected from each author's public activity feed in a logged-in browser session, extracting the post text directly from the page (a lightweight, assisted approach rather than bulk automated scraping, which LinkedIn's terms prohibit). Saved verbatim with each post's date and permalink.

Commits are made incrementally as material is gathered, so the history reflects steady progress rather than one final dump.

## Tools & workflow

This project was built with an AI-assisted workflow — using AI tools as leverage while keeping my own judgment on topic choice, expert selection, verification, and synthesis.

- **Claude Code** — my primary research and drafting assistant for this step.
- **Claude browser extension** — used to navigate each expert's public LinkedIn activity and collect their posts.
- **Supadata API + Python** (see [`/scripts`](scripts/)) — to pull YouTube transcripts programmatically.
- **Git / GitHub** — version control, with small incremental commits throughout.

*(The Step 1 environment was set up in Cursor IDE with the Claude Code and Codex extensions.)*

The judgment calls — which topic to pick, which experts made the cut, who to drop, how to verify recency, and what the cross-cutting themes mean — were mine. The AI tools accelerated the execution; they didn't make the decisions.

## Early synthesis

I didn't want to stop at collecting links. [`research/key-themes.md`](research/key-themes.md) distills the cross-cutting patterns across all 10 experts — e.g. *"AEO is an extension of SEO, not a new channel," "win on information gain, not polish," "ground the model in real data and build systems not prompts," "measure AI visibility like polling"* — and maps each theme to the experts who support it and what it implies for a playbook. It's an early read, but it shows the material is already converging on a clear structure.

---
---

# Step 3 — The Playbook

The research above is now a working document: **[`PLAYBOOK.md`](PLAYBOOK.md)** — a four-layer SOP (foundation → production → distribution/consensus → measurement) for AI-powered SEO content production at a B2B SaaS like 100Hires. Every recommendation cites its source with an exact dated link and, where the material was collected in Step 2, a second link to the verbatim copy in [`/research/`](research/) — so any claim can be checked against the text it came from.

Beyond the SOP core, the playbook contains the judgment sections the brief asks for:

- **Where experts disagree** — three real disagreements, each with both sides and a side taken and argued; plus one famous "disagreement" I checked and found false, kept as a sidebar because the dissolution was the more useful result.
- **What I rejected and why** — four ideas from my own sources, rejected for four different reasons: evidence, incentive, dependency, and context.
- **My original ideas** — two, not found in the sources: *trace-before-trust* (verification as a shipped practice — demonstrated in this repository, not just proposed) and a *B2C2B pull strategy* transferred from my own clinic-marketing work.
- **Weaknesses of this playbook** — what might not work (with exits named in advance), which assumptions are untested, what's missing, and where the playbook's claims stop.
- **Who I would NOT recommend following** — a verdict produced by applying one trust instrument to all ten experts, not a mood about one.
- **A verification ledger** — every load-bearing number traced to its primary source before being cited. The tracing corrected two widely-quoted numbers along the way; both stories are told inside the document, because a method that never catches anything isn't a method.

One technical note: the exact LinkedIn post dates cited throughout were recovered by decoding each post URL's activity ID (the first 41 bits encode the posting timestamp in milliseconds) and cross-checking against collection-time notes.

Built with the same AI-assisted workflow as Step 2 — AI tools for research acceleration, drafting support, and verification mechanics; the judgment calls, side-takings, rejections, and ideas are mine to make and mine to defend.
