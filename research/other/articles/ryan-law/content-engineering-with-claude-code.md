# How I Do Content Engineering with Claude Code

- **Author:** Ryan Law (Director of Content Marketing, Ahrefs)
- **Source:** https://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/
- **Published:** 28 April 2026
- **Captured:** 2026-06-12 — *structured notes + key passages, not a full copy of the article.*

## Core thesis
AI is now good enough to **automate the formulaic parts of content marketing with no loss of quality** — *when* the system encodes real editorial experience. His pipeline takes a keyword to a publish-ready draft in **6–12 minutes**; the team has published ~15 articles and updated ~30 this way. He explicitly refuses to "scale content" to thousands of articles.

## The system, in 7 moves
1. **Chain editorial "skill" files** — ~23 Markdown skill files, each mirroring one step of the human process (keyword research → topic-gap analysis → outlining → drafting…). A master `blog-pipeline` skill triggers them in order. Each skill = how to do the step + best-practice examples + output format.
2. **Output every step to its own file** — outlines/research/drafts each saved, so when a 10-minute run produces a bad article you can see *which stage* failed, fix that skill, and restart from the last good step.
3. **Test cases for recursive self-improvement** — uses Anthropic's `skill-creator` to run each stage with and without the custom guidance, then has the LLM suggest improvements; keeps skills short ("their most effective essence"), since bloated skills get ignored.
4. **Give LLMs great data from great sources** — wired to the **Ahrefs MCP** so Claude pulls real keyword metrics, questions, and SERP/intent data instead of hallucinating. Also mandates competitor data, deep research, and a product-features doc.
5. **Front-load human direction** — a `context` parameter lets a human add a one-paragraph angle at the *start*. Thesis: small expert direction up front beats heavy editing at the end.
6. **Build interactive previews** — a skill renders each draft as an Ahrefs-styled HTML page in Chrome for review (experimenting with inline accept/decline + comments Claude can action).
7. **Fork and personalize** — every team member forks the repo and tunes it to their own voice/data/best articles — "a personalised content copilot."

## Key passages (quoted, attributed)
> "By default, LLMs are very convincing bloviators… Mandating specific data sources to use is key to getting great results."

> *(commenter he endorses)* "Ryan's SKILL files are good because Ryan already knew what to put in them… The gap isn't just in the tool. It's in the person behind it too."

## Notable details
- Only uses it on topics he understands well and that Ahrefs has already covered, so he can validate every claim.
- "We have no plans to 'scale content' with AI" — it maintains an evergreen library on core topics; AI handles drudgery only.

## Playbook takeaway
The production layer should be a **forkable repo of editorial skill files + a pipeline orchestrator + real data via MCP/API + per-step outputs for debugging + light human direction up front** — with an explicit guardrail: automate the drudgery, never publish past what a skilled human would approve.
