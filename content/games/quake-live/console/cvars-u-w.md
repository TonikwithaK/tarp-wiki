---
title: "CVars: U–W"
game: quake-live
layer: canon
type: reference
tags: [quake-live, console, cvars, ui, reference]
status: canon
promoted: 2026-06-10
source: https://www.euere.eu/ql/
---

# Console Variables: U–W

Full reference sourced from euere.eu/ql/ — updated September 2025.

---

## U — UI Variables

### General
| CVar | Default | Description |
|------|---------|-------------|
| `ui_bigFont` | 0.4 | Large font size in UI |
| `ui_smallFont` | 0.25 | Small font size in UI |
| `ui_debug` | 0 | UI debugging mode |
| `ui_serverStatusTimeOut` | 7000 | Server status timeout (ms) |

### Create Server Menu
| CVar | Default | Description |
|------|---------|-------------|
| `ui_gametype` | 3 | Gametype selector in start server menu |
| `ui_dedicated` | 0 | 0=listen server, 1=dedicated server |
| `ui_fragLimit` | 10 | Frag limit for start server menu |
| `ui_captureLimit` | 5 | Capture limit for start server menu |

### Team Configuration
| CVar | Default | Description |
|------|---------|-------------|
| `ui_redteam` | Pagans | Red team name |
| `ui_blueteam` | Stroggs | Blue team name |

### Enemy/Team Model Colorization
| CVar | Default | Description |
|------|---------|-------------|
| `ui_enemyHeadColor` | 27 | Enemy head color |
| `ui_enemyUpperColor` | 27 | Enemy upper body color |
| `ui_enemyLowerColor` | 27 | Enemy lower body color |
| `ui_forceEnemyModel` | — | Force enemy model |
| `ui_teamHeadColor` | 96 | Teammate head color |
| `ui_teamUpperColor` | 96 | Teammate upper body color |
| `ui_teamLowerColor` | 96 | Teammate lower body color |
| `ui_forceTeamModel` | — | Force team model |

### Single-Player Limits
| CVar | Default | Description |
|------|---------|-------------|
| `ui_ffa_fraglimit` | 20 | FFA frag limit |
| `ui_ffa_timelimit` | 0 | FFA time limit |
| `ui_ctf_capturelimit` | 8 | CTF capture limit |
| `ui_ctf_timelimit` | 30 | CTF time limit |
| `ui_team_fraglimit` | 0 | TDM frag limit |
| `ui_team_timelimit` | 20 | TDM time limit |
| `ui_tourney_fraglimit` | 0 | Tournament frag limit |
| `ui_tourney_timelimit` | 15 | Tournament time limit |

---

## V — Video Output

| CVar | Default | Description |
|------|---------|-------------|
| `vid_xpos` | 3 | Window x position on desktop |
| `vid_ypos` | 22 | Window y position on desktop |

Command: `vid_restart` — restart video system to apply changed r_ cvars.

---

## W

| CVar | Default | Description |
|------|---------|-------------|
| `win_wndproc` [R] | — | Window procedure debug address |

## Related

- [[console|Console Overview]]
- [[console/cvars-a-c|CVars A–C]]: bots, crosshair, HUD, client settings
- [[console/cvars-d-p|CVars D–P]]: game settings, weapon values, physics
- [[console/cvars-r-t|CVars R–T]]: rendering, sound, server settings
- [[console/appendix|Appendix]]: flag legend, color chart
