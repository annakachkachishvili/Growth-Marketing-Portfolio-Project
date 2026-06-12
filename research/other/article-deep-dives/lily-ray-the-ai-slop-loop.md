# Deep dive — "The AI Slop Loop" (Lily Ray)

- **Author:** Lily Ray (VP SEO & AI Search, Amsive; founder, Algorythmic)
- **Source:** https://lilyraynyc.substack.com/p/the-ai-slop-loop
- **Published:** 14 April 2026
- **Read & summarized:** 2026-06-12 — *my notes on the article, not a copy of it.*

## Why it's in this collection
The clearest, evidence-backed case for *why content quality and accuracy still matter* in the AI era — the guardrail every AI-content playbook needs. Especially relevant for 100Hires, whose stated fear is "AI-generated garbage."

## Core thesis
AI search systems treat **repetition as consensus**: if enough sources repeat a claim, RAG-based systems (Perplexity, AI Overviews, ChatGPT) present it as fact — regardless of whether a human ever verified it. AI-generated slop seeds a misinformation **feedback loop** that then becomes training/retrieval data for the next batch of AI answers.

## The evidence (this is what makes it strong)
- **The fake "September 2025 Perspectives update":** Perplexity told her about a Google core update that never happened, citing two AI-generated agency blog posts. Months later, LLMs *still* confidently describe this non-existent update.
- **The pizza experiment:** she published an AI-generated post about a fake Google update, including that Google "approved the update between slices of leftover pizza." **Within 24 hours, AI Overviews served the fabricated detail back as fact** — and even contextualized it against a real 2024 pizza-query incident. (She later deleted the post because it was spreading.)
- **The BBC "hot dog" test:** a journalist with a low-traffic site published a fake "best tech journalists at eating hot dogs" page; within 24 hours Google's AI Overviews and ChatGPT parroted it (Claude did not).
- **NYT data:** AI Overviews were accurate ~91% of the time — but at 5T+ searches/year that's still tens of millions of wrong answers per hour. Worse, **56% of *correct* answers were "ungrounded"** (the linked sources didn't fully support the claim), and that got *worse* with the newer model (37% → 56%).
- **Tiered accuracy:** ~94% of ChatGPT users are on the free tier; the more accurate models are paywalled. Billions on free AI search are getting the least reliable answers and the systems "never admit uncertainty."

## Notable line
> "Until that changes, the burden of fact-checking falls on the user. And most users don't know they're carrying it."

## Playbook takeaway
Two direct implications:
1. **Quality/verification is a moat, not a nicety.** A playbook should mandate human fact-checking and primary-source grounding — both to avoid publishing slop and because accurate, well-sourced content is what survives as AI systems clean up.
2. **Don't learn GEO/SEO tactics *from* an LLM** — the space is contaminated with fabricated advice. Verify against named, experienced experts. (This is also why this whole project collected from *real practitioners* and verified their links.)
