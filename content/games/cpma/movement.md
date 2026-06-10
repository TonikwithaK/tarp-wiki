---
title: Movement
game: cpma
type: mechanics
tags: [movement, cpm, air-control, strafe-jump, physics]
status: canon
created: 2026-06-10
updated: 2026-06-10
---

CPMA's movement is defined by the CPM physics mode. VQ3 mode is also available and behaves identically to base Q3.

## Physics Constants (CPM)

| Constant | CPM | VQ3 |
|---|---|---|
| Ground speed | 320 UPS | 320 UPS |
| Air acceleration | 15.0 | 10.0 |
| Air control | Full | Minimal |
| Bunny hopping | Yes | No |
| Double jump | Yes (400ms window) | No |
| Weapon switching | Instant | 450ms delay |
| Ramp jump | Height + directional | Height only |

## Air Control

The defining difference between CPM and VQ3. In CPM, strafing while airborne with +forward held allows meaningful steering. Players can turn 90 degrees or more without losing momentum. This makes route-finding and recovery from awkward trajectories fundamentally different from VQ3.

Strafe keys (A/D) handle large directional changes in the air. W-only is used for small adjustments.

## Bunny Hopping

Maintaining momentum through a series of jumps without losing speed on landing. Works in CPM, does not work in VQ3 (speed drops to ground cap on contact).

## Double Jump

Landing on a step or ramp within 400ms of a previous jump grants a height bonus on the next jump. Used in route design and to reach otherwise inaccessible positions.

## Strafe Jumping (CPM)

Still present and useful in CPM, but the higher air acceleration (`15.0` vs `10.0`) means velocity builds faster. Combined with air control, CPM strafe jumping produces higher starting speeds than VQ3 for a given amount of mouse input.

Circlejump speeds: VQ3 achieves roughly 407 UPS from a standing start with a good circlejump. CPM achieves roughly 492 UPS under the same conditions.

## Weapon Jumping

Rocket and grenade jumping work identically to VQ3 in terms of physics. Instant weapon switching means transitions to and from jump weapons are faster.

## Related

- [[games/cpma/index|CPMA]]
- [[games/quake-3/movement|Quake III Arena Movement]]
- [[games/defrag/index|Defrag]]
- [[games/quake-live/movement|Quake Live Movement]]
