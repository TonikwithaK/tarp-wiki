---
title: Rulesets
game: reflex
layer: canon
type: reference
tags: [reflex, rulesets, competitive, sushi, casual, weapons, movement]
confidence: high
sources: [reflex-cr2-ruleset-source, reflex-casual-ruleset-source, reflex-sushi-ruleset-source]
promoted: 2026-06-10
canon_attempts: 1
---

A ruleset in Reflex is a config layer applied on top of the game that simultaneously defines weapon behavior, movement constants, and match settings. It is not a gametype or mode. Rulesets are set independently of modes. Three rulesets are active: Competitive, Sushi, and Casual.

## Competitive

Based on CR2, authored by Ramagan (EU). Merged into the base competitive ruleset. Dominant in EU.

CR2 replaced CR1. CR1 was retired because its trace radii were too large. CR2 uses smaller trace radii throughout.

- Match length: 10 minutes
- Melee: 90 dmg, 800ms reload
- Plasma: 15 dmg/cell, trace radius 2.0
- Ion Cannon: 6 dmg/tick, 44ms interval
- Grenade: 200 unit explosion radius, 650 gravity
- Rocket: 120 unit explosion radius
- Bolt Rifle: 1375ms reload
- Movement: jump 255 u/s, gravity 750, friction 6.0, air decel 2.5

Reference: https://reflex.fun/cr2

## Sushi

Authored by Soh (NA). Dominant in NA.

- Movement: jump 270 u/s, gravity 800, friction 5.0, air decel 1.5
- Melee: 100 dmg, 1000ms reload
- Plasma: 16 dmg/cell, trace radius 0.5
- Ion Cannon: 7 dmg/tick, 50ms interval (approx. 140 DPS)
- Burstgun: 3 segments at 25000 u/s, 8 dmg/segment (effectively hitscan)
- Grenade: 150 unit explosion radius, 635 gravity
- Shotgun: 900ms reload
- All primary weapon trace radii (Shotgun, Ion Cannon, Bolt Rifle) are tighter than Competitive

Sushi Discord: discord.gg/HQcPP2W

## Casual

Shares Competitive weapon values with several exceptions.

- Match length: 5 minutes (vs. 10 in Competitive)
- Item pickup timers visible to all players: `gconst_expose_timers_to_lua 1`
- `gconst_powerups_drop 1` enabled
- Plasma: 16 dmg/cell (vs. 15 in Competitive)
- Grenade: 180 unit explosion radius (vs. 200 Competitive, 150 Sushi)
- Ion Cannon ammo pickup: 75 (vs. 40 in Competitive)

## Ruleset Diff

| Constant | Competitive | Sushi | Casual |
|---|---|---|---|
| Melee damage | 90 | 100 | 90 |
| Melee reload | 800ms | 1000ms | 800ms |
| Plasma cell damage | 15 | 16 | 16 |
| Grenade explosion radius | 200 | 150 | 180 |
| Grenade gravity | 650 | 635 | 700 |
| Shotgun reload | 925ms | 900ms | 900ms |
| Ion Cannon damage/tick | 6 | 7 | 6 |
| Ion Cannon reload interval | 44ms | 50ms | 44ms |
| Burstgun segments | 6 | 3 | 6 |
| Burstgun dmg/segment | 6 | 8 | 6 |
| Burstgun projectile speed | 4000 u/s | 25000 u/s | 4000 u/s |
| Jump velocity | 255 u/s | 270 u/s | 255 u/s |
| Gravity | 750 | 800 | 750 |
| Ground friction | 6.0 | 5.0 | 6.0 |
| Air deceleration | 2.5 | 1.5 | 2.5 |
| Match time limit | 10 min | — | 5 min |
| Item timers visible | No | — | Yes |

## Related

- [[weapons]]
- [[movement]]
