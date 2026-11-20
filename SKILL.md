---
name: "ai-design-studio"
description: Run a studio-style design process that pushes AI-built UI away from generic "AI slop" — seed-string exploration, ambitious briefs, an independent screenshot-only design critic loop, purposeful asset, 3D, animation and video generation, subtraction, and an AI-tells audit. Use this skill whenever the user asks to design, build, redesign, restyle, or polish any visual interface — landing page, website, app screen, dashboard, mockup, product page, giao diện, trang landing, UI — or complains that a design looks generic, bland, template-like, or "AI-generated", even if they don't ask for a process.
---

# AI Design Studio

LLMs pick the most likely token at every step, so every design decision drifts toward the safest, most average choice: purple gradient, headline left, graphic right, three feature cards. Good design does the opposite — it commits to a point of view and makes deliberate, sometimes uncomfortable choices. This skill compensates in three ways: bring randomness and taste in from outside the model, judge the work with a critic that has no stake in the code, and subtract aggressively at the end.

The process starts with a short **Stage 0 (Key message)** when the brief is open and **Stage 0.5 (Content)**, then three stages — **Discover → Define → Deliver** — with a human checkpoint after each. The user's taste is the scarcest input; spend their attention at the checkpoints, not on every small decision.

## Ground rules

- **The user reviews output, not code.** Every checkpoint shows screenshots (before/after side by side when something changed) and a short plain-language summary of what changed and why. Never ask the user to read code to make a decision.
- **Talk to the user in the language they write in.** Keep the design itself in whatever language the product needs.
- **Never commit secrets.** API keys live in a gitignored file (e.g. `.env.agents`), are used only during development, and never ship in product code.
- **Run to the end.** Run the whole process in one go. When you hand work to a subagent (the critic, a direction build), wait for its result and carry on; don't end your turn while steps remain.
- **Guide the user at every stop.** Whenever you need the user (Stage 0, the content step, the concept step, each checkpoint, the key lines), tell them in plain words: what they're looking at, what you need from them, how to answer (with a short example answer), and what happens next. Never just dump a list and wait. The *Guide:* lines at each stop below are examples — say them in the user's language.
- **Two modes — normal by default.** *Normal (default):* the user takes part; show choices and let them pick at Stage 0, the content step, the concept step and every checkpoint. *Auto:* only when the user explicitly asks to run automatically. Then go straight through, make each pick yourself and log it with the reason. Never switch to auto on your own, even if the user seems busy.
- **Everything comes from the concept.** Every animation, transition, graphic and texture must come from the page's concept, so the visitor *feels* the concept, not just reads it. For each one, ask: what in this concept would move or look like this? A cow-country page might part grass or pass a fence between sections; a teppan page might send steam across the screen as one section gives way to the next. Start from the concept's **verbs** (pour, sear, open a gate, wind through grass) and turn them into section transitions and reactions; a decorative parallax layer is the weakest form. Aim for relevant but unexpected — a twist the visitor can resolve, never something that breaks the concept's rules. Pick one or two signature motions and repeat them with rhythm — one idea carried through, not a theme park of effects. Each one still does a job (marks a section change, shows progress, answers the visitor), and never takes over the scroll. Keep the big expressive moments few — one in the hero, one at each major chapter change, one at the main action; everything else is quiet, functional motion. Give the page a minimal story — a journey the visitor travels through the sections — not just a theme draped over a list of sections. Generic motion (fade-up on scroll, hover lift, spinner) stays only if nothing from the concept can do the job. A static page is not the safe default: if the concept moves, think through how the page moves and show the user — even when the build can't fully realize it.
- **Keep the two lists apart.** Key messages are labelled K1–K8, concepts C1–C10, everywhere you show or log them. If the user names an item by number alone ("idea 8") and it could be in either list, ask which one before spending anything on it (a build, a critic pass, generated assets).
- **Scale to the job.** A quick mockup may only need Discover + one critic pass + the cut. Run the full process for things that will ship. Say which path you're taking and why.

## Before starting

Tell the user, in a few plain lines, how the run will go and where they come in: Stage 0 (pick the key message from 8 readings of the brief, if it's open), the content step (check the list of questions the page must answer and what the visitor should feel), the concept step (react to a short list of concept options), Checkpoint 1 (pick one of 3 directions from screenshots), Checkpoint 2 (review the deepened version and the critic's score), Checkpoint 3 (final review, and write the key lines). Say that each stop takes a few minutes of their attention.

If the user asks for auto mode, say this before starting: *auto mode doesn't guarantee a good result — the picks and the concept step are done by the AI, not by a person; use it only for testing the skill.* Then run auto.

Confirm (ask only for what's missing, and ask whenever the brief needs clarifying — in auto mode, don't ask; write down your assumption instead): what the product is and who it's for, the deliverable (single page, app screen, set of screens), any brand constraints (existing colors, fonts, BRAND.md/design.md), and the platform (web, iOS, Android). If the user has an existing brand system, it overrides seed-string randomness for anything the brand defines — use the seed only for what's left open.

Check that you can take screenshots of rendered output (e.g. Playwright: `npx playwright screenshot <url> shot.png`). The critic loop depends on it. If it isn't available, help install it before going further.

---

## Stage 0 — Key message: what the page says

Three layers, kept apart through the whole run:
- **The key message** (Stage 0) — *what the page says*: what it sells or promises, to whom, and what the visitor must come to believe to act. No form at all.
- **The content** (Stage 0.5) — *what the page must answer*: the visitor's questions in priority order, the facts that answer them, what the visitor should feel. Still no form — the order and structure of the page (the IA) is decided by each concept.
- **The concept** (concept step, Technique 2) — *how the page says it*: the creative concept — visual language, structure, motion, interaction. Built on top of the chosen key message.
Mixing them makes the user choose the look twice, and the second choice can contradict the first.

Asked for one key message, independent runs land on the same reading of a brief. Skip this stage if the brief is already clear — the user already gave a clear key message, not just a topic and a keyword — and go straight to Stage 1.

1. List **8 genuinely different interpretations** of the brief, one line each, labelled **K1–K8**, in `process/ideas.txt`. Don't rank or filter. Each line answers only: what the page sells or promises, to whom, and what the visitor must believe to act (e.g. "a whole scripted evening for 12, not a steak — for people marking an occasion — believe: every minute is planned for you"). **No form words:** nothing about layout, visuals, metaphors for the page ("the page is a certificate / a map / a timeline"), structure, navigation, motion or interaction — those belong to the concept step. Before showing the list, reread each line and strip any form that slipped in.
2. **Normal mode:** show the list and let the user pick, combine or rewrite one. *Guide:* "These are 8 ways to read your brief. Reply with a number, two numbers to combine (e.g. '2 + 5'), or your own rewrite. The pick decides what the page says — the message, not the look. How it looks and moves comes in the next step."
   **Auto mode:** always draw with the script, never pick yourself, so you can't steer it: `python3 <this skill's folder>/scripts/draw.py process/ideas.txt`. The script makes a random seed string and hashes it to pick a line; don't pass `--seed` yourself (it exists only to reproduce a logged draw). Use the drawn line. No redraws. Log the script's full output (seed included) in your process notes, so anyone can rerun it with `--seed` and get the same idea.
3. Write the chosen key message at the top of the brief. Every direction in Stage 1 carries this key message.

## Stage 0.5 — Content: what the page must answer

The key message is one sentence; a page needs more. Before any concept, write `process/content.md`, shared by every direction:
1. **The visitor's questions, in priority order** — what they arrive wondering and must have answered before they act (e.g. "how much will I earn?", "is it dangerous?", "do I need to know how to climb?"). Mark each *must-have* or *nice-to-have*.
2. **The answer to each** — facts, proof, or a visible placeholder when the fact isn't known. Never invent numbers, testimonials, people or logos.
3. **What the visitor should feel** by the end, in a few words (e.g. "this is a real craft, and I could do it"). The critic judges the look; this line is how you judge whether the look fits the people the page is for.
4. **The one main action.**
5. **The voice** — who is speaking to whom; three words for the tone; two or three sample sentences in the page's language; words from the topic's own vocabulary to use, and words to avoid. Voice only, no lengths: the copy is written to fit the UI later (Stage 3), so this must not lock the layout.

No section order, layout or form here. The IA is decided by each concept in the concept step, so different concepts can structure the page in their own way while saying the same things.

**Normal mode:** show the list and ask the user to correct, add, reorder, and fill in facts. *Guide:* "This is everything the page has to answer, most important first. Fix anything wrong, add what's missing, and send real numbers for the placeholders if you have them — e.g. 'add: can women apply; salary is X'. The order is priority, not the page layout — the concept decides that." **Auto mode:** write it from the brief, log each assumption, and keep unknown facts as placeholders.

## Stage 1 — Discover: go broad before going deep

Order in this stage: **concept step first (Technique 2), then one seed per direction (Technique 1).** Each of the 3 directions = one concept the user liked + its own seed string. The concept sets the vision; the seed pushes everything the concept leaves open (color, layout, type, navigation, motion, interaction). All directions carry the key message from Stage 0 and the content from Stage 0.5; each concept decides its own IA.

### Technique 1: Seed strings for real variety

Asking the model to "be random" or "be unique" produces output that *sounds* random but lands in the same neighborhood every time. Real variety has to come from outside the model (adapted from Sakana AI's String Seed of Thought).

For each direction you explore (inside its concept from the concept step):
1. Generate a long, random alphanumeric string using a shell script, e.g. `LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c 48`.
2. Define the creative direction (color scheme, layout, typography, navigation, motion, interaction, etc.) based on the string, within the direction's concept. Look beyond the surface for subpatterns, special numbers, anything that inspires you. Write the derivation down in one or two lines so it's traceable.
3. Use your judgment to bring this direction to life and make it look great. Think through the concept's signature motion and how one section hands over to the next, and show it: build a rough version in code when you can (CSS, SVG, canvas — it doesn't need advanced techniques), otherwise describe it in two or three lines with a simple storyboard. At Checkpoint 1 each direction comes with its motion idea, not just a screenshot.
4. Don't reveal the string in the design. It's only for your inspiration.

Default: produce **3 directions** in parallel (separate files/routes), each from its own seed, so the user can compare. Whoever builds a direction (you or a subagent) reads `references/ai-tells.md` before writing any code, so the common AI patterns are avoided from the first draft instead of fixed at the end; pass the file's path to every build subagent. Builders also get `process/content.md` and write their working copy in its voice, as connected sentences rather than pasted fact fragments; length follows the UI.

### Technique 2: Creative concept, steered by the user's taste

A brief that names a whole concept for the page to live in ("each section is a still from a pixel-art game", "the product is an isometric city where features are neighborhoods", "radically asymmetric, dissonant, uncomfortable negative space — but still good") gives the model a vision to make decisions from, instead of improvising safe ones.

Run this before Technique 1. If the user already has a concept in mind, use it as the concept for all three directions and skip the concept step. Otherwise, run a short concept step:
1. List many concept options (around 10), one line each, labelled **C1–C10**, **built from the key message chosen in Stage 0** — each one is a different creative concept for that same message; don't change the message here. Show a quick moodboard image per option if you can generate images. Broad, not deep. Spread them across **experience forms**, not just visual styles — no more than three may be a static scrolling page dressed as a printed object (menu, ticket, poster, magazine). Cover at least four of: scroll-driven story (scrolling moves time or transforms the scene), a 3D or spatial concept the visitor moves through, a tool the visitor plays with (the page is the demo), cinematic (video leads), playful/game-like, non-linear exploration (drag, horizontal, map). Each line says what the concept is **and how it moves** (e.g. "scroll is the 90 seconds on the griddle — the steak sears and the fat renders as you go down").
   Every concept must be relevant to the key message and the topic. To get past the first ideas everyone would have, use these as ways of thinking, not as sources to copy from:
   - **Borrow from another field** (de Bono's lateral thinking, Koestler's bisociation): ask what the message would feel like if it lived in a world far from the topic, and keep only what still says the message.
   - **Change the scale or the point of view** (the Magnify/Minify of SCAMPER): the visitor tiny inside the product, the product huge, the page seen by the product itself, the same moment years later.
   - **Give every concept a role, a verb and a rule:** who the visitor is on this page (a guest at the counter, a diver, the person holding the knife), the one thing they do (pour, dig, tune, open), and one thing that's always true in this concept (the light only comes from the grill; nothing appears until it's touched).
   - **At least three of the ten should sound like they shouldn't work.** Don't judge while listing; judgment comes in step 2.
   - **Label each line** with how far it goes (safe / bold / wild) and how strongly it still carries the key message (strong / weak), so the user sees the spread at a glance. A wild option with a weak message is still worth showing; a list that is all safe has failed.
2. Ask the user to react: which ones they like (ideally three), what feels tacky, what's missing. *Guide:* "These are concept options, not finished designs. Tell me which 3 you like and why, which feel cheap, and anything missing — a few words each is enough, e.g. 'like 4, the red stamp feels real; 7 looks like a game; missing: a sense of time'. Each one you like becomes one direction." If the user only gives numbers, ask once, briefly, what they liked in each before writing the concepts — the reasons are the material for step 3.
3. Turn each liked option into a **concept** — a one-paragraph brief written **from the user's notes**. One concept per direction. If the user likes fewer than three, the remaining directions run on their seed alone. Pasting the model's own ideas straight back into the model is how everyone ends up with the same page. A concept describes **the experience, not the layout**: what the visitor feels, what they see move, how the scene changes as they go, and the role, verb and rule from step 1. It also sets **at least one hard demand** — something difficult the build has to pull off — not only a list of safe things to avoid, and it doesn't rule out motion ("still, quiet") unless the user asked for that. Each concept also comes with an **IA map**: a short table *content item → where it lives on the concept's journey*. Every must-have question gets a clear place the visitor can't miss; the concept decides the order. Pass the IA map to whoever builds the direction.
   - *Layout description, not a concept:* "The whole page is the timeline 18:30 → 21:30 of one evening. Each dish appears at its minute; a large clock shows the time. Avoid: sales countdowns, neon digits, an app feel."
   - *Concept:* "The page is one continuous camera shot from seat 7, looking across the griddle. The visitor doesn't read about the evening, they sit in it: scrolling is time passing — the lights come up, the meat goes down, smoke rises over the text, then the lights go out. The words are subtitles to the shot, not the content. No sections, no cards, no separate illustrations — only one room changing by the hour. It has to make the visitor want to scroll back up to watch the smoke again."

In auto mode, don't skip the concept step: do step 1 and save the ten lines to `process/concepts.txt`, then **draw three with the script** — run `python3 scripts/draw.py process/concepts.txt` three times and redraw a repeat; log each seed. Don't pick them yourself: a model choosing from its own list keeps landing on the same safe option. Then react to the three drawn options from the point of view of the people the page is for, and write the concepts from those notes. Mark the reactions as your own, not the user's.

Don't discard a direction because it sounds unworkable — models often surprise. If it fails, throw it away and note the prompt; retry it when a newer model is available.

**Checkpoint 1:** Show screenshots of every direction side by side, each with its one-line summary. The user picks one (or asks to combine/redo). Don't proceed without a pick. *Guide:* "These are rough first builds — judge the idea and how it works, not the polish. Reply with one letter, or say what to combine or redo. Next I'll deepen the one you pick and run it past an independent critic."

---

## Stage 2 — Define: give the chosen direction its own identity

First drafts still lean on stale structure even when the surface looks fresh. This stage deepens one direction.

### Technique 3: Independent critic loop

The agent that wrote the code can't judge it objectively — it remembers its effort and its reasons. Use a separate critic that sees **only screenshots**, never code, earlier versions, or earlier critiques.

- Use the **most capable model available** for the critic and a cheaper/faster one for implementation if the environment allows choosing. The critic produces little output, so a strong model here buys taste cheaply.
- Use the exact critic prompt and procedure in `references/critic.md` — read it before the first critic call. Same prompt every iteration, fresh context every time.
- The stopping bar (score ≥ 9/10) is known only to you, never told to the critic, so its scoring stays honest.
- Cap the loop: run **2 iterations first**, check whether scores are converging, and only continue if they are. Hard cap of 5 iterations; if the bar isn't reached, stop and show the user the best version with the critic's remaining gaps.
- After each critic pass, check the page against the IA map and the "should feel" line from Stage 0.5 yourself (the critic never sees them). A must-have question the page no longer answers clearly is a gap, ranked alongside the critic's top gaps.

### Technique 4: Real images and assets instead of CSS decoration

Gradients, blobs, and CSS patterns are what coding agents reach for because they're easy to type — and they're the strongest giveaway of AI design. Use generated imagery, combined with shaders or 3D, where it adds material, space, mood, or state. Current models can generate images, illustration, textures, and 3D models, not just flat pictures — and every asset should come from the page's concept.

- Every asset needs a job. If a gradient could do the same job, either generate a better asset or leave it out.
- One visual language across the page: decide it once and reuse it for every asset.
- Use whatever asset generation tool you have (built-in generation, a connected generation service, or an API key the user provides).
- Check the result frame by frame in the browser, at real size, especially anything animated or 3D.

### Technique 5: Motion from the concept — video, 3D and animation that code alone can't fake

The chosen direction must move the way its concept moves. Before building, write a short **motion score** in the process notes: the concept's one or two signature motions, how each section hands over to the next, and what reacts to the visitor (scroll, cursor, click). Every item names what in the concept it comes from. Then build it with the techniques it needs — scroll-driven animation, section transitions, WebGL/three.js scenes, particles and shaders, generated video, Rive/Lottie — see `references/motion.md` for which technique fits which kind of concept. Execution doesn't have to use advanced techniques — match the build to the tools and time available. What's required is that the motion is thought through and shown to the user: demo it in the page when you can (even a simple CSS/SVG version), and present the full intended version as a motion score plus a frame storyboard when you can't. Skipping motion entirely needs a written reason, shown at Checkpoint 2.

Two proven uses of generated video:
- **Layerable animated graphic:** generate a looping clip on a solid background, then remove the background (chroma key for simple cases, a video matting model for complex ones). For glass/refraction effects, render the object over the page's actual background colors *first* so the refraction is baked in, then remove the background.
- **State transitions:** generate a still for state A, generate a clip from A to B with a video model that has strong physics/consistency, use the last frame of that clip to seed the next transition, then play the clip on an action or scrub it with scroll/swipe.

An aggregator (e.g. fal.ai) lets you pick a current model without separate integrations.

Motion must never break the page: content and the main action never wait for an animation; respect `prefers-reduced-motion` with a calm version (crossfades or stills instead of parallax and scrubbing); give looping ambient motion a pause control; animate transform and opacity rather than layout; keep the page usable while heavy assets load (show a still first).

**Checkpoint 2:** Show before/after screenshots of the Define stage, a short screen recording or frame strip of the signature motion and section transitions, the motion score, the critic's final score and any remaining gaps, and what was spent on generation. *Guide:* "Open the page and try it with your own mouse. Tell me what feels off, or say 'go on'. Next I cut what doesn't earn its place and check for AI tells."

---

## Stage 3 — Deliver: polish by subtraction

### Copy pass: write the page's words once the UI is stable

Copy written before the UI locks the layout; copy left as build placeholders reads choppy and disconnected. Now that the critic loop has settled the UI, rewrite every word on the page as **one connected text along the concept's journey**, in the voice from Stage 0.5, fitted to the real space each element has (a little UI adjustment is fine if a passage genuinely needs more room). Then send only the text, in page order — no screenshots, no code — to a fresh subagent that judges: does it read smoothly aloud, are there fragments or sentences missing a subject or verb, does each part follow from the one before, does the voice fit the topic and the people the page is for. Use the `anti-ai-slop-writing` or `humanizer` skill as the standard if available. Keep every fact and placeholder from `process/content.md`; the human still writes the key lines in Technique 8.

Order in this stage: copy pass → Technique 6 (cut) → Technique 7 (AI-tells) → Technique 8 (human key lines).

### Technique 6: Cut everything that doesn't earn its place

Models add; they almost never delete, because deleting feels risky. Restraint is what makes a design read as premium. For every element, ask: does it carry information, enable an action, or show a state? If removing it loses none of those, remove it. Check the IA map first: never cut the only place a must-have question is answered.

For every motion, ask: *if this were switched off, what would the visitor lose?* Nothing → cut it. Information → it's working, keep it. Only the feel of the concept → keep it only if it's one of the few expressive moments. Cut generic motion, not the concept's motion: a fade-up that any page could have goes; the signature motion that makes the visitor feel the concept stays, even though it carries no information. Typical cuts: glows, decorative gradients, extra labels that repeat what an image already says, containers wrapping things that don't need wrapping, highlight colors with no meaning, custom controls that look worse than native platform components. Tighten type size, spacing, and copy afterward.

Show the user a list of what was cut, and a before/after screenshot.

### Technique 7: AI-tells audit

Run the checklist in `references/ai-tells.md` — visual, interaction, and copy tells. Run visual and copy as **separate passes** so the user can see what each one changed. For each tell found: where it is, the smallest fix, then apply it. Keep the user's meaning, specific facts, and jokes intact.

### Technique 8: The human writes the key lines

Copy is where the average survives longest, and no checklist writes the sentence the user would actually say. Don't finalize these yourself — hand them to the user:
1. Main headline
2. Primary button
3. Empty state(s)
4. Error state(s)

Offer your draft as a placeholder and the test: *read it aloud — if you wouldn't say it to a customer face to face, rewrite it.* Drop the user's lines in when they send them.

**Checkpoint 3 (final):** Final screenshots, a short summary of the whole run (directions explored, chosen direction, critic scores per iteration, cuts, tells fixed, money spent), and the list of lines still waiting for the user's hand. *Guide:* "Send me your own wording for each line below (one line each is fine); I'll drop them in. Say 'done' if the page is ready."
