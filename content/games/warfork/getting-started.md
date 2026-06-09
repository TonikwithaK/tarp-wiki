---
title: "Getting Started — Warfork"
game: warfork
layer: canon
type: guide
tags: [warfork, getting-started, download, setup]
status: canon
promoted: 2026-06-09
---

# Getting Started — Warfork

Warfork is a free arena FPS forked from Warsow, built around fast movement mechanics and precision gunplay. This page covers installation, basic setup, and where to find things once you're in.

## Download

**Steam** is the easiest route. Search for Warfork or navigate directly to App ID `671610`. The game is free.

**Linux dedicated servers** use SteamCMD. Anonymous login pulls App ID `1136510` (the dedicated server package). If you need the full client via SteamCMD, log in with your Steam account and use App ID `671610`.

```
# Anonymous server install
steamcmd +login anonymous +app_update 1136510 validate +quit

# Full client (requires login)
steamcmd +login <username> +app_update 671610 validate +quit
```

For server setup beyond the install step, see [[server-hosting]].

## Bug Reports

Report bugs and reach the community on Discord: **discord.gg/VY95TKZ**

## Config File Locations

Warfork stores persistent settings, binds, and autoexec scripts in a `basewf` folder under your user profile. The location depends on your OS:

| Platform | Path |
|----------|------|
| Windows  | `%USERPROFILE%\My Documents\My Games\Warfork 2.1\basewf\` |
| Mac      | `~/Library/Application Support/Warfork-2.1/basewf/` |
| Linux    | `~/.local/share/warfork-2.1/basewf/` |

`config.cfg` inside that folder stores your settings. You can edit it directly or let the game write to it via the console. See [[console]] for how to work with it effectively.

## Player Name Color Codes

Color your name by inserting a caret followed by a digit anywhere in the string. These work in the name field and in chat.

| Code | Color  |
|------|--------|
| `^0` | Black  |
| `^1` | Red    |
| `^2` | Green  |
| `^3` | Yellow |
| `^4` | Blue   |
| `^5` | Cyan   |
| `^6` | Purple |
| `^7` | White  |
| `^8` | Orange |
| `^9` | Gray   |

Example: `^1War^7fork` renders "War" in red and "fork" in white.

## Next Steps

- [[controls]] — default keybinds and how to rebind
- [[console]] — opening the console, useful commands, config workflow
- [[server-hosting]] — running your own server
