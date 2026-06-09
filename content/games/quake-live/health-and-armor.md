---
title: "Health and Armor"
game: quake-live
layer: canon
type: mechanic
tags: [quake-live, health, armor, items, mechanics]
status: canon
promoted: 2026-06-09
---

## Health Items

| Item | Color | Amount | Cap |
|---|---|---|---|
| Small Health | Yellow bubble | +25 | 100 |
| Medium Health | Orange bubble | +50 | 100 |
| Health Bubble (small) | Green | +5 | 200 |
| Mega Health | Blue | +100 | 200 |

---

## Armor Items

| Item | Amount | Cap |
|---|---|---|
| Armor Shard | +5 | 200 |
| Green Armor | +25 | 200 |
| Yellow Armor | +50 | 200 |
| Red Armor | +100 | 200 |

---

## Item IDs (Items.md source, tjone270/Quake-Live)

| ID | Item |
|---|---|
| 1 | Armor Shard |
| 2 | Yellow Armor |
| 3 | Red Armor |
| 4 | Green Armor |
| 5 | 5 Health |
| 6 | 25 Health |
| 7 | 50 Health |
| 8 | Mega Health |

---

## Key Mechanics

- Base max health: 100 HP.
- Overheal cap: 200 HP (reachable via Mega Health or green small health bubbles).
- Armor cap: 200.
- Armor absorbs up to 2/3 of incoming damage.
- Health above 100 decays at 1 HP per second back toward 100.
- Armor above 100 decays at 1 per second back toward 100.
- Health and armor are independent stats; each stacks to 200 separately.

---

## Respawn Timers

Timers begin when the item is picked up.

| Item | Respawn Time |
|---|---|
| All armor types | 25 seconds |
| Mega Health | 35 seconds |
| Weapons (standard) | 5 seconds |

---

## Related

- [Movement](movement) — rocket jumping health cost
- [Gametypes: Duel](gametypes/duel) — item timing in competitive play
