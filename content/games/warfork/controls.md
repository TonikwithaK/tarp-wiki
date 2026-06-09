---
title: "Controls"
game: warfork
layer: canon
type: reference
tags: [warfork, controls, keybinds, reference]
status: canon
promoted: 2026-06-09
---

# Controls

Default keyboard and mouse bindings from the [game source](https://github.com/TeamForbiddenLLC/warfork-qfusion/blob/master/assets/default_binds_kbmouse.cfg).

## Movement

| Key | Action |
|---|---|
| W / Up Arrow | Forward |
| S / Down Arrow | Back |
| A / Left Arrow | Move left |
| D / Right Arrow | Move right |
| Space | Jump |
| C | Crouch |
| Left Alt | Walk (reduces speed to 160 UPS) |
| Mouse2 (RMB) | Dash / walljump (context dependent) |

## Weapons

Direct keys are strongly preferred by competitive players over scroll wheel. Switching weapons on scroll during a firefight is too slow and imprecise.

| Key | Weapon |
|---|---|
| 1 | Gunblade |
| 2 | Machinegun |
| 3 | Riotgun |
| 4 | Grenade Launcher |
| 5 | Rocket Launcher |
| 6 | Plasmagun |
| 7 | Lasergun |
| 8 | Electrobolt |
| 9 | Instagun |
| Mouse wheel up | Next weapon |
| Mouse wheel down | Previous weapon |
| Q | Last weapon |
| Backspace | Drop weapon |
| L | Drop bomb / flag |

## Combat

| Key | Action |
|---|---|
| Mouse1 (LMB) | Attack (primary fire) |
| Mouse2 (RMB) | Special (secondary fire / dash / walljump) |
| Z | Zoom |

## Interface

| Key | Action |
|---|---|
| Tab | Scoreboard |
| F1 | Vote yes |
| F2 | Vote no |
| F3 | Join |
| F4 | Ready |
| F5 | Chase / spectate |
| F8 | Callvotes menu |
| F12 | Screenshot |
| Enter / T | Chat |
| Y / Right Shift | Team chat |
| Left Shift | Quick menu |
| H | Vsay goodgame |
| ` (backtick) | Open console |

## Notes

**MOUSE2 triple duty:** RMB is bound to `+special`, which the engine routes based on game state — secondary fire when applicable, dash when grounded, walljump when airborne near a wall. This is not a rebind; it is a single binding with context-dependent behavior.

**Weapon switching:** Rebinding weapons to direct keys (1–8) and using Q for last weapon is the competitive standard. Scroll wheel is too imprecise under fire.

## See Also

- [[console]] — configuration and cvars
- [[movement]] — dash and walljump mechanics
