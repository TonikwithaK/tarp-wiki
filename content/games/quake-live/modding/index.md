---
title: "Modding"
game: quake-live
layer: canon
type: reference
tags: [quake-live, modding, minqlx, server, reference]
status: canon
promoted: 2026-06-10
---

Quake Live modding is primarily server-side. The client is a fixed Steam binary. Server customization is done through factories (gametype rule files), minqlx plugins (Python), and server cvars.

## minqlx

minqlx is the primary server-side plugin framework. It hooks into the Quake Live dedicated server and exposes a Python API for game events, player management, commands, and external integrations.

Source: [minqlx on GitHub](https://github.com/MinoMino/minqlx)

### Plugin capabilities

- Hook game events: player connect, disconnect, kill, round start/end, map change
- Add server commands prefixed with `!` (configurable via `qlx_commandPrefix`)
- Integrate Redis for persistent player data (stats, permissions, preferences)
- Modify game state: force balance teams, set scores, change maps, kick players
- Build external integrations: Discord bots, stat trackers, Elo systems

### Setup

minqlx is included in the quakelive-server-standards Docker images. For manual setup:

```bash
qlx_database    "Redis"
qlx_redisAddress "localhost"
```

## Factories

Factories define gametype rules as JSON. Each `.factories` file contains one or more factory definitions. Placed in `baseq3/scripts/`.

Fields:

| Field | Purpose |
|---|---|
| `basegt` | Base gametype (`duel`, `ca`, `ctf`, `tdm`, `ffa`) |
| `id` | Factory identifier |
| `title` | Display name |
| `cvars` | Rule overrides applied on top of base gametype defaults |

Factories control: timelimit, fraglimit, physics mode (VQL/PQL), item availability, spawn loadouts, and custom rules.

## Map Pools

Map pools are defined in `mappool.txt` in the server root. One map name per line. The server rotates through this list. Standard competitive pools are maintained by quakelive-server-standards per gametype.

## Physics Mode

Physics mode is set per-factory via the `pmove_BunnyHop` and related cvars:

| Setting | Mode |
|---|---|
| `pmove_BunnyHop 0` | VQL (Vanilla Quake Live) |
| `pmove_BunnyHop 1` | PQL (CPM-like physics) |

VQL is standard for most competitive gametypes. PQL servers are available but less common.

## Related

- [[server-hosting|Server Hosting]]: Docker setup, ports, RCON
- [[../console|Console]]: server cvar reference
