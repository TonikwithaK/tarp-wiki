---
title: "Getting Started"
game: quake-live
layer: canon
type: guide
tags: [quake-live, getting-started, setup, config]
status: canon
promoted: 2026-06-09
---

## Download

Quake Live is available on Steam. It is free to play.

---

## Config File Locations

| Platform | Path |
|---|---|
| Steam (Windows) | `Steam\SteamApps\common\Quake Live\<steamID64>\baseq3` |
| Windows standalone | `%AppData%\..\LocalLow\id Software\quakelive\home\baseq3` |
| Linux | `~/.quakelive/quakelive/home/baseq3` |
| Mac | `~/Library/Application Support/Quakelive/` |

---

## Config Files

- `repconfig.cfg`: Auto-generated. Stores key bindings and preferences. Do not edit directly.
- `qzconfig.cfg`: Auto-generated. Stores other settings. Do not edit directly.
- `autoexec.cfg`: User-created. Executes on every launch. This is where player settings go.

---

## Setup Workflow

1. Join any game.
2. Open the console: hold `Ctrl+Alt`, then press `~`. Alternatively, set `com_allowConsole 1` in a config, then use `~` directly.
3. Run `/writeconfig myconfig` to dump current settings to a file.
4. Create `autoexec.cfg` in the baseq3 folder.
5. Add `exec myconfig` to `autoexec.cfg`.

**Console tips:**
- Tab autocompletes commands.
- PgUp / PgDn scrolls the console output.

---

## Spawn Defaults

Players spawn with:

- Machine Gun
- 125 HP

All other weapons, health, and armor must be picked up from the map. There is no health regeneration.

---

## Related

- [Movement](movement)
- [Health and Armor](health-and-armor)
