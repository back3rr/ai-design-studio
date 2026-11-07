---
name: "ai-design-studio"
description: Run a studio-style design process that pushes AI-built UI away from generic "AI slop" — seed-string exploration, ambitious briefs, an independent screenshot-only design critic loop, purposeful image/video generation, subtraction, and an AI-tells audit. Use this skill whenever the user asks to design, build, redesign, restyle, or polish any visual interface — landing page, website, app screen, dashboard, mockup, product page, giao diện, trang landing, UI — or complains that a design looks generic, bland, template-like, or "AI-generated", even if they don't ask for a process.
---

# AI Design Studio

LLMs pick the most likely token at every step, so every design decision drifts toward the safest, most average choice: purple gradient, headline left, graphic right, three feature cards. Good design does the opposite — it commits to a point of view and makes deliberate, sometimes uncomfortable choices. This skill compensates in three ways: bring randomness and taste in from outside the model, judge the work with a critic that has no stake in the code, and subtract aggressively at the end.

The process has three stages — **Discover → Define → Deliver** — with a human checkpoint after each. The user's taste is the scarcest input; spend their attention at the checkpoints, not on every small decision.

## Ground rules

- **The user reviews output, not code.** Every checkpoint shows screenshots (before/after side by side when something changed) and a short plain-language summary of what changed and why. Never ask the user to read code to make a decision.
- **Talk to the user in the language they write in.** Keep the design itself in whatever language the product needs.
- **Ask before spending money.** Image/video generation APIs cost real money. Before the first paid call in a session, state which service, roughly how many generations, and wait for a yes.
- **Never commit secrets.** API keys live in a gitignored file (e.g. `.env.agents`), are used only during development, and never ship in product code.
- **Run to the end.** Run the whole process in one go. When you hand work to a subagent (the critic, a direction build), wait for its result and carry on; don't end your turn while steps remain.
- **Scale to the job.** A quick mockup may only need Discover + one critic pass + the cut. Run the full process for things that will ship. Say which path you're taking and why.

## Before starting

Confirm (ask only for what's missing): what the product is and who it's for, the deliverable (single page, app screen, set of screens), any brand constraints (existing colors, fonts, BRAND.md/design.md), and the platform (web, iOS, Android). If the user has an existing brand system, it overrides seed-string randomness for anything the brand defines — use the seed only for what's left open.

Check that you can take screenshots of rendered output (e.g. Playwright: `npx playwright screenshot <url> shot.png`). The critic loop depends on it. If it isn't available, help install it before going further.

---

## Stage 1 — Discover: go broad before going deep

### Technique 1: Seed strings for real variety

Asking the model to "be random" or "be unique" produces output that *sounds* random but lands in the same neighborhood every time. Real variety has to come from outside the model (adapted from Sakana AI's String Seed of Thought).

For each direction you explore:
1. Generate a long, random alphanumeric string using a shell script, e.g. `LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c 48`.
2. Define the creative direction (color scheme, layout, typography, navigation, motion, interaction, etc.) based on the string. Look beyond the surface for subpatterns, special numbers, anything that inspires you. Write the derivation down in one or two lines so it's traceable.
3. Use your judgment to bring this direction to life and make it look great.
4. Don't reveal the string in the design. It's only for your inspiration.

Default: produce **3–4 directions** in parallel (separate files/routes), each from its own seed, so the user can compare.

### Technique 2: Ambitious briefs, steered by the user's taste

A brief that names a whole world for the page to live in ("each section is a still from a pixel-art game", "the product is an isometric city where features are neighborhoods", "radically asymmetric, dissonant, uncomfortable negative space — but still good") gives the model a vision to make decisions from, instead of improvising safe ones.

When the user doesn't have a world in mind, run a short taste pass:
1. List many design-language ideas, one line each. Broad, not deep. Include a few that sound like they shouldn't work.
2. Ask the user to react to two or three: what they like, what feels tacky, what's missing.
3. Write the build brief **from the user's notes**, including what to avoid. Pasting the model's own ideas straight back into the model is how everyone ends up with the same page.

When no user is available (they asked you to decide everything yourself), don't skip the taste pass: do step 1, then react to two or three ideas yourself from the point of view of the people the page is for, then write the brief from those notes. Mark the reactions as your own, not the user's.

Don't discard a direction because it sounds unworkable — models often surprise. If it fails, throw it away and note the prompt; retry it when a newer model is available.

**Checkpoint 1:** Show screenshots of every direction side by side, each with its one-line concept. The user picks one (or asks to combine/redo). Don't proceed without a pick.

---

## Stage 2 — Define: give the chosen direction its own identity

First drafts still lean on stale structure even when the surface looks fresh. This stage deepens one direction.

### Technique 3: Independent critic loop

The agent that wrote the code can't judge it objectively — it remembers its effort and its reasons. Use a separate critic that sees **only screenshots**, never code, earlier versions, or earlier critiques.

- Use the **most capable model available** for the critic and a cheaper/faster one for implementation if the environment allows choosing. The critic produces little output, so a strong model here buys taste cheaply.
- Use the exact critic prompt and procedure in `references/critic.md` — read it before the first critic call. Same prompt every iteration, fresh context every time.
- The stopping bar (score ≥ 9/10) is known only to you, never told to the critic, so its scoring stays honest.
- Cap the loop: run **2 iterations first**, check whether scores are converging, and only continue if they are. Hard cap of 5 iterations; if the bar isn't reached, stop and show the user the best version with the critic's remaining gaps.

### Technique 4: Real images instead of CSS decoration

Gradients, blobs, and CSS patterns are what coding agents reach for because they're easy to type — and they're the strongest giveaway of AI design. Use generated imagery (optionally combined with shaders or 3D) where it adds material, space, mood, or state.

- Every image needs a job. If a gradient could do the same job, either generate a better image or leave it out.
- Use whatever image tool is available (built-in image generation, a connected generation service, or an API key the user provides). Ask before the first paid call.
- Check the result frame by frame in the browser, especially anything animated.

### Technique 5: Video for motion that code can't fake

Use only when motion would genuinely improve the design. Two proven uses:
- **Layerable animated graphic:** generate a looping clip on a solid background, then remove the background (chroma key for simple cases, a video matting model for complex ones). For glass/refraction effects, render the object over the page's actual background colors *first* so the refraction is baked in, then remove the background.
- **State transitions:** generate a still for state A, generate a clip from A to B with a video model that has strong physics/consistency, use the last frame of that clip to seed the next transition, then play the clip on an action or scrub it with scroll/swipe.

An aggregator (e.g. fal.ai) lets you pick a current model without separate integrations. Video is the most expensive step — always confirm cost first.

**Checkpoint 2:** Show before/after screenshots of the Define stage, the critic's final score and any remaining gaps, and what was spent on generation.

---

## Stage 3 — Deliver: polish by subtraction

### Technique 6: Cut everything that doesn't earn its place

Models add; they almost never delete, because deleting feels risky. Restraint is what makes a design read as premium. For every element, ask: does it carry information, enable an action, or show a state? If removing it loses none of those, remove it.

Typical cuts: glows, decorative gradients, extra labels that repeat what an image already says, containers wrapping things that don't need wrapping, highlight colors with no meaning, custom controls that look worse than native platform components. Tighten type size, spacing, and copy afterward.

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

**Checkpoint 3 (final):** Final screenshots, a short summary of the whole run (directions explored, chosen direction, critic scores per iteration, cuts, tells fixed, money spent), and the list of lines still waiting for the user's hand.
