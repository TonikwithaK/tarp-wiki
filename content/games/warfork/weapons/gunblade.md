---
title: "Gunblade"
game: warfork
layer: canon
type: mechanic
tags: [warfork, gunblade, weapons]
status: canon
source: source/gameshared/gs_weapondefs.c
promoted: 2026-06-09
---

# Gunblade

The Gunblade is the default starting weapon in most game modes. It has two fire modes with completely different mechanics and ammo pools.

## Fire Modes

**Strong (projectile) — Mouse1**
Fires a slow projectile (3000 speed) with a 70-unit splash radius. 35 damage, 90 knockback, full self-damage (1.0 ratio), 600ms reload. Uses `AMMO_GUNBLADE` — max 1 round. You spawn with it loaded and it does not replenish from pickups.

**Weak (melee) — Mouse2**
A close-range slash. 50 damage, 50 knockback, zero self-damage, zero ammo cost. Infinite use. The melee range is fixed at 64 units.

The melee is strictly better damage than the projectile at close range, costs nothing, and reloads at the same rate. Most players default to melee when using the Gunblade at all.

## Role

The Gunblade is not a competitive combat weapon. Its real value is in **weapon jumping** — the projectile's knockback (90) and full self-damage let you use it for movement boosts in a pinch, similar to a rocket jump but weaker and with limited ammo.

At close range where you've exhausted other options, the melee is a real 50-damage hit. That's meaningful for finishing an opponent below that threshold when you're out of rockets or LG ammo.

## Notes

- The projectile ammo (1 round max) does not drop from players or spawn on maps in standard modes — you have what you spawn with
- Melee has a fixed range of 64 units — you need to be very close
- The weapon slot is 1 — direct keybind is `1`

## Related

- [[index|Weapons]] — full stats and weapon overview
- [[movement]] — weapon jump applications
