---
title: "Controls"
game: warfork
layer: canon
type: reference
tags: [warfork, controls, keybinds, reference]
status: canon
promoted: 2026-06-09
---

All bindings are fully customizable via the `bind` command in console or the settings menu. Default bindings are from the [game source](https://github.com/TeamForbiddenLLC/warfork-qfusion/blob/master/assets/default_binds_kbmouse.cfg).

To rebind a key:
```
bind <key> <command>
```
To see all current bindings:
```
bindlist
```
Config is saved to `config.cfg` in your data folder. See [[getting-started]] for data folder locations.

---

## Movement

| Command | Default | Notes |
|---|---|---|
| `+forward` | W | |
| `+back` | S | |
| `+moveleft` | A | |
| `+moveright` | D | |
| `+moveup` (jump) | Space | Hold to autohop (disable with `cg_noAutoHop 1`) |
| `+movedown` (crouch) | C | |
| `+speed` (walk) | Left Alt | Reduces speed to 160 UPS |
| `+special` (dash / walljump) | Mouse2 | See note below |

`+special` is context-dependent: dash when grounded, walljump when airborne near a wall, secondary fire on weapons that have it. One binding covers all three.

---

## Weapons

| Command | Default | Slot |
|---|---|---|
| `use Gunblade` | 1 | 1 |
| `use Machinegun` | 2 | 2 |
| `use Riotgun` | 3 | 3 |
| `use Grenade Launcher` | 4 | 4 |
| `use Rocket Launcher` | 5 | 5 |
| `use Plasmagun` | 6 | 6 |
| `use Lasergun` | 7 | 7 |
| `use Electrobolt` | 8 | 8 |
| `use Instagun` | 9 | 9 (Instagib only) |
| `weapnext` | Mouse wheel up | |
| `weapprev` | Mouse wheel down | |
| `weaplast` | Q | Switch to last used weapon |
| `drop fullweapon` | Backspace | Drop current weapon |
| `drop flag` | L | Drop bomb or flag (objective modes) |

**Competitive standard:** Direct keys for primary weapons (RL, LG, EB) and Q for `weaplast`. Many players rebind primaries to closer keys (e.g. RL to mouse4, LG to mouse5, EB to E) and keep slots 1–9 as fallbacks. Scroll wheel is too imprecise for weapon switching under fire.

`weapcross` is an alternative approach: shows weapon sets near your crosshair that can be cycled. Example:
```
bind p "weapcross 1"   // Gunblade / Machinegun
bind [ "weapcross 3"   // Rocket Launcher / Plasmagun
bind ] "weapcross 4"   // Lasergun / Electrobolt
```

---

## Combat

| Command | Default |
|---|---|
| `+attack` | Mouse1 |
| `+special` | Mouse2 |
| `+zoom` | Z |

---

## Communication

| Command | Default | Notes |
|---|---|---|
| `messagemode` | Enter / T | Global chat |
| `messagemode2` | Y / Right Shift | Team chat |
| `+quickmenu` | Left Shift | Quick menu with common vsay commands |
| `vsay goodgame` | H | Voice say: good game |
| `vsay` | | Run without argument for full vsay list |

---

## Interface

| Command | Default |
|---|---|
| `+scores` | Tab |
| `vote yes` | F1 |
| `vote no` | F2 |
| `join` | F3 |
| `ready` | F4 |
| `chase` | F5 |
| `menu_callvotes` | F8 |
| `screenshot` | F12 |
| `toggleconsole` | ` (backtick) |

---

## Useful Binds

Toggle console (also configurable via settings):
```
bind ` "toggleconsole"
```

Kill yourself (useful in race to restart a run):
```
bind k "kill"
```

Quick ready toggle:
```
bind F4 "toggleready"
```

Print current position (useful for map exploration):
```
bind p "position"
```

---

## Related

- [[console]]: full command and cvar reference
- [[movement]]: dash and walljump mechanics
- [[getting-started]]: data folder paths and config locations
