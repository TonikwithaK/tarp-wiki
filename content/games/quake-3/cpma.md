---
title: CPMA
game: quake-3
type: reference
tags: [cpma, promode, cpm, quake3, arena-fps]
status: canon
created: 2026-06-10
updated: 2026-06-10
---

Challenge ProMode Arena (CPMA) is a modification for Quake 3 Arena focused on competitive gameplay. Originally called Challenge ProMode (CPM), it was created in May 1999 by Richard "Hoony" Sandlant shortly after the release of the Q3 beta. It became the standard competitive mod for Q3 after the Cyberathlete Professional League adopted it, and was used in the Electronic Sports World Cup (ESWC).

Three things define CPMA as distinct from base Q3: full air control, the held Mega Health, and the double jump. Everything else -- instant weapon switching, rebalanced weapons, additional gametypes -- matters, but these three are what the mod is built around.

The recommended engine for playing CPMA today is CNQ3 (Challenge Quake 3), maintained by the same team. Download and guides at [playmorepromode.com](https://playmorepromode.com).

## Air Control

In base Q3 (VQ3), holding forward while airborne contributes almost nothing to steering. Directional changes require landing contact or wall interaction. In CPM, strafing while airborne steers the player meaningfully -- turns of 90 degrees or more are possible without losing momentum. A/D handles large changes, W handles small adjustments.

This changes the geometry of the game. Routes that require sharp mid-air turns are not possible in VQ3. In CPM they are expected. The skill floor for using air control effectively is high; the ceiling is what separates top-level CPM movement from everything else.

Air acceleration in CPM is `15.0` vs VQ3's `10.0`. Combined with air control, circlejump speeds are higher: roughly 492 UPS in CPM vs 407 UPS in VQ3 from a standing start.

## Held Mega Health

In base Q3, the Mega Health respawns on a fixed timer from the moment it is picked up -- the carrier has no influence over when it comes back.

CPMA's behavior depends on the ruleset and gametype. In the CPM duel ruleset, the Mega Health timer does not start until the carrier's health drops to 100 or below -- a player sitting above 100 HP indefinitely delays the respawn. This makes Mega Health a strategic resource in a way it is not in VQ3: controlling it means not just picking it up but understanding when to let health decay and when to hold it.

Other gametypes in CPMA (CTF, TDM, etc.) use simple Mega Health -- the same fixed respawn timer as VQ3.

## Double Jump

Landing on a step or ramp within 400ms of a previous jump grants additional upward velocity on the next jump. The timing window is tight. Used correctly it allows players to reach positions that would require a weapon jump in VQ3, and it chains with air control to extend routes significantly.

It is not a second press of the jump key -- it is the physics response to landing at the right moment in a jump arc. Maps designed for CPM are built with this in mind.

## Physics Constants (CPM vs VQ3)

| Constant | CPM | VQ3 |
|---|---|---|
| Ground speed | 320 UPS | 320 UPS |
| Air acceleration | 15.0 | 10.0 |
| Air control | Full | Minimal |
| Bunny hopping | Yes | No |
| Double jump | Yes (400ms window) | No |
| Weapon switching | Instant | 450ms delay |
| Ramp jump | Height + directional | Height only |

CPMA supports both CPM and VQ3 physics. VQ3 mode behaves identically to base Q3.

## Ruleset Variants

| Variant | Notes |
|---|---|
| CPM / PM2 | Challenge ProMode II. Current standard. |
| PMC / PM1 | ProMode Classic. Original ruleset. |
| CQ3 | Challenge Quake 3 ruleset. |
| VQ3 | Vanilla Q3 physics. |

## Gametypes

Inherits FFA, TDM, 1v1 Tournament, and CTF from base Q3. CPMA-exclusive modes:

| Mode | Description |
|---|---|
| Clan Arena (CA) | Full loadout on spawn. No pickups. Respawn only between rounds. |
| Freeze Tag | Freeze all enemy players to win the round. Frozen players thawed by teammate contact for 3 seconds. |
| Capture Strike | CTF + Rocket Arena hybrid. Teams alternate offense and defense. |
| Not Team Fortress (NTF) | Class-based CTF. 4 classes: Fighter, Scout, Sniper, Tank. Health and armor regenerate. |
| HoonyMode | Tennis-format 1v1. Players choose spawn points, deaths score points. |

## Weapons

CPMA rebalances Q3's weapons. Instant weapon switching removes the 450ms switch delay from base Q3.

## Key Versions

| Version | Date |
|---|---|
| Beta 3 | March 24, 2000 |
| 1.0 | August 28, 2000 |
| 1.52 (latest) | March 31, 2019 |

## Related

- [[games/quake-3/index|Quake III Arena]]
- [[games/quake-3/movement|Q3 Movement]]
- [[games/quake-3/defrag|Defrag]]
- [[games/quake-live/index|Quake Live]]
