---
title: "Console Commands"
game: quake-live
layer: canon
type: reference
tags: [quake-live, console, commands, reference]
status: canon
promoted: 2026-06-10
source: https://www.euere.eu/ql/
---

# Console Commands

Full reference sourced from euere.eu/ql/ — 205 commands documented, updated September 2025.

Commands are entered directly in the console or bound to keys via `bind <key> <command>`. For button/input commands (movement, fire, etc.) see [[console/button-commands|Button Commands]].

---

## A
| Command | Usage | Description |
|---------|-------|-------------|
| `addbot` | `addbot <botname> [skill 1-5] [team] [msec delay]` | Add a computer opponent |
| `alias` | `alias <aliasname> [command]` | Set an alias for a command |

---

## B
| Command | Usage | Description |
|---------|-------|-------------|
| `bind` | `bind <key> [command]` | Assign action to a key |
| `bindlist` | `bindlist` | Display current binds |
| `block` | `block [playername]` | Block player's chat |
| `blocklist` | `blocklist` | List currently blocked players |

---

## C
| Command | Usage | Description |
|---------|-------|-------------|
| `callvote` | (see below) | Call a vote |
| `centerview` | `centerview` | Snap view to horizontal plane |
| `clear` | `clear` | Clear console output |
| `clearcvar` | `clearcvar` | Clear a cvar or all cvars |
| `clientkick` | `clientkick <slot>` | Kick client by slot number |
| `cmdlist` | `cmdlist <query>` | List available commands |
| `condump` | `condump <filename>.txt` | Write console contents to file |
| `connect` | `connect <ip:port>` | Connect to server by IP |
| `cvar_restart` | `cvar_restart` | Restart CVAR system |
| `cvarlist` | `cvarlist <query>` | List CVARs matching query |

### callvote options
```
callvote map_restart
callvote nextmap
callvote map <mapname>
callvote g_gametype <n>
callvote kick <player>
callvote clientkick <clientnum>
callvote timelimit <time>
callvote fraglimit <frags>
callvote shuffle
callvote teamsize <number>
callvote cointoss <heads/tails>
```

---

## D
| Command | Usage | Description |
|---------|-------|-------------|
| `demo` | `demo <demoname>` | Play a demo file |
| `devmap` [C] | `devmap <mapname>` | Open map with cheats enabled |
| `dir` | `dir [directory]/[extension]` | Show files in directory |
| `disconnect` | `disconnect` | Leave current server |
| `dropflag` | `dropflag` | Drop flag in CTF |
| `droppowerup` | `droppowerup` | Drop a power-up |
| `dropweapon` | `dropweapon` | Drop current weapon |
| `dumpuser` | `dumpuser <userid>` | Display info about a client |

---

## E
| Command | Usage | Description |
|---------|-------|-------------|
| `echo` | `echo <string>` | Print message to console |
| `exec` | `exec <filename>` | Execute a .cfg file |

---

## F
| Command | Usage | Description |
|---------|-------|-------------|
| `find` | `find <substring>` | Case-sensitive console entry search |
| `follow` | `follow <position|name>` | Follow player in spectator (1=leader, 2=2nd, or name) |
| `forfeit` | `forfeit` | Forfeit the game |

---

## G
| Command | Usage | Description |
|---------|-------|-------------|
| `gfxinfo` | `gfxinfo` | List graphics settings info |
| `give` [C] | `give [item]` / `give all` | Give item to player |
| `god` [C] | `god` | Toggle invincibility |

---

## K
| Command | Usage | Description |
|---------|-------|-------------|
| `kick` | `kick <playername>` | Kick a client (server) |
| `kill` | `kill` | Kill your player (requires g_allowKill 1) |

---

## M
| Command | Usage | Description |
|---------|-------|-------------|
| `map` | `map <mapname>` | Load a map (server) |
| `map_restart` | `map_restart` | Restart current map |
| `messagemode` | `messagemode` | Open all-chat input |
| `messagemode2` | `messagemode2` | Open team chat input |

---

## N
| Command | Usage | Description |
|---------|-------|-------------|
| `nextmap` | `nextmap` | Load next map |
| `noclip` [C] | `noclip` | Toggle noclip |
| `notarget` [C] | `notarget` | Bots ignore you |

---

## P
| Command | Usage | Description |
|---------|-------|-------------|
| `players` | `players` | List connected players and IDs |

---

## Q
| Command | Usage | Description |
|---------|-------|-------------|
| `quit` | `quit` | Quit the game |

---

## R
| Command | Usage | Description |
|---------|-------|-------------|
| `rcon` | `rcon <command>` | Send RCON command (requires rcon_password) |
| `record` | `record <demoname>` | Start recording a demo |
| `reconnect` | `reconnect` | Reconnect to last server |

---

## S
| Command | Usage | Description |
|---------|-------|-------------|
| `say` | `say <message>` | Chat to all |
| `say_team` | `say_team <message>` | Chat to team |
| `set` | `set <cvar> <value>` | Set a cvar |
| `seta` | `seta <cvar> <value>` | Set and archive a cvar |
| `serverinfo` | `serverinfo` | Display current server info |
| `status` | `status` | Server status and player list |
| `stopdemo` | `stopdemo` | Stop playing demo |
| `stoprecord` | `stoprecord` | Stop recording demo |

---

## T
| Command | Usage | Description |
|---------|-------|-------------|
| `tell` | `tell <clientnum> <message>` | Private message |
| `toggle` | `toggle <cvar>` | Toggle a boolean cvar |

---

## U
| Command | Usage | Description |
|---------|-------|-------------|
| `unbind` | `unbind <key>` | Remove a key binding |
| `unbindall` | `unbindall` | Remove all key bindings |

---

## V
| Command | Usage | Description |
|---------|-------|-------------|
| `vid_restart` | `vid_restart` | Restart video system (apply r_ cvar changes) |
| `vote` | `vote yes` / `vote no` | Cast a vote |
| `vstr` | `vstr <variable>` | Execute contents of a string variable |

---

## W
| Command | Usage | Description |
|---------|-------|-------------|
| `weapon` | `weapon <number>` | Switch to weapon by slot |
| `weapnext` | `weapnext` | Next available weapon |
| `weapprev` | `weapprev` | Previous available weapon |
| `writeconfig` | `writeconfig <filename>` | Write current cvar settings to file |

The most important use of writeconfig: if settings are not saving, run `writeconfig autoexec` in console after making changes.

## Related

- [[console|Console Overview]]: config files, console access
- [[console/button-commands|Button Commands]]: movement, fire, hold-key inputs
- [[console/premium-server-commands|Premium Server Commands]]: admin and owner commands
- [[controls|Controls]]: key binding reference
