# Ryan Law — LinkedIn posts

- **Profile:** https://www.linkedin.com/in/thinkingslow/
- **Role:** Director of Content Marketing at Ahrefs (former CMO at Animalz)
- **Collected:** 2026-06-12
- **Method:** Browser-based collection from the author's public activity feed (logged-in session; post text extracted from the page, not bulk scraped)

---

## Post — 12 hours ago
**Link:** https://www.linkedin.com/feed/update/urn:li:activity:7470769358055825408/

"does AI content work?" is entirely the wrong thing to ask. a much better question is "how is AI content materially different from 'normal' content?"

usually when people publish "AI content" they are unwittingly engaging in a *different* strategy to traditional content marketing, and creating something *different* from traditional content. they create obvious hallmarks of AI use.

for example:

- publishing content much faster than usual, often on newer domains with little authority, no branded search demand, etc.
- relying entirely on an AI model's internal knowledge, without sourcing information from a range of external sources
- failing to include internal and external links, images, visual interest, first-person experiences
- leaving obvious artefacts of AI use in the article, like obviously AI-generated imagery, obvious AI turns-of-phrase
- AI writing patterns and watermarks that haven't been "humanised" by anchoring text generation in specific writing examples.

some of these hallmarks make the content WORSE than normal (and hence contribute to poor performance), others are very DIFFERENT from normal (and make it easy to single out content as likely AI-generated) - both of which can contribute to that content not performing well.

i obviously don't know the exact mechanisms at play when Google sinks an AI-generated blog after 3-months, but i DO know that many of these aforementioned signals are very obvious to Google: indexing requests, branded search demand, AI content detection (even if only directionally accurate), user engagement signals

we use generative AI a lot at Ahrefs, and i'm happy to do this because we do not compromise on our editorial standards. our AI process mirrors our human editorial process, step for step; it is better and more detailed than the human equivalent in many areas, because LLMs are more tireless researchers, more thorough adherents to brand voice.

we are substituting one tool for another, one method of construction for another, but the end product is the same. we have even now published AI-generated content that is subjectively BETTER than our previously human-made content, because AI removed the data, design and updating constraints that previously limited our team.

you need to determine your own risk tolerance, but in my opinion, using AI to create content is not a problem - but using AI to create something that is WORSE or DIFFERENT to "normal" content marketing is. "creating bad content" or "scaling content too soon" is where problems emerge, and many people do this unwittingly when they use AI.

if you want to win, change your framing and use AI to make content that is cooler and better than you were able to do before ✌

---

## Post — 3 days ago
**Link:** https://www.linkedin.com/feed/update/urn:li:activity:7469755485517271040/

if i was starting my FIRST DAY as a new Head of Content, here's what i would do:

- build a new blog using a static site generator, host with GitHub, deploy with Netlify or Cloudflare Pages. for an existing blog like WordPress, set up an MCP connector. the goal is a fully AI-native blog, analysis, content creation, updating, all from the terminal, all in my control

- get access to Gong/Intercom/Slack and extract common entities and n-grams. find the language customers and prospects really use, use this as seed keywords for topic research

- build key "source of truth" files in markdown i can reference throughout my workflows: a master list of product features and use cases, canonical writing voice with specific reference articles, key strategic priorities to shape everything we do

- crawl our sitemap and generate vector embeddings for every article. use this to analyse topical authority (and topic "drift") and automate internal linking

- schedule a recurring, automated content audit: pull rankings and backlink data via the Ahrefs MCP, analyse AI search visibility with Brand Radar, flag technical issues with Site Audit, look for traffic decay via GSC and make a priority list of content updates

- set up a daily cron job to refresh our highest priority articles: extract the article content, run through AI Content Helper to fill topic gaps, update old claims and statistics, save as a draft for my review

- run a content gap analysis using the Ahrefs MCP to find key topics our competitors have covered that we haven't. use Firehose to get a daily update of new articles and industry news emailed to me

- build my Content OS: a centralised dashboard that pulls all of these reports and workflows into one place. this is exactly what i've done at Ahrefs using Agent A

---
i sound like an obnoxious AI hype bro, but all these workflows are things my team have actually built. many of them will become the norm sooner rather than later

AI is truly putting the "manager" into "Content Marketing Manager". we now operate at a higher level of abstraction, building systems to support our work instead of doing everything ourselves

and as crazy as this sounds, this isn't so much the "first 30-days" of content marketing as the first 30-MINUTES, because so much of this infrastructure can be built agentically. you just need to have the vision, know what to ask for, and use your taste and experience to nudge as these systems get built for you

if you don't know where to start: pick one of these ideas, login to Claude Code or Codex or Agent A, paste the bullet and ask it to build it

---

## Post — 1 week ago
**Link:** https://www.linkedin.com/feed/update/urn:li:activity:7466085949089742848/

content marketing is going through the biggest step-change since Google appeared. one personal example:

i have an old website i built a decade ago. the content was old, the design was old, i had no time to improve it. resigned to a slow death. c'est la vie.

but now: i migrated the website from Squarespace to static HTML. i vibe-coded a brand new design with tons of custom widgets. i hooked it up to Codex and now, every day, Codex chooses one old article to improve, automatically.

it pulls performance data from the Ahrefs MCP. it reviews top-ranking articles. it finds content gaps, adds new sections, generates new images, improves internal linking, and generates a preview for me to provide feedback on.

it takes me about 10-minutes to review and finalise the article, and Codex saves my feedback to a memory file that it reviews the next time it goes to update an article. it is literally like having a team working for me, to my exact specification, reviving all of my old projects, and it costs me $20/m.

and this is just a dumb hobby project: imagine what content marketing is about to look like at successful, tech-literate companies with big budgets and bigger revenue goals?

of course, it's a classic monkey paw: the same technology that is automating high-quality content marketing is also nerfing the value companies can derive from it.

but i think there will always be value (and reward) for extremely high-quality content, and strangely, i think AI is about to become essential for making competitive, high-quality content. how can "traditional" content marketing compete with automated content updating, with deeper research, with unique data visualisations and custom-coded page experiences?

content marketing is absolutely crazy right now, and frankly i am having the best time

---

## Post — 2 weeks ago
**Link:** https://www.linkedin.com/feed/update/urn:li:activity:7464941601384128512/

Here's a full 9-minute walkthrough of my AI content automation system, built using Agent A.

This is a full content automation system that covers keyword research, competitor analysis, topic research, outlining, mentioning Ahrefs products and articles, drafting, internal linking, simple image generation, preview, editing, formatting for publication, and even updating content after it's published.

The system is built with no code using full access to Ahrefs data, and includes dozens of customizable skill files based on my real editorial process. I've used this process to publish and update dozens of live articles on the Ahrefs blog.

It's easy to make bad content with AI, but it's getting easier and easier to make great content too. Hope this is helpful!
