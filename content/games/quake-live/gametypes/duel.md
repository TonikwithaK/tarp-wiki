---
title: "Duel"
game: quake-live
layer: canon
type: reference
tags: [quake-live, duel, game-mode, 1v1]
status: canon
promoted: 2026-06-09
---

1v1 gametype. The player with the most frags at the end of the time limit wins. If a frag limit is set, the first player to reach it wins.

## Default Settings

| Setting | Value |
|---------|-------|
| Time limit | 10 minutes |
| Score limit | 0 (disabled) |

## Starting Conditions

Players spawn with Machine Gun and 125 HP. All other weapons and items must be picked up from the map.

## Respawn Timers

Timers begin when the item is picked up. Standard values -- map-specific configurations can override these.

| Item | Respawn Time |
|------|-------------|
| Armor (all types) | 25 seconds |
| Mega Health | 35 seconds (standard) |
| Weapons (standard) | 5 seconds |

### Map Variance

Some maps ship with non-standard Mega Health timers set in their factory or map configuration. Vertical Vengeance is a known example: Mega Health respawns at 2 minutes instead of 35 seconds. Item timers should always be verified per map before assuming standard values apply.

## Item Decay

Health and armor above 100 decay at 1 point per second. A player at 200 HP and 200 armor who takes no damage and picks up no items will reach 100 HP and 100 armor after 100 seconds.

## Movement

Strafe jumping is the standard movement technique in Duel. VQL physics apply unless the server is configured otherwise.

## Rocket Jumping

Rocket jumping is available in Duel. Self-damage from rocket jumping reduces the player's health.

---

**Related:** [[../movement/index|Movement]], [[../health-and-armor/index|Health and Armor]], [[../weapons/index|Weapons]], [[index|Gametypes]]
