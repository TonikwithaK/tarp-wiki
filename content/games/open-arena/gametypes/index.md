---
title: "Gametypes"
game: open-arena
layer: canon
type: reference
tags: [open-arena, gametypes]
status: canon
promoted: 2026-06-10
---

Set via console: `g_gametype <value>` then `map_restart`. Must be set before the `map` command in server config files.

| g_gametype | Gametype |
|------------|----------|
| 0 | Free For All |
| 1 | Tournament (1v1) |
| 2 | Single Player Deathmatch (SP only) |
| 3 | Team Deathmatch |
| 4 | Capture The Flag |
| 5 | One Flag Capture |
| 6 | Overload |
| 7 | Harvester |
| 8 | Elimination |
| 9 | CTF Elimination |
| 10 | Last Man Standing |
| 11 | Double Domination |
| 12 | Domination |

`g_gametype 2` is not intended for multiplayer. Avoid it on public servers.

## Special Options

Instantgib, All Rockets, and Vampire Mode can be applied as modifiers on top of standard gametypes.

## Related

- [[games/open-arena/index\|Overview]]
- [[games/open-arena/weapons/index\|Weapons]]
- [[games/open-arena/health-and-armor\|Health and Armor]]
