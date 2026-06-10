---
title: "Server Hosting"
game: warfork
layer: canon
type: reference
tags: [warfork, server, hosting, administration]
status: canon
promoted: 2026-06-09
---

This guide covers installing and running a dedicated Warfork server on Linux.

## Dependencies

Install these before proceeding:

```
wget tar rsync unzip tmux jq bc
```

## SteamCMD Installation

| App | ID | Auth |
|---|---|---|
| Game client | 671610 | Steam login required |
| Dedicated server | 1136510 | Anonymous login |

Use App ID **1136510** for Linux dedicated servers: no Steam account needed.

```bash
steamcmd +login anonymous +app_update 1136510 validate +quit
```

The server binary is `wf_server`. It installs to your SteamCMD `steamapps/common/` directory.

## Ports

Open these on your firewall and forward them if behind NAT:

| Port | Protocol | Purpose |
|---|---|---|
| 44400 | UDP | Game traffic (sv_port) |
| 44444 | TCP | HTTP downloads (sv_http_port) |

## Starting the Server

Basic launch with command-line overrides:

```bash
./wf_server +set sv_hostname "My Server" +set g_gametype ca +set g_maplist "wfca1 wfca2"
```

For a persistent session using tmux:

```bash
tmux new-session -d -s warfork "./wf_server +set sv_hostname 'My Server' +set g_gametype ca +set g_maplist 'wfca1 wfca2'"
```

Reattach with `tmux attach -t warfork`.

## Config Files

Server configs are auto-generated on first run at:

```
configs/server/gametypes/<gametype>.cfg
```

Edit these files directly after the first run. Settings in the config are loaded at startup; command-line `+set` overrides take precedence.

## Core Server CVars

| Cvar | Default | Description |
|---|---|---|
| `sv_hostname` |: | Name shown in server browser |
| `sv_port` | 44400 | UDP port |
| `sv_public` |: | Report to master server (1 = yes) |
| `sv_pure` | 0 | Enforce pure client (0 = off) |
| `sv_maxclients` |: | Max player slots |
| `g_gametype` |: | Gametype: dm, ca, ctf, duel, tdm, race, etc. |
| `g_timelimit` | 10 | Match time limit in minutes |
| `g_scorelimit` | 0 | Frag/score limit (0 = disabled) |
| `g_maplist` |: | Space-separated map rotation |
| `g_maprotation` |: | 0 = same map, 1 = ordered, 2 = random |
| `g_numbots` | 0 | Number of bots |
| `g_warmup_timelimit` | 5 | Warmup duration in minutes |
| `g_instagib` | 0 | Instagib modifier (0/1) |
| `g_allow_falldamage` |: | Enable fall damage |
| `g_allow_selfdamage` |: | Enable self damage |
| `g_allow_teamdamage` |: | Enable team damage |
| `g_allow_stun` |: | Enable stun mechanic |

## CA-Specific CVars

These are defined in `ca.as` and written to `configs/server/gametypes/ca.cfg` on first run.

| Cvar | Default | Description |
|---|---|---|
| `g_scorelimit` | 11 | First team to 11 rounds wins |
| `g_ca_timelimit1v1` | 60 | Time limit (seconds) for 1v1 situations in a round |
| `g_noclass_inventory` | `gb mg rg gl rl pg lg eb cells shells grens rockets plasma lasers bolts bullets` | Weapons players spawn with |
| `g_class_strong_ammo` | `1 75 20 20 40 125 180 15` | Ammo counts at spawn: GB MG RG GL RL PG LG EB |
| `g_allow_selfdamage` | 0 | Disabled in CA by default |
| `g_allow_teamdamage` | 0 | Disabled in CA by default |

## RCON

Set `rcon_password` in your server config or on the command line. From a connected client or remote console:

```
rcon login <password>
rcon status
rcon kick <playername>
rcon map <mapname>
rcon addip <ipaddress>
```

`rcon addip` bans by IP. Persistent bans are stored in `configs/server/banned.cfg`.

## See Also

- [[games/warfork/console|Console]]: full cvar and command reference
- [[games/warfork/modding/custom-gametypes|Custom Gametypes]]: writing and loading custom gametypes
