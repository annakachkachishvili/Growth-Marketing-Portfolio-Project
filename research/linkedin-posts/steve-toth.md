# Steve Toth — LinkedIn posts

- **Profile:** https://www.linkedin.com/in/stevetothjr/
- **Role:** Founder of SEO Notebook & AI Notebook (27k+ subs); AI SEO for B2B brands
- **Collected:** 2026-06-12
- **Method:** Manual collection from public LinkedIn activity (most recent, on-topic posts)

---

## Post — 2 days ago
**Link:** https://www.linkedin.com/feed/update/urn:li:activity:7470097463970844672/

AEO tip: If your company grew by acquisition, AI probably credits the brands you BOUGHT, not you. Here's how to claim it back.

This is everywhere with private equity companies and roll-ups. Picture a business that acquired the leading tools in three totally different categories. Ask an LLM "best [category]" and it names the product they bought, never the parent. The capability is theirs; the credit isn't.

With SEO, it was "easy." 301 redirect the acquired site, rank and bank off all that new link equity. With LLMs, it's a whole different ball game.

Here's the short version of how to fix it:

1. Audit the LLMs. Ask "what is [parent]?" and "best [category]?" across ChatGPT, Gemini, Perplexity, Copilot and Claude. Log who gets the credit on each (we use the dataforseo MCP in Claude for this).

2. Map the entity gap. List every acquired product and the category it owns. Flag each spot where the model says the acquired brand instead of the parent.

3. Fix the entity graph. Wikidata/Wikipedia first sentence, Organization + sameAs schema, and consistent "[Parent] [Product]" naming everywhere. This is the KEY step most people skip.

4. Re-optimize the third-party listings. G2, Capterra, TrustRadius, Crunchbase, LinkedIn — tag the parent and rewrite descriptions so the product sits under it. (My move: dump every listing URL into Ahrefs Batch Analysis and fix the highest-authority ones first.)

5. Suppress the stragglers. Pre-acquisition pages on legacy domains get 301'd, consolidated or no-indexed.

6. Publish highly retrievable announcement posts and press releases about the acquisition and link to the new brand.

7. Monitor every 4 weeks. Re-query and score outputs.

The honest caveat: LLMs are slow to unlearn. Models don't update frequently and it takes time for new training data to enter the fold. The move is to strengthen the connective tissue for "[Parent]'s [Product]" across the web.

---

## Post — 6 days ago
**Link:** https://www.linkedin.com/feed/update/urn:li:activity:7468647893676232704/

Getting cited in AI Overviews IS just SEO. Google's right about that one. But...

Just because the on-page work is the same as what we've done to rank to win featured snippets for a decade. Principles like: (1) declarative phrasing; (2) short dependency hops between subject, predicate, and object; (3) clear, retrievable answers — one idea per paragraph with supporting points in that same paragraph.

But if that's all AEO is to you, then sure, it's "just SEO." Citations and mentions are the floor, not the game.

Here's what the "just SEO" camp conveniently leaves out:
- The brand-aware buyer who already knows you and is using AI to determine fit and build their shortlists
- The specific claims you want to be known for, and how to influence them
- How you're represented and recommended on the deal-breakers that influence the free trials and demos they book

Your buyer isn't just asking AI "who are the best vendors?" The ones at the bottom of the funnel ask deal-breakers like: "does [product] support SSO?", "is [product] SOC 2 Type II compliant?", "can [product] handle thousands of users at once?", and "what's it going to cost?"

B2B AEO isn't only about getting mentioned and cited for high-CPC keywords. It's about not getting disqualified because the LLMs don't represent you the way your top salesperson does. And these questions are being asked across every AI surface, not just Google.

---

## Post — 3 days ago
**Link:** https://www.linkedin.com/feed/update/urn:li:activity:7469735028202201088/

Google published a checklist for making your content "helpful." It's 32 self-assessment questions buried in their people-first content guide. They quietly refreshed it back in December. Almost nobody noticed.

Questions like:
→ Does your content give original info?
→ Is it written by someone who clearly knows the topic?
→ Are you faking freshness by swapping out dates?

The problem with checking pages against it yourself: slow, inconsistent, and two people can score the same page differently.

So I built a custom GPT that assesses your content against the guidelines and hands you a letter grade. Use it as part of your QA layer to rank higher.

---

## Post — 1 day ago
**Link:** https://www.linkedin.com/feed/update/urn:li:activity:7470459834891395073/

AI Tip: Before you run out of context window, make Claude write the SOP for all the hard work you just put in.

I just spent a long session building an insane, interactive pitch deck with Claude Code. Dozens of refinements, design guidelines, structural decisions, all living inside one conversation. The problem? Context windows run out. And when they do, every refinement you taught the model disappears with the chat.

So before I hit the wall, I sent one final prompt: "Create an SOP with a master prompt containing all of the refinements, guidelines and the process I shared so that I can make a deck like this more easily the next time."

Why this works:
- Claude has the FULL context of every correction you made during the session
- The output is a reusable master prompt, not just notes
- Next time, you paste the SOP into a fresh chat and start at 80% instead of 0%
- You can save it as a Claude Skill or project instruction so it triggers automatically
- Each session compounds: refine the SOP, re-save, repeat

The lesson: the deck was the deliverable, but the SOP is the asset. Hours of back-and-forth refinement is real IP, and it evaporates if you don't capture it before the context runs out. One caveat: do this BEFORE you're at the very end of the window, or Claude loses the early refinements you most want captured.
