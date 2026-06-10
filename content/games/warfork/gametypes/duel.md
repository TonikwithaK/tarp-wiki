---
title: "Duel"
game: warfork
layer: canon
type: mechanic
tags: [warfork, duel, game-mode, 1v1]
status: canon
promoted: 2026-06-09
---

# Duel

1v1. First to the frag limit wins, or most frags when time expires. Default: no frag limit, 10 minute time limit.

## Item Timers

Source: `duel.as`

| Item | Respawn |
|---|---|
| Mega Health | 20s after the holder drops to 100 HP or below |
| Ultra Health | 40s |
| Armor | 25s |
| Weapons | 10s |
| Ammo | 20s |
| Powerups | 90s |

**Mega Health timing works differently from other items.** The 20 second timer does not start when the item is picked up. It starts when the holder's HP falls back to 100 or below. If a player picks up Mega Health and sits at 150 HP, the timer is frozen. The moment they drop to 100, the 20 second countdown begins.

This means you cannot predict the Mega Health respawn from the pickup moment alone. You have to know when your opponent took damage.

---

## Starting Conditions

Players spawn with Machine Gun and initial health/armor. Full weapon set requires map pickups. The Rocket Launcher is typically the first priority.

---

## Item Control

The Mega Health and major armor determine sustained fighting capacity. Whoever controls them consistently will have more health and armor over the course of a match.

Standard tracking method: note the pickup time, add the respawn interval, account for the HP condition on Mega Health. Most players track this mentally and use audio cues from item pickups.

---

## Duel Arena Variant

Queue-based. Players spawn with all weapons. Winner stays, next in queue enters. First to 11 frags. No item pickups, no timer tracking. Tests mechanical skill in isolation from map and item knowledge.

---

## Related

- [[games/warfork/movement|Movement]]: movement mechanics
- [[games/warfork/health-and-armor|Health And Armor]]: pickup values and armor interaction
- [[games/warfork/weapons/index|Index]]: weapon stats
- [[games/warfork/gametypes/index|Index]]: all gametypes
