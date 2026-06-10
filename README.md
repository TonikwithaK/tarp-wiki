# TARP: The Arena Revival Project

A knowledge base for competitive Arena FPS. Covers mechanics, movement, weapons, gametypes, and modding. Facts checked against source code or first-hand testing before publishing.

**Site:** [tonikwithak.github.io/tarp-wiki](https://tonikwithak.github.io/tarp-wiki)
**Deployed via:** GitHub Actions | See [ACKNOWLEDGEMENTS.md](./ACKNOWLEDGEMENTS.md)

---

## Games

| Game | Theme |
|---|---|
| [Warfork](https://tonikwithak.github.io/tarp-wiki/games/warfork/) | Cyan / Coral |
| [Quake Live](https://tonikwithak.github.io/tarp-wiki/games/quake-live/) | Red / Black / White |
| [Reflex Arena](https://tonikwithak.github.io/tarp-wiki/games/reflex/) | Grey / Red |

---

## Content structure

Content lives in `vault/canon/`, which maps directly to the public site via Quartz. Each game gets its own subdirectory:

```
vault/canon/
  games/
    warfork/
    quake-live/
    reflex/
```

Pages in those directories are published. Pages outside `canon/` are not.

---

## Adding a game theme

Each game has one SCSS file in `quartz/styles/games/`. To add a new game:

1. Create `quartz/styles/games/_<game-slug>.scss`
2. Use an existing file as a template
3. Set the slug selector: `[data-slug^="games/<game-slug>"]`
4. Add `@use "./games/<game-slug>";` to `quartz/styles/custom.scss`

Game theme variables:

```scss
--game-accent      // primary accent color
--game-accent-alt  // secondary accent (optional)
--game-muted       // low-opacity tint for backgrounds
```

---

## Page helpers

Drop these HTML blocks into any markdown page. They inherit the active game theme automatically.

**`callout-info`** — informational note, tinted with game accent:
```html
<div class="callout-info">Strafe-jumping scales with framerate below 125 fps.</div>
```

**`callout-warn`** — warning or caveat, yellow border:
```html
<div class="callout-warn">Server-side values differ from client-side display.</div>
```

**`stat-block`** — monospaced stat with a label:
```html
<div class="stat-block"><strong>320 u/s</strong> Ground speed (default)</div>
```

**`version-note`** — version context, muted italic:
```html
<div class="version-note">Changed in v2.1.0 — knockback values reduced by 15%.</div>
```

---

## LLM access

Content index at [tonikwithak.github.io/tarp-wiki/llms.txt](https://tonikwithak.github.io/tarp-wiki/llms.txt).
