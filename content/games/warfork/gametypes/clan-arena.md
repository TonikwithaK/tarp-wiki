---
title: "Clan Arena"
game: warfork
layer: canon
type: mechanic
tags: [warfork, clan-arena, game-mode, team]
status: canon
promoted: 2026-06-09
---

# Clan Arena

Clan Arena (CA) is a team elimination mode. Two teams compete across a series of rounds. The team that wins 11 rounds first wins the match.

---

## Rules

Each round, all players spawn simultaneously and fight until one team is fully eliminated. Dead players spectate for the remainder of that round. The last team with at least one player alive wins the round.

When both teams are down to exactly one player each, a 60-second clock starts. If neither player is eliminated before time expires, the round is a draw.

Teams are locked when the countdown starts. Items do not spawn during rounds.

---

## Limits

| Setting | Value |
|---|---|
| Score limit | 11 rounds |
| Time limit | None (0) |
| 1v1 time limit | 60 seconds |

---

## Respawn Timers

These timers apply to items on the map. CA has no item pickups during rounds (spawnableItemsMask = 0), so these values are present in the gametype configuration but do not affect active rounds.

| Item | Respawn |
|---|---|
| Health | 25s |
| Armor | 25s |
| Mega Health | 20s (after holder drops to 100 HP or below) |
| Ultra Health | 60s |
| Weapon | 15s |
| Ammo | 20s |
| Powerup | 90s |

---

## Spawn Loadout

Every player spawns with the following each round:

- Armor: 150
- Default weapon selected: Rocket Launcher
- Weapons (g_noclass_inventory): GB, MG, RG, GL, RL, PG, LG, EB

Ammo at spawn (g_class_strong_ammo):

| Weapon | Ammo |
|---|---|
| GB | 1 |
| MG | 75 |
| RG | 20 |
| GL | 20 |
| RL | 40 |
| PG | 125 |
| LG | 180 |
| EB | 15 |

---

## Damage Rules

| Setting | Value |
|---|---|
| Self-damage | Disabled (g_allow_selfdamage 0) |
| Team damage | Disabled (g_allow_teamdamage 0) |
| Fall damage | Disabled (g_allow_falldamage 0) |
| Stun | Disabled (g_allow_stun 0) |

---

## Round Structure

Each round follows this sequence:

1. PREROUND: 7 seconds. Players are held in ghost state and cannot shoot.
2. ROUND: Active play. Players release simultaneously at round start.
3. ROUNDFINISHED: 1.5 seconds.
4. POSTROUND: 3 seconds.

Spawns are placed at opposite ends of the map. Alpha and Beta spawn points are chosen to maximize distance between teams.

---

## Teams

- Two teams: Alpha and Beta.
- Competitive format: 3v3 double elimination.

---

## Related

- [[movement]]
- [[weapons/index]]
- [[health-and-armor]]
- [[gametypes/index]]
