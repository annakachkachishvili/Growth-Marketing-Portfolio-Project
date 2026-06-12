# Deep dive — "How I Do Content Engineering with Claude Code" (Ryan Law, Ahrefs)

- **Author:** Ryan Law (Director of Content Marketing, Ahrefs)
- **Source:** https://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/
- **Published:** 28 April 2026
- **Read & summarized:** 2026-06-12 — *these are my notes on the article, not a copy of it.*

## Why it's in this collection
This is the single most relevant piece in the whole research set: a working content-automation system built in **Claude Code** (the exact tool 100Hires uses), by a content leader who refuses to trade quality for scale. It's a near-complete blueprint for the "production system" layer of a playbook.

## Core thesis
AI is now good enough to **automate the formulaic parts of content marketing with no loss of quality** — but only when the system encodes real editorial experience. The system takes a keyword to a publish-ready draft in **6–12 minutes**; the Ahrefs team has published ~15 articles and updated ~30 this way. Crucially, he refuses to use it to "scale content" to thousands of articles — it maintains an evergreen library on a handful of core topics.

## The system, in 7 moves
1. **Chain editorial "skill" files** — ~23 Markdown skill files, each mirroring one step of the human process (keyword research, topic-gap analysis, outlining, drafting…). A master `blog-pipeline` skill triggers them in order. Each skill = how to do the step + best-practice examples + output format.
2. **Output every step to its own file** — outlines, research primers, drafts are each saved, so when a 10-minute run produces a bad article you can see *which stage* failed, fix that skill, and restart from the last good step.
3. **Create test cases for recursive self-improvement** — uses Anthropic's `skill-creator` to run each stage with and without the custom guidance, then has the LLM suggest improvements. Keeps skills short and "to their most effective essence" (bloated skills get ignored by the model).
4. **Give LLMs great data from great sources** — the system is wired to the **Ahrefs MCP** so Claude pulls real keyword metrics, questions, and SERP/intent data instead of hallucinating. Also mandates competitor data, deep research from trusted sources, and a product-features doc.
5. **Front-load human direction** — a `context` parameter lets a human add a one-paragraph angle at the *start* (e.g. "take a 'steal your competitor's best content' angle, feature the Content Gap tool…"). His thesis: *small expert direction up front beats heavy editing at the end.*
6. **Build interactive previews** — a skill renders each draft as an Ahrefs-styled HTML page in Chrome for review (with experiments toward inline accept/decline and comments for Claude to action).
7. **Fork and personalize** — every team member forks the repo and tunes it to their own voice, data sources, and best articles — "a personalised content copilot."

## Notable specifics worth stealing
- **Mandating data sources is the anti-hallucination lever:** "By default, LLMs are very convincing bloviators… Mandating specific data sources to use is key to getting great results."
- **The skill files only work because of expertise.** He quotes a commenter: *"Ryan's SKILL files are good because Ryan already knew what to put in them… The gap isn't just in the tool. It's in the person behind it too."*
- Only uses it on topics he understands well and that Ahrefs has already covered, so he can validate every claim.

## Playbook takeaway
The production system for a B2B SaaS like 100Hires shouldn't be "prompts" — it should be a **forkable repo of editorial skill files + a pipeline orchestrator + real data via MCP/API + per-step outputs for debugging + light human direction up front.** And the guardrail is explicit: automate the drudgery, never "scale" past what a skilled human would approve.
