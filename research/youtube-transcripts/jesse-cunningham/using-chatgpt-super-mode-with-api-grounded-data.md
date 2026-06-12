# Using ChatGPT SUPER Mode with API Grounded Data

- **Author:** jesse-cunningham
- **Source:** https://www.youtube.com/watch?v=XxTY7LFEliQ
- **Collected:** 2026-06-12
- **Method:** Supadata YouTube Transcript API
- *Auto-generated transcript, formatted into timestamped paragraphs and lightly corrected for obvious transcription errors (e.g. "GBT"→"GPT", "SERs"→"SERPs", "HFS"→"Ahrefs"). The speakers' actual wording is otherwise unchanged.*

---

## Key points (my synthesis)

*Distilled by me from the transcript below — these are my notes, not the creator's words.*

- Practical build: a **custom GPT connected to the DataForSEO API** returns real search volume, CPC, and competition, and reads live SERPs — replacing expensive tools for solo/local SEO at roughly per-API-call cost (<$50/mo even for agency use).
- Strongest tactic: use it to **read the SERP makeup and infer Google's intent classification** (their example: Google treats "go-kart rental San Diego" as a *tourist experience*, not racing) — then build **intent-cluster pages, not keyword pages**.
- "Ground" the LLM in real data to kill hallucination — the differentiator vs. people using raw ChatGPT.
- Note on schema: structured data still works, but LLMs parse it differently than Google's rich-results engine.
- ⚠️ Caveat: doubles as a pitch for their community; the transferable skill is the **intent-from-SERP** method.

---

## Transcript

**[00:00]** If you combine ChatGPT with grounded data, which is what we're going to do in this video, APIs plus ChatGPT, you can make a lot of money. Everyone should be doing this because it makes life easy. It's more accurate than ever before. And guess what? You don't have to pay for the expensive SEO tools. Okay, so this is the tool we're going to go over. It's actually pushing out the content right now. It looks like regular ChatGPT stuff. It's not in any way, shape, or form because we have grounded data. What we have here is called the SEO research

**[00:32]** assistant. We're going to use Google. We're going to use two examples. Let's talk about it. Sean, you built this darn thing. What is it all about? Why is it powerful? >> It's basically a custom GPT, but then it has access to the real world data. It uses an API and it plugs it in. And now you have real search volumes. All the same stuff that Ahrefs uses but for a fraction of the cost. >> All right. All right. So, you can see here it said talk to um API.data for SEO. Hopefully, I'm not giving away any of my keys. So, when you come over to

**[01:05]** the classroom in the Rank Expand Academy, this is one of the first things you'll learn to do. Gear up. You have access right here, your SEO research assistant. You go to the course and boom, you're going to start to build it. Very easy. You can set this up in 10 minutes. But the key here is we can get CPC, true CPC data. We can get competition. We can get top of page bid. Basic SEO stuff. But the cool part is we get to talk to it, right? So I'm going to say, explain this to me like I'm in 10th grade. Um, what should I do? Um, give me data.

**[01:43]** So, the idea is that we own a go-kart rental company in San Diego. A very odd thing to rent, but looks kind of cool, right? I would do this. It doesn't look half bad. But let's say we want to rank our website for this. We can use this tool. So, here is what it says. Step one, what the data actually says uh from the API keyword, go-kart rental San Diego. Searches per month is 10 people. Cost per click is two. All right. what this means plain English only 10 people per month search this all right what you should do instead think of keywords like

**[02:15]** a net so the cool part here and here's your net go after these the cool part here is you can talk to GPT you can talk to it do what it does best conversationally and then have grounded data right that's the whole key here right >> yeah what this allows you to do is even if you don't know any SEO as of this moment you can you can turn out like $1,200 SEO audits like you've done so for the last five years. And basically, you can pull all the data, let ChatGPT do the analysis, and then uh do an

**[02:50]** interpretation of the data, interrogate the data, and come up with a good SEO strategy uh like a grounded and and datadriven SEO strategy that will actually work. It will pull all the search engine result pages. it can take a look at the competitors, read their pages, all of this stuff. So, basically what you have is like an a senior SEO consultant in a box, and even if you don't know anything, uh, you can run with it. >> Look at this. Kind of embarrassing, but it said the API call for multiple

**[03:22]** keywords failed. Uh, payment credit card issue on the provider side. So, >> with that said, I think we're going to have to pivot. You're going to have to share screen on yours. I have to update my credit card. and said, "Here's estimated but realistic results. We do not want estimated results. That stinks. We need real results. >> This is what you usually get and that is what we want to stay away from actually." >> Okay, perfect. So, Sean, let's see if yours works. So, we have a little bit of Dutch on the screen because you're in the Netherlands, but I think people can get past that if you only speak English. All right, so what do we got here? So,

**[03:57]** this right here, is it pulling directly from the uh API data? >> It is. Yeah, it is uh reading the search engine result page to see what's on there and it tells us what is actually ranking right now. So, Google interprets this keyword as tourist experience, not racing go-karts. So, this this gives us a little bit of information about intent. One brand is dominating, mixed intent is opportunity, and then it gives us a strategy how to beat this search engine result page, the

**[04:29]** SER See that right there? Let's go back up. What was the um the prompt that you used? >> I said, "I am ranking go-kart rental San Diego. Pull from API to inform a strategy." >> How simple is that? And then here we go. I mean, three years ago, most SEOs couldn't give you this type of insight and certainly not in the matter of time that this has given us. >> No, not at all. No. I've seen SEO consultants

**[05:02]** not even get here in a in multiple hours. You need to do a lot of data analysis and synthesis to to get to this point. And then the the coolest thing about this GPT is we can now interrogate the strategy. We can take a look ourselves. We can add observations and really develop this thing. And in like half an hour you have like a real good strategy. Interesting. All right, keep going down. Create intent specific landing pages.

**[05:35]** Great. Target this but include. Okay, so it's telling us what to put in the copy. You're free re reframing the keyword. Yeah, the one insight that it said about experiences. That's pretty impressive that it pulled it here. Go back up. Let's figure out how did it Maybe we should challenge it. How did you How do you figure it's about experiences? >> Yep, that's good. How did you see what it says? Let's see how fast

**[06:08]** ChatGPT is nowadays. >> There you go. >> Yeah, it's the kind of thinking that separates service level SEO from actual ranking strategy. It's very confident. uh it didn't guess it. I reverse engineered it from the SER makeup. So the search engine result page makeup, the type of uh results it was getting. Who ranks? Uh this is very good. This is like best practice. Um who ranks for these keywords, the language used in

**[06:41]** titles, tours and activities, experience, and then a local pack reinforces it. So it looked at reviews even. So this GPT has access to a lot of data. >> Yeah, no kidding. See, this is man, it's just kind of like if if this is all you use as an SEO, especially if you're a solo shop, an entrepreneur, this is all you really need. This is this is it. You don't need Ahrefs anymore,

**[07:14]** especially if it's just local SEO. You don't need Semrush. You could just jam with this thing. And then the cost is fractional. You're paying per API call. What is your take on how much this thing costs? >> Way too way too little for what it delivers. So to give you a ballpark, I don't know the exact numbers, but we use this thing all the time and our people use it and and we run audits all day long. And then I think we've topped up our credit like more than a month ago and it was 50 bucks. So this thing runs

**[07:47]** for less than 50 bucks and we do agency work. >> So most people if they're just solo are going to it's going to be way less than that. >> Interesting. >> Let's do this. >> I just wanted to point this out. This this little snippet right here. So this is why I said uh AI is a great learning tool. Like really really good. If you don't know anything about SEO, these I I've worked with SEO consultants, uh, bless them, but they they didn't know this. And this is such a valuable insight and ChatGPT just hands it to

**[08:21]** you and now you know this. So, it's about intent. It's not about the keyword. And this is like SEO 2.0. Not not all SEOs are up to speed with this. And so, it it build an entire strategy around this insight. >> Yeah, that's gold. Most I mean just to stay there for a second, most people assume or want it to mean a thing, but all that matters is what Google thinks about it, >> right? >> Yes. >> And so being able to read the search results and figuring out what the actual classification by Google is, that is

**[08:57]** exactly what this this assistant did right there. And it did it super quick for like a scent. See, if I wanted to learn Dutch, Sean, Dutch is like a hard language, right? I'd imagine. But probably the best way for me to learn Dutch is to move to the Netherlands and be immersed, right? Just get in it. And so for newbies, we've seen people who are new at SEO, new at GEO. They come in here, they use this tool, and it's like being immersed because you can talk to it. Like, you don't understand this core principle, ask it another question. You know, this is being immersed in SEO instead of just

**[09:30]** looking at data from Ahrefs and Semrush, which are good. But I still use them. We still use them, right? >> Yes. >> How can I leverage intent versus keyword? >> All right. >> So now now I'm into a learning uh learning process all of a sudden. And so if the client has a question about the strategy, I can go back here, ask the questions to the GPT and it will explain it uh and I can just use that to explain it to the client. So this is a way to learn so quickly. match the dominant intent then twist it

**[10:05]** then differentiate interesting build pages around intent clusters not keywords intent right especially with local SEO is everything nice yeah it's gold it's not always going to be 100% but at least we ground the data right we ground the GPT with data whereas everyone else is just usually using hallucinations on data when they use GPT which is the big problem. >> Yeah, 100%. Yeah. >> So, if someone's interested in this,

**[10:38]** this is like a core offering, a very basic offering on what you'll get in the Rank Expand Academy. Um, I don't want to say basic in a bad way, but just this is like the first thing you learn to do because it's foundational to everything else. Yeah, it's uh it's it's one of the many workflows and tools that we offer. any of these tools, any of these workflows you can use to make a lot of money, just leveraging the the capabilities there and not over complicating things. The structured data expert, something

**[11:11]** totally different. I've seen people online, this is a tangent, but might as well talk about it. They're like, "Structured data doesn't work on websites." There's a lot of talk about this right now. I don't know if you would want to get into it, but structured data does work on websites, but AI parses it differently than Google used to parse schema, which is interesting. >> Correct. >> Correct. So, basically the uh the divide is is real. Google uses structured data to pull for their rich results. And so, it's a great way to jump the queue. If you have your structured data set up

**[11:44]** properly and you know what Google wants and how it uses it and you just one up your competition, you'll get pref prefer preference and so you can jump the organic search results and get a rich result with structured data which is very powerful. But I've read studies on this and and the the the data is out. So yeah, AI doesn't read structured data in the same way, but it does read it and it does uh take it into account and is very powerful. >> Yeah, I think you can probably

**[12:17]** manipulate LLMs with it right now, >> but that's a conversation for a different time. >> I say we leave it there, Sean. If someone wants all this stuff, >> where do they get it? Like what what do they do? >> They simply go to uh sign up for the school community. It's all there. It's a It's a great community of good people and it's a good way to get feedback as well. So, if you want to learn this stuff and you want feedback and you want to improve, you can get there using this community and just this community alone. We have many success stories inside the

**[12:49]** community as of this moment. So it's it's very inspirational.
