---
title: "Instagun"
game: warfork
layer: canon
type: mechanic
tags: [warfork, instagun, weapons, instagib]
status: canon
source: source/gameshared/gs_weapondefs.c
promoted: 2026-06-09
---

# Instagun

The Instagun is exclusive to Instagib mode. It is not available in standard gametypes.

## Stats

200 damage, instant travel (hitscan), 1300ms cooldown, 80-unit splash radius, 0.1 self-damage ratio, 95 knockback, 1000ms stun. Strong mode ammo max: 5. Weak mode ammo max: 15.

The 200 damage is a one-shot kill against any player at full health. The 80-unit splash means a shot that lands near a player but misses directly can still kill — the splash radius is small but real.

## Mechanics

Despite being hitscan like the Electrobolt, the Instagun has a splash component. A near-miss inside 80 units still deals splash damage — at 200 base with no minimum, a close miss can still connect for enough to kill.

The 1300ms cooldown is the longest of any weapon in the game — 50ms longer than the Electrobolt. Every missed shot is a significant window.

## Role

In Instagib, everything reduces to: hit your shot, don't get hit. There is no health management, no item timing, no weapon switching. Movement becomes the only defense — constant strafing and air control to avoid being a predictable target.

The Instashield and Instajump modifiers (when enabled by the server) add a layer on top of this:
- **Instashield**: brief invulnerability, used to push aggressively or absorb a shot
- **Instajump**: enhanced jump height and speed for more dynamic aerial movement

## Comparison to Electrobolt

The Instagun and Electrobolt share the same aim requirement — hitscan, single shot, punishing cooldown — but differ in key ways:

| | Instagun | Electrobolt |
|---|---|---|
| Damage | 200 (one-shot) | 75 |
| Cooldown | 1300ms | 1250ms |
| Splash | 80 radius | none |
| Ammo max | 5 / 15 | 10 |
| Self-damage | 0.1 | 0 |

The Instagun's splash gives it a slight margin for near-misses that the EB doesn't have.

## Related

- [[index|Weapons]] — full stats and weapon overview
- [[../gametypes/instagib|Instagib]] — the gametype this weapon belongs to
- [[electrobolt]] — the closest standard-mode equivalent
