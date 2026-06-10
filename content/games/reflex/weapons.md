---
title: Weapons
game: reflex
layer: canon
type: reference
tags: [reflex, weapons, competitive, sushi, casual]
confidence: high
sources: [reflex-cr2-ruleset-source, reflex-casual-ruleset-source, reflex-sushi-ruleset-source]
promoted: 2026-06-10
canon_attempts: 1
---

# Weapons

All values sourced directly from ruleset files. Three active rulesets: Competitive (CR2 merged), Sushi (NA), Casual. Where a ruleset does not override a value, the Casual file is the baseline.

The Rocket Launcher, Ion Cannon, and Bolt Rifle are the three primary competitive weapons. The Stake Launcher exists in the files but is disabled (`gconst_stakelauncher_enabled 0`).

## Damage and Reload

| Weapon | Competitive | Sushi | Casual | Reload (Comp) | Reload (Sushi) | Reload (Cas) | Type |
|---|---|---|---|---|---|---|---|
| Melee | 90 | 100 | 90 | 800ms | 1000ms | 800ms | Melee |
| Burstgun | 6×6 = 36 | 8×3 = 24 | 6×6 = 36 | 500ms | 500ms | 500ms | Projectile |
| Shotgun | 5×? pellets | 5×? pellets | 5×? pellets | 925ms | 900ms | 900ms | Hitscan |
| Grenade Launcher | 100 direct | 100 direct | 100 direct | — | — | 800ms | Projectile |
| Plasma Rifle | 15/cell | 16/cell | 16/cell | 100ms | 100ms | 100ms | Projectile |
| Rocket Launcher | 100 direct | 100 direct | 100 direct | 800ms | 800ms | 800ms | Projectile |
| Ion Cannon | 6/tick (44ms) | 7/tick (50ms) | 6/tick (44ms) | 44ms | 50ms | 44ms | Hitscan beam |
| Bolt Rifle | 80 | 80 | 80 | 1375ms | 1375ms | 1375ms | Hitscan |

Ion Cannon DPS: Competitive ~136, Sushi 140, Casual ~136.

Burstgun in Sushi has projectile speed 25000 u/s (effectively hitscan). Competitive/Casual speed is 4000 u/s. Sushi Burstgun fires 3 segments vs 6 in Competitive/Casual.

Shotgun pellet count not present in any ruleset file.

## Explosion Radii

| Weapon | Competitive | Sushi | Casual | Splash mult (Comp) | Splash mult (Sushi) | Splash mult (Cas) |
|---|---|---|---|---|---|---|
| Grenade Launcher | 200 units | 150 units | 180 units | 0.85 | 0.90 | 0.85 |
| Plasma Rifle | 32 units | 32 units | 32 units | 1.0 | 1.0 | 1.0 |
| Rocket Launcher | 120 units | 125 units | 120 units | 0.85 | 0.90 | 0.85 |

Grenade gravity: Competitive 650, Sushi 635, Casual 700. Grenade initial speed: 700 u/s in all three.

## Trace Radii

| Weapon | Competitive | Sushi | Casual |
|---|---|---|---|
| Shotgun pellets | 0.5 | 0.25 | 0.5 |
| Grenade Launcher | 1.75 | 1.0 | 1.75 |
| Plasma Rifle | 2.0 | 0.5 | 2.0 |
| Rocket Launcher | 1.1 | 1.0 | 1.1 |
| Ion Cannon beam | 0.5 | 0.25 | 0.5 |
| Bolt Rifle | 0.5 | 0.25 | 0.5 |

Sushi uses tighter trace radii across the board. Plasma Rifle drops from 2.0 to 0.5 in Sushi.

## Knockback

| Weapon | Ground (Comp) | Air (Comp) | Ground (Sushi) | Air (Sushi) | Self |
|---|---|---|---|---|---|
| Melee | 1.38 | 0.83 | 1.25 | 0.75 | — |
| Burstgun | 1.25 | 1.5 | 1.4 | 1.6 | — |
| Shotgun | 1.6 | 1.4 | 1.6 | 1.4 | — |
| Plasma Rifle | 0.85 | 1.0 | 0.925 | 1.1 | Comp: 2.0 / Sushi: 1.6 |
| Rocket Launcher | 0.85 | 1.0 | 0.90 | 1.0 | Comp: 1.12 / Sushi: 1.1 |
| Ion Cannon | 1.6 | 1.6 | 1.65 | 1.65 | — |
| Bolt Rifle | 0.5 | 0.5 | 0.5 | 0.5 | — |

Rocket self-knockback exceeds the enemy multiplier in both rulesets, enabling rocket-jumping. Plasma self-knockback (Comp: 2.0, Sushi: 1.6) enables plasma-climbing.

## Ammo

| Weapon | Max (Comp/Sushi/Cas) | Weapon pickup | Ammo pickup | Start |
|---|---|---|---|---|
| Burstgun | 20 / 30 / 20 | 10 / 15 / 10 | 5 / 15 / 10 | 10 / 30 / 10 |
| Shotgun | 12 / 16 / 12 | 6 / 8 / 6 | 3 / 4 / 6 | — |
| Grenade Launcher | 10 / 10 / 10 | 5 / 5 / 5 | 3 / 3 / 5 | — |
| Plasma Rifle | 100 / 100 / 100 | 50 / 50 / 50 | 25 / 25 / 50 | — |
| Rocket Launcher | 20 / 20 / 20 | 10 / 10 / 8 | 5 / 5 / 8 | — |
| Ion Cannon | 160 / 140 / 160 | 80 / 70 / 75 | 40 / 35 / 75 | — |
| Bolt Rifle | 10 / 10 / 10 | 5 / 5 / 5 | 3 / 3 / 5 | — |

## Projectile Speeds

| Weapon | Speed |
|---|---|
| Burstgun (Competitive/Casual) | 4000 u/s |
| Burstgun (Sushi) | 25000 u/s |
| Plasma Rifle (Competitive/Casual) | 2000 u/s |
| Plasma Rifle (Sushi) | 1750 u/s |
| Rocket Launcher (all) | 1000 u/s |
| Grenade Launcher (all) | 700 u/s initial |

Bolt Rifle range: 16384 units. Ion Cannon range: 768 units.

## Related

- [[movement]]
- [[modes]]
