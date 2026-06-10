---
title: "Health and Armor"
game: warfork
layer: canon
type: mechanic
tags: [warfork, health, armor, items, mechanics]
status: canon
promoted: 2026-06-09
---

# Health and Armor

Health and armor are the primary survival resources in Warfork combat.

## Health

Your base maximum health is 100 HP. Most health items restore up to that cap. Some items push you above it: this is called overhealing. Overhealed HP decays back down to 100 over time; it does not stay permanently.

### Health Items

| Item | HP Restored | Notes |
|------|-------------|-------|
| Health Bubble | 5 HP | |
| Small Health | 25 HP | |
| Large Health | 50 HP | |
| Mega Health | 100 HP | Restores to full; can push you above 100 HP (overheals) |
| Ultra Health | 200 HP | Major overheal; may be Warfork-specific: verify availability on your server or ruleset |

Overhealed HP decays gradually back to 100.

### HUD Feedback

The health display on your HUD changes color as your HP changes.

### Simple Items

The "Simple Items" display setting replaces 3D pickup models with flat 2D sprites. This is a performance and readability option: it does not change pickup values or behavior in any way.

## Armor

Armor Points (AP) act as a damage buffer. When you take damage, AP is consumed first. Only after your AP is depleted does damage start reducing your HP. This makes armor the primary survival resource in a firefight: a player with high armor and average health is typically harder to kill than one with full health and no armor.

### Armor Items

| Item | Notes |
|------|-------|
| Armor Shard | Small AP pickup, found throughout maps |
| Green Armor | Moderate AP restore; lower cap |
| Yellow Armor | High AP restore; higher cap |

Each armor tier has a different maximum cap. Picking up armor beyond your current cap for that tier still grants AP up to the new cap, but you cannot mix-and-match to exceed what each type allows. Yellow Armor provides the most protection and is the highest-value spawn on most maps.

### Armor Bar

The armor bar on your HUD changes color based on your current AP level.

## Respawn Timers

Item respawn timers vary by gametype. In Duel:

| Item | Respawn Timer |
|------|---------------|
| Armor | 25s |
| Health items | 25s |
| Mega Health | 20s after the holder's HP drops to 100 or below |
| Ultra Health | 40s |

CA does not spawn items at all (`spawnableItemsMask = 0`).

## Related

- [[games/warfork/powerups|Powerups]]
- [[games/warfork/gametypes/duel|Duel]]
