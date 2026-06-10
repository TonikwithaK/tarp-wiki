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

Open the console with `~` (tilde). First time: press `Ctrl+Alt+~`, then type `com_allowConsole "1"` to allow `~` access from that point on.

Tab auto-completes commands and map names. PgUp/PgDn to scroll.

---

## Config Files

| File | Description |
|------|-------------|
| `repconfig.cfg` | Auto-generated. Key bindings and preferences. Never manually edit |
| `qzconfig.cfg` | Auto-generated. Other settings. Never manually edit |
| `autoexec.cfg` | User-created. Runs automatically on launch. Safe to edit in WordPad/a text editor that isn't Notepad |

To apply changes made in console: `writeconfig autoexec`

To reset all settings: delete `repconfig.cfg`, `qzconfig.cfg`, and `autoexec.cfg`, then relaunch.

If settings won't save, run `writeconfig autoexec` in console after making changes.

---

## File Locations

| Platform | Path |
|----------|------|
| Windows | `C:\Users\<user>\AppData\Roaming\id Software\quakelive\home\baseq3\` |
| Linux | `~/.quakelive/quakelive/home/baseq3/` |

---

## CVAR Reference

1,079 CVARs documented. Sourced from [euere.eu/ql](https://www.euere.eu/ql/) (September 2025).

- [[console/cvars-a-c|CVars A–C]]: bots, crosshair, HUD, client network, com_
- [[console/cvars-d-p|CVars D–P]]: game settings, weapon damage, knockback, physics
- [[console/cvars-r-t|CVars R–T]]: rendering, sound, server settings
- [[console/cvars-u-w|CVars U–W]]: UI variables

---

## Command Reference

205 commands documented. Sourced from [euere.eu/ql](https://www.euere.eu/ql/).

- [[console/commands|Console Commands]]: full alphabetical reference
- [[console/button-commands|Button Commands]]: +attack, +forward, +moveup, etc.
- [[console/premium-server-commands|Premium Server Commands]]: admin and owner commands for paid servers

---

## Quick Reference

### Commonly Used CVars

```
com_maxfps        125       Frame rate cap (125 recommended for consistent physics)
pmove_fixed       1         Fixed physics timestep
pmove_msec        8         8ms = 125Hz physics
rate              25000     Network data rate (bytes/sec)
snaps             40        Snapshot rate from server
cl_maxpackets     125       Outgoing packet rate
cl_timenudge      0         Packet timing offset

r_fullscreen      1         Fullscreen
r_mode            -1        Custom resolution
r_customwidth     1920      Resolution width
r_customheight    1080      Resolution height
r_picmip          0         Texture detail (0=highest, 16=near solid)

cg_fov            100       Field of view
cg_drawCrosshair  4         Crosshair style (0–10)
cg_crosshairSize  24        Crosshair size
cg_simpleItems    1         2D item icons
cg_noProjectileTrail 1      No projectile trails
cg_autoswitch     0         No auto weapon switch

s_volume          0.7       Master volume
s_musicvolume     0         Mute music
```

### Common Commands

```
/connect <ip:port>     Connect to server
/disconnect            Leave server
/map <mapname>         Load map (server)
/callvote map <map>    Vote to change map
/players               List players and IDs
/rcon <command>        RCON command
/exec <file>           Execute a .cfg file
/bind <key> <cmd>      Bind key
/cvarlist              List all cvars
/writeconfig autoexec  Save settings
```

---

## Related

- [[controls|Controls]]: key binding reference
- [[modding/server-hosting|Server Hosting]]: server-side setup
- [[console/appendix|Appendix]]: CVAR flag legend, prefix reference, color chart
