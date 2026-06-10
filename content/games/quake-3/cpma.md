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

The mod introduced CPM physics -- a distinct movement system with full air control -- which became the foundation for Defrag's CPM mode, Quake Live's PQL (Pro mode), and the physics lineage that influenced Reflex Arena.

The recommended engine for playing CPMA today is CNQ3 (Challenge Quake 3), maintained by the same team. Download and guides at [playmorepromode.com](https://playmorepromode.com).

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

## Air Control

The defining difference between CPM and VQ3. In CPM, strafing while airborne with +forward held allows meaningful steering. Players can turn 90 degrees or more without losing momentum.

Strafe keys (A/D) handle large directional changes in the air. W-only is used for small adjustments.

## Bunny Hopping

Maintaining momentum through a series of jumps without losing speed on landing. Works in CPM, does not work in VQ3 (speed drops to ground cap on contact).

## Double Jump

Landing on a step or ramp within 400ms of a previous jump grants a height bonus on the next jump.

## Strafe Jumping

Still present and useful in CPM. Higher air acceleration (`15.0` vs `10.0`) means velocity builds faster. Combined with air control, CPM strafe jumping produces higher starting speeds than VQ3 for a given mouse input.

Circlejump speeds: VQ3 roughly 407 UPS from a good standing circlejump. CPM roughly 492 UPS under the same conditions.

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
