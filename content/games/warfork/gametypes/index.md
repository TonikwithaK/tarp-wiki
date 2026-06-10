---
title: "Gametypes"
game: warfork
layer: canon
type: reference
tags: [warfork, gametypes, game-modes]
status: canon
promoted: 2026-06-09
---

# Gametypes

Warfork ships with 13 default gametypes written in AngelScript. Custom gametypes can be added via the same scripting system.

Instagib (`g_instagib 1`) is a modifier that can be applied to most modes, not a standalone gametype.

## Gametypes

| Gametype | Description |
|---|---|
| [[games/warfork/gametypes/duel|Duel]] | 1v1, frag or time limit, item pickups, Mega Health respawns 20s after holder drops to 100 HP |
| [[games/warfork/gametypes/clan-arena|Clan Arena]] | Team elimination, rounds, full loadout at spawn, 150 armor, no self/team/fall damage, first to 11 rounds |
| [[games/warfork/gametypes/deathmatch|Deathmatch]] | Free-for-all frag race, 15 minute default, weapon pickups |
| [[games/warfork/gametypes/team-deathmatch|Team Deathmatch]] | Team frag race, 20 minute default, individual frags score for team |
| [[games/warfork/gametypes/capture-the-flag|Capture The Flag]] | Steal enemy flag, return to base while own flag is present |
| [[games/warfork/gametypes/bomb-and-defuse|Bomb And Defuse]] | Plant/defuse, 60s round time, 4s arm, 7s defuse, teams swap sides |
| [[games/warfork/gametypes/race|Race]] | Movement course, fastest time wins, no combat, infinite ammo, plasmaclimbing routes |
| [[games/warfork/gametypes/instagib|Instagib]] | Modifier applied to other modes, Instagun replaces all weapons, one-hit kill |
| [[games/warfork/gametypes/headhunt|Headhunt]] | One designated target, all others hunt them, killer becomes new target |

## Variant and Community Gametypes

**Duel Arena:** Queue-based all-weapons duel, first to 11, no item pickups. Runs inside the duel gametype.

**Exhaustion:** Community-made, team elimination with escalating respawn penalty. Requires custom server configuration.

**Class-based CTF (ctftactics):** CTF with player classes and special abilities.

## Related

- [[games/warfork/movement|Movement]]
- [[games/warfork/weapons/index|Index]]
- [[games/warfork/modding/custom-gametypes|Custom Gametypes]]
