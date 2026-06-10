---
title: "Console"
game: quake-live
layer: canon
type: reference
tags: [quake-live, console, cvars, commands, reference]
status: canon
promoted: 2026-06-10
source: https://www.euere.eu/ql/
---

Open with `~` (tilde). First time: `Ctrl+Alt+~`, then run `com_allowConsole "1"` so `~` works from that point on. Tab auto-completes. PgUp/PgDn scrolls.

Full source: [euere.eu/ql](https://www.euere.eu/ql/) — 1,079 CVARs, 205 commands. Updated September 2025.

## Config Files

| File | Description |
|------|-------------|
| `repconfig.cfg` | Auto-generated. Key bindings and preferences. Never manually edit |
| `qzconfig.cfg` | Auto-generated. Other settings. Never manually edit |
| `autoexec.cfg` | User-created. Runs on launch. Safe to edit in any plain text editor (not Notepad on Windows) |

**Settings not saving:** run `writeconfig autoexec` in console after making changes.

**Reset all settings:** delete `repconfig.cfg`, `qzconfig.cfg`, and `autoexec.cfg`, then relaunch.

| Platform | Path |
|----------|------|
| Windows | `C:\Users\<user>\AppData\Roaming\id Software\quakelive\home\baseq3\` |
| Linux | `~/.quakelive/quakelive/home/baseq3/` |

## CVAR Flags

| Flag | Name | Description |
|------|------|-------------|
| `[A]` | Archive | Saved to vars.rc |
| `[C]` | Cheat-Protected | Only usable in cheat-enabled servers or localhost |
| `[I]` | Init | Cannot be set from console; command line only |
| `[L]` | Latched | Requires server restart to apply |
| `[R]` | Read-Only | Display only; cannot be set |
| `[S]` | Server Info | Server broadcasts to clients |
| `[U]` | User Info | Client broadcasts to server on connect or change |
| `[T]` | QL Database | Saved to QL database |
| `[W]` | Write-Protected | Cannot be set by user at all |

## CVAR Prefix Reference

| Prefix | Domain |
|--------|--------|
| `BOT_` | Bot settings |
| `CG_` | Client game settings |
| `CL_` | Client-side settings |
| `CM_` | Collision map settings |
| `COM_` | Common settings |
| `FS_` | Game files settings |
| `G_` | Server-side game settings |
| `GT_` | Connection settings |
| `IN_` | General input device settings |
| `JOY_` | Joystick input settings |
| `M_` | Mouse input settings |
| `NET_` | Network settings |
| `PMOVE_` | Player movement server settings |
| `R_` | Video rendering settings |
| `S_` | Sound system settings |
| `SV_` | Server-side settings |
| `SYS_` | System configuration settings |
| `UI_` | User interface settings |
| `WEB_` | Website settings |

## CVARs: A

| CVar | Default | Description |
|------|---------|-------------|
| `activeAction` | - | Executed on client's first active frame; use to script timedemo start after loading |
| `appendlogfile` | 0 | Appends log file writing (0=disabled, 1=enabled) |
| `archss` | OS | Displays OS architecture |
| `armor_tiered` | 0 | Enables QW-inspired tiered armor rules on server |

## CVARs: B — Bots

| CVar | Default | Description |
|------|---------|-------------|
| `bot_enable` [R] | 1 | Enable/disable bots on server/offline match |
| `bot_minplayers` [S] | 0 | Auto-fill disconnected player slots with bots |
| `bot_challenge` | 0 | Makes bots slightly more challenging |
| `bot_dynamicSkill` [A] | 0 | 0=fixed skill, 1=matches "My Skill" setting |
| `bot_startingSkill` [A] | 1 | 1=Easy, 2=Bring It On, 3=Medium, 4=Hardcore, 5=Nightmare |
| `bot_thinktime` [C] | 100 | AI frame interval in ms |
| `bot_gauntlet` [A] | 0 | Force bots to use gauntlet only |
| `bot_gauntletOnly` | 0 | Force bots to chase humans with gauntlet |
| `bot_grapple` | 0 | Allow bots to use grappling hook |
| `bot_rocketjump` | 1 | Allow bots to rocket jump |
| `bot_teamkill` | 0 | When enabled, bots shoot teammates |
| `bot_followMe` [A] | 0 | Make bots follow you in debug mode |
| `bot_followDist` | 250 | Following distance when bot_followMe 1 |
| `bot_training` [A] | 0 | Sets server into training mode |
| `bot_instaGibAimSkill` | 0.4 | Bot aim skill in instagib rails (0.0-1.0) |
| `bot_nochat` | 0 | Disable bot chat |
| `bot_fastchat` | 0 | More frequent bot chat |
| `bot_debug` [C] | 0 | Enable bot debug subsystems |
| `bot_developer` [C] | 0 | Enable bot developer mode |
| `bot_pause` [C] | 0 | Pause bots for debugging |
| `bot_report` [C] | 0 | Bots report their current actions |
| `bot_hud` [C] | -1 | Print bot debug info on HUD (-1=off, 0=freeze, 1=live) |
| `bot_memorydump` [C] | 0 | Display bot memory allocation |
| `bot_aasoptimize` | 0 | Optimize bot intelligence for specific map |
| `bot_forceclustering` | 0 | Force recalculation of AAS clustering |
| `bot_forcereachability` | 0 | Force recalculation of AAS reachabilities |
| `bot_forcewrite` | 0 | Force writing new AAS file |
| `bot_predictobstacles` | 1 | Enable bot obstacle prediction |
| `bot_testsolid` [C] | 0 | Test for solid areas in AAS file |
| `bot_interbreedbots` [C] | 10 | Number of bots for goal fuzzy logic interbreeding |
| `bot_interbreedcycle` [C] | 20 | Matches between interbreeding cycles |
| `bot_interbreedchar` [C] | - | Bot character for interbreeding |
| `bot_interbreedwrite` [C] | - | File to write interbreeded fuzzy logic to |

## CVARs: C

| CVar | Default | Description |
|------|---------|-------------|
| `capturelimit` [S,A] | 8 | Captures needed to win CTF |
| `cg_draw2D` [A] | 1 | 0=no HUD, 1=show HUD |
| `cg_drawFPS` [A] | 0 | FPS counter |
| `cg_drawTimer` [A] | 0 | Match timer |
| `cg_drawSpeed` [A] | 0 | Speed display |
| `cg_drawAmmoWarning` [A] | 1 | Low ammo warning |
| `cg_drawStatus` [A] | 1 | Health/armor HUD |
| `cg_drawTeamOverlay` [A] | 1 | 1=top-right, 2=bottom-right |
| `cg_drawAttacker` [A] | 0 | Show last player to damage you |
| `cg_drawFragMessages` [A] | 1 | Frag messages at top of view |
| `cg_speedometer` [A] | 0 | 1=graph, 2=value+graph, 3=value only |
| `cg_lagometer` [A] | 0 | 1=netgraph, 2=netgraph+ping estimation |
| `cg_fov` [A,T] | 100 | Field of view (10-130) |
| `cg_zoomfov` [A,T] | 22.5 | Zoomed FOV (10-130) |
| `cg_drawCrosshair` [A] | 5 | Crosshair style 0-10 (0=off) |
| `cg_crosshairSize` [A,T] | 32 | Size in pixels |
| `cg_crosshairColor` [A,T] | 7 | Color (1-26) |
| `cg_crosshairBrightness` [A,T] | 1.0 | Brightness (0.0-1.0) |
| `cg_crosshairHealth` [A,T] | 0 | Color crosshair by health |
| `cg_crosshairX` [A,T] | 0 | X offset from center (-300 to 300) |
| `cg_crosshairY` [A,T] | 0 | Y offset from center (-220 to 220) |
| `cg_crosshairPulse` [A,T] | 1 | Pulse on item pickup |
| `cg_crosshairHitStyle` [A,T] | 2 | Hit indicator style (0-8) |
| `cg_crosshairHitColor` [A,T] | 1 | Hit indicator color (1-26) |
| `cg_crosshairHitTime` [A,T] | 200 | Duration of hit effect (ms) |
| `cg_drawCrosshairNames` [A] | 1 | 0=off, 1=names, 2=names+teammate health/armor |
| `cg_drawCrosshairNamesOpacity` [A,T] | 0.75 | Opacity of crosshair names (0.0-1.0) |
| `cg_drawCrosshairTeamHealth` [A,T] | 2 | Show teammate health/armor when targeted |
| `cg_crosshairTeamHealthSize` [A,T] | 0.12f | Font size for teammate health readout |
| `cg_autoswitch` [A] | 1 | Auto-switch to picked-up weapon (0=off recommended) |
| `cg_predictItems` [A] | 1 | Client-side item pickup prediction |
| `cg_simpleItems` [A] | 0 | Simple 2D item icons instead of 3D models |
| `cg_gibs` [A] | 1 | Gib effects |
| `cg_blood` [A] | 1 | Blood effects |
| `cg_brassTime` [A] | 2500 | Bullet casings duration (0=off) |
| `cg_noProjectileTrail` [A] | 0 | Disable projectile trails (1=off) |
| `cg_forceModel` [A] | 0 | Force all players to use your model |
| `cg_enemyModel` [A] | - | Model override for enemies |
| `cg_enemyColors` [A] | - | Hex color for enemies |
| `cg_teamModel` [A] | - | Model override for teammates |
| `cg_teamColors` [A] | - | Hex color for teammates |
| `cg_teamChatsOnly` [A] | 0 | Filter chat to team only |
| `cl_maxpackets` [A] | 30 | Outgoing packet rate (125 recommended) |
| `cl_timenudge` [A] | 0 | Packet timing offset (-1 to -30; negative = earlier) |
| `cl_mouseAccelStyle` [A] | 0 | Acceleration style (0=Quake3, 1=simple) |
| `com_maxfps` [A] | 85 | Max rendered FPS (125 recommended for physics) |
| `com_hunkMegs` [I] | 96 | Memory reserved for gameplay (MB) |
| `com_soundMegs` [I] | 16 | Memory for sounds (MB) |
| `com_allowConsole` | 0 | Allow ~ to open console |

## CVARs: D

| CVar | Default | Description |
|------|---------|-------------|
| `debug_protocol` | - | Network protocol debugging |
| `debuggraph` [C] | 0 | Displays debugging graph |
| `dedicated` [L] | 0 | 0=Listen server, 1=Dedicated server |
| `developer` | 0 | Developer mode |
| `dmflags` [S,A] | 0 | Deathmatch flags: 4=no self splash on HP, 8=no self splash on armor, 16=no fall damage |

## CVARs: F

| CVar | Default | Description |
|------|---------|-------------|
| `fixedtime` [C] | 0 | Enables system wait on rendering |
| `fraglimit` [S,A] | 30 | Frag limit (0=none) |
| `fs_basegame` [I] | - | Default data directory |
| `fs_basepath` [I] | - | Base game root path |
| `fs_cdpath` [I] | - | Alternate hierarchy path |
| `fs_copyfiles` [I] | - | Copies files from fs_cdpath to fs_basepath (dev tool) |
| `fs_debug` | 0 | File system debugging |
| `fs_game` [I] | - | Game directory path |
| `fs_homepath` [I] | - | Write access path; location for custom mods/content |
| `fs_restrict` [I] | - | Demo/restricted mode test tool |

## CVARs: G

| CVar | Default | Description |
|------|---------|-------------|
| `g_gametype` [S,L] | 0 | 0=FFA, 1=Tournament (Duel), 2=Race, 3=TDM, 4=Clan Arena, 5=CTF, 6=One-Flag CTF, 7=Overload, 8=Harvester, 9=Freeze Tag |
| `g_ca` | 0 | Non-functional CA toggle (use g_gametype 4) |
| `g_freeze` | 0 | Non-functional Freeze Tag toggle (use g_gametype 9) |
| `g_domination` | 0 | Domination mode (non-functional) |
| `g_compmode` [S,I] | 0 | Competition mode |
| `g_training` | 0 | Training mode (skill placement match) |
| `g_quadHog` | 0 | Score only while holding Quad |
| `g_allowVote` [A] | 1 | Enable voting |
| `g_allowSpecVote` | 0 | Allow spectators to vote |
| `g_allowStandardVote` | 1 | Allow standard members to vote |
| `g_allowVoteMidGame` | 0 | Allow voting during match |
| `g_voteFlags` [S,A] | 0 | Bitmask of disabled vote commands: &1=map, &2=map_restart, &4=nextmap, &8=gametype, &16=kick, &64=timelimit, &128=fraglimit, &256=shuffle, &512=teamsize, &1024=cointoss, &2048=ruleset |
| `g_voteDelay` | 0 | Min time before voting allowed in warmup |
| `g_voteLimit` | 0 | Max times same vote can be called |
| `g_knockback` | 1000 | General knockback base |
| `g_knockback_lg` | 1.50 | Lightning gun knockback (highest) |
| `g_knockback_gl` | 1.10 | Grenade knockback |
| `g_knockback_pg` | 1.10 | Plasma knockback |
| `g_knockback_pg_self` | 1.30 | Plasma self-splash knockback |
| `g_knockback_rl` | 0.90 | Rocket knockback |
| `g_knockback_rg` | 0.85 | Railgun knockback (lowest) |
| `g_knockback_z` | 24 | Vertical knockback offset (units) |
| `g_max_knockback` | 120 | Maximum knockback cap |
| `g_velocity_pg` | 2000 | Plasma projectile speed (units/sec) |
| `g_velocity_rl` | 1000 | Rocket projectile speed (units/sec) |
| `g_velocity_bfg` | 1800 | BFG projectile speed (units/sec) |
| `g_velocity_gl` | 700 | Grenade projectile speed (units/sec) |
| `g_startingHealth` | 100 | Spawn health |
| `g_startingArmor` | 0 | Spawn armor |
| `g_startingHealthBonus` | 25 | Bonus health on spawn |
| `g_startingammo_mg` | 100 | MG ammo on spawn |
| `g_enableMachinegun` | 1 | Spawn with MG |
| `g_ca_startingHealth` | 200 | Clan Arena spawn health |
| `g_timelimit` [S,A] | 0 | Time limit in minutes (0=none) |
| `g_fraglimit` [S,A] | 30 | Frag limit (0=none) |
| `g_friendlyFire` [S,A] | 0 | Friendly fire |
| `g_allowKill` [A] | 1 | Allow kill command |
| `g_inactivity` | 0 | Kick inactive players after N seconds (0=disabled) |
| `g_warmup` | 20 | Warmup time (seconds) |
| `g_overtime` | 0 | Enable overtime |
| `g_doWarmup` | 0 | Enable warmup period |
| `g_log` | - | Server log filename |
| `g_logSync` | 0 | Synchronous game logging |
| `g_teamForceBalance` | 0 | Force balanced teams |
| `g_teamAutoJoin` | 0 | Auto-assign team on connect |
| `g_redTeam` | Pagans | Red team name |
| `g_blueTeam` | Stroggs | Blue team name |
| `g_quadfactor` | 3 | Quad damage multiplier |
| `g_weaponRespawn` | 5 | Weapon respawn time (seconds) |
| `g_weaponTeamRespawn` | 30 | Team game weapon respawn |
| `g_healthRegenTime` | 0 | Health regen time (CA) |
| `g_armorRegenTime` | 0 | Armor regen time (CA) |
| `g_startingWeapons` | 3 | Starting weapon bitmask: &1=Gauntlet, &2=MG, &4=SG, &8=GL, &16=RL, &32=LG, &64=Rail, &128=PG, &256=BFG, &512=Grapple, &1024=Nailgun, &2048=Prox, &4096=Chaingun, &8192=Map default |

Weapon damage reference (from g_ cvars):

| Weapon | Direct | Splash | Radius |
|--------|--------|--------|--------|
| BFG | 100 | 100 | 80 |
| Chaingun | 8/bullet | - | - |
| Gauntlet | 50 | - | - |
| Grenade Launcher | 100 | 100 | 150 |
| Lightning Gun | 7/tick | - | - |
| Machinegun | 5 (4 TDM) | - | - |
| Nailgun | 12/nail | - | - |
| Plasmagun | 20/cell | 15 | 20 |
| Railgun | 80 | - | - |
| Rocket Launcher | 100 | 84 | 120 |
| Shotgun | 5/pellet (4 TDM) | - | - |
| Prox Mine | 0 | 100 | 150 |

## CVARs: N

| CVar | Default | Description |
|------|---------|-------------|
| `net_noudp` [I] | 0 | Disable UDP networking |
| `net_ip` [I] | - | IP address to bind server to |
| `net_port` [I] | 27960 | Network port |
| `net_socksEnabled` [I] | 0 | Enable SOCKS proxy |
| `nextmap` | - | Map to load after current map ends |

## CVARs: P — Physics

| CVar | Default | Description |
|------|---------|-------------|
| `pmove_fixed` | 0 | Fixed physics timestep (1=required for consistent physics) |
| `pmove_msec` | 8 | Physics timestep in ms (8=125Hz) |
| `pmove_float` | 0 | Floating point movement |
| `pm_bunnyhopping` | 1 | Enable bunny hopping |
| `pm_airstrafejump` | 1 | Enable air-strafing during jumps |
| `pm_maxStepSize` | 18 | Maximum step height |
| `pm_fallheight_damage` | 74 | Fall damage threshold (units/sec) |

## CVARs: R — Rendering

| CVar | Default | Description |
|------|---------|-------------|
| `r_mode` | -2 | Resolution: -2=desktop, -1=custom, 0-27=presets |
| `r_customwidth` | 1600 | Custom width (when r_mode -1) |
| `r_customheight` | 1024 | Custom height (when r_mode -1) |
| `r_fullscreen` | 0 | 0=Windowed, 1=Fullscreen |
| `r_aspectRatio` | 0 | 0=4:3, 1=16:9, 2=16:10, 3=5:4 |
| `r_displayRefresh` | 0 | Monitor refresh rate (Hz) |
| `r_colorbits` | 32 | Color depth (16 or 32) |
| `r_depthbits` | 0 | Z-buffer depth |
| `r_texturebits` | 32 | Texture quality (16 or 32) |
| `r_noFastRestart` | 0 | 0=attempt mode switch without full reload |
| `r_picmip` | 0 | Texture detail: 0=highest, 16=near solid colors; requires vid_restart |
| `r_textureMode` | GL_LINEAR_MIPMAP_LINEAR | Bilinear=GL_LINEAR_MIPMAP_NEAREST, Trilinear=GL_LINEAR_MIPMAP_LINEAR |
| `r_detailtextures` | 1 | Detail texturing |
| `r_roundImagesDown` | 1 | Round images down; boosts performance |
| `r_simpleMipMaps` | 1 | Simple MIP mapping; boosts performance |
| `r_intensity` | 1 | Brightness on textures and model skins |
| `r_fullbright` | 0 | 1=all map textures at full brightness |
| `r_ext_compressed_textures` | 0 | External texture compression |
| `r_gamma` | 1 | Image luminance |
| `r_contrast` | 1.0 | Contrast |
| `r_ambientScale` | 10 | Ambient light among players |
| `r_overBrightBits` | 1 | Ambient lighting on entities (0-4) |
| `r_mapOverBrightBits` | 2 | Ambient lighting on map geometry (0-10) |
| `r_dynamiclight` | 1 | Dynamic lights |
| `r_directedScale` | 1 | Lighting intensity on world objects |
| `r_drawSun` | 0 | Sunlight simulation (0 recommended) |
| `r_flares` | 0 | Projectile flare effects |
| `r_flareSize` | 40 | Size of flares |
| `r_flareFade` | 7 | Fading scale of flares |
| `r_vertexlight` | 0 | 0=light maps, 1=vertex lighting |
| `r_lightmap` | 0 | Light data model |
| `r_teleporterFlash` | 1 | 0=black frame on teleport instead of white flash |
| `r_enablePostProcess` | 1 | Post-processing pipeline (performance hit) |
| `r_enableBloom` | 0 | Bloom (requires r_enablePostProcess 1) |
| `r_enableColorCorrect` | 1 | Color correction (requires r_enablePostProcess 1) |
| `r_BloomBrightThreshold` | 0.125 | Lower=more bloom (0-1) |
| `r_BloomIntensity` | 0.750 | Bloom intensity (0-10) |
| `r_BloomSaturation` | 0.800 | Bloom color saturation (0-10) |
| `r_BloomSceneIntensity` | 1.000 | Non-bloomed world brightness (0-10) |
| `r_BloomPasses` | 1 | Rendering passes for bloom |
| `r_floatingPointFBOs` | 0 | Experimental floating point FBOs; modern GPUs only |
| `r_facePlaneCull` | 1 | Brush face culling; boosts performance |
| `r_lodbias` | 0 | Geometric detail: 0=High, 1=Medium, 2=Low |
| `r_subdivisions` | 4 | Patch subdivisions; 80=angled surfaces for performance |
| `r_fastsky` | 0 | 1=disable sky boxes |
| `r_fastSkyColor` | 0x000000 | Solid sky color when r_fastsky 1 (hex) |
| `r_drawentities` | 1 | Draw world entities |
| `r_maxpolys` | 600 | Max polygons drawn |
| `r_maxpolyverts` | 3000 | Max polygon vertices |
| `r_ext_compiled_vertex_array` | 1 | CVA extension; boosts performance |

## CVARs: S — Sound

| CVar | Default | Description |
|------|---------|-------------|
| `s_volume` [A] | 0.8 | Master volume (0.0-1.0) |
| `s_musicvolume` [A] | 0.25 | Music volume (0=mute) |
| `s_doppler` | 1 | Doppler effect (0=off) |
| `s_khz` [I] | 22 | Sampling rate (11, 22, or 44 kHz) |
| `s_mixahead` | 0.2 | Sound mixing ahead time |
| `s_mixPreStep` | 0.05 | Sound pre-step time |
| `s_show` | 0 | Sound debug info |
| `s_testsound` | 0 | Play test sound |
| `s_separation` | 0.5 | Stereo separation |
| `s_ambient` | 1 | Ambient sounds |

## CVARs: SV — Server

| CVar | Default | Description |
|------|---------|-------------|
| `sv_maxclients` [I] | 8 | Maximum clients |
| `sv_hostname` [S,A] | noname | Server name |
| `sv_fps` | 20 | Server frame rate |
| `sv_timeout` | 200 | Client timeout (seconds) |
| `sv_zombietime` | 2 | Time (minutes) to keep zombie client slots |
| `sv_pure` | 1 | Pure server (clients must match server pk3s) |
| `sv_cheats` [S,I] | 0 | Enable cheat cvars |
| `sv_maxRate` | 0 | Maximum client data rate cap |
| `sv_minPing` [S] | 0 | Minimum client ping filter |
| `sv_maxPing` [S] | 0 | Maximum client ping filter |
| `sv_allowDownload` | 0 | Allow clients to download missing files |
| `sv_floodprotect` | 1 | Flood protection |
| `sv_password` | - | Server password |
| `sv_rconPassword` | - | RCON password |
| `sv_privateClients` | 0 | Reserved player slots |
| `sv_privatePassword` | - | Password for reserved slots |
| `sv_keywords` [S] | - | Keywords for server browser filtering |
| `sv_paknames` [R] | - | List of pk3 files server is running |
| `sv_master1` through `sv_master5` | - | Master server addresses |

## CVARs: T

| CVar | Default | Description |
|------|---------|-------------|
| `timelimit` [S,A] | 0 | Match time limit in minutes |
| `timescale` [C] | 1 | Game speed multiplier (cheat) |

## CVARs: U — UI

| CVar | Default | Description |
|------|---------|-------------|
| `ui_bigFont` | 0.4 | Large font size in UI |
| `ui_smallFont` | 0.25 | Small font size in UI |
| `ui_debug` | 0 | UI debugging mode |
| `ui_menuFiles` | ui/menus.txt | Menu control/content files |
| `ui_serverStatusTimeOut` | 7000 | Server status timeout (ms) |
| `username` | - | Network login ID |
| `ui_gametype` | 3 | Gametype in start server menu |
| `ui_netGametype` | 3 | Network gametype in Create Server menu |
| `ui_dedicated` | 0 | 0=listen server, 1=dedicated server |
| `ui_fragLimit` | 10 | Frag limit for start server menu |
| `ui_captureLimit` | 5 | Capture limit for start server menu |
| `ui_mapIndex` | 0 | Map selection in Create Server menu |
| `ui_redteam` | Pagans | Red team name |
| `ui_blueteam` | Stroggs | Blue team name |
| `ui_enemyColor` | 0 | Enemy model colorization |
| `ui_enemyHeadColor` | 27 | Enemy head color |
| `ui_enemyUpperColor` | 27 | Enemy upper body color |
| `ui_enemyLowerColor` | 27 | Enemy lower body color |
| `ui_forceEnemyModel` | - | Force enemy model |
| `ui_teamHeadColor` | 96 | Teammate head color |
| `ui_teamUpperColor` | 96 | Teammate upper body color |
| `ui_teamLowerColor` | 96 | Teammate lower body color |
| `ui_forceTeamModel` | - | Force team model |
| `ui_ffa_fraglimit` | 20 | FFA frag limit |
| `ui_ffa_timelimit` | 0 | FFA time limit |
| `ui_ctf_capturelimit` | 8 | CTF capture limit |
| `ui_ctf_timelimit` | 30 | CTF time limit |
| `ui_team_fraglimit` | 0 | TDM frag limit |
| `ui_team_timelimit` | 20 | TDM time limit |
| `ui_tourney_fraglimit` | 0 | Tournament frag limit |
| `ui_tourney_timelimit` | 15 | Tournament time limit |
| `ui_bloomPreset` | Default | Bloom preset |
| `ui_screenDamage` | 0 | Screen damage indicator |
| `ui_screenDamage_Team` | 0 | Team screen damage indicator |

## CVARs: V–W

| CVar | Default | Description |
|------|---------|-------------|
| `vid_xpos` | 3 | Window x position on desktop |
| `vid_ypos` | 22 | Window y position on desktop |
| `win_wndproc` [R] | - | Window procedure debug address |

## Color System

Three separate color systems in QL:

| Palette | Use |
|---------|-----|
| 8-color | Text: clan tags and player names (Black unavailable for names) |
| 26-color | Weapons: railgun trail, grenade color |
| Hex | Skins, grenade color, fast sky color |

| 8# | 26# | Name | Hex | R | G | B |
|----|-----|------|-----|---|---|---|
| 1 | 1 | Red | FF0000 | 255 | 0 | 0 |
| | 2 | Orange-Red | FF4000 | 255 | 64 | 0 |
| | 3 | Dark Orange | FF8000 | 255 | 128 | 0 |
| | 4 | Orange | FFC000 | 255 | 192 | 0 |
| 3 | 5 | Yellow | FFFF00 | 255 | 255 | 0 |
| | 6 | Green-Yellow | C0FF00 | 192 | 255 | 0 |
| | 7 | Chartreuse | 80FF00 | 128 | 255 | 0 |
| | 8 | Green 1 | 40FF00 | 64 | 255 | 0 |
| 2 | 9 | Green 2 | 00FF00 | 0 | 255 | 0 |
| | 10 | Spring Green 1 | 00FF40 | 0 | 255 | 64 |
| | 11 | Spring Green 2 | 00FF80 | 0 | 255 | 128 |
| | 12 | Green-Cyan | 00FFC0 | 0 | 255 | 192 |
| 5 | 13 | Cyan | 00FFFF | 0 | 255 | 255 |
| | 14 | Deep Sky Blue | 00C0FF | 0 | 192 | 255 |
| | 15 | Azure | 0080FF | 0 | 128 | 255 |
| | 16 | Cobalt | 0040FF | 0 | 64 | 255 |
| 4 | 17 | Blue | 0000FF | 0 | 0 | 255 |
| | 18 | Electric Ultramarine | 4000FF | 64 | 0 | 255 |
| | 19 | Electric Purple | 8000FF | 128 | 0 | 255 |
| | 20 | Lilac | C000FF | 192 | 0 | 255 |
| 6 | 21 | Magenta 1 | FF00FF | 255 | 0 | 255 |
| | 22 | Magenta 2 | FF00C0 | 255 | 0 | 192 |
| | 23 | Bright Pink | FF0080 | 255 | 0 | 128 |
| | 24 | Folly | FF0040 | 255 | 0 | 64 |
| 7 | 25 | White | FFFFFF | 255 | 255 | 255 |
| | 26 | Medium Grey | 808080 | 128 | 128 | 128 |
| 8/0 | - | Black | 000000 | 0 | 0 | 0 |

## Commands: A–C

| Command | Usage | Description |
|---------|-------|-------------|
| `addbot` | `addbot <name> [skill 1-5] [team] [delay]` | Add a bot |
| `alias` | `alias <name> [command]` | Set a command alias |
| `arena` | `arena <file>.sp_arena` | Load arena from scripts file |
| `bind` | `bind <key> [command]` | Assign action to key |
| `bindlist` | `bindlist` | Show current binds |
| `block` | `block [playername]` | Block player chat |
| `blocklist` | `blocklist` | List blocked players |
| `callvote` | (see below) | Call a vote |
| `centerview` | `centerview` | Snap view to horizontal |
| `clear` | `clear` | Clear console output |
| `clearcvar` | `clearcvar` | Clear a cvar or all cvars |
| `clientkick` | `clientkick <slot>` | Kick client by slot |
| `cmdlist` | `cmdlist <query>` | List commands |
| `condump` | `condump <file>.txt` | Dump console to file |
| `connect` | `connect <ip:port>` | Connect to server |
| `cvar_restart` | `cvar_restart` | Restart CVAR system |
| `cvarlist` | `cvarlist <query>` | List CVARs |

callvote options:
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

## Commands: D–K

| Command | Usage | Description |
|---------|-------|-------------|
| `demo` | `demo <demoname>` | Play a demo |
| `devmap` [C] | `devmap <mapname>` | Open map with cheats |
| `dir` | `dir [dir]/[ext]` | Show files in directory |
| `disconnect` | `disconnect` | Leave server |
| `dropflag` | `dropflag` | Drop flag (CTF) |
| `droppowerup` | `droppowerup` | Drop powerup |
| `dropweapon` | `dropweapon` | Drop current weapon |
| `dumpuser` | `dumpuser <userid>` | Info about a client |
| `echo` | `echo <string>` | Print to console |
| `exec` | `exec <filename>` | Execute .cfg file |
| `fdir` | `fdir <filter>` | Search game directory |
| `find` | `find <substring>` | Search console entries |
| `follow` | `follow <pos/name>` | Follow player in spectator (1=leader, 2=2nd, or name) |
| `forfeit` | `forfeit` | Forfeit the game |
| `gfxinfo` | `gfxinfo` | Graphics settings info |
| `give` [C] | `give [item]` | Give item to player |
| `god` [C] | `god` | Toggle invincibility |
| `imagelist` | `imagelist` | List textures for current map |
| `in_restart` | `in_restart` | Restart input drivers |
| `kick` | `kick <playername>` | Kick a client |
| `kill` | `kill` | Kill yourself (requires g_allowKill 1) |

## Commands: M–Z

| Command | Usage | Description |
|---------|-------|-------------|
| `map` | `map <mapname>` | Load map (server) |
| `map_restart` | `map_restart` | Restart current map |
| `messagemode` | `messagemode` | Open all-chat |
| `messagemode2` | `messagemode2` | Open team chat |
| `music` | `music <filename>` | Play music |
| `nextmap` | `nextmap` | Load next map |
| `noclip` [C] | `noclip` | Toggle noclip |
| `notarget` [C] | `notarget` | Bots ignore you |
| `players` | `players` | List players and IDs |
| `quit` | `quit` | Quit game |
| `rcon` | `rcon <command>` | Send RCON command |
| `record` | `record <demoname>` | Start recording demo |
| `reconnect` | `reconnect` | Reconnect to last server |
| `say` | `say <message>` | Chat to all |
| `say_team` | `say_team <message>` | Chat to team |
| `set` | `set <cvar> <value>` | Set cvar |
| `seta` | `seta <cvar> <value>` | Set and archive cvar |
| `sets` | `sets <cvar> <value>` | Set server info cvar |
| `setu` | `setu <cvar> <value>` | Set userinfo cvar |
| `serverinfo` | `serverinfo` | Server info |
| `status` | `status` | Server status and players |
| `stopdemo` | `stopdemo` | Stop playing demo |
| `stoprecord` | `stoprecord` | Stop recording demo |
| `tell` | `tell <clientnum> <msg>` | Private message |
| `toggle` | `toggle <cvar>` | Toggle boolean cvar |
| `toggleconsole` | `toggleconsole` | Toggle console |
| `unbind` | `unbind <key>` | Remove key binding |
| `unbindall` | `unbindall` | Remove all bindings |
| `unban` | `unban <name>` | Remove from ban list |
| `userinfo` | `userinfo` | Display your userinfo |
| `vid_restart` | `vid_restart` | Restart video system |
| `vstr` | `vstr <variable>` | Execute string variable |
| `vote` | `vote yes/no` | Cast vote |
| `weapon` | `weapon <number>` | Switch to weapon slot |
| `weapnext` | `weapnext` | Next weapon |
| `weapprev` | `weapprev` | Previous weapon |
| `writeconfig` | `writeconfig <file>` | Write settings to file |

## Button Commands

Used with `bind <key> <command>`:

| Command | Description |
|---------|-------------|
| `+attack` | Fire weapon |
| `+button0` | Fire weapon (alternate) |
| `+button2` | Use holdable item |
| `+button3` | Gesture |
| `+chat` | Chat window |
| `+forward` | Move forward |
| `+back` | Move backward |
| `+moveleft` | Strafe left |
| `+moveright` | Strafe right |
| `+moveup` | Jump / swim up |
| `+movedown` | Crouch / swim down |
| `+left` | Turn left |
| `+right` | Turn right |
| `+lookup` | Look up |
| `+lookdown` | Look down |
| `+mlook` | Mouse look |
| `+speed` | Walk toggle |
| `+strafe` | Strafe mode toggle |
| `+zoom` | Zoom |
| `+scores` | Scoreboard |
| `+acc` | Accuracy panel |

## Premium Server Commands

Available on paid/rented servers. Access levels: none = all players, admin = admins, owner = owner only.

| Command | Level | Description |
|---------|-------|-------------|
| `players` | none | List players with IDs and status |
| `timeout` | none | Pause game for 30 seconds |
| `timein` | none | Resume after timeout |
| `abort` | admin | End game, return to warmup |
| `allready` | admin | Force all players ready |
| `kickban` | admin | Remove and ban player (takes ID) |
| `lock` | admin | Stop players joining a team |
| `unlock` | admin | Allow players to join teams |
| `mute` | admin | Block player chat (takes ID) |
| `unmute` | admin | Remove mute (takes ID) |
| `pause` | admin | Pause match indefinitely |
| `unpause` | admin | Resume match |
| `put` | admin | Move player to team: r/b/s (takes ID) |
| `opsay` | admin | Broadcast message to all |
| `op` | owner | Grant admin privileges (takes ID) |
| `deop` | owner | Remove admin privileges (takes ID) |
| `stopserver` | owner | Shut down server immediately |

## Related

- [[games/quake-live/controls|Controls]]
- [[games/quake-live/modding/server-hosting|Server Hosting]]
