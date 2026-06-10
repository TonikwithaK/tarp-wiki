---
title: "Controls"
game: quake-live
layer: canon
type: reference
tags: [quake-live, controls, binds, keybindings, reference]
status: canon
promoted: 2026-06-10
---

Default key bindings for Quake Live. All bindings are configurable via the Options menu or the console with `/bind <key> <command>`.

## Default Bindings

| Key | Action |
|---|---|
| W | Move forward |
| S | Move backward |
| A | Strafe left |
| D | Strafe right |
| Space | Jump |
| Ctrl | Crouch |
| Mouse1 | Attack (fire) |
| Mouse2 | Zoom / alternate fire |
| Mouse wheel up | Previous weapon |
| Mouse wheel down | Next weapon |
| 1 | Gauntlet |
| 2 | Machine Gun |
| 3 | Shotgun |
| 4 | Grenade Launcher |
| 5 | Rocket Launcher |
| 6 | Lightning Gun |
| 7 | Railgun |
| 8 | Plasma Gun |
| 9 | BFG10K |
| 0 | Nailgun / Chaingun (if available) |
| F | Use item (holdable) |
| Tab | Scoreboard |
| T | Team chat |
| Y | All chat |
| ~ | Console |
| Escape | Menu / pause |

## Custom Binding via Console

```
/bind <key> <command>
/bind mouse1 +attack
/bind space +moveup
/bind q "weapon 5"      // direct weapon slot bind
/bind e "weapon 6"
/bind r "weapon 7"
```

## Sensitivity Setup

Configure in console:

```
/sensitivity 3.5
/m_yaw 0.022
/m_pitch 0.022
/m_accel 0
```

## Related

- [[console|Console]]: full cvar and command reference
- [[getting-started|Getting Started]]: initial setup
