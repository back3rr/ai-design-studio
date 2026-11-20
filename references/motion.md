# Motion techniques — which technique fits which concept

Read this when writing the motion score (Technique 5). Status checked 2026-11; browser support and tool versions change fast, so check caniuse/MDN before relying on a newer API.

## Start from the concept's verbs
Name what happens in the concept (pour, sear, open, grow, wind, drip, tear, travel), then pick the technique that can make that happen on screen. Patterns that recur in award-winning concept sites:
- **The product's own action is the transition** — pouring, dripping, tearing a wrapper.
- **Scroll is time** — the dish cooks, the season turns, the journey advances as you scroll.
- **Material simulation** — glass, cork, liquid, smoke, grass behave like the real thing.
- **An object or map is the navigation** — a vehicle you drive, plots of land you hover.
- **The product's colors mark where you are.**
A plain decorative parallax layer is the weakest form; use it only as background depth.

## Technique map
| The concept needs… | Technique | Notes |
|---|---|---|
| Scroll moving time or transforming the scene | GSAP + ScrollTrigger (free for commercial use since 2025), with Lenis for smooth scroll; or native CSS `animation-timeline: scroll()/view()` | Native CSS: Chrome/Edge 115+, Safari 26+; Firefox support uncertain — wrap in `@supports` with a fallback. Lenis turns smoothing off under reduced motion. |
| A real action played by scroll (cooking, opening, assembling) | Generated video → frame sequence drawn on `<canvas>`, scrubbed by scroll (Apple-style) | 60–180 frames; large sequences eat memory (hundreds of MB) — use smaller frames or a single still on phones. |
| One section turning into the next (gate opens, steam wipes, liquid fills) | View Transitions API (same-document is Baseline since late 2025); SVG mask / clip-path wipes; WebGL noise/displacement transition shaders on a persistent canvas (Codrops tutorials) | Cross-document view transitions: Chrome 126+, Safari 18.2+, Firefox partial. |
| A space the visitor moves through, an object to turn | three.js (WebGPURenderer with WebGL2 fallback in recent versions; pin the version), React Three Fiber, `<model-viewer>` for a single product | WebGPU ships in all major browsers but not on every device — keep the WebGL fallback. |
| Many living things (grass field, crowd, herd) | Instanced meshes with wind in the vertex shader (Codrops "Fluffiest Grass"); WebGPU compute for very large counts | |
| Smoke, steam, embers, sparks, dust | Particles + shaders (GLSL/TSL) | Keep particle counts modest on mobile. |
| Materials that react (fire, liquid, fabric, paper, glass) | Fragment shaders, post-processing | |
| Characters, icons, small state changes that react to the visitor | Rive (state machines, interactive) or dotLottie (now also has state machines); SVG morphing | |
| Things that fall, bounce, tear | Physics (Matter.js 2D, Rapier 3D) or springs (Motion) | |
| A looping element layered on the page | Transparent video: HEVC-with-alpha for Safari listed first, VP9-alpha WebM for Chrome | ffmpeg can silently drop Apple's alpha channel — check the output. |

## Generated assets into the page
- **3D:** generate (e.g. Meshy, Tripo, Rodin, Hunyuan3D, TRELLIS) → clean up if needed → `gltf-transform optimize` (Meshopt geometry, KTX2 or WebP textures). Check each tool's output license (some free tiers require credit; some releases exclude regions).
- **Video:** generate on a solid background → remove background → export transparent video or a frame sequence.
- **Textures:** generate, then make PBR maps when the material matters.

## Engineering rules
- Animate `transform` and `opacity`, not layout properties; scroll-linked motion that moves layout hurts CLS.
- Show a still first and start heavy scenes after the main content is visible; content and the main action never wait for motion.
- `prefers-reduced-motion`: replace parallax, scrubbing and large movement with crossfades or stills. Lenis and Motion handle part of this; check the rest yourself.
- Looping ambient motion longer than 5 seconds next to content needs a pause control (WCAG 2.2.2).
- Don't take over the scroll (scrolljacking): users lose their place.
- Test on a phone-sized viewport and a slow connection; give mobile a lighter version if the GPU can't keep up.

Sources: research notes in the creative-vibe-design repo, "Chuyển động theo concept trang" (2026-11).
