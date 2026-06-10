---
title: Health and Armor
game: reflex
layer: canon
type: reference
tags: [reflex, health, armor, items, mega, carnage, pickups]
confidence: medium
sources: [reflex-reflexfiles-armor-health-archived]
promoted: 2026-06-10
canon_attempts: 1
---

## Health Pickups

| Pickup | Value | Respawn |
|---|---|---|
| Small health | 5 | 25s |
| Medium health | 25 | 25s |
| Large health | 50 | 25s |
| Mega Health | 100 | 30s after carrier takes 100 damage |

Health above 100 decays at 1 HP/second. Maximum health: 200 (overheal via pickups).

Mega Health respawn timer starts only after the player who picked it up has received 100 cumulative damage. Then 30 seconds from that point.

## Armor

| Tier | Absorption | Added on Pickup | Max (no shards) |
|---|---|---|---|
| Green | 50% | 50 | 100 |
| Yellow | 66% | 100 | 150 |
| Red | 75% | 150 | 200 |

All armor respawns 25 seconds after grab. No degeneration between pickups.

Absorption: incoming damage is split between armor and health. At 75% absorption (Red), a 100-damage rocket costs 75 armor and 25 health.

Shards add 5 armor each. Max 200 with shards. Shards do not change the current absorption tier. If no armor is held, shards default to Green tier.

## Armor Pickup Restrictions

Lower-tier armor cannot be picked up unless current armor is below threshold:

| Armor | Can pick up if... |
|---|---|
| Green | Below 100 Green, or below 75 Yellow, or below 66 Red |
| Yellow | Below 150 Yellow, or below 133 Red |
| Red | Below 200 Red |

At 131+ Red armor, Yellow armor cannot be picked up.

## Rocket Survivability

| Loadout | Rockets to die |
|---|---|
| No armor | 1 |
| Green armor | ~2 |
| Yellow armor | ~3 |
| Red armor | ~4 |
| Any tier + Mega Health | +1 |

Each tier adds approximately one rocket's worth of survivability.

## 1v1 Item Layout

Standard 1v1 maps use a 1 Red Armor / 2 Yellow Armor / 1 Mega Health item layout. Controlling player holds Red Armor; disadvantaged player takes Yellow Armor + Mega Health. Stack difference is one rocket or less.

## Powerups

| Powerup | Effect | Duration | Respawn |
|---|---|---|---|
| Carnage | 4x damage multiplier | 30s | 90s after grab |

Carnage drops on death. The drop timer pauses but the respawn timer continues. Carnage spawns in CTF every 90 seconds, typically near map center.

## Arena Mode Spawn Loadout

Players spawn in Arena modes (AFFA, ATDM, A1v1) with 200 armor / 100 health and all weapons. No item pickups during rounds.

## Related

- [[weapons]]
- [[modes]]
