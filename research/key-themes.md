# Key themes across the research

*My synthesis after reading all the collected material. The goal of Step 2 was to gather high-signal sources; this is an early read of the patterns they share, to show the material is strong enough to build a real AI-SEO content playbook on. Each theme notes which experts support it and what it implies for a playbook.*

Last updated: 2026-06-12

---

### 1. AEO / GEO is an *extension* of SEO, not a separate channel
The strongest voices push back on treating "AI search optimization" as a brand-new discipline with its own team and tactics.
- **Jake Ward:** "Please STOP doing 'AEO'… treat AI search as an expansion of SEO, not a completely different channel."
- **Steve Toth:** "Getting cited in AI Overviews IS just SEO… but citations are the floor, not the game."
- **Lily Ray:** "The worst thing you can do for your AI search visibility is destroy your SEO."
→ **Playbook implication:** build on SEO fundamentals first; layer AI-specific tactics on top rather than siloing them.

### 2. AI citations are won through third-party consensus and "best-X" lists
What earns a recommendation is what *others* say about you, repeated across the web.
- **Jake Ward:** ~44% of AI citations come from "best X" lists — more than blogs, landing, product and home pages combined; build consensus across many trusted sources.
- **Steve Toth:** fix the entity graph and re-optimise third-party listings (G2, Capterra, Wikipedia) so AI credits the right brand.
- **Lily Ray:** brands manipulating this with scaled listicles get penalised — earn it, don't fake it.
→ **Playbook implication:** prioritise getting onto (and near the top of) trusted comparison/best-of pages, *and* publish your own genuinely useful comparison/alternatives pages.

### 3. Win on information gain, not polish
Generic AI content that just rewrites the top 10 results is the failure mode everyone warns about.
- **Gael Breton:** the "Frustrated Reader" method — a sub-agent finds what existing articles *fail* to answer, then research agents mine Reddit/YouTube/forums for what people actually learned.
- **Ryan Law:** "AI content isn't the problem; *worse* or *different* content is." Keep editorial standards; AI substitutes the tool, not the bar.
- **Lily Ray:** scaled, zero-information-gain templates were the exact thing crushed by recent Google updates.
→ **Playbook implication:** research-first workflow; require original data / real information gain before publishing anything AI-assisted.

### 4. Ground the model in real data, and build *systems*, not one-off prompts
The operators don't prompt ad-hoc — they wire tools and memory into repeatable pipelines.
- **Jesse Cunningham:** custom GPT + DataForSEO API ("grounding") to remove hallucination; "a senior SEO consultant in a box."
- **Ryan Law:** a "Content OS" — Ahrefs MCP, vector embeddings for internal linking, cron-jobbed content refreshes, source-of-truth markdown files.
- **Julian Goldie:** an "agent operating system" with an Obsidian memory vault the agents read *first*.
- **Steve Toth:** capture every session's refinements as a reusable SOP / Claude Skill before the context window runs out.
→ **Playbook implication:** the deliverable isn't prompts, it's a documented system — memory files, connected data (MCP/APIs), and reusable skills/SOPs.

### 5. Think in intent, entities and topical authority — not keywords
- **Jesse Cunningham:** read the SERP to infer Google's *intent* classification, then build intent-cluster pages (not keyword pages).
- **Koray Gübür:** Visual Semantics + topical maps + the "Authority Signature" patent (Google can attribute topical authority to *authors*, per-topic); consolidate diluted entities into one domain.
- **Steve Toth:** fix the entity graph (schema, consistent naming, Wikidata) so models attribute capability to the right brand.
→ **Playbook implication:** structure content around entities and intent clusters with strong internal linking, and get the author/brand entity right.

### 6. Measure AI visibility rigorously — prompt tracking is polling, not rank tracking
- **Kevin Indig:** designed prompt panels — ~40 seed prompts (brand/category/problem), run 5×/week per platform, segmented by persona, with mention rate, citation rate, position, sentiment and confidence intervals.
- **Aleyda Solís:** build a *representative* AI-search prompt library (not a tool's random defaults) mapped to real buyer journeys.
- **Steve Toth & Lily Ray:** audit LLMs on deal-breaker prompts; convert real-volume keywords into AI prompts at scale; re-check on a cadence.
→ **Playbook implication:** measurement starts with a representative prompt library and per-platform, per-persona scoring — plus page-level feedback loops (the new GSC Generative AI report).

### 7. The click is collapsing — optimise for recommendation *and* owned audience
- **Aleyda Solís (citing Fishkin/Similarweb):** in 2026, fewer than one-third of Google searches send a click; replace "traffic" as the KPI and build presence on platforms you don't own.
- **Jake Ward / Julian Goldie:** "omnipresence" — turn one topic into many formats across many surfaces so AI pattern-matches you as the answer.
→ **Playbook implication:** measure citations/recommendations and owned-audience growth (newsletters, social, video), not just sessions.

### 8. The quality guardrail: durable tactics beat loopholes
- **Lily Ray:** loopholes that work for a few months become liabilities; play "defensive" SEO; Google is targeting "inauthentic mentions."
- **Gael Breton & Ryan Law:** the credible path is making AI content genuinely *better*, not gaming the system.
→ **Playbook implication:** bias every recommendation toward what still works *after* the platforms clean up the spam.

---

## What this points to for the playbook (later step)
A defensible AI-SEO content playbook for a B2B SaaS like 100Hires would likely have four layers:
1. **Foundation** — SEO fundamentals + clean entity/schema/topical structure.
2. **Production system** — research-first, data-grounded, agent-assisted content ops (memory files + MCP/API + reusable skills) that protects editorial quality.
3. **Distribution / consensus** — best-of & comparison pages, third-party listings, multi-format omnipresence to earn AI citations.
4. **Measurement** — a representative prompt library with per-platform, per-persona tracking and page-level feedback loops.

The collected sources give strong, current, practitioner-tested material for every one of these layers.
