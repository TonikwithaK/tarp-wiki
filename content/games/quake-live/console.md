---
title: "Console Commands"
game: quake-live
layer: canon
type: reference
tags: [quake-live, console, cvars, commands, reference]
status: canon
promoted: 2026-06-10
---

# Console

Open the console with `~` (tilde/backtick). Commands and cvars can be entered directly. Config files are stored in `baseq3/` under the Quake Live install directory.

## Config File Locations

| Platform | Path |
|---|---|
| Windows | `C:\Users\<user>\AppData\Roaming\id Software\quakelive\home\baseq3\` |
| Linux | `~/.quakelive/quakelive/home/baseq3/` |

Primary config files: `autoexec.cfg` (runs on launch), `server.cfg` (server settings).

---

## Sensitivity and Input

```
sensitivity          5          Mouse sensitivity multiplier
m_yaw                0.022      Horizontal mouse turn rate
m_pitch              0.022      Vertical mouse turn rate
m_accel              0          Mouse acceleration (0 = off)
cl_mouseAccelStyle   0          Acceleration style (0 = Quake3 style)
in_nograb            0          Release mouse from window (1 = ungrab)
```

---

## Video

```
r_fullscreen         1          Fullscreen mode (1 = on, 0 = windowed)
r_mode               -1         Resolution mode (-1 = custom)
r_customwidth        1920       Custom resolution width
r_customheight       1080       Custom resolution height
com_maxfps           125        Frame rate cap (125 recommended for physics)
r_overBrightBits     0          Overbright rendering
r_gamma              1.0        Gamma value
r_picmip             1          Texture detail (higher = lower quality, better FPS)
r_vertexlight        0          Vertex lighting (0 = lightmaps)
cg_drawFPS           1          Show FPS counter
```

---

## Network

```
rate                 25000      Network data rate (bytes/sec); increase on fast connections
snaps                40          Snapshot rate from server
cl_maxpackets        125        Outgoing packet rate
cl_timenudge         0          Packet timing offset (negative = earlier, use -1 to -30)
```

---

## HUD and Display

```
cg_drawTimer         1          Match timer
cg_drawSpeed         1          Speed display
cg_drawAmmoWarning   1          Low ammo warning
cg_drawCrosshair     4          Crosshair style (0-10)
cg_crosshairSize     24         Crosshair size in pixels
cg_crosshairColor    white      Crosshair color
cg_crosshairHealth   0          Color crosshair by health (0 = off)
cg_drawStatus        1          Show health/armor HUD
cg_gibs              1          Gib effects
cg_blood             1          Blood effects
cg_brassTime         0          Bullet casings duration (0 = off, reduces clutter)
```

---

## Sound

```
s_volume             0.7        Master volume (0.0 to 1.0)
s_musicvolume        0          Music volume (0 = mute music)
s_doppler            0          Doppler effect (0 = off)
```

---

## Weapon and Combat

```
cg_autoswitch        0          Auto-switch to picked-up weapon (0 = off recommended)
cg_predictItems      1          Client-side item pickup prediction
pmove_fixed          1          Fixed physics timestep (required for consistent physics)
pmove_msec           8          Physics timestep in ms (8 = 125Hz physics)
```

---

## Competitive Settings

```
cg_teamChatsOnly     0          Filter chat to team only
cg_noProjectileTrail 1          Disable projectile trails (reduces visual noise)
cg_simpleItems       1          Simple 2D item icons instead of 3D models
cg_forceModel        0          Force all players to your model
cg_enemyModel        keel/default  Model override for enemies
cg_enemyColors       FFFF00     Hex color for enemy players
cg_teamModel         keel/default  Model override for teammates
cg_teamColors        0000FF     Hex color for teammates
```

---

## Common Commands

```
/connect <ip:port>   Connect to a server
/disconnect          Disconnect from server
/quit                Quit the game
/map <mapname>       Load a map (server-side)
/callvote map <map>  Vote to change map
/callvote kick <id>  Vote to kick a player
/players             List connected players and IDs
/rcon <command>      Send RCON command (requires rcon_password set)
/condump             Dump console output to file
/exec <file>         Execute a .cfg file
/bind <key> <cmd>    Bind a key to a command
/unbind <key>        Remove a key binding
/bindlist            List all current bindings
/cvarlist            List all cvars
/set <cvar> <value>  Set a cvar
/toggle <cvar>       Toggle a boolean cvar
```

---

## Item Timer Commands (minqlx)

On servers running minqlx with item timer plugins, commands are prefixed with `!`:

```
!help                List available plugin commands
!time                Server time
!maps                List available maps
```

Specific commands depend on which minqlx plugins the server has loaded.

## Related

- [[controls|Controls]]: key bindings
- [[modding/server-hosting|Server Hosting]]: server-side cvar reference
