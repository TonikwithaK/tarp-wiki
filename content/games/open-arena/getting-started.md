---
title: "Getting Started"
game: open-arena
layer: canon
type: reference
tags: [open-arena, getting-started]
status: canon
promoted: 2026-06-10
---

OpenArena is free. No account, no installer required. Download, extract, run.

## Download

[openarena.ws/download.php?view.4](http://openarena.ws/download.php?view.4) (full ZIP, 0.8.8)

Extract to any folder. Run `openarena.exe` (Windows) or `openarena` (Linux/Mac).

## Console

Open with `Shift+Esc`. Alternatives depending on keyboard: `~`, `` ` ``, `'`, `½`, `^`, `§`.

Commands must start with `/` or `\`. Without the slash, input is treated as chat.

Tab autocompletes commands and map names. Up/Down arrows browse history.

## Config Files

Config is saved to `q3config.cfg` in the game's homepath.

| Platform | Path |
|----------|------|
| Windows | `%APPDATA%\OpenArena\baseoa\` |
| Linux | `~/.openarena/baseoa/` |
| Mac | `~/Library/Application Support/OpenArena/baseoa/` |

Create `autoexec.cfg` in the `baseoa` folder to run commands on every launch.

`/writeconfig <filename>` saves current settings to file.

## Spawn Defaults

Players spawn with Gauntlet and Machine Gun only. All other weapons must be picked up.

Starting HP: 125 (decays to 100). Starting armor: 0.

## Key Settings

```
sensitivity          Mouse sensitivity
cg_fov          90   Field of view (wider = ~120)
cg_drawfps       1   FPS counter
com_maxfps     125   Frame rate cap
r_gamma        1.0   Gamma
r_picmip         0   Texture quality (0=max)
cg_drawCrosshair 4   Crosshair style
```

## Related

- [[games/open-arena/index\|Overview]]
- [[games/open-arena/console\|Console]]
- [[games/open-arena/movement\|Movement]]
