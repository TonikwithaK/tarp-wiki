---
title: "Weapons"
game: warfork
layer: canon
type: reference
tags: [warfork, weapons, mechanics, stats]
status: canon
promoted: 2026-06-09
---

# Weapons

Stats verified against the [game source](https://github.com/TeamForbiddenLLC/warfork-qfusion/blob/master/source/gameshared/gs_weapondefs.c). Primary values reflect the **strong fire mode** (default fire), which is what most players use. Weak fire mode differences are noted per weapon.

---

## Stats Reference

| Weapon | Dmg | Pellets | Reload | Proj Speed | Self-Dmg | Knockback | Stun | Splash R | Ammo Max |
|--------|-----|---------|--------|------------|----------|-----------|------|----------|----------|
| Gunblade (strong) | 35 | 1 | 600ms | 3000 | 1.0 | 90 | 0 | 70 | 1 |
| Gunblade (melee) | 50 |: | 600ms | melee | 0 | 50 | 0 | 0 | ∞ (free) |
| Machinegun | 10 | 1 | 100ms | instant | 0 | 10 | 50ms | 0 | 100 |
| Riotgun | 5 | 20 | 900ms | instant | 0 | 7/pellet | 85ms | 0 | 20 |
| Grenade Launcher | 80 | 1 | 800ms | 1000 | 1.0 | 100 | 1250ms | 125 | 20 |
| Rocket Launcher | 80 | 1 | 950ms | 1150 | 1.0 | 100 | 1250ms | 125 | 20 |
| Plasmagun | 15 | 1 | 100ms | 2500 | 0.5 | 20 | 200ms | 45 | 150 |
| Lasergun | 7 | 1 | 50ms | instant | 0 | 14 | 300ms | 0 | 150 |
| Electrobolt | 75 | 1 | 1250ms | instant | 0 | 80 | 1000ms | 0 | 10 |
| Instagun | 200 | 1 | 1300ms | instant | 0.1 | 95 | 1000ms | 80 | 5 |

### Table Notes

- **Riotgun:** 20 pellets × 5 dmg = 100 max damage; 20 × 7 = 140 max knockback at point blank. Weak mode fires 25 pellets at 4 dmg each (same 100 total damage, different spread profile).
- **Lasergun:** 7 dmg × 20 ticks/sec = 140 DPS theoretical max. `smooth_refire=true`: the only weapon with this flag. Fires as a true continuous beam rather than discrete shots.
- **Instagun:** Instagib mode only. Ammo max of 5 in strong mode (15 in weak). Has a small splash radius of 80 units: not purely hitscan. Self-damage ratio of 0.1 applies.
- **Electrobolt:** No damage falloff at range: minimum damage equals full damage (75). The `projectile_timeout` field controls the min-damage range threshold but the min is set equal to the max, so effective damage is flat at all distances.
- **Gunblade melee (weak fire):** Free and infinite: costs no ammo. At 50 damage it actually out-damages the projectile mode (35 dmg) at close range.
- **GL/RL weak modes:** Slightly larger splash radius (135) compared to strong mode (125).
- **EB weak mode:** Same 75 damage, but only 40 knockback vs. strong mode's 80.

---

## Weapon Descriptions

**Gunblade:** Starting weapon in most modes. Two fire modes: projectile (35 dmg, 1.0 self-damage, 90 knockback, 600ms reload, 1 ammo max) and free melee (50 dmg, 64-unit range, no ammo cost). Projectile enables weapon jumps. Melee out-damages the projectile at close range.

**Machinegun:** Hitscan, 10 dmg per shot, 100ms reload, 100 ammo max. Spread of 10 in both directions. No self-damage. Stun 50ms per shot. Damage falls off in practice at range due to spread.

**Riotgun:** 20 pellets per shot, 5 dmg each, up to 100 total damage at point blank. 900ms cooldown. 85ms stun per pellet. Hitscan. No self-damage. Weak mode: 25 pellets at 4 dmg each (same 100 total, different spread profile).

**Grenade Launcher:** Bouncing explosive, 80 dmg, 125-unit splash radius, 800ms reload, projectile speed 1000. 1250ms fuse timer: detonates on players or when timer expires, not on surface contact. Full self-damage (1.0). Grenade jumps possible via self-damage and knockback. Weak mode splash radius 135.

**Rocket Launcher:** 80 dmg, 125-unit splash radius, 950ms reload, projectile speed 1150. Detonates on contact. Full self-damage (1.0). 100 knockback. Rocket jumps possible. One of the three primary competitive weapons (RL/LG/EB). Weak mode splash radius 135.

**Plasmagun:** 15 dmg per shot, 100ms reload, projectile speed 2500, 150 ammo max, 45-unit splash radius, 0.5 self-damage. 15 dmg x 10 shots/sec = 150 DPS theoretical max. Plasmaclimbing: firing at surfaces generates knockback for movement.

**Lasergun:** Continuous hitscan beam, 7 dmg per tick, 50ms tick rate (20 ticks/sec = 140 DPS theoretical max). `smooth_refire=true`: fires as an uninterrupted beam. 14 knockback per tick, 300ms stun per tick. No splash, no self-damage. 150 ammo max. One of the three primary competitive weapons.

**Electrobolt:** Long-range hitscan, 75 dmg, 1250ms cooldown. No damage falloff at any range. 1000ms stun on hit. 80 knockback. 10 ammo max. Weak mode: same 75 dmg, 40 knockback. One of the three primary competitive weapons.

**Instagun:** Instagib mode only. 200 dmg (one-shot kill at full health), 1300ms cooldown, instant travel. 80-unit splash radius, 0.1 self-damage ratio. Ammo: 5 strong / 15 weak.

---

## Primary Competitive Triad

**Rocket Launcher (close-mid) · Lasergun (mid) · Electrobolt (long).** Most high-level play centers around these three.

---

## Related

Link to individual weapon pages for deeper coverage: [[games/warfork/weapons/rocket-launcher|Rocket Launcher]], [[games/warfork/weapons/lasergun|Lasergun]], [[games/warfork/weapons/electrobolt|Electrobolt]], [[games/warfork/weapons/plasmagun|Plasmagun]], [[games/warfork/weapons/riotgun|Riotgun]], [[games/warfork/weapons/grenade-launcher|Grenade Launcher]], [[games/warfork/weapons/machinegun|Machinegun]]
