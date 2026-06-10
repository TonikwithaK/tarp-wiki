---
title: "Console Commands"
game: warfork
layer: canon
type: reference
tags: [warfork, console, cvars, commands, reference]
status: canon
promoted: 2026-06-09
---

Open the console with `~` (backtick). Full source: [Warfork Wiki](https://warforkwiki.com/index.php?title=Console_Commands).

## Cvar Flags

| Flag | Meaning |
|---|---|
| `*` | Saved to config.cfg |
| `U` | Uploaded to server (player info) |
| `S` | Server info, synced to all clients |
| `-` | Read-only |
| `L` | Requires subsystem restart |
| `C` | Cheat cvar, requires `sv_cheats 1` |

---

## Visibility and Models

```
cg_teamALPHAcolor        "254 101 101"    RGB color for Alpha team players
cg_teamBETAcolor         "153 204 255"    RGB color for Beta team players
cg_teamPLAYERScolor      "0 255 70"       RGB color for non-team gametypes
cg_teamALPHAmodelForce   1                Force all Alpha players to one model
cg_teamBETAmodelForce    1                Force all Beta players to one model
cg_teamALPHAskin         "default"        "default" or "fullbright"
cg_teamBETAskin          "default"        "default" or "fullbright"
cg_outlinePlayers        1                Outline player models
cg_outlineModels         1                Outline all models
cg_outlineWorld          0                Outline world geometry (expensive)
cg_forceMyTeamAlpha      0                Always show HUD/colors as if on Alpha
```

---

## HUD

```
cg_clientHUD             ""               HUD name (adem, classic, default)
cg_specHUD               ""               HUD while spectating
cg_showHUD               1                Enable HUD
cg_draw2D                1                Enable all 2D rendering (HUD, scores)
cg_showSpeed             1                Speed display (0=off, 1=bottom center)
cg_showTimer             1                Match timer
cg_showFPS               0                FPS counter
cg_showPickup            1                Item pickup notifications
cg_showObituaries        3                Kill feed
cg_showAwards            1                Award popups (On Fire!, etc.)
cg_showPressedKeys       0                Show key presses (useful for demos)
cg_showItemTimers        3                Item timers in spectator mode
cg_showMiniMap           0                Minimap if gametype supports it
cg_weaponlist            1                Weapon list on HUD
cg_showTeamLocations     1                Teammate location indicators
cg_showTeamMates         1                Teammate indicators
cg_showPlayerNames       1                Names above player models
cg_showPlayerNames_zfar  824              Distance at which names stop rendering
cg_damageNumbers         1                Damage numbers when hitting players
cg_damageNumbersColor    8                Color (0=white 2=red 3=green 5=yellow)
cg_damageNumbersSize     1                Size (1=tiny 2=small 3=medium 4=large)
cg_damage_indicator      1                Directional hit indicator
cg_strafeHUD             0                Strafe angle indicator (see movement)
```

---

## Crosshair

```
cg_crosshair             1                Style (0=none, 1-13)
cg_crosshair_color       "255 255 255"    RGB
cg_crosshair_size        24               Size
cg_crosshair_damage_color "255 0 0"       Color when landing a hit
cg_showCrosshairDamage   1                Change crosshair color on hit
cg_crosshair_strong      0                Separate crosshair for strong fire
cg_crosshair_strong_color "255 255 255"   RGB for strong crosshair
cg_crosshair_strong_size 24               Size for strong crosshair
```

---

## Visual Effects

```
cg_simpleItems           0                2D item models (0=3D, 1=animated 2D, 2=static 2D)
cg_decals                1                Projectile impact decals
cg_particles             1                Particle effects
cg_gibs                  1                (Placeholder, no effect)
cg_bloodTrail            10               Damage ring density (0=off)
cg_bloodTrailAlpha       1.0              Damage ring transparency
cg_cartoonEffects        7                Cartoon effects (2=dust, 4=dash, 7=all)
cg_explosionsDust        0                Explosion dust on GL/RL impact
cg_explosionsRing        0                Explosion ring on GL/RL impact
cg_ebbeam_alpha          0.4              Electrobolt beam transparency
cg_ebbeam_time           0.6              Electrobolt beam duration
cg_ebbeam_width          64               Electrobolt beam width
cg_teamColoredBeams      0                LG beam color matches team color
cg_colorCorrection       1                Map color correction (GPU dependent)
```

---

## Movement

```
cg_movementStyle         0                0=old movement, 1=new movement (U flag, uploaded to server)
cg_noAutoHop             0                Disable autohop (holding space) (U flag)
```

---

## Mouse

```
sensitivity              3                Base mouse sensitivity
m_yaw                    0.022            X axis speed scale
m_pitch                  0.022            Y axis speed scale (set in config)
m_raw                    1                Raw mouse input (recommended: 1)
m_accel                  0                Mouse acceleration (0=off)
m_accelStyle             0                Accel style (0=legacy, 1=QL style, 2=extended)
m_accelOffset            0                Accel offset for styles 1/2
m_accelPow               2                Accel exponent for style 2 (must be >2)
m_filter                 0                Input filtering (0=off, 1=linear, 2=extrapolation)
m_filterStrength         0.5              Filter strength
m_sensCap                0                Max sensitivity cap for style 2
zoomsens                 0                Sensitivity while zoomed (0=use normal sensitivity)
zoomfov                  30               FOV while zoomed
```

---

## Graphics

```
fov                      100              Field of view
r_gamma                  1.0              Gamma
r_brightness             0                Brightness (0-1.0)
r_dynamiclight           1                Dynamic lighting
r_fastsky                0                Simple skybox (performance)
r_shadows                0                Shadows (0=off, 1=simple, 2=shadowmaps)
r_detailtextures         1                Detail textures
r_picmip                 0                Texture quality (0=max, higher=lower)
r_fxaa                   1                FXAA antialiasing
r_soft_particles         1                Soft particles
r_multithreading         1                Multithreaded rendering
r_fullbright             0                Max brightness all textures (cheat)
r_drawflat               0                Flat wall/floor colors (for visibility)
r_wallcolor              "255 255 255"    Wall color with r_drawflat 1
r_floorcolor             "255 153 0"      Floor color with r_drawflat 1
cl_maxfps                250              FPS cap (client)
r_maxfps                 250              FPS cap (renderer)
```

---

## Audio

```
s_volume                 0.8              Master volume
s_musicvolume            0.15             Music volume
cg_volume_effects        1.0              Effects volume
cg_volume_announcer      1.0              Announcer volume
cg_volume_hitsound       1.0              Hit sound volume
cg_volume_players        1.0              Player sound volume
cg_volume_voicechats     1.0              Vsay volume
cg_chatBeep              1                Chat notification sound
s_module                 1                Sound engine (0=none, 1=Qfusion, 2=OpenAL)
s_globalfocus            0                Mute when alt-tabbed
```

---

## Weapon

```
cg_weaponAutoswitch      2                Auto-switch (0=off, 1=one click, 2=two clicks)
cg_gun                   1                Show weapon model
cg_gun_fov               90               Weapon model FOV
cg_gun_alpha             1                Weapon model transparency
cg_gunbob                1                Weapon bob
cg_gunx / cg_guny / cg_gunz  0           Weapon model position offset
cg_predictLaserBeam      1                Draw LG beam predictively regardless of lag
```

---

## Demo and Recording

```
cg_autoaction_demo       0                Auto-record demos after warmup
cg_autoaction_screenshot 0                Auto-screenshot final scoreboard
cg_autoaction_stats      0                Auto-save match stats
record <name>                             Record single-POV demo
serverrecord <name>                       Record multi-POV demo (server-side)
demoavi                                   Export demo to frames/audio
cl_demoavi_fps           30               Frame rate for demoavi export
```

---

## Race

```
cg_raceGhosts            0                Show ghost replays in race
cg_raceGhostsAlpha       0.25             Ghost transparency
```

---

## Player Info

```
name                                      Your nickname (U flag)
clan                                      Clan tag on scoreboard (U flag)
model                    "bigvic"         Player model (U flag)
skin                     "default"        Skin ("default" or "fullbright")
color                    "255 255 255"    Player color RGB (U flag)
hand                     0                Weapon hand (0=right, 1=left)
handicap                 0                Reduce damage output by x%
fov                      100              Field of view
sensitivity              3                Mouse sensitivity
```

---

## Server Admin

```
sv_hostname                               Server name in browser (S flag)
sv_port                  44400            UDP port
sv_public                0                List on master servers (1=yes)
sv_pure                  0                Enforce pure client files
sv_maxclients                             Max player slots (S, L)
sv_cheats                0                Enable cheat cvars (S, L)
sv_skilllevel            2                Bot difficulty (0=easy, 1=medium, 2=hard)
sv_http                  1                HTTP file server for downloads
sv_http_port             44444            HTTP server port
sv_MOTD                  0                Enable message of the day
sv_MOTDString                             MOTD text (overrides file)
sv_MOTDFile                               Path to MOTD file
g_gametype               "dm"             Gametype (requires map reload)
g_timelimit              10               Match length in minutes
g_scorelimit             0                Score/frag limit (0=disabled)
g_maplist                                 Map rotation list
g_maprotation            1                0=same, 1=ordered, 2=random
g_instagib               0                Enable instagib (S, L)
g_allow_falldamage       1                Fall damage
g_allow_selfdamage       1                Self damage from weapons
g_allow_teamdamage       1                Friendly fire
g_allow_stun             1                Stun mechanic
g_numbots                0                Number of bots
g_warmup_timelimit       5                Warmup duration in minutes
g_vote_allowed           1                Allow all callvotes
g_vote_percent           55               Percent needed to pass a vote
g_operator_password                       Operator password (empty=disabled)
rcon_password                             RCON password
rcon_address                              RCON target IP
```

---

## Useful Commands

```
bind <key> <command>          Bind a key
unbind <key>                  Unbind a key
bindlist                      List all bindings
alias <name> <command>        Create an alias
toggle <cvar> [val1] [val2]   Toggle cvar between values
exec <file>                   Execute a config file
writeconfig <name>            Save current config to file
connect <ip>                  Connect to server
disconnect                    Disconnect
map <mapname>                 Change map (server)
callvote <vote> [arg]         Call a vote
opcall <vote> [arg]           Operator instant vote
rcon <command>                Remote console command
status                        Server status
players                       List players
kill                          Kill yourself
spec                          Join spectators
join [team]                   Join game
ready / notready              Toggle ready status
say <message>                 Global chat
say_team <message>            Team chat
vsay <name>                   Voice say (run without arg for full list)
cvarlist                      List all cvars
cmdlist                       List all commands
```

---

## Config Locations

| OS | Path |
|---|---|
| Windows | `%USERPROFILE%/My Documents/My Games/Warfork 2.1/basewf/` |
| Mac | `~/Library/Application Support/Warfork-2.1/basewf/` |
| Linux | `~/.local/share/warfork-2.1/basewf/` |

`config.cfg` is loaded on startup. `autoexec.cfg` in the same folder runs after it and takes precedence.
