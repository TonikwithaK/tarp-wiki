---
title: "Console"
game: quake-live
layer: canon
type: reference
tags: [quake-live, console, cvars, commands, reference]
status: canon
promoted: 2026-06-10
---

# Console

Open with `~` (tilde). First time: press `Ctrl+Alt+~`, then run `com_allowConsole "1"` so `~` works from that point on.

Tab auto-completes commands and map names. PgUp/PgDn scrolls the output.

Full CVAR and command reference (1,079 CVARs, 205 commands): [euere.eu/ql](https://www.euere.eu/ql/)

---

## Config Files

| File | Description |
|------|-------------|
| `repconfig.cfg` | Auto-generated. Key bindings and preferences. Never manually edit |
| `qzconfig.cfg` | Auto-generated. Other settings. Never manually edit |
| `autoexec.cfg` | User-created. Runs on launch. Safe to edit in any plain text editor (not Notepad on Windows) |

**Settings not saving:** run `writeconfig autoexec` in console after making changes.

**Reset all settings:** delete `repconfig.cfg`, `qzconfig.cfg`, and `autoexec.cfg`, then relaunch.

### File Locations

| Platform | Path |
|----------|------|
| Windows | `C:\Users\<user>\AppData\Roaming\id Software\quakelive\home\baseq3\` |
| Linux | `~/.quakelive/quakelive/home/baseq3/` |

---

## Competitive CVars

```
com_maxfps           125    Frame rate cap (125 = consistent physics)
pmove_fixed          1      Fixed physics timestep
pmove_msec           8      8ms timestep = 125Hz physics
rate                 25000  Network data rate (bytes/sec)
cl_maxpackets        125    Outgoing packet rate
cl_timenudge         0      Packet timing offset (-1 to -30 for compensation)
snaps                40     Snapshot rate from server
```

---

## Video CVars

```
r_fullscreen         1      Fullscreen (0 = windowed)
r_mode               -1     Resolution mode (-1 = custom, -2 = desktop)
r_customwidth        1920   Custom width
r_customheight       1080   Custom height
r_picmip             0      Texture detail (0 = highest, 16 = near solid colors)
r_gamma              1      Gamma
r_vertexlight        0      0 = lightmaps, 1 = vertex lighting
r_fastsky            0      1 = disable skyboxes
r_dynamiclight       1      Dynamic lights (0 = off for performance)
r_enablePostProcess  0      Post-processing (off recommended for competitive)
```

---

## HUD CVars

```
cg_draw2D            1      HUD on/off
cg_fov               100    Field of view (10–130)
cg_drawCrosshair     4      Crosshair style (0–10, 0 = off)
cg_crosshairSize     24     Crosshair size in pixels
cg_crosshairColor    7      Color (1–26)
cg_crosshairHealth   0      Color crosshair by health (1 = on)
cg_crosshairHitStyle 2      Hit indicator style (0–8)
cg_drawFPS           1      FPS counter
cg_drawTimer         1      Match timer
cg_drawSpeed         0      Speed display
cg_lagometer         0      Netgraph (1 = on)
cg_simpleItems       1      2D item icons instead of 3D models
cg_noProjectileTrail 1      No projectile trails
cg_autoswitch        0      No auto weapon switch on pickup
cg_brassTime         0      No bullet casings
```

---

## Sound CVars

```
s_volume             0.7    Master volume (0.0–1.0)
s_musicvolume        0      Music volume (0 = mute)
s_doppler            0      Doppler effect (0 = off)
```

---

## Common Commands

```
connect <ip:port>      Connect to server
disconnect             Leave server
map <mapname>          Load a map (server)
callvote map <map>     Vote to change map
callvote kick <name>   Vote to kick player
players                List players and their IDs
rcon <command>         Send RCON command (requires rcon_password)
exec <filename>        Execute a .cfg file
bind <key> <command>   Bind a key
unbind <key>           Remove a binding
bindlist               List all current bindings
cvarlist               List all cvars
toggle <cvar>          Toggle a boolean cvar
writeconfig autoexec   Save current settings to autoexec.cfg
condump <file>.txt     Dump console output to file
vid_restart            Restart video (apply r_ cvar changes)
```

---

## Button Commands

Used with `bind <key> <command>`:

```
+attack        Fire weapon
+moveup        Jump / swim up
+movedown      Crouch / swim down
+forward       Move forward
+back          Move back
+moveleft      Strafe left
+moveright     Strafe right
+zoom          Zoom
+scores        Scoreboard
+speed         Walk toggle
+chat          Chat window
+acc           Weapon accuracy panel
```

---

## Premium Server Commands

Available on paid/rented servers. Access levels: none = all players, admin = admins, owner = owner only.

| Command | Level | Description |
|---------|-------|-------------|
| `players` | none | List players with IDs and status |
| `timeout` | none | Pause game for 30 seconds |
| `timein` | none | Resume after timeout |
| `abort` | admin | End game, return to warmup (no stats counted) |
| `allready` | admin | Force all players ready |
| `kickban` | admin | Remove and ban player for current period (takes ID) |
| `lock` | admin | Stop players joining a team |
| `unlock` | admin | Allow players to join teams |
| `mute` | admin | Block player chat |
| `unmute` | admin | Remove mute |
| `pause` | admin | Pause match indefinitely |
| `unpause` | admin | Resume match |
| `put` | admin | Move player to team (r/b/s for red/blue/spec, takes ID) |
| `opsay` | admin | Broadcast message to all players |
| `op` | owner | Grant admin privileges (takes ID) |
| `deop` | owner | Remove admin privileges (takes ID) |
| `stopserver` | owner | Shut down server immediately |

---

## CVAR Flag Legend

| Flag | Meaning |
|------|---------|
| `[A]` | Archived — saved to config |
| `[C]` | Cheat-protected — localhost/cheat servers only |
| `[I]` | Init — command line only, not settable from console |
| `[L]` | Latched — requires restart to apply |
| `[R]` | Read-only |
| `[S]` | Server info — broadcast to clients |
| `[U]` | User info — sent to server on connect |
| `[T]` | Saved to QL database |

## Related

- [[games/quake-live/controls|Controls]]
- [[games/quake-live/modding/server-hosting|Server Hosting]]
