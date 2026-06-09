---
title: Movement
game: reflex
layer: canon
type: mechanic
tags: [reflex, movement, strafe-jump, air-control, bunny-hop, rocket-jump, plasma-climb]
confidence: high
sources: [reflex-casual-ruleset-source, reflex-sushi-ruleset-source, reflex-reflexfiles-movement-physics-archived]
promoted: 2026-06-10
canon_attempts: 1
---

# Movement

## Physics Origins

Reflex uses a variant of Challenge ProMode Arena (CPMA) physics. The lineage is: Quake 3 (VQ3) → CPMA mod → Reflex CPM physics.

Newborn, one of the Reflex developers, was involved in the original creation of CPMA for Quake 3. The Reflex engine was built from scratch using DX11: nothing was ported from Quake 3, but the physics were reconstructed to match the CPMA feel.

Key difference from VQ3: CPM allows full directional air control. Holding W in the air steers toward the look direction. Side-strafing (A/D only) without W is reduced in efficiency. VQ3 has limited air control; CPM and Reflex use forward-key directional steering.

Reflex-specific addition over CPMA: the triple jump. VQ3 and CPM support double jump. Reflex allows stacking a third jump. The physics variant is called "Reflex CPM physics" with no formal unique name.

## Constants

| Constant | Competitive | Sushi | Casual |
|---|---|---|---|
| Ground speed | 320 u/s | 320 u/s | 320 u/s |
| Crouch speed | 120 u/s | 120 u/s | 120 u/s |
| Jump velocity | 255 u/s | 270 u/s | 255 u/s |
| Double jump velocity | 105 u/s | 105 u/s | 105 u/s |
| Gravity | 750 | 800 | 750 |
| Ground acceleration | 4000 | 4000 | 4000 |
| Ground friction | 6.0 | 5.0 | 6.0 |
| Air acceleration | 0.95 | 1.0 | 0.95 |
| Air control | 150 | 150 | 150 |
| Bunny accelerate | 60 | 70 | 60 |
| Bunny wishspeed | 30 | 28 | 30 |
| Air deceleration | 2.5 | 1.5 | 2.5 |

`gconst_player_isbullet 1` applies in all rulesets: the player collides as a point rather than a capsule.

Competitive and Casual share identical movement constants. Sushi has higher jump velocity (270 vs 255), higher gravity (800 vs 750), lower ground friction (5 vs 6), and lower air deceleration (1.5 vs 2.5).

## Strafe-Jumping

Reflex uses CPMA-style physics. Air control value is 150 in all three rulesets. Holding W in the air and moving the mouse steers the player toward the look direction while preserving speed. This allows direction changes mid-air without the momentum bleed typical of Quake-style strafe-jumping.

Bunny hop acceleration parameters differ between rulesets: Sushi uses accelerate 70 / wishspeed 28 vs Competitive's 60 / 30.

## Double Jump

A second jump can be triggered while airborne. It adds the double jump velocity (105 u/s) on top of existing vertical velocity rather than resetting it. The higher base jump velocity in Sushi (270 u/s) produces greater combined height.

## Rocket-Jumping

Rocket self-knockback multiplier (Competitive: 1.12, Sushi: 1.1) exceeds the multiplier applied to enemies (0.85 / 0.90), producing net upward or forward velocity when firing at the ground. Explosion radius in Competitive is 120 units, Sushi 125.

## Plasma-Climbing

Firing the Plasma Rifle at walls or floors beneath the player produces upward velocity via the self-knockback multiplier (Competitive: 2.0, Sushi: 1.6). The plasma cell has a small explosion radius (32 units) and full splash multiplier (1.0), making it effective for sustained vertical climbing on surfaces. Primarily used in Race mode.

## Related

- [[weapons]]
