---
title: Quake III Arena
game: quake-3
type: index
tags: [quake3, id-tech-3, arena-fps]
status: canon
created: 2026-06-10
updated: 2026-06-10
---

Quake III Arena is a multiplayer first-person shooter developed by id Software and released December 2, 1999. It runs on id Tech 3, the same engine that underlies ioquake3, OpenArena, and several other games in this wiki.

Unlike its predecessors, Q3 has no traditional single-player campaign. The game is built entirely around the arena format: players compete in timed matches on hand-crafted maps for frags, flags, or score. A bot roster simulates multiplayer for offline play.

The source code was released August 19, 2005 and is available on [GitHub](https://github.com/id-Software/Quake-III-Arena).

## Physics

Q3 uses what is now called VQ3 (Vanilla Quake 3) physics. Ground speed is 320 UPS. Air control is minimal when holding forward. The primary movement technique is strafe-jumping: combining a strafe key with mouse movement to exploit the engine's per-axis speed check and accumulate velocity beyond the base cap.

VQ3 physics became the reference point for every mod that followed. CPMA diverged from it deliberately. Quake Live's default mode (VQL) is VQ3 with minor modifications. Defrag runs both VQ3 and CPM as separate physics modes.

## Weapons

9 weapons. Gauntlet and Machine Gun are spawn weapons. Detailed stats on the weapons page.

## Gametypes

4 gametypes in base Q3: FFA, 1v1 Tournament, Team Deathmatch, Capture the Flag. Team Arena added more.

## Mod Ecosystem

Q3's open architecture and eventual source release produced a large mod ecosystem. The ones with enough community and documentation to warrant pages here:

- **CPMA** (Challenge ProMode Arena): rewrote movement physics, rebalanced weapons, added air control. The origin of CPM physics used across Defrag, Quake Live PQL, and Reflex Arena.
- **Defrag**: movement-focused speedrunning mod. Runs both VQ3 and CPM physics. Active community at defrag.racing.
- **ExcessivePlus**: high-damage, high-speed gameplay variant. No longer actively maintained but present in OA servers historically.
- **OSP**: match facilitation mod. No physics changes. Primarily a tournament toolset.

## Source Ports

The original binary does not run well on modern systems. Recommended:

| Port | Notes |
|---|---|
| [ioquake3](https://ioquake3.org/) | Most authentic. SDL-based, multi-platform. |
| [Quake3e](https://github.com/ec-/Quake3e) | Competitive-focused. Bug fixes, security, QoL. |
| [Spearmint](https://github.com/zturtleman/spearmint/) | MSAA, XInput, 4-player split-screen. |

Config lives at `baseq3/q3config.cfg`. Edit settings via `autoexec.cfg` -- `q3config.cfg` is auto-generated and will be overwritten.

## Related

- [[games/quake-3/movement|Movement]]
- [[games/quake-3/weapons|Weapons]]
- [[games/quake-3/gametypes|Gametypes]]
- [[games/quake-3/getting-started|Getting Started]]
- [[games/quake-3/cpma|CPMA]]
- [[games/quake-3/defrag|Defrag]]
- [[games/quake-live/index|Quake Live]]
