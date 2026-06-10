---
title: Server Hosting
game: reflex
layer: canon
type: reference
tags: [reflex, server, hosting, docker, dedicated]
confidence: high
sources: [reflex-server-hosting-docker]
promoted: 2026-06-10
canon_attempts: 1
---

# Server Hosting

## Docker Deployment

The community-standard Linux server setup uses Docker Compose: https://github.com/furioness/reflex-arena-srv-docker

It handles server auto-start, ruleset syncing from https://github.com/Nailok/reflex_rulesets, replay archiving with automatic compression, and a static web page for replay downloads.

```bash
git clone https://github.com/furioness/reflex-arena-srv-docker
cd reflex-arena-srv-docker
cp docker-compose.example.yml docker-compose.yml
# edit docker-compose.yml
docker compose up -d
```

## Ports

| Port | Protocol | Purpose |
|---|---|---|
| 25787 (and up) | UDP + TCP | Game server (one port per instance) |
| 80 | TCP | Replay web page |

Both UDP and TCP must be open on each game server port.

## Server CVARs

All settings are passed via `+` prefixed commands in `docker-compose.yml`. Common settings apply to all instances; per-instance settings override them.

| CVAR | Description |
|---|---|
| `+sv_maxclients <n>` | Player slot limit |
| `+sv_steam <0\|1>` | Steam authentication |
| `+sv_allowedit <0\|1>` | Allow in-game map editor |
| `+sv_country <code>` | Country code shown in server browser |
| `+sv_startmap <name>` | Map name on server start |
| `+sv_startwmap <id>` | Workshop map ID on server start |
| `+sv_startruleset <name>` | Ruleset on server start (e.g. `competitive`, `sushi`, `casual`) |
| `+sv_startmode <mode>` | Game mode on server start (e.g. `1v1`, `ffa`, `tdm`) |
| `+sv_hostname <name>` | Server name in browser |
| `+sv_gameport <port>` | UDP/TCP port for this instance |

## Rulesets

The `ruleset_service` container syncs from https://github.com/Nailok/reflex_rulesets on each `docker compose up`. Local rulesets go in `rulesets_local/`. Git rulesets take precedence over local ones.

## Replays

Replays are compressed to `.zip` automatically. The replay database in `db/` retains match history even after replay files are deleted. Cleanup runs hourly based on free disk ratio (`MIN_FREE_SPACE_RATIO: 0.25`) and a minimum retention floor (`MIN_REPLAY_RETENTION_MiB: 3500`).

Duel replay size: ~3 MB compressed. ~3,000 replays per 10 GB storage.

Known limitation: players who disconnect before a match ends are not listed in the parsed replay metadata.

## VPS Guidelines

| Factor | Recommendation |
|---|---|
| CPU | High frequency preferred over core count |
| RAM | ~250 MB per server instance |
| Swap | Add 1-3 GB |
| Capacity | ~3 servers × 9 players on 1 vCPU / 1 GB RAM |
| Storage | ~3 MB per duel replay compressed |

## Health Checks

| Endpoint | Check |
|---|---|
| `http://your_host` | HTTP 200 |
| `https://reflex.syncore.org/api/serverIDs?hosts=your_host` | `serverCount` > `1` |

## Related

- [[games/reflex/modes|Modes]]
- [[games/reflex/console|Console]]
