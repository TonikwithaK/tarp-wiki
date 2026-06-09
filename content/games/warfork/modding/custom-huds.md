---
title: "Custom HUDs"
game: warfork
layer: canon
type: reference
tags: [warfork, modding, hud, scripting]
status: canon
promoted: 2026-06-09
---

Warfork HUDs are plain-text scripts using a draw command language. They live in:

```
HUD scripts live in [assets/data0_21/huds/](https://github.com/TeamForbiddenLLC/warfork-qfusion/tree/master/assets/data0_21/huds)
```

## Default HUDs

| File | Description |
|---|---|
| `adem.hud` | Competitive HUD with strafe indicator |
| `classic.hud` | Classic Warsow-style layout |
| `default.hud` | Standard HUD |
| `spec.hud` | Spectator HUD |

Switch HUD in console:

```
cg_clientHUD "adem"
```

Set to an empty string to use the engine default.

## Draw Commands

| Command | Description |
|---|---|
| `setCursor x, y` | Set absolute draw position |
| `moveCursor dx, dy` | Move relative to current position |
| `setSize w, h` | Set draw dimensions |
| `setAlign horizontal, vertical` | Alignment: `#LEFT` `#CENTER` `#RIGHT` / `#TOP` `#MIDDLE` `#BOTTOM` |
| `setColor r, g, b, a` | Set draw color (0.0 to 1.0 per channel) |
| `setScale mode` | Scaling: `#DEFAULTSCALE`, `#SCALEBYWIDTH`, `#SCALEBYHEIGHT` |
| `drawPicByName path` | Draw a full texture |
| `drawSubPicByName path s t s2 t2` | Draw a sub-region of a texture |
| `if <condition>` / `endif` | Conditional block |

## HUD Variables

Variables are prefixed with `%`. They are read-only values injected by the engine at draw time.

| Variable | Description |
|---|---|
| `%HEALTH` | Current health points |
| `%ARMOR` | Current armor value |
| `%SPEED` | Current speed in units per second (UPS) |
| `%STRAFEANGLE` | Strafe angle used by the strafe indicator |
| `%ACCELERATION` | Current acceleration (positive = gaining speed, negative = losing) |
| `%DIFF_ANGLE` | Difference between movement direction and facing direction |
| `%RACE` | 1 when in race mode |
| `%MATCH_STATE` | Current match state constant |
| `%PMOVE_TYPE` | Current movement type constant |
| `%SHOW_STRAFE` | 1 when strafe HUD is enabled via `cg_strafeHUD` |

## Strafe HUD

The strafe indicator (`cg_strafeHUD 1`) is defined in `inc/strafe.hud` and included by `adem.hud`. It renders only when all three conditions are true:

- `%SHOW_STRAFE != 0`
- In race mode or in warmup: `%RACE || %MATCH_STATE == MATCH_STATE_WARMUP`
- Movement type is normal: `%PMOVE_TYPE == PMOVE_TYPE_NORMAL`

**Triangle size** is computed as `0.03 * 4500 - %STRAFEANGLE`. A larger strafe angle shrinks the visual target area.

**Bar position** shifts horizontally based on `%DIFF_ANGLE`: the angle between your movement direction and where you are facing.

**Color logic:**

| Color | Condition | Meaning |
|---|---|---|
| White | Default | Neutral |
| Red | `%ACCELERATION < -5000` | Losing speed |
| Green | `%ACCELERATION > 0.8` | Gaining speed: correct strafe |

## Include System

HUDs can include sub-scripts:

```
#include "inc/strafe.hud"
#include "inc/clock.hud"
```

The default HUDs use an `inc/` subdirectory with modular components: `strafe.hud`, `clock.hud`, `minimap.hud`, `powerups.hud`, `fps.hud`.

## Installing a Custom HUD

1. Place `myhud.hud` in `basewf/huds/`
2. Set `cg_clientHUD "myhud"` in console or your autoexec config
3. The HUD loads on the next map load or respawn

Custom HUDs can also be packaged inside a `.pk3` file under the `huds/` path.

## See Also

- [[console]]: full cvar reference including `cg_clientHUD`, `cg_strafeHUD`
- [[../movement]]: strafe mechanics context for interpreting the strafe indicator
