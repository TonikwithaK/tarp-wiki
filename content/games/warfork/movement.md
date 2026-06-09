---
title: "Movement — Warfork"
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
confidence: medium
sources:
- file: raw_sources/warfork/Mechanics/Movement.md
promoted: 2026-06-09
canon_attempts: 1
---

# Movement — Warfork

Movement is a core part of competitive Warfork play. A player with strong movement is significantly harder to hit and can control map space more effectively. The basics are accessible but the ceiling is high.

## Running and Walking

The standard running speed is 320u/s. Walking (hold Alt) moves at 160u/s. Holding the jump key allows repeated jumping without speed loss — most advanced movement builds on this.

## Dashing

Dashing is Warfork's signature movement ability. A dash is a short directional burst triggered by RMB that immediately redirects movement at ground contact. Starting a run with a dash is the fastest way to gain initial speed (450u/s).

**Key rules:**
- Cannot dash while holding the jump key
- Works at any speed — enables high-speed direction changes
- One dash per second cooldown
- Can pre-hold the dash button before landing
- With no directional key held, dashes toward wherever you're looking
- If executed cleanly, no speed is lost

## Walljumping

Walljumping (RMB before touching a wall) lets players jump off walls. Combined with dashing, it enables movement sequences that can catch enemies off guard.

**Key rules:**
- Can be performed while holding the jump key (unlike dashing)
- 1.3 second cooldown
- Can pre-hold the dash button before wall contact
- Dash and walljump cooldowns are independent — walljumping immediately after a dash is valid
- Being stunned temporarily disables walljumping

## Strafing

Strafing is the fastest way to build speed without weapons. Start with a forward dash, hold spacebar to jump continuously, and strafe A/D while moving the mouse in the same direction. The strafeHUD indicator (enable with `cg_strafeHUD 1`) shows a white bar that should track inside the triangle toward its wide side — when correct the triangles turn green and speed builds. Alternate A/D to keep accelerating.

### Air Control

In the air, hold W and spacebar and move the mouse to change direction. Changing direction in air bleeds speed gradually. You can look around freely without changing trajectory by releasing all directional keys.

Note: strafeHUD only appears above 450u/s.

## Bunnyhopping

Bunnyhopping is a simpler but slower alternative to strafing — no W key required, just spacebar and A/D with mouse movement in the same direction. Common for players coming from Source games. Notably slower than proper strafing.

## Plasmaclimbing

Plasmaclimbing uses the Plasmagun (PG) to climb surfaces by firing at walls or floors beneath the player. Primarily used in Race mode on specific maps but executable in any gametype with a PG equipped.

## See Also

- [[controls]] — keybind reference
- [[weapons]] — Plasmagun details for plasmaclimbing
