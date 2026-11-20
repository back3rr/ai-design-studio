# ai-design-studio

A Claude skill that runs a design-studio process, so interfaces built by AI stop looking "AI-made".

Language models pick the most likely option at every step. In design, that gives you the same page every time: purple gradient, headline on the left, graphic on the right, three feature cards. This skill pushes the other way:

- **Randomness from outside the model.** Random seed strings shape each direction, and in auto mode a script draws the key message and the concepts. The model doesn't get to pick its favorite.
- **Human taste at the right moments.** The user reacts to options and picks at a few checkpoints, without reading any code.
- **An independent critic.** A fresh agent judges each version from screenshots only, over several rounds.
- **Subtraction.** The last stage cuts what doesn't earn its place and removes common "AI-made" tells.

## How it works

| Stage | What happens | Where the user comes in |
|---|---|---|
| **0 · Key message** | 8 readings of the brief: what the page says, to whom, and what the visitor must believe. No layout or visuals yet. | Pick one (K1–K8) |
| **0.5 · Content** | The visitor's questions in priority order, answers from facts, what they should feel, one main action, and the voice. | Correct and add |
| **1 · Discover** | About 10 creative concepts (C1–C10). Each liked concept gets an IA map and its own seed, then becomes one of 3 rough directions, motion included. | React to concepts, then pick a direction (Checkpoint 1) |
| **2 · Define** | Deepen the chosen direction: critic loop, generated assets, motion that comes from the concept. | Review the result and score (Checkpoint 2) |
| **3 · Deliver** | Copy pass on the finished UI, cut, AI-tells audit. | Write the key lines (Checkpoint 3) |

Skip Stage 0 if the brief already has a clear key message. Scale down for quick mockups: one critic pass and the cut may be enough.

### Two modes

- **Normal (default):** the user picks at every stop.
- **Auto:** only when the user asks for it. A script draws the key message and the concepts; the AI makes the other picks and logs its reasons. Use it to test the skill, not for real work: the skill's value is human taste.

## Install

**Claude Code:** copy this folder to `~/.claude/skills/ai-design-studio/`.

**claude.ai:** upload the folder as a skill.

Screenshots are required for the critic loop. If Playwright isn't installed, the skill helps set it up.

## Usage

Ask Claude to design or restyle an interface. The skill triggers on its own:

```
Design a landing page for a wind power company
```

```
This dashboard looks generic. Redesign it.
```

To run without stopping, add "run in auto mode".

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | The process |
| `references/critic.md` | Critic prompt and procedure |
| `references/ai-tells.md` | Common "AI-made" patterns to avoid |
| `references/motion.md` | Which motion technique fits which kind of concept |
| `scripts/draw.py` | Draws one line at random from a list, with a logged seed so any draw can be reproduced |

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Sources

- The seed technique is adapted from *String Seed of Thought* (Sakana AI) and Anshu Chimala's seed prompt on Lenny's Newsletter.
