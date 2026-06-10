---
title: "Capture the Flag"
game: quake-live
layer: canon
type: mechanic
tags: [quake-live, ctf, capture-the-flag, game-mode, team]
status: canon
source: quakelive-server-standards
promoted: 2026-06-09
---

# Capture the Flag

Verified from `ctf.factories` (quakelive-server-standards).

## Format

Two teams. Each team has a flag at its base. Pick up the enemy flag and return it to your base while your own flag is present to score. Continuous respawn.

## Mode Settings

| cvar | Value | Notes |
|---|---|---|
| `timelimit` | 15 | Minutes |
| `g_overtime` | 0 | No overtime |
| `g_ammoPack` | 1 | Ammo packs enabled |
| `g_ammoRespawn` | 10 | Ammo respawn in seconds |
| `g_battleSuitDampen` | 0.33 | Battle Suit reduces incoming damage by 67% |
| `g_suddenDeathRespawn` | 1 | Sudden death respawn enabled |

## Spawn

Machine Gun + 125 HP. All weapons and items acquired from map pickups. Ammo respawns at 10 seconds.

Powerups including the Battle Suit are present on CTF maps.

---

## Related

- [[index|Gametypes]]
- [[../movement|Movement]]
- [[../health-and-armor|Health and Armor]]
- [[../weapons/index|Weapons]]
