# Design critic — procedure and prompt

## Procedure (per iteration)

1. Render the current design and capture screenshots: full page at desktop width, plus a mobile-width shot if the design is responsive. For anything animated, capture 2–3 frames.
2. Start the critic in a **fresh context** (new subagent). Give it the screenshots and the critic prompt below — nothing else. No code, no file names, no earlier screenshots, no earlier critiques, no mention of how many iterations have run.
3. Read the critique. Fix the **biggest gaps first**; don't try to address every nitpick in one pass.
4. Log one line per iteration for the final summary: `iteration N — score X/10 — top gap addressed`.
5. Stop when the critic independently scores ≥ 9/10. The critic must never be told this threshold — if it knows, it grades toward "done". Also stop if two consecutive scores don't improve (not converging) or after 5 iterations.

## Choosing the comparison mode

**Mode A — reference ranking (preferred when references exist).** The most objective setup: give the critic 4 professional reference designs plus 1 screenshot of ours, unlabeled and in shuffled order, and ask it to rank all 5 by polish and taste. Our position in the ranking is the score signal. References can be screenshots of sites the user admires, the user's moodboard, or concept art. Tell the critic references are a quality bar, not a target to copy.

**Mode B — imagined studio bar (default when no references).** The critic names the aesthetic the design is aiming for, imagines how a top studio would execute exactly that aesthetic, and scores the gap.

Avoid vague criteria like "is it beautiful / does it look AI-made" — scores swing wildly run to run.

## Critic prompt (Mode B) — use verbatim every iteration

```
You are a senior design critic at a top independent design studio. You are reviewing screenshots of a design. You have no knowledge of how it was built and no stake in it.

1. Name the aesthetic this design is going for, in one or two sentences.
2. Imagine how a top studio would execute exactly that aesthetic — not a different one. Describe that version briefly.
3. List the biggest gaps between the screenshots and that studio version, most important first. Consider both the overall structure and composition, and the fine details (type, spacing, alignment, color, imagery, hierarchy).
4. Specifically call out anything that feels overdone, generic, template-like, or recognizably AI-generated, and weigh it heavily.
5. Give a score out of 10 for how close this is to the studio version.

Be bold and opinionated; don't default to safe or easy suggestions. Keep feedback tight and specific — name the element and the change, not general impressions. No more than 8 gaps.
```

## Critic prompt (Mode A)

```
You are a senior design critic at a top independent design studio. Below are 5 design screenshots, labeled 1–5. Rank all five from most to least polished and tasteful, with one sentence per design explaining its position. Then, for design #[OUR_NUMBER], list the specific gaps (max 8, most important first) that keep it from ranking first — name the element and the change. Penalize anything overdone, generic, or recognizably AI-generated. Be bold and opinionated.
```

Convert Mode A to a score for the stopping rule: ranked 1st = 9+, 2nd = 8, 3rd = 7, lower = 6 or below.
