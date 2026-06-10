---
title: "Canon Structure Notes"
layer: canon
type: meta
---

# Canon Structure Notes

## Top-level layout

vault/canon/ follows a per-game folder structure. Each game has its own directory under games/. No cross-game pages: every page belongs to exactly one game.

vault/canon/index.md is the entry point and nav hub only. No game content there.

## Per-game folder convention

Each game directory contains:
- index.md: overview, what the game is, navigation to sub-pages. Kept as a single page even if substantial.
- Flat pages for top-level topics: movement.md, health-and-armor.md, getting-started.md, console.md, controls.md, weapons.md (if the game has few enough weapons for one page), gametypes.md (same), powerups.md.
- Sub-folders only when a topic has 3+ substantial pages: weapons/, gametypes/, modding/.

## Weapons: folder vs. flat

Warfork and Quake Live have weapons/ sub-folders because each weapon has enough distinct mechanics, stats, and competitive role to warrant its own page. Both have 8-9 weapons.

Open Arena, Quake III, Reflex, and Xonotic use a single weapons.md because their weapon coverage is reference-level (stats + brief notes), not deep per-weapon analysis. If any of these grow to full per-weapon coverage, split to weapons/.

## Gametypes: folder vs. flat

Warfork and Quake Live use gametypes/ sub-folders (5-10 modes each, meaningful per-mode content).

Open Arena, Quake III use gametypes.md (brief, no per-mode depth warranted yet).

Reflex uses modes.md because "modes" is the in-game terminology.

## Modding sub-folder

Warfork modding/ contains: index.md (nav + engine overview), server-hosting.md, custom-gametypes.md, custom-huds.md, custom-shaders.md, gametype-scripting-reference.md.

Quake Live modding/ contains: index.md (minqlx reference, factories format, physics mode), server-hosting.md (ports, server.cfg, Docker, RCON).

Rule: index.md holds the conceptual/API reference. Operation-specific pages (server-hosting) focus on deployment and link back to index for details. No duplication of field tables or capability lists.

## Games without sub-folders

Reflex, Open Arena, Xonotic, Quake III: flat per-game directories only. Topics are scoped to what's actually been written. Add sub-folders if/when a topic generates 3+ pages.

## Xonotic note

xonotic/gameplay.md covers health/armor, sound awareness, console, competitive settings. It does not overlap with index.md. index.md is the overview; gameplay.md is the mechanical detail. Both are needed.

## Thin-file decision log

QL weapons/shotgun.md and weapons/gauntlet.md are intentionally short. Each covers a single weapon with limited complexity. Short is correct; merging into a weapons index page would bury distinct content under a wall of text.

QL gametypes/ffa.md and gametypes/tdm.md are similarly brief. Content is factory-verified and correct. Short pages are the right call for simple modes.
