---
title: "Console"
game: open-arena
layer: canon
type: reference
tags: [open-arena, console, cvars, commands]
status: canon
promoted: 2026-06-10
source: https://openarena.fandom.com/wiki/Console
---

Full reference: [openarena.fandom.com/wiki/Console](https://openarena.fandom.com/wiki/Console)

Open with `Shift+Esc`. Alternatives: `~`, `` ` ``, `'`, `½`, `^`, `§`, `\`.

Commands must start with `/` or `\`. Without the slash, input is treated as chat. On a dedicated server (`oa_ded`), no slash is needed.

Command names are case-insensitive. Tab autocompletes.

## Setting Variables

| Command | Behavior |
|---------|----------|
| `/set <var> <val>` | Sets cvar. Not saved on exit unless already in q3config.cfg. |
| `/seta <var> <val>` | Sets and archives. Saved on exit / writeconfig. |
| `/setu <var> <val>` | Sets as userinfo (client settings like rate). |
| `/sets <var> <val>` | Sets as serverinfo (visible in server browser). Has data limit. |
| `/unset <var>` | Deletes user-created variable (not pre-defined ones). |
| `/reset <var>` | Resets variable to default. |
| `/cvar_restart` | Flushes all custom and most pre-defined vars. Deletes stats and SP progress. No confirmation. |

## Common CVARs

```
sensitivity          Mouse sensitivity
m_yaw        0.022  Horizontal mouse scale
m_pitch      0.022  Vertical mouse scale
cg_fov          90  Field of view
com_maxfps     125  Frame rate cap
cg_drawfps       1  FPS counter
cg_drawspeed     1  Speed display
r_gamma        1.0  Gamma
r_picmip         0  Texture quality (0=max, higher=lower)
rate         25000  Network data rate
snaps           40  Snapshot rate
cl_maxpackets  125  Outgoing packet rate
```

## Common Commands

```
/map <mapname>              Load map
/devmap <mapname>           Load map with cheats
/map_restart [seconds]      Restart current game
/connect <ip:port>          Connect to server
/disconnect                 Return to main menu
/quit                       Exit game
/exec <filename.cfg>        Execute config file
/writeconfig <filename>     Save config to file
/cvarlist                   List all variables
/cmdlist                    List all commands
/condump <filename>         Export console log to file
```

## RCON

```
# On server:
\rconpassword "your_password"

# On client:
\rconpassword "your_password"
\rconaddress <ip:port>      (if not connected)
\rcon <command>
```

Never use `/sets` to set rconpassword. It becomes visible in `/serverstatus`.

## Logging

```
/logfile 0   No log (default)
/logfile 1   Buffered log to qconsole.log
/logfile 2   Continuous log to qconsole.log
```

## Related

- [[games/open-arena/getting-started\|Getting Started]]
- [[games/open-arena/index\|Overview]]
