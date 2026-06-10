---
title: "Clan Arena"
game: quake-live
layer: canon
type: mechanic
tags: [quake-live, clan-arena, game-mode, team]
status: canon
source: quakelive-server-standards
promoted: 2026-06-09
---

# Clan Arena

Verified from `ca.factories` (quakelive-server-standards).

## Format

Team vs team, round-based. No respawns during a round. Round ends when all players on one team are eliminated. Last team standing wins the round.

## Spawn

Community standard spawn (`g_startingWeapons: 8447`): all standard weapons.

### Starting Ammo

| Weapon | Starting Ammo |
|---|---|
| Rocket Launcher | 50 |
| Lightning Gun | 150 |
| Railgun | 25 |
| Plasma Gun | 100 |
| Grenade Launcher | 25 |
| Machine Gun | 100 |
| Shotgun | 50 |
| Heavy MG | 150 |

### Starting Stats

- Health: 200
- Armor: 100
- Health bonus: 0

## Mode Settings

| cvar | Value | Notes |
|---|---|---|
| `dmflags` | 28 | No self-damage, no friendly fire |
| `g_allowKill` | 0 | Suicide disabled |
| `g_overtime` | 0 | No overtime |

Items do not spawn in CA. No item pickups.

---

## Related

- [[index|Gametypes]]
- [[../weapons/index|Weapons]]
- [[../health-and-armor|Health and Armor]]
