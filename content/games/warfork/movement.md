---
title: "Movement"
game: warfork
layer: canon
type: mechanic
tags:
- movement
- warfork
- dash
- walljump
- strafe-jump
- air-control
- bunny-hop
- plasma-climb
confidence: high
promoted: 2026-06-09
canon_attempts: 1
---

# Movement

Values verified against the [game source](https://github.com/TeamForbiddenLLC/warfork-qfusion/blob/master/source/gameshared/gs_pmove.c).

## Speed Constants

| State | Speed |
|---|---|
| Walking (Left Alt held) | 160 UPS |
| Running | 320 UPS |
| Crouching | 100 UPS |
| Dash minimum horizontal | 450 UPS |
| Jump vertical velocity | ~297.5 UPS |
| Dash vertical velocity | ~184.9 UPS |
| Walljump vertical velocity | ~350.6 UPS |
| Strafe bunny soft cap | 925 UPS |

---

## Dash

**Trigger:** RMB (`BUTTON_SPECIAL`) while grounded.

- Horizontal speed: floor of 450 UPS. If you are already moving faster, your current speed is preserved.
- Vertical component: ~184.9 UPS upward.
- Direction: taken from your input (forward + strafe blend). If no directional input is held, defaults to your facing direction.
- Cooldown: 1000ms.
- Cannot be triggered during knockback.
- RMB must be released and re-pressed between dashes (`PMF_SPECIAL_HELD` flag). Holding RMB does not repeat the dash.
- Air control is suppressed for the first ~800ms after a dash.

---

## Walljump

**Trigger:** RMB while airborne and near a wall.

- Wall detection uses 12 radial traces. Only near-vertical surfaces register: floors and ceilings are ignored.
- Vertical velocity: ~350.6 UPS. Significantly more height than a dash.
- Horizontal velocity: clips off the wall surface, with a minimum of ~240 UPS enforced.
- Cooldown: 1300ms.
- One walljump per airtime: the cooldown must fully expire before another walljump is possible.
- Dash and walljump cooldowns are independent. You can walljump immediately after a dash lands.
- **Failed / stunned walljump:** If the walljump fires but conditions aren't fully met, you receive only ~53.1 UPS vertical and a shortened 700ms cooldown.

---

## Strafe Jumping

The primary method for building and maintaining speed above the run cap.

**How to strafe:**

1. Jump with Space.
2. Hold W + A or W + D while airborne.
3. Move the mouse smoothly in the same direction as the strafe key: left for W+A, right for W+D.
4. Land and jump again immediately with Space.
5. Alternate W+A and W+D each jump cycle to keep accelerating.

Speed gain per frame scales with the angle between your current velocity vector and your wish direction. The strafe key and mouse movement must stay aligned for the angle to remain in the gain zone.

**Soft cap:** 925 UPS. CPM-style bunny acceleration applies diminishing returns above this value. Speed can exceed 925 UPS but gains become marginal.

**StrafeHUD:** Enable with `cg_strafeHUD 1`. A white bar appears inside a triangle indicator. The bar should track toward the wide side of the triangle. Triangles turn green when the angle is correct and speed is building. The HUD only appears above 450 UPS.

---

## Air Control

Air control is distinct from strafing and only activates under specific conditions.

- **Active only when W is held without A or D.**
- Hold W and move the mouse to curve your trajectory in mid-air.
- Strength scales as cos²(angle) relative to your current velocity: most effective when your facing is close to your movement direction.
- Does not function during walljumping or knockback.
- Purpose: precise mid-air directional adjustments without triggering strafe acceleration. Useful for aiming at a landing spot after a jump without bleeding speed in an unintended direction.

---

## Bunnyhopping

Bunnyhopping is distinct from strafe jumping and builds speed more slowly.

- Jump continuously with Space: W is not required.
- Add A or D and move the mouse in that direction to slowly build speed.
- No CPM-style forward acceleration: the ceiling is lower than proper strafe jumping.
- Useful for tight turns where strafing momentum would overshoot.
- Familiar to players coming from Source games, but notably slower than Warfork strafe jumping.

---

## Plasmaclimbing

**Trigger:** Fire the Plasmagun (weapon 6) at a wall or floor near your position.

Each plasma bolt produces splash knockback on impact. Firing at a surface below or beside you propels you away from the impact point. Chain shots to sustain upward or lateral movement.

- Used to climb vertical surfaces and reach elevated positions that are otherwise inaccessible.
- Primary use case is Race mode: many race maps have routes that require plasmaclimbing.
- Functional in any gametype while carrying the Plasmagun.

---

## Speed Reference

| State | Speed |
|---|---|
| Walking (Alt held) | 160 UPS |
| Running | 320 UPS |
| Dash minimum | 450 UPS |
| Efficient strafing | 600–800 UPS |
| Strafe soft cap | 925 UPS |

---

## Related

- [[games/warfork/controls|Controls]]: key bindings including RMB, Space, and weapon slots
- [[games/warfork/weapons|Weapons]]: Plasmagun details for plasmaclimbing
- [[games/warfork/gametypes/race|Race]]: Race mode routes and movement requirements
