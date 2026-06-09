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

**Gunblade:** Starting weapon in most modes. Two fire modes: the projectile (35 dmg, full self-damage) is mostly used for weapon jumping; the free melee (50 dmg) is the better damage option at point-blank and costs no ammo. Most players ignore it as a serious combat weapon but the melee is a real option at close range.

**Machinegun:** Hitscan, high fire rate, low damage per shot. Spread of 10 in both directions. 100 ammo capacity. Best use is finishing opponents below 30–40 HP rather than opening fights. Can maintain accuracy while moving. Falls off noticeably at range due to spread.

**Riotgun:** 20 pellets in a cone, up to 100 total damage at point blank. Significant stun (85ms per pellet that connects). 900ms cooldown makes every shot count: missing at close range is a major opening. NOT a spray weapon. Circle-strafing and jumping over the shooter are effective counters to the slow fire rate and conical spread.

**Grenade Launcher:** Bouncing explosive, 1250ms fuse timer. Projectile speed 1000. Full self-damage. The fuse means it doesn't detonate on contact with surfaces: only on players or when the timer expires. Useful for indirect angles, vertical coverage, and area denial. Grenade jumps are possible via self-damage + knockback. Weak mode has a slightly larger splash radius (135 vs 125).

**Rocket Launcher:** Primary close-to-mid weapon. Projectile speed 1150 (faster than the GL). Detonates on contact. 950ms reload. Full self-damage: the splash radius means firing near your feet at close range damages you. Rocket jumps are possible. One of the three primary competitive weapons (RL/LG/EB). Weak mode has slightly larger splash (135 vs 125).

**Plasmagun:** Rapid fire (100ms cooldown), projectile speed 2500. 0.5 self-damage ratio. 150 ammo capacity. Moderate damage per shot but builds quickly at close-to-mid range. The plasmaclimbing mechanic: firing at surfaces for knockback-based movement: is a core traversal technique. See [[movement]].

**Lasergun:** Continuous beam, hitscan, fires every 50ms (20 ticks/sec). The only weapon with `smooth_refire`: it fires as an uninterrupted beam rather than discrete shots. 7 damage per tick × 20 ticks = 140 DPS theoretical max. 14 knockback per tick pushes the target continuously. 300ms stun per tick. No splash, no self-damage. High ammo consumption (150 max, drains fast). The primary tracking weapon: requires keeping the beam on a moving target. One of the three primary competitive weapons.

**Electrobolt:** Long-range hitscan, 75 damage, 1250ms cooldown. No damage falloff: deals 75 at any range. 1000ms stun on hit: the highest stun of any single shot, significantly disrupting the target's movement. 80 knockback. Only 10 ammo max. The longest reload in the kit means a miss is a significant window for the opponent. Weak fire mode deals the same damage but only 40 knockback (half). One of the three primary competitive weapons.

**Instagun:** Instagib mode only. 200 damage (one-shot kill), 1300ms cooldown, instant travel. Has a small 80-unit splash radius with 0.1 self-damage ratio: not a pure hitscan like the EB, but functionally similar at practical distances. Ammo limited to 5 (strong mode) / 15 (weak mode). See [[instagib]].

---

## Primary Competitive Triad

**Rocket Launcher (close-mid) · Lasergun (mid) · Electrobolt (long).** Most high-level play centers around these three. The other weapons fill specific roles: Riotgun for close ambushes, Plasmagun for movement and sustained pressure, Machinegun for cleanup: but the RL/LG/EB combination defines the competitive meta.

---

## See Also

Link to individual weapon pages for deeper coverage: [[rocket-launcher]], [[lasergun]], [[electrobolt]], [[plasmagun]], [[riotgun]], [[grenade-launcher]], [[machinegun]]
