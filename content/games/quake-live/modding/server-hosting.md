---
title: "Server Hosting"
game: quake-live
layer: canon
type: reference
tags: [quake-live, server, hosting, docker, minqlx]
status: canon
source: quakelive-server-standards
promoted: 2026-06-09
---

# Server Hosting

Source: [quakelive-server-standards](https://github.com/quakelive-server-standards/quakelive-server-standards)

## Overview

Quake Live dedicated servers run as a Steam process. The community-standard deployment uses Docker. The quakelive-server-standards project provides Docker images per gametype with community-tuned factory files, map pools, and minqlx plugin sets.

## Ports

Three ports are required per server instance.

| Port (default) | Protocol | Purpose |
|---|---|---|
| 27960 | UDP | Game |
| 27960 | TCP | Stats (ZeroMQ) |
| 28960 | TCP | RCON (ZeroMQ) |

RCON port = game port + 1000. Stats port = same as game port.

## Standard server.cfg

From quakelive-server-standards `configs/standard/server.cfg`.

```
g_accessFile         "access.txt"        Player access/ban file
g_floodprot_decay    1000                Flood protection decay
g_floodprot_maxcount 10                  Max messages before flood kick
net_ip               "0.0.0.0"           Bind all interfaces
net_strict           "1"                 Strict network mode
qlx_commandPrefix    "!"                 minqlx command prefix
qlx_database         "Redis"             minqlx database backend
qlx_pluginsPath      "minqlx-plugins"    Plugin directory
qlx_redisAddress     "redis"             Redis host
zmq_rcon_enable      "1"                 Enable RCON
zmq_rcon_ip          "0.0.0.0"           RCON bind address
zmq_stats_enable     "1"                 Enable stats API
zmq_stats_ip         "0.0.0.0"           Stats bind address
sv_fps               "40"                Server tick rate
sv_idleExit          "120"               Shutdown after 120s empty
sv_master            "1"                 List on master server
sv_serverType        "2"                 Server type flag
```

## Docker Quickstart

```bash
git clone https://github.com/quakelive-server-standards/quakelive-server-standards.git
# Install Docker: https://docs.docker.com/engine/install/
cd _myservers
# Copy docker-compose.source.yml to docker-compose.yml and edit
docker-compose up -d
```

## Example Docker Compose Service (Duel)

```yaml
duel1:
  image: quakeliveserverstandards/duel
  restart: always
  ports:
    - '27960:27960/udp'
    - '27960:27960/tcp'
    - '28960:28960/tcp'
  environment:
    - NET_PORT=27960
    - SV_HOSTNAME=My Duel Server
    - SV_TAGS=duel
  volumes:
    - './access.txt:/home/steam/ql/baseq3/access.txt'
    - './autoexec.cfg:/home/steam/ql/baseq3/autoexec.cfg'
    - '../configs/standard/server.cfg:/home/steam/ql/baseq3/server.cfg'
    - '../factories/standard/duel/duel.factories:/home/steam/ql/baseq3/scripts/duel.factories'
    - '../mappools/standard/duel/mappool.txt:/home/steam/ql/baseq3/mappool.txt'
    - '../minqlx-plugins/standard/duel:/home/steam/ql/minqlx-plugins'
  depends_on:
    - redis
```

## Factories

A `.factories` file defines gametype rules as a JSON object.

| Field | Purpose |
|---|---|
| `basegt` | Base gametype (`duel`, `ca`, `ctf`, `tdm`, `ffa`, etc.) |
| `id` | Factory identifier used in server config |
| `title` | Display name |
| `cvars` | Overrides applied on top of base gametype defaults |

Example duel standard factory `cvars`:

```json
{
  "fraglimit": "0",
  "timelimit": "10",
  "pmove_BunnyHop": "0",
  "pmove_JumpTimeDeltaMin": "50",
  "g_itemTimers": "0",
  "g_itemHeight": "15"
}
```

## minqlx

minqlx is a server-side plugin framework for Quake Live. Plugins are Python scripts that hook into game events (player connect, kill, round end, etc.) and can add commands, modify rules, and integrate external services.

| Setting | Value |
|---|---|
| Plugin directory | `minqlx-plugins/` in server root |
| Command prefix | `!` (default, configurable via `qlx_commandPrefix`) |
| Database | Redis (required for most plugins) |

## RCON

Quake Live uses ZeroMQ-based RCON. Standard Quake 3 UDP RCON tools are not compatible.

- Enable with `zmq_rcon_enable 1`
- Port: game port + 1000
- Requires a ZeroMQ-compatible client

Compatible tools:

| Tool | Language | URL |
|---|---|---|
| ql-api | TypeScript | https://github.com/quakelive-server-standards/ql-api |
| id-rcon-cli | Python | https://github.com/quakelive-server-standards/id-rcon-cli |
| ql-console | JavaScript | https://github.com/quakelive-server-standards/ql-console |

---

## Related

- [[../gametypes/index|Gametypes]]
