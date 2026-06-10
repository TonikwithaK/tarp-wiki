---
title: "Gametypes"
game: warfork
layer: canon
type: reference
tags: [warfork, gametypes, game-modes]
status: canon
promoted: 2026-06-09
---

Warfork ships with 13 default gametypes written in AngelScript. Custom gametypes can be added via the same scripting system.

Instagib (`g_instagib 1`) is a modifier that can be applied to most modes, not a standalone gametype.

## Gametypes

| Gametype | Description |
|---|---|
| [[duel]] | 1v1, frag or time limit, item pickups, Mega Health respawns 20s after holder drops to 100 HP |
| [[clan-arena]] | Team elimination, rounds, full loadout at spawn, 150 armor, no self/team/fall damage, first to 11 rounds |
| [[deathmatch]] | Free-for-all frag race, 15 minute default, weapon pickups |
| [[team-deathmatch]] | Team frag race, 20 minute default, individual frags score for team |
| [[capture-the-flag]] | Steal enemy flag, return to base while own flag is present |
| [[bomb-and-defuse]] | Plant/defuse, 60s round time, 4s arm, 7s defuse, teams swap sides |
| [[race]] | Movement course, fastest time wins, no combat, infinite ammo, plasmaclimbing routes |
| [[instagib]] | Modifier applied to other modes, Instagun replaces all weapons, one-hit kill |
| [[headhunt]] | One designated target, all others hunt them, killer becomes new target |

## Variant and Community Gametypes

**Duel Arena:** Queue-based all-weapons duel, first to 11, no item pickups. Runs inside the duel gametype.

**Exhaustion:** Community-made, team elimination with escalating respawn penalty. Requires custom server configuration.

**Class-based CTF (ctftactics):** CTF with player classes and special abilities.

## Related

- [[movement]]
- [[weapons/index]]
- [[modding/custom-gametypes]]
