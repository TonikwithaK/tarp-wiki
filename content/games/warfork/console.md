---
title: "Console — Warfork"
game: warfork
layer: canon
type: reference
tags: [warfork, console, commands, configuration]
status: canon
promoted: 2026-06-09
---

# Console — Warfork

The console is the primary interface for configuring Warfork beyond what the menus expose. Most serious players use it regularly — for testing settings, enabling HUD elements, and scripting behaviors that aren't bindable through the UI.

## Opening the Console

Press the backtick key (`~`) in-game to toggle the console open and closed. You can also access it through the menu icon in the top corner of the main screen.

## Where Settings Are Stored

Persistent settings are written to `config.cfg` in your `basewf` folder (see [[getting-started]] for the path). When you set a cvar in the console and it survives a restart, it was written there. You can also edit `config.cfg` directly in a text editor — useful for bulk changes, autoexec scripts, or transferring configs between machines.

Changes made mid-session without a `set` or equivalent write command may not persist. When in doubt, confirm with `writeconfig` or check that your value appears in `config.cfg`.

## Client vs. Server Commands

Commands in Warfork are scoped. Some are **client-only** — they affect your local game and can be set freely. Others are **server-only** — they require you to be running the server, or to have admin access on a remote server. Running a server-side command as a client without permissions will either silently fail or return an error.

Server admins typically interact with the server directly via its executable or RCON, not through a game client console.

## Command Flags

Many cvars accept flags that control their behavior — whether a value is archived to config, whether it's visible to clients, whether it can be changed by clients on a server, and so on. These are set internally by the engine; as a player you mostly see their effects rather than setting flags yourself. What matters practically: if a cvar doesn't stick after a restart, it may not be archived, and you'll need to set it in your `autoexec.cfg` instead.

## HUD and Display Commands

**`cg_strafeHUD 1`** — enables the strafe efficiency indicator on your HUD. This is a visual bar that shows how effectively you're converting mouse movement into air acceleration. Indispensable for learning strafejumping. See [[movement]] for full context on how to read and use it.

## Bot Commands

Bots are useful for offline testing — practicing aim, checking weapon behavior, or verifying that a config change works as expected without needing a live server.

| Command | Effect |
|---------|--------|
| `bot_dummy` | Spawns a stationary dummy bot for aim practice |
| `bot_showcombat` | Visualizes the bot's combat decision-making |
| `bot_showlrgoal` | Shows the bot's long-range navigation goal |
| `bot_showpath` | Displays the bot's current navigation path |

These are primarily development and debugging tools, but `bot_dummy` in particular is useful for weapon testing and warming up aim offline.

## Cheats

`sv_cheats` is a server-side cvar that gates access to cheat commands. It cannot be enabled on someone else's server without admin permissions. On a local server you control, setting `sv_cheats 1` unlocks commands like `give`, `noclip`, and others. This is useful for map exploration, testing item locations, or practicing specific scenarios without playing a full match.

## Related Pages

- [[movement]] — strafe HUD and movement mechanics
- [[getting-started]] — config file locations and initial setup
