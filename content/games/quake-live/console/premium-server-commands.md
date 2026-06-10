---
title: "Premium Server Commands"
game: quake-live
layer: canon
type: reference
tags: [quake-live, console, server, admin, reference]
status: canon
promoted: 2026-06-10
source: https://www.euere.eu/ql/
---

# Premium Server Commands

These commands are available on Premium (paid/rented) Quake Live servers. Access levels: none = all players, admin = server admins, owner = server owner only.

Player IDs for commands like `kickban`, `put`, `mute` come from the output of `players`.

| Command | Level | Description |
|---------|-------|-------------|
| `players` | none | List connected players with IDs and status (* = Owner, @ = Admin) |
| `timeout` | none | Pause game for 30 seconds. Auto-unpauses unless timein is called |
| `timein` | none | Unpause the game (resume after timeout). Unpauses after 5-second countdown |
| `abort` | admin | End current game with no result, return to warmup. Games aborted before scoreboard don't count for stats |
| `allready` | admin | Force all players ready and start match. Requires at least one player on each team |
| `banlist` | admin | List currently banned accounts. Banlist clears at end of each game period |
| `kickban` | admin | Remove a player and ban them for current period. Takes player ID |
| `lock` | admin | Stop players from joining a team. Players already on team can still go to spectator |
| `mute` | admin | Block a player's chat. Only muted player and admins see messages as "(muted)" |
| `opsay` | admin | Broadcast a message to all players on the server |
| `pause` | admin | Pause match indefinitely. Admin-only, no auto-unpause. Can use while spectating |
| `put` | admin | Move player to team. Takes player ID and team: r=Red, b=Blue, s=Spectator |
| `unban` | admin | Remove player from banlist. Takes account name |
| `unlock` | admin | Allow players to join teams. Admins unlock both; others unlock their own only |
| `unmute` | admin | Remove muted status. Takes player ID |
| `unpause` | admin | Continue match after 5-second countdown. Can override player-initiated timeouts |
| `deop` | owner | Remove admin privileges from a player. Player reverts to access level NONE |
| `op` | owner | Grant admin privileges to a player. Admins can do everything except op others |
| `stopserver` | owner | Immediately shut down the server. Notify players before using |

## Related

- [[console|Console Overview]]
- [[console/commands|Console Commands]]: full command reference
- [[modding/server-hosting|Server Hosting]]: server setup and configuration
