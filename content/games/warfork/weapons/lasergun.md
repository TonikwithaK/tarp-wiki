---
title: "Lasergun"
game: warfork
layer: canon
type: mechanic
tags: [warfork, lasergun, weapons, hitscan]
status: canon
promoted: 2026-06-09
---

The Lasergun is the primary tracking weapon in Warfork and the mid-range weapon in the RL/LG/EB competitive triad.

## Stats

| Stat | Value |
|------|-------|
| Damage | 7 per tick |
| Fire Rate | 50ms per tick (~140 DPS sustained) |
| Self-Damage | 0 |
| Knockback | 14 per tick |
| Stun | 300 per tick |
| Splash Radius | None |
| Range | Long |

## Mechanics

The Lasergun fires a continuous hitscan beam with no travel time. Damage registers at one tick every 50ms (20 ticks/sec), dealing 7 damage, 14 knockback, and 300 stun per tick. Sustained over one second, that is 140 DPS. The beam has no spread and no damage falloff. There is no self-damage and no splash.

The Lasergun is the only weapon with the `smooth_refire` flag, which produces its continuous beam behavior rather than discrete shots.

Maximum ammo capacity is 150. At 20 ticks per second, sustained fire burns through ammo quickly.

In weak mode, the Lasergun has identical stats.

## Role

The Lasergun covers mid-range engagements in the RL/LG/EB triad.

## Counters

Breaking line of sight stops the beam entirely. The Rocket Launcher is more efficient at close range: its splash radius reduces the precision required, and damage per shot exceeds what the LG deals in the same time frame at that distance.

## Related

- [[weapons]]: full stats and weapon overview
- [[electrobolt]]: long-range triad weapon
- [[movement]]
