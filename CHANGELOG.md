# Changelog

Newest first. Each change says what changed and why.

## 2026-11-20

### Voice in Stage 0.5, copy written after the UI

User feedback: after the AI-tells audit, the copy was still choppy, hard to follow, and lacked flow and a tone that fit the topic. Copy should be written after the UI, because writing it first locks the UI in place.

- **Stage 0.5 adds the voice:** who speaks to whom, 3 words for the tone, 2–3 sample sentences, words to use and to avoid. No lengths.
- **During the build:** agents write working copy in that voice, as connected sentences rather than pasted fact fragments. Length follows the UI.
- **Copy pass at the start of Stage 3**, once the UI is stable: rewrite all copy as one connected text along the concept's journey, fitted to the real space. Small UI adjustments are allowed. A fresh agent that reads only the text checks whether it reads smoothly aloud, has fragments, flows from part to part, and fits the voice. The standard is the `anti-ai-slop-writing` or `humanizer` skill if available.
- **Stage 3 order:** copy pass → cut → AI-tells audit → the user writes the key lines.

**Why:** the AI-tells audit only removes clichés; it doesn't create flow. `content.md` is a fact table, so agents pasted it as disconnected sentences. The critic only sees screenshots, so nobody read the copy start to finish.

### Separate labels for the two lists

Key messages are labelled K1–K8 and concepts C1–C10. If the user names a bare number ("idea 8") that exists in both lists, ask which one before spending anything on it. `scripts/draw.py` strips the labels when drawing.

**Why:** in the wind-power test the user meant key message #8, the AI read it as concept #8 and built a whole direction: one build, one critic pass and about 945 image credits wasted.

### Stage 0.5 · Content and the IA map

New order: key message → content → concept (the concept defines the IA) → seed → build.

- **Stage 0.5 · Content** (`process/content.md`, shared by all directions): the visitor's questions in priority order, marked must-have or nice-to-have; answers from facts, with a visible placeholder where a fact is missing, never invented; what the visitor should feel by the end; one main action. No section order, layout or form.
- **IA map per concept:** a table of where each piece of content lives on the concept's journey. Every must-have question needs a clear place; the concept decides the order. The map goes to the builder.
- **After each critic round**, the AI checks the page against the IA map and the "should feel" line, which the critic doesn't see. A must-have question the page no longer answers counts as a gap. The cut (Technique 6) must not remove the only place a must-have question is answered.

**Why:** in the wind-power test the skill jumped from a one-sentence key message straight to the concept. Each build agent invented its own page structure, and the critic called the chosen direction "a recruitment template wearing the concept's costume". Locking the IA before the concept would give every concept the same frame, so the concept decides it.

### Removed "ban the obvious first"

The concept step no longer starts by listing the obvious concepts and excluding them. The other techniques stay.

### A concept describes the experience, not the layout

From the Kobe test, where the session admitted its own brief was "a layout description, not an ambitious brief":

- If the user answers with numbers only ("7 and 6"), ask once what they liked in each. The concept is written from those notes.
- A concept says what the visitor feels, what they see move, how the scene changes, plus a role, a verb and a rule.
- It sets at least one hard demand the build must pull off, and doesn't rule out motion unless the user wants that.
- Added an example pair: a layout description rewritten as a concept.
- **Auto mode:** the script draws 3 concepts from the AI's list of 10, with seeds logged. A model choosing from its own list keeps landing on the safe option.

### Techniques for bold concepts

Added to the concept step as ways of thinking, not sources to copy from:

- **Borrow from another field** (de Bono's lateral thinking; Koestler's bisociation). No ready-made list of fields: the AI latches onto keywords in a list instead of thinking further.
- **Change the scale or point of view** (the Magnify/Minify of SCAMPER).
- **Give every concept a visitor role, a verb and a world rule** (from game design).
- **At least 3 of 10 options should sound like they shouldn't work** (Osborn's deferred judgment; the number is ours).
- **Label each option** safe / bold / wild × strong / weak message.

The origins of these techniques come from Claude's knowledge and were not re-checked.

### Renamed to industry terms

- Stage 0 "Idea" → **Key message** (what the page says).
- "Taste pass" → **concept step**; "world" → **concept** (how the page says it: visuals, structure, motion, interaction).
- **Design direction** stays for the 3 builds in Stage 1 (each = 1 concept + 1 seed).

### Smaller changes

- Builders read `references/ai-tells.md` before building in Stage 1, instead of only at the end.
- Technique 4 just says "use the asset-generation tool you have". Removed the fallback prompts for other tools and the license-check rule.
- Removed the ask-before-spending rule. Checkpoints 2 and 3 still report what was spent.

### Motion and imagery come from the concept

After the Kobe test produced a flat page (13 still images, no video, no 3D, 2 color-change effects):

- **New ground rule:** every animation, transition and graphic comes from the page's concept. Start from the concept's verbs (pour, sear, open a gate) to make transitions. Each motion needs a job and never takes over the scroll. A static page is no longer the safe default. No sound.
- **Concept options span experience forms** (scroll-driven story, 3D space, tool, cinematic, game, non-linear). At most 3 may be a static page dressed as print.
- **Stage 1 drafts** need a signature motion and at least one transition.
- **Technique 5:** write a motion score before building. Skipping motion needs a written reason. Added `references/motion.md` with a technique map and engineering rules (reduced motion, transform/opacity, pause control, no scrolljacking).
- **Advanced techniques are not required.** Motion must be thought through and shown: demo it in the page when possible, otherwise a motion score and a frame storyboard.
- **The critic** also sees motion frame strips. A critic shown only stills rewards static pages.
- Three rules from research on concept-driven motion:
  - **Self-check:** "if this motion were switched off, what would the visitor lose?" Nothing → cut it.
  - **Budget of expressive moments:** the hero, each major chapter change, the main action. Everything else stays quiet.
  - **Minimal story:** the page is a journey, not a theme draped over sections.

No study directly compares concept-driven and generic motion on the web; this is a heuristic backed by theory.

### Assets and 3D in Techniques 4 and 5

Current models can generate assets, 3D and animation, so the skill says so, written as principles rather than tool lists, which go stale.

### Key message separate from concept

Stage 0 answers only what the page sells, to whom, and what the visitor must believe. Words about layout, visuals, structure or motion are banned there. The concept step then builds different concepts on the same message.

**Why:** in the Kobe test the key messages mixed in form, so the user had to choose the look twice.

### Stage 0, two modes, and guidance at every stop

- **Stage 0 (key message):** the AI lists 8 readings of the brief. In auto mode `scripts/draw.py` draws one with a random seed (SHA-256, modulo the list length), so the AI can't steer, and anyone can rerun the draw with `--seed`.
- **Two modes:** normal by default, auto only on request, with a warning that auto is for testing.
- **3 directions by default** (previously 3–4).
- **Stage 1 order:** concept first, seed second. Each direction = 1 liked concept + its own seed.
- **Guide the user at every stop:** what they're looking at, what's needed, how to answer (with an example), what happens next.

**Why Stage 0:** in tests, the AI left to choose landed on the same reading 5 times out of 5. When code drew from the AI's own list, 5 runs gave 5 different ideas.

## 2026-11-07

1. **Read the seed with Lenny's prompt.** The seed is a letters + digits string (instead of hex). The AI looks for "subpatterns, special numbers, anything that inspires you".
2. **Read the seed for interaction too:** navigation, motion and interaction, alongside color, layout and type.
3. **Run the taste pass without a human.** In autonomous mode the AI reacts from the visitor's point of view and marks the reaction as its own.
4. **Run everything in one go.** Wait for the critic subagent and carry on.

**Why:** internal tests on one brief (a house-building company, keyword "reputable"):

- Change 1: the old seed line got 2 of 15 directions out of familiar molds; Lenny's line got 6–7 of 15.
- Change 3: all 5 auto runs on the old version skipped the brief step.
- Change 4: 2 runs stopped midway at "waiting for the critic".

Small test (5 runs each side, 1 brief, non-blind judging), only enough to show large differences.

**Known risk:** a letters + digits string has no ready-made color codes the way hex does, so the AI picks colors itself. In the test, 5 of 15 directions landed on nearly the same rust red.
