---
title: Console
game: reflex
layer: canon
type: reference
tags: [reflex, console, config, cvars, binds]
confidence: medium
sources: [phylum-cfg-guide, xytaglyph-guide]
promoted: 2026-06-10
canon_attempts: 1
---

The console opens with tilde (`~`).

## Config Files

Config files are stored in the game directory:
- 32-bit Windows: `C:\Program Files\Steam\steamapps\common\Reflex\`
- 64-bit Windows: `C:\Program Files (x86)\Steam\steamapps\common\Reflex\`

`saveconfig game` saves current settings to `game.cfg`. `loadconfig NAME` loads `NAME.cfg` (do not include the `.cfg` extension; it is appended automatically).

Recommended setup: create a personal `.cfg` file, clear the contents of `game.cfg`, and replace them with `loadconfig NAME`.

## Bind Syntax

```
bind <key> <command> [value]
```

Commands starting with `+` have a paired `-` release command. `addbind <key> <command>` adds to an existing bind without overriding it.

## Graphics CVARs

| CVAR | Values | Description |
|------|--------|-------------|
| `r_resolution <x> <y>` | integers | Resolution |
| `r_fullscreen` | `0\|1` | Fullscreen toggle |
| `r_refreshrate` | integer | Refresh rate (preferred over r_resolution parameter) |
| `r_vsync` | `0\|1` | Vsync (0 recommended unless using 120/144hz monitor) |
| `r_bloom` | `0\|1` | Bloom effects |
| `r_fxaa` | `0\|1` | FXAA anti-aliasing |
| `r_dynamic_lights` | `0\|1` | Dynamic lights from projectiles |
| `r_dynamic_shadows` | `0\|1` | Dynamic shadows |
| `r_decals` | integer | Blood/impact effects (0 = off) |
| `r_showFps` | `0\|1` | FPS counter |
| `com_maxfps` | integer | FPS cap (recommended: 120-250) |
| `r_fov` | integer | Field of view (recommended: 90-115) |
| `cl_show_gun` | `0\|1` | Show/hide weapon model |

## Mouse CVARs

| CVAR | Values | Description |
|------|--------|-------------|
| `m_speed` | float | Mouse sensitivity |
| `m_invert` | `0\|1` | Invert Y-axis |

## Gameplay CVARs

| CVAR | Values | Description |
|------|--------|-------------|
| `cl_predict_items` | `0\|1` | 0 prevents false item pickups not yet registered by server |
| `cl_input_subframe` | `0\|1` | 1 sets input polling to 1000hz, independent of framerate |

## Crosshair CVARs

| CVAR | Values | Description |
|------|--------|-------------|
| `cl_crosshair` | `1-16` | Crosshair style |
| `cl_show_crosshair` | `0\|1` | Show/hide crosshair |
| `cl_crosshair_colour` | `1-6` | 1=Green, 2=Teal, 3=Red, 4=Purple, 5=Yellow, 6=White |

For custom crosshairs, edit `game.cfg` directly under `ui_define Crosshairs` and modify the type/r/g/b values.

## Weapon Model Offset CVARs

| CVAR | Default | Description |
|------|---------|-------------|
| `cl_weapon_offset_x` | `5` | Horizontal position (0=center, 5=right, -5=left) |
| `cl_weapon_offset_y` | `-10` | Vertical position (0=front of camera) |
| `cl_weapon_offset_z` | `5` | Depth (-100 hides gun) |

To hide the weapon model without `cl_show_gun 0`: set `offset_x 0`, `offset_y -10`, `offset_z -100`.

## High-Performance Config Block

```
cl_gibs_maxcount 1
cl_gibs_expire_time 1
r_dynamic_shadows 0
r_bloom 0
r_fxaa 0
r_dynamic_lights 0
r_decals 0
```

## Console Commands

### In-Game

| Command | Description |
|---------|-------------|
| `callvote map <name>` | Vote to change map |
| `callvote mode <mode>` | Vote to change gametype (1v1, ffa, tdm, ctf, 2v2, AFFA, ATDM, A1v1) |
| `callvote restart` | Vote to restart match |
| `callvote ruleset casual` | Vote to switch ruleset |
| `connect <ip>` | Direct connect to server |
| `disconnect` | Return to menu |
| `suicide` | Kill yourself (useful in Race mode) |
| `vote_yes` / `vote_no` | Respond to active vote |
| `name <foo>` | Change display name |
| `unbind <key>` | Clear a single bind |
| `unbindall` | Clear all binds |

### Spectator

| Command | Description |
|---------|-------------|
| `cl_playerState <1\|2\|3>` | 1=playing, 2=spectating, 3=editing |
| `cl_camera_next_player` | Advance to next player POV |
| `cl_camera_prev_player` | Go to previous player POV |
| `cl_camera_freecam` | Free camera mode |

## Related

- [[getting-started|Getting Started]]
