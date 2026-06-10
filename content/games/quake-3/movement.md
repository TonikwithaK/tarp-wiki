---
title: Movement
game: quake-3
type: mechanics
tags: [movement, strafe-jump, physics, vq3]
status: canon
created: 2026-06-10
updated: 2026-06-10
---

## Physics Constants (VQ3, patch 1.32)

| Constant | Value |
|---|---|
| Ground speed | 320 UPS |
| Max strafe speed | 320 UPS |
| Jump velocity | 270 UPS |
| Gravity | 800 UPS² |
| Ground acceleration | 10 |
| Air acceleration | 1 |
| Friction | 6 |
| Physics framerate | 125 fps (server-side) |

## Strafe Jumping

The engine checks speed limits per-axis, not on the resultant vector. When a player holds a strafe key and rotates the view, the engine calculates the wish direction as the combination of the two inputs. If the projection of current velocity onto the wish direction is below the speed cap, the engine adds acceleration in that direction -- even if total velocity already exceeds the cap.

This allows velocity to accumulate beyond 320 UPS. Timing the key presses to each jump cycle and maintaining a precise angle between the view direction and strafe direction is the core of VQ3 strafe-jumping.

Strafe variants:

| Variant | Description |
|---|---|
| Single-beat | Alternating L/R strafe each jump cycle. Most universal. |
| Double-beat | Two direction changes per jump. Used for trajectory correction in tight corridors. |
| Half-beat | Used above 1000 UPS. Minimal mouse movement, rapid key alternation. |
| Inverted | Mouse moves against strafe key direction. High muscle memory demand. |

## Air Control

Minimal in VQ3. Holding +forward while airborne contributes almost no steering. Directional changes require landing contact (groundframes) or wall interaction. This is the primary distinction from CPM physics.

## Rocket Jump

Firing a rocket at the ground and jumping simultaneously. The player takes half the splash damage and receives upward velocity from the knockback. The maximum height from a single rocket jump is approximately 1060 units (VQ3, 125fps server rate).

Self-damage is half of the rocket's splash damage. At point-blank range against a wall, this results in roughly 50 damage to the shooter.

## Plasma Climb

Rapid plasma shots against a wall at shallow angle provide upward velocity without the height spike of a rocket jump. Holding jump while shooting impairs the climbing velocity; release jump between shots.

## Grenade Jump

Similar to rocket jump but the grenade must be placed first and timed to detonate at the moment of the jump. More difficult to execute but does not require line-of-sight to the explosion.

## Physics Framerate

Server physics run at 125 fps. Client framerate does not affect physics calculations in unmodified Q3. Running at 125 fps client-side aligns client and server frames, which affects timing of certain techniques (overbounces, specific jump heights). This is relevant for Defrag in particular.

## Related

- [[games/quake-3/index|Quake III Arena]]
- [[games/cpma/movement|CPMA Movement]]
- [[games/defrag/index|Defrag]]
- [[games/quake-live/movement|Quake Live Movement]]
