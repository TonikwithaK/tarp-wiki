---
title: "Console"
game: warfork
layer: canon
type: reference
tags: [warfork, console, cvars, commands, reference]
status: canon
promoted: 2026-06-10
source: https://warforkwiki.com/index.php?title=Console_Commands
---

Open with `` ` `` (backtick/tilde). Full reference: [warforkwiki.com](https://warforkwiki.com/index.php?title=Console_Commands) (last updated December 2023).

## CVAR Flags

| Flag | Meaning |
|------|---------|
| `*` | Saved to config.cfg |
| `U` | Uploaded to server (player info) |
| `S` | Server info, synced to all clients |
| `-` | Read-only |
| `L` | Requires subsystem restart to apply |
| `C` | Cheat variable, requires `sv_cheats 1` |

Variables can have multiple flags or none. Server-side commands can only be executed via server console or RCON.

## bot

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `bot_dummy` |  | 0 | <0/1> | If enabled, bots will be completely stationary and not fire any weapons. |
| `bot_showcombat` |  | 0 | <0/1> | If enabled, combat messages for bots will be displayed. |
| `bot_showlrgoal` |  | 0 | <0/1> | If enabled, the long range goals for bots will be displayed. |
| `bot_showpath` |  | 0 | <0/1> | If enabled, a path will be drawn that the bot is following. |
| `bot_showsrgoal` |  | 0 | <0/1> | If enabled, the short range goals for bots will be displayed. |

## cg

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `cg_autoaction_demo` | * | 0 | <0/1> | Enables automatic demo recording of matches after warmup mode is finished. |
| `cg_autoaction_screenshot` | * | 0 | <0/1> | Enables automatic screenshot of final standings on the scoreboard when the match is finished. |
| `cg_autoaction_spectator` | * | 0 | <0/1> | Use autoaction when spectating games. |
| `cg_autoaction_stats` | * | 0 | <0/1> | If enabled, your statistics will be written to /stats/gametype/ in your data folder when the match is finished in following file format: gametype_yyyy-mm-dd-hh-mm_map_playername_id.txt |
| `cg_bloodTrail` | * | 10 | <value> | Changes the density of damage rings rendered when a player is hit. |
| `cg_bloodTrailAlpha` | * | 1.0 | <0-1> | Sets the transparency of damage rings rendered. |
| `cg_cartoonEffects` | * | 7 | <2/4/7> | Enables cartoon effects. |
| `cg_cartoonHitEffect` | * | 0 | <0/1> | If enabled, critical hit effects are displayed for high damage value attacks. |
| `cg_chatBeep` | * | 1 | <0/1> | Enables the chat beep sound when someone sends a message. |
| `cg_chatFilter` | * | 0 | <0-2> | Filters chat messages. |
| `cg_chatFilterTV` | * | 2 | <0-4> | Filters Warfork TV chat messages. |
| `cg_clientHUD` | * |  | <HUD name> | Changes your HUD. |
| `cg_colorCorrection` | * | 1 | <0/1> | Enables color correction. |
| `cg_crosshair` | * | 1 | <0-13> | Changes your crosshair style. |
| `cg_crosshair_color` | * | 255 255 255 | <R G B> | Changes the color of your crosshair. |
| `cg_crosshair_damage_color` | * | 255 0 0 | <R G B> | Changes the color of your crosshair when you hit an enemy. |
| `cg_crosshair_font` | * | Warsow Crosshairs |  | Changes the font of your crosshair. |
| `cg_crosshair_size` | * | 24 | <size> | Changes the size of your crosshair. |
| `cg_crosshair_strong` | * | 0 | <0-13> | Changes your crosshair style for strong ammo. 0 disables it. |
| `cg_crosshair_strong_color` | * | 255 255 255 | <R G B> | Changes the color of your crosshair for strong ammo. |
| `cg_crosshair_strong_size` | * | 24 | <size> | Changes the size of your crosshair for strong ammo. |
| `cg_damage_blend` |  | 1 | <0-1> | This command no longer works and is a placeholder. |
| `cg_damage_indicator` | * | 1 | <0-1> | If enabled, a red damage indicator will appear in the direction(s) you were hit. |
| `cg_damage_indicator_time` | * | 25 | <value> | Sets how long the red damage indicator will be visible. |
| `cg_damageNumbers` | * | 1 | <0/1> | Enables Damage Numbers that are displayed when attacking a player. |
| `cg_damageNumbersColor` | * | 8 | <0-11> | Changes the color of your Damage Numbers. |
| `cg_damageNumbersDistance` | * | 48 | <1-200> | The vertical distance above the player model that Damage Numbers are displayed. |
| `cg_damageNumbersOffset` | * | 1 | <1-5> | The offset distance between the Damage Number and its shadow. |
| `cg_damageNumbersSize` | * | 1 | <1-4> | Changes the size of your Damage Numbers. |
| `cg_debugHUD` |  | 0 | <0/1> | If enabled, the HUD name that's being loaded will print to console. |
| `cg_debugPlayerModels` | *,C | 0 | <0/1> | If enabled, player model information will be displayed on each map load in console. |
| `cg_debugWeaponModels` | *,C | 0 | <0/1> | If enabled, weapon model information will be displayed on each map load in console. |
| `cg_decals` | * | 1 | <0/1> | If enabled, you will see projectile impact effects on walls. |
| `cg_draw2D` |  | 1 | <0/1> | If enabled, you will see the HUD (scores, ammunition, clock, etc.) |
| `cg_ebbeam_alpha` | * | 0.4 | <0-1> | Sets the transparency of the Electrobolt Beam. 0 = 100% Transparent & 1 = 100% Solid |
| `cg_ebbeam_old` | * | 0 | <0/1> | If enabled, you will see the old (simplistic) Electrobolt beam. |
| `cg_ebbeam_time` | * | 0.6 | <value> | Sets how long the Elecrobolt beam will be visible. |
| `cg_ebbeam_width` | * | 64 | <value> | Sets the width of the Elecrobolt beam. |
| `cg_explosionsDust` | * | 0 | <0/1> | If enabled, an explosion dust will appear around Grenade Launcher and Rocket Launcher projectiles upon impact. |
| `cg_explosionsRing` | * | 0 | <0/1> | If enabled, an explosion ring will appear around Grenade Launcher and Rocket Launcher projectiles upon impact. |
| `cg_flashWindowCount` | * | 4 | <value> | The amount of times Warfork flashes in your taskbar if warmup ends and a match starts. |
| `cg_forceMyTeamAlpha` | * | 0 | <0/1> | If enabled, your HUD, teammates and enemies will appear as if you always were in the Alpha team. |
| `cg_gamepad_accelMax` | * | 2 | <value> | Maximum acceleration of the gamepad. |
| `cg_gamepad_accelSpeed` | * | 3 | <value> | Speed of gamepad's acceleration. |
| `cg_gamepad_accelThres` | * | 0.9 | <value> | Threshold of gamepad's acceleration. |
| `cg_gamepad_moveThres` | * | 0.239 | <value> | Specifies the dead-zone for movement. |
| `cg_gamepad_pitchInvert` | * | 0 | <0/1> | If enabled, the gamepad will be inverted. |
| `cg_gamepad_pitchSpeed` | * | 240 | <value> | Specifies the sensitivity when looking up and down. |
| `cg_gamepad_pitchThres` | * | 0.265 | <value> | Specifies the dead-zone for looking up and down. |
| `cg_gamepad_runThres` | * | 0.75 |  |  |
| `cg_gamepad_strafeRunThres` | * | 0.45 |  |  |
| `cg_gamepad_strafeThres` | * | 0.239 |  |  |
| `cg_gamepad_swapSticks` | * | 0 | <0/1> | Swaps sticks on your gamepad. |
| `cg_gamepad_yawSpeed` | * | 260 | <value> | Specifies the sensitivity when looking left and right. |
| `cg_gamepad_yawThres` | * | 0.265 | <value> | Specifies the dead-zone for looking left and right. |
| `cg_gibs` | * | 1 | <0/1> | This command is a placeholder. |
| `cg_gun` | * | 1 | <0/1> | Shows your weapon. |
| `cg_gun_alpha` | * | 1 | <0-1> | Transparency of your weapon model. |
| `cg_gun_fov` | * | 90 | <1-160> | Field-of-View of your weapon model. |
| `cg_gunbob` | * | 1 | <0/1> | Enables bobbing of the weapon model. |
| `cg_gunx` | * | 0 | <value> | Moves your weapon's model on the X axis. |
| `cg_guny` | * | 0 | <value> | Moves your weapon's model on the Y axis. |
| `cg_gunz` | * | 0 | <value> | Moves your weapon's model on the Z axis. |
| `cg_handOffset` | * | 5 | <value> | The offset of your hand's position. 0 means middle. |
| `cg_instabeam_alpha` | * | 0.4 | <0-1> | Transparency of the instabeam. |
| `cg_instabeam_time` | * | 0.4 | <value> | The time an instagun beam will be displayed before disappearing. |
| `cg_instabeam_width` | * | 7 | <value> | The width of an instagun beam. |
| `cg_laserBeamSubdivisions` | * | 10 | <value> | The higher the number the smoother the laser beam looks. |
| `cg_movementStyle` | *,U | 0 | <0/1> | Old movement = 0 and New movement = 1 |
| `cg_noAutoHop` | *,U | 0 | <0/1> | If enabled, disables autohop by holding spacebar. |
| `cg_outlineModels` | * | 1 | <0/1> | Outlines models. |
| `cg_outlinePlayers` | * | 1 | <0/1> | Outlines players. |
| `cg_outlineWorld` | * | 0 | <0/1> | Outlines every object in maps. |
| `cg_particles` | * | 1 | <0/1> | Enables particles. |
| `cg_pickup_flash` | * | 0 | <0/1> | If enabled, you will see a flash when picking up an item or weapon. |
| `cg_placebo` | * | 0 | <value> | An easteregg for comedic purpose that does nothing. It will be removed shortly. |
| `cg_playerTrailsColor` |  | 0.0 1.0 0.0 | <R G B> | This command has already been removed from the game and only exists in default.cfg. The next update will purge the remnants. |
| `cg_playList` | * | sounds/music/match.m3u | <path> | Path to a music playlist. |
| `cg_playListShuffle` | * | 1 | <0/1> | Plays songs randomly from the music playlist. |
| `cg_predict` |  | 1 | <0/1> | Predicts players' movement on multiplayer servers for smoothness. |
| `cg_predict_optimize` |  | 1 | <0/1> | Optimizes cg_predict's behavior. |
| `cg_predictLaserBeam` | * | 1 | <0/1> | If enabled, a perfectly straight line laserbeam will always be drawn regardless of server lag. If disabled, a laserbeam will be drawn based on server lag. |
| `cg_projectileAntilagOffset` | * | 1.0 | <value> | The defined value adds a time offset to counter anti-lag visualization. |
| `cg_projectileFireTrail` | * | 90 | <value> | Controls the amount of firetrail left behind when firing the Rocket Launcher or Grenade Launcher. |
| `cg_projectileFireTrailAlpha` | * | 0.45 | <0-1> | Controls the transparency level of the firetrail left behind when firing the Rocket Launcher or Grenade Launcher. |
| `cg_projectileTrail` | * | 60 | <value> | Controls the amount of smoke left behind when firing the Rocket Launcher or Grenade Launcher. |
| `cg_raceGhosts` | * | 0 | <0/1> | Enables ghosts while racing. |
| `cg_raceGhostsAlpha` | * | 0.25 | <0-1> | Transparency of race ghosts. |
| `cg_reactionKills` | * | 1 | <0/1> | Enables Reaction Kills. |
| `cg_reactionKillsTimeout` | * | 45 | <1-180> | Frequency of Reaction Kills in seconds. |
| `cg_reactionRoundStart` | * | 1 | <0/1> | Enables Round Start Reactions. |
| `cg_reactionRoundStartOdds` | * | 5 | <1-100> | Odds of Round Start Reactions. |
| `cg_scoreboardFontFamily` | * | Droid Sans Mono |  | Name of font used in scoreboard. |
| `cg_scoreboardFontSize` | * | 12 | <value> | Size of scoreboard's font. |
| `cg_scoreboardMonoFontFamily` | * | Droid Sand Mono |  |  |
| `cg_scoreboardStats` | * | 1 | <0-1> | If enabled, Weapons Statistics will be shown on the Scoreboard. |
| `cg_scoreboardTitleFontFamily` | * | Hemi Head |  | Name of font used in the scoreboard's title. |
| `cg_scoreboardTitleFontSize` | * | 24 | <value> | Size of the font used in scoreboard's title. |
| `cg_scoreboardWidthScale` | * | 1.0 | <value> | Width scale of the scoreboard. |
| `cg_shadows` | * | 1 | <0-2> | Enables shadows. Uses simple shadows if set to 1, shadowmaps if set to 2. 0 to disable. |
| `cg_showAwards` | * | 1 | <0/1> | Shows awards upon certain events (On Fire! etc.). |
| `cg_showBloodTrail` | * | 1 | <0/1> | If enabled, damage rings will be rendered when a player is hit. |
| `cg_showCaptureAreas` | * | 1 | <0/1> | A command that does nothing. It will be removed shortly. |
| `cg_showChasers` | * | 1 | <0/1> | Displays chasers on the scoreboard (if there are any). |
| `cg_showCrosshairDamage` | * | 1 | <0/1> | Changes the crosshair's color to the damage color if an enemy gets hit. |
| `cg_showFPS` | * | 0 | <0/1> | Enables an FPS counter. |
| `cg_showhelp` | * | 1 | <0/1> | Displays help text under the timer. |
| `cg_showHUD` | * | 1 | <0/1> | Enables HUD. |
| `cg_showItemTimers` | * | 3 | <value> | Displays when items will spawn on your HUD (only in spectator mode). |
| `cg_showMiniMap` | * | 0 | <0/1> | Displays a minimap (if supported by gamemode). |
| `cg_showMiss` |  | 0 | <0/1> | For debugging server events. If enabled, will dump prediction misses to console in x:y format. x = time y = distance error. |
| `cg_showObituaries` | * | 3 | <value> | Displays who fragged who using which weapon on your HUD. |
| `cg_showPickup` | * | 1 | <0/1> | Displays when you pickup an item on your HUD. |
| `cg_showPlayerNames` | * | 1 | <0/1> | Displays player names above player models. |
| `cg_showPlayerNames_alpha` | * | 0.4 | <0-1> | Transparency of player names. |
| `cg_showPlayerNames_barWidth` | * | 8 | <value> | Bar width above your teammates player model, which contains information such as Health and Armor. |
| `cg_showPlayerNames_xoffset` |  | 0 | <value> | Move player names by this much on the X axis. |
| `cg_showPlayerNames_yoffset` |  | 16 | <value> | Move player names by this much on the Y axis. |
| `cg_showPlayerNames_zfar` | * | 824 | <value> | Defines the distance that player names are still drawn over models. |
| `cg_showPlayerTrails` |  | 0 | <0/1> | This command has already been removed from the game and only exists in default.cfg. The next update will purge the remnants. |
| `cg_showPointedPlayer` | * | 1 | <0/1> | If enabled, when your mouse is pointed over a teammate or enemy their name will be drawn over the player model. |
| `cg_showPressedKeys` | * | 0 | <0/1> | If enabled, will show the key presses of players. |
| `cg_showSelfShadow` | * | 0 | <0/1> | Enables seeing your own shadow. |
| `cg_showSpeed` | * | 1 | <0-3> | Changes the position of the speed display of the player. 0 to disable. Values higher than 1 aren't supported on all HUDs. |
| `cg_showTeamLocations` | * | 1 | <0/1> | If enabled and your HUD supports it, your teammates location will be shown. |
| `cg_showTeamMates` | * | 1 | <0/1> | Show teammates indicators. |
| `cg_showTimer` | * | 1 | <0/1> | Displays the match's timer. |
| `cg_showViewBlends` | * | 1 | <0/1> | If enabled, fullscreen overlays for underwater and pain effects will be displayed. |
| `cg_showZoomEffect` | * | 1 | <0/1> | If enabled, the zoom effect is shown. |
| `cg_simpleItems` | * | 0 | <0-2> | Replaces 3D models of pickupable items with simplistic 2D models. |
| `cg_simpleItemsSize` | * | 16 | <value> | Changes the size of simplistic item models. |
| `cg_specHUD` | * | <undefined> | <HUD name> | Changes the HUD while spectating. |
| `cg_strafeHUD` | * | 0 | <0/1> | Enables strafe HUD. |
| `cg_teamALPHAcolor` | * | 254 101 101 | <R G B> | Color of team Alpha players. |
| `cg_teamALPHAmodel` | * | bigvic | <model name> | Default model of team Alpha players. |
| `cg_teamALPHAmodelForce` | * | 1 | <0/1> | Changes models of all team Alpha players to a user-chosen one. |
| `cg_teamALPHAskin` | * | default | <default/fullbright> | Changes models skin of all Team Forbidden players to a user-chosen one. |
| `cg_teamBETAcolor` | * | 153 204 255 | <R G B> | Color of team Beta players. |
| `cg_teamBETAmodel` | * | padpork | <model name> | Default model of team Beta players. |
| `cg_teamBETAmodelForce` | * | 1 | <0/1> | Changes models of all team Beta players to a user-chosen one. |
| `cg_teamBETAskin` | * | default | <default/fullbright> | Changes models skin of all Team Icy players to a user-chosen one. |
| `cg_teamColoredBeams` | * | 0 | <0/1> | If enabled, the LG beam color will be changed to the team color of the attacker. |
| `cg_teamColoredInstaBeams` | * | 1 | <0/1> | Changes the color of the InstaBeam to the team color of the attacker. |
| `cg_teamPLAYERScolor` | * | 0 255 70 | <R G B> | Color of team Players players (non-team based gametypes). |
| `cg_teamPLAYERScolorForce` | * | 0 | <0/1> | Changes color of all team Players players to a user-chosen one. |
| `cg_teamPLAYERSmodel` | * | bigvic | <model name> | Default model of team Players players. |
| `cg_teamPLAYERSmodelForce` | * | 0 | <0/1> | Changes models of all team Players players to a user-chosen one. |
| `cg_teamPLAYERSskin` | * | default | <default/fullbright> | Changes models skin of all team Players players to a user-chosen one. |
| `cg_thirdPerson` | C | 0 | <0/1> | Enables third person view. |
| `cg_thirdPersonAngle` |  | 0 | <value> | Changes the angle of third person view. |
| `cg_thirdPersonRange` |  | 70 | <value> | The distance that the player model appears from the camera when in third person view. |
| `cg_touch_flip` | * | 0 |  |  |
| `cg_touch_lookDecel` | * | 8.5 |  |  |
| `cg_touch_lookInvert` | * | 0 |  |  |
| `cg_touch_lookSens` | * | 9 |  |  |
| `cg_touch_lookThres` | * | 5 |  |  |
| `cg_touch_moveThres` | * | 24 |  |  |
| `cg_touch_scale` | * | 100 |  |  |
| `cg_touch_showMoveDir` | * | 1 |  |  |
| `cg_touch_strafeThres` | * | 32 |  |  |
| `cg_touch_zoomThres` | * | 24 |  |  |
| `cg_touch_zoomTime` | * | 250 |  |  |
| `cg_viewBob` | * | 1 | <0/1> | Enabled head bobbing. |
| `cg_viewSize` | * | 100 | <40-100> | The percentage of the viewable area displayed on your screen. |
| `cg_voiceChats` | * | 1 | <0/1> | Enables voice commands (also known as "VSAYS"). |
| `cg_volume_announcer` | * | 1.0 | <0-2.0> | Changes the volume of the announcer. |
| `cg_volume_effects` | * | 1.0 | <0-2.0> | Changes the volume of the effects. |
| `cg_volume_hitsound` | * | 1.0 | <0-2.0> | Changes the volume of the hitsound. |
| `cg_volume_players` | * | 1.0 | <0-2.0> | Changes the volume of player sounds. |
| `cg_volume_voicechats` | * | 1.0 | <0.0-2.0> | Changes the volume of voice commands. |
| `cg_weaponAutoswitch` | * | 2 | <0-2> | Enables auto switching of weapons when you're out of ammo. |
| `cg_weaponFlashes` | * | 2 | <0-2> | Enables weapon flashes. |
| `cg_weaponlist` | * | 1 | <0/1> | If enabled, the weapon list will be displayed on your HUD. |

## cl

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `cl_anglespeedkey` |  | 1.5 | <value> | Defines the multiplier for how fast you turn when running is toggled. |
| `cl_checkForUpdate` | * | 1 | <0/1> | If enabled, the client will be permitted to check for updates. |
| `cl_compresspackets` | * | 1 | <0/1> | Compresses network packets. |
| `cl_debug_serverCmd` | *,C | 0 | <0/1> | If enabled, server debug information will printed to console. |
| `cl_debug_timeDelta` | * | 0 | <0/1> | If enabled, server debug information (netcode) will printed to console. |
| `cl_demoavi_audio` | * | 0 |  | If set to 1 Warfork will create a .wav when using demoavi cl_demoavi_video should be set to 0 since it will lag the game when capturing resulting in audio that is not realtime. |
| `cl_demoavi_fps` | * | 30.3 |  | Determines how many frames per second get captured by demoavi |
| `cl_demoavi_scissor` | * | 0 |  |  |
| `cl_demoavi_video` | * | 1 | <0/1> | If set to 1 Warfork will output frames when using demoavi |
| `cl_download_allow_modules` | * | 1 | <0/1> | Allows the downlaoding of modules. |
| `cl_download_name` |  | <value> | *write protected* | The name of what's being downloaded. |
| `cl_download_percent` |  | 0 | *write protected* | The percentage of what's being downloaded. |
| `cl_downloads` | * | 1 | <0/1> | If enabled, your client is allowed to download files (maps, textures, etc.) directly from the server you're connecting to. |
| `cl_downloads_from_web` | *,- | 1 | *write protected* | If enabled, your client is allowed to download files (maps, textures, etc.) from a webserver. |
| `cl_downloads_from_web_timeout` | * | 600 | <value> | The time before a client timeout when attempting to download from a webserver. |
| `cl_extrapolate` | * | 1 |  |  |
| `cl_flip` | * | 0 |  |  |
| `cl_maxfps` | * | 250 | <24-1000> | Sets the FPS limit. |
| `cl_mm_autologin` | * | 1 | <0/1> | If enabled, matchmaking will automatically be logged into. |
| `cl_mm_session` | U,- | 0 | *write protected* | Contains your matchmaking session information. |
| `cl_mm_user` | * | <undefined> | <value> | Contains your matchmaking username. |
| `cl_mumble` | *,L | 0 | <0/1> | Enables positional audio support for Mumble |
| `cl_mumble_scale` | * | 0.0254 | <value> | Scales the positional audio distance for Mumble. |
| `cl_pitchspeed` |  | 150 | <value> | The speed the player's screen moves up and down when using keyboard keys. |
| `cl_port` |  | 0 | *write protected* | IPv4 client port |
| `cl_port6` |  | 0 | *write protected* | IPv6 client port |
| `cl_pps` | * | 40 | <value> | The amount packets per second that client is sending to the server. |
| `cl_run` | * | 1 | <0/1> | If enabled, running will be toggle automatically. |
| `cl_shownet` |  | 0 | <0/1> | If enabled, latency information for network packets will be printed in console. |
| `cl_sleep` | * | 0 | <0/1> | If enabled, you will get lower CPU usage with the cost of higher mouse latency and less stable fps. |
| `cl_stereo` | * | 0 | <0/1> | If enabled, stereoscopic rendering mode will be toggled. |
| `cl_stereo_separation` | * | 0.4 | <0-1.0> | Camera offset with cl_stereo |
| `cl_timeout` |  | 120 | <value> | Kicks the player if connection is lost for more than x seconds. |
| `cl_ucmdMaxResend` | * | 3 |  |  |
| `cl_yawspeed` |  | 140 |  |  |

## cm

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `cm_mapHeader` |  | <undefined> | <value> | Stores map header information in the cvar. |
| `cm_mapVersion` |  | <undefined> | <value> | Stores map format description (IBSP, FBSP, etc.) in the cvar. |
| `cm_noAreas` | C | 0 | <0/1> | Disables area culling. |
| `cm_noCurves` | C | 0 | <0/1> | If enabled, you can clip through curved surfaces. |

## com

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `com_introPlayed3` | * | 1 |  |  |
| `com_showtrace` |  | 0 | <0/1> | If enabled, the number of traces that has to be made will be displayed in console. |

## con

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `con_chatmode` | * | 3 |  |  |
| `con_drawNotify` | * | 0 |  |  |
| `con_fontSystemBigSize` | * | 24 | <value> |  |
| `con_fontSystemConsoleSize` | * | 14 | <value> |  |
| `con_fontSystemFallbackFamily` | *,L | Droid Sans Fallback |  |  |
| `con_fontSystemFamily` | * | Droid Sans |  |  |
| `con_fontSystemMediumSize` | * | 16 | <value> |  |
| `con_fontSystemMonoFamily` | * | Droid Sans Mono |  |  |
| `con_fontSystemSmallSize` | * | 14 | <value> |  |
| `con_fontSystemTinySize` | * | 8 | <value> |  |
| `con_messageMode` |  | 0 |  |  |
| `con_notifytime` | * | 3 |  |  |
| `con_printText` | * | 1 |  |  |

## fs

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `fs_basegame` |  | basewf | *write protected* |  |
| `fs_basepath` |  | . | *write protected* |  |
| `fs_cdpath` |  |  | *write protected* |  |
| `fs_game` | S,L | basewf |  |  |
| `fs_usedownloadsdir` |  | 1 | *write protected* |  |
| `fs_usehomedir` |  | 1 | *write protected* |  |

## g

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `g_allow_bunny` | *,- | 1 | *write protected* |  |
| `g_allow_falldamage` | * | 1 | <0/1> | Enables fall damage. |
| `g_allow_selfdamage` | * | 1 | <0/1> | If enabled, players can hurt themselves with own weapons. |
| `g_allow_spectator_voting` | * | 1 | <0/1> | Allows spectators to vote. Affects callvotes. |
| `g_allow_stun` | * | 1 | <0/1> | If enabled, players can get stunned. |
| `g_allow_teamdamage` | * | 1 | <0/1> | Enables friendlyfire. |
| `g_ammo_respawn` | * | 0 | <value> | Changes the ammo respawn time. |
| `g_antilag` | *,S,L | 1 | <0/1> | Enables antilag. |
| `g_antilag_maxtimedelta` | * | 200 | <value> |  |
| `g_antilag_timenudge` | * | 0 |  |  |
| `g_asGC_interval` | * | 10 |  |  |
| `g_asGC_stats` | * | 0 |  |  |
| `g_autorecord` | * | 0 | <0/1> | Automatically records all demos. |
| `g_autorecord_maxdemos` | * | 0 | <value> | Maximum amount of automatically recorded demos to keep (deletes old ones once limit is exceeded). |
| `g_bomb_armtime` | * | 4 | <value> | (Bomb-exclusive) Changes the amount of time needed to arm a bomb.. |
| `g_bomb_bombtimer` | * | 25 | <value> | (Bomb-exclusive) Time before the bomb explodes after arming. |
| `g_bomb_carriers` | * | 1 | <value> | (Bomb-exclusive) |
| `g_bomb_defusetime` | * | 7 | <value> | (Bomb-exclusive) Changes the amount of time needed to defuse an armed bomb. |
| `g_bomb_roundtime` | * | 60 | <value> | (Bomb-exclusive) Sets the round time (in seconds). |
| `g_bomb_spawnprotection` | * | 3 | <value> | (Bomb-exclusive) |
| `g_challengers_queue` |  | 1 | <0/1> | Enables the challengers queue. |
| `g_countdown_time` | * | 5 | <value> |  |
| `g_disable_opcall_allow_falldamage` | * | 0 | <0/1> | Disables "allow_falldamage" opcall. |
| `g_disable_opcall_allow_selfdamage` | * | 0 | <0/1> | Disables "allow_selfdamage" opcall. |
| `g_disable_opcall_allow_teamdamage` | * | 0 | <0/1> | Disables "allow_teamdamage" opcall. |
| `g_disable_opcall_allow_uneven` | * | 0 | <0/1> | Disables "allow_uneven" opcall. |
| `g_disable_opcall_allready` | * | 0 | <0/1> | Disables "allready" opcall. |
| `g_disable_opcall_extended_time` | * | 0 | <0/1> | Disables "extended_time" opcall. |
| `g_disable_opcall_gametype` | * | 0 | <0/1> | Disables "gametype" opcall. |
| `g_disable_opcall_instajump` | * | 0 | <0/1> | Disables "instajump" opcall. |
| `g_disable_opcall_instashield` | * | 0 | <0/1> | Disables "instashield" opcall. |
| `g_disable_opcall_kick` | * | 0 | <0/1> | Disables "kick" opcall. |
| `g_disable_opcall_kickban` | * | 0 | <0/1> | Disables "kickban" opcall. |
| `g_disable_opcall_lock` | * | 0 | <0/1> | Disables "lock" opcall. |
| `g_disable_opcall_map` | * | 0 | <0/1> | Disables "map" opcall. |
| `g_disable_opcall_maxteamplayers` | * | 0 | <0/1> | Disables "maxteamplayers" opcall. |
| `g_disable_opcall_mute` | * | 0 | <0/1> | Disables "mute" opcall. |
| `g_disable_opcall_nextmap` | * | 0 | <0/1> | Disables "nextmap" opcall. |
| `g_disable_opcall_numbots` | * | 0 | <0/1> | Disables "numbots" opcall. |
| `g_disable_opcall_rebalance` | * | 0 | <0/1> | Disables "rebalance" opcall. |
| `g_disable_opcall_remove` | * | 0 | <0/1> | Disables "remove" opcall. |
| `g_disable_opcall_restart` | * | 0 | <0/1> | Disables "restart" opcall. |
| `g_disable_opcall_scorelimit` | * | 0 | <0/1> | Disables "scorelimit" opcall. |
| `g_disable_opcall_shuffle` | * | 0 | <0/1> | Disables "shuffle" opcall. |
| `g_disable_opcall_timein` | * | 0 | <0/1> | Disables "timein" opcall. |
| `g_disable_opcall_timelimit` | * | 0 | <0/1> | Disables "timelimit" opcall. |
| `g_disable_opcall_timeout` | * | 0 | <0/1> | Disables "timeout" opcall. |
| `g_disable_opcall_unlock` | * | 0 | <0/1> | Disables "unlock" opcall. |
| `g_disable_opcall_unmute` | * | 0 | <0/1> | Disables "unmute" opcall. |
| `g_disable_opcall_vmute` | * | 0 | <0/1> | Disables "vmute" opcall. |
| `g_disable_opcall_vunmute` | * | 0 | <0/1> | Disables "vunmute" opcall. |
| `g_disable_opcall_warmup_timelimit` | * | 0 | <0/1> | Disables "warmup_timelimit" opcall. |
| `g_disable_vote_allow_falldamage` | * | 0 | <0/1> | Disables "allow_falldamage" callvote. Doesn't affect opcalls. |
| `g_disable_vote_allow_selfdamage` | * | 0 | <0/1> | Disables "allow_selfdamage" callvote. Doesn't affect opcalls. |
| `g_disable_vote_allow_teamdamage` | * | 0 | <0/1> | Disables "allow_teamdamage" callvote. Doesn't affect opcalls. |
| `g_disable_vote_allow_uneven` | * | 0 | <0/1> | Disables "allow_uneven" callvote. Doesn't affect opcalls. |
| `g_disable_vote_allready` | * | 0 | <0/1> | Disables "allready" callvote. Doesn't affect opcalls. |
| `g_disable_vote_extended_time` | * | 0 | <0/1> | Disables "extended_time" callvote. Doesn't affect opcalls. |
| `g_disable_vote_gametype` | * | 0 | <0/1> | Disables "gametype" callvote. Doesn't affect opcalls. |
| `g_disable_vote_instajump` | * | 0 | <0/1> | Disables "instajump" callvote. Doesn't affect opcalls. |
| `g_disable_vote_instashield` | * | 0 | <0/1> | Disables "instashield" callvote. Doesn't affect opcalls. |
| `g_disable_vote_kick` | * | 0 | <0/1> | Disables "kick" callvote. Doesn't affect opcalls. |
| `g_disable_vote_kickban` | * | 0 | <0/1> | Disables "kickban" callvote. Doesn't affect opcalls. |
| `g_disable_vote_lock` | * | 0 | <0/1> | Disables "lock" callvote. Doesn't affect opcalls. |
| `g_disable_vote_map` | * | 0 | <0/1> | Disables "map" callvote. Doesn't affect opcalls. |
| `g_disable_vote_maxteamplayers` | * | 0 | <0/1> | Disables "maxteamplayers" callvote. Doesn't affect opcalls. |
| `g_disable_vote_mute` | * | 0 | <0/1> | Disables "mute" callvote. Doesn't affect opcalls. |
| `g_disable_vote_nextmap` | * | 0 | <0/1> | Disables "nextmap" callvote. Doesn't affect opcalls. |
| `g_disable_vote_numbots` | * | 0 | <0/1> | Disables "numbots" callvote. Doesn't affect opcalls. |
| `g_disable_vote_rebalance` | * | 0 | <0/1> | Disables "rebalance" callvote. Doesn't affect opcalls. |
| `g_disable_vote_remove` | * | 0 | <0/1> | Disables "remove" callvote. Doesn't affect opcalls. |
| `g_disable_vote_restart` | * | 0 | <0/1> | Disables "restart" callvote. Doesn't affect opcalls. |
| `g_disable_vote_scorelimit` | * | 0 | <0/1> | Disables "scorelimit" callvote. Doesn't affect opcalls. |
| `g_disable_vote_shuffle` | * | 0 | <0/1> | Disables "shuffle" callvote. Doesn't affect opcalls. |
| `g_disable_vote_timein` | * | 0 | <0/1> | Disables "timein" callvote. Doesn't affect opcalls. |
| `g_disable_vote_timelimit` | * | 0 | <0/1> | Disables "timelimit" callvote. Doesn't affect opcalls. |
| `g_disable_vote_timeout` | * | 0 | <0/1> | Disables "timeout" callvote. Doesn't affect opcalls. |
| `g_disable_vote_unlock` | * | 0 | <0/1> | Disables "unlock" callvote. Doesn't affect opcalls. |
| `g_disable_vote_unmute` | * | 0 | <0/1> | Disables "unmute" callvote. Doesn't affect opcalls. |
| `g_disable_vote_vmute` | * | 0 | <0/1> | Disables "vmute" callvote. Doesn't affect opcalls. |
| `g_disable_vote_vunmute` | * | 0 | <0/1> | Disables "vunmute" callvote. Doesn't affect opcalls. |
| `g_disable_vote_warmup_timelimit` | * | 0 | <0/1> | Disables "warmup_timelimit" callvote. Doesn't affect opcalls. |
| `g_enforce_map_pool` | * | 0 | <0/1> | Enables enforcing the map pool for "map" callvote. |
| `g_floodprotection_delay` |  | 10 | <value> | Blocks the chat for x seconds to player who triggered the flood protection. |
| `g_floodprotection_messages` |  | 4 | <value> | How many messages can a player send in y seconds before triggering the flood protection. |
| `g_floodprotection_seconds` |  | 4 | <value> | Triggers flood protection if a player sends more than x messages in y seconds. |
| `g_floodprotection_team` |  | 0 | <value> | Triggers flood protection if a player sends more than x team messages in y seconds. |
| `g_gametype` | *,S,L | dm | <gametype> | Changes the gametype. Requires server restart / map reload. |
| `g_gametypes_available` | S,- |  | *write protected* |  |
| `g_gametypes_list` | *,- |  | *write protected* |  |
| `g_gravity` |  | 850 | <value> | Obsolete ConVar. |
| `g_health_respawn` | * | 0 |  |  |
| `g_inactivity_maxtime` |  | 90.0 | <value> | A player will get moved to spectators team if inactive for longer than x seconds (doesn't affect warmup). |
| `g_instagib` | *,S,L | 0 | <0/1> | Enables InstaGib. Requires server restart. |
| `g_instajump` | * | 1 | <0/1> | Enables InstaJump. |
| `g_instashield` | * | 1 | <0/1> | Enables InstaShield. |
| `g_knockback_scale` | * | 1.0 | <value> | Changes the knockback scale of weapons. Affects normal weapons AND Instagun. |
| `g_map_pool` | * |  | <maplist> | Only allows these maps to appear in "map" callvote. Needs g_enforce_map_pool set to 1. |
| `g_maplist` | * |  | <maplist> | Sets the server's map list. |
| `g_maprotation` | * | 1 | <0-2> | Sets map rotation mode. 0 - same map, 1 - in order, 2 - random. |
| `g_match_extendedtime` | * | 2 | <value> | Changes the overtime's length to x minutes. 0 to disable. |
| `g_match_score` | S,- |  | *write protected* |  |
| `g_match_time` | S,- |  | *write protected* |  |
| `g_maxtimeouts` | * | 2 | <value> | How many timeouts can be called per match. |
| `g_maxvelocity` |  | 16000 | <value> | Obsolete ConVar. |
| `g_needpass` | S,- | 1 | *write protected* |  |
| `g_numbots` | * | 0 | <value> | Amount of bots on the server. |
| `g_operator_password` | * |  | <password> | Sets the operator password. Operator is disabled if empty. |
| `g_postmatch_timelimit` | * | 4 | <value> |  |
| `g_race_gametype` | S,- | 0 | *write protected* |  |
| `g_scorelimit` | * | 0 | <value> | Amount of points required to obtain by a player / team to end the match. |
| `g_spawnsystem_wave_maxcount` | * | 16 | <value> |  |
| `g_spawnsystem_wave_time` | * | 15 | <value> |  |
| `g_teams_allow_uneven` | * | 1 | <0/1> | Allow the teams to be uneven. If enabled, allows players to switch teams anytime. |
| `g_teams_maxplayers` | * | 0 | <value> | How many players can a single team have. |
| `g_timelimit` | * | 10 | <value> | Sets the duration of matches (in minutes). |
| `g_uploads_demos` |  | 1 | <0/1> | Allows players to download demos from the server. |
| `g_votable_gametypes` | * |  | <gametypes> | A list of gametypes allowed to be used in "gametype" callvote. |
| `g_vote_allowed` | * | 1 | <0/1> | Allows / disallows calling ALL votes (including opcalls). |
| `g_vote_cooldowntime` | * | 5 | <value> | A player needs to wait x seconds after calling a vote to call another one. |
| `g_vote_electtime` | * | 20 | <value> | Specifies how long do callvotes last (in seconds). |
| `g_vote_maxchanges` | * | 3 | <value> | Specifies how many times can a player change their vote. |
| `g_vote_percent` | * | 55 | <0-100> | How much % of players need to vote yes for the vote to pass. |
| `g_warmup_timelimit` | * | 5 | <value> | Sets how long do warmups take (in minutes). |
| `g_weapon_respawn` | * | 0 |  |  |

## gl

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `gl_cull` |  | 1 | <0/1> | Enable OpenGL Culling. |
| `gl_drawbuffer` |  | GL_BACK | <value> | Specifies the buffer which display information will be written to. |
| `gl_driver_win` | *,L | opengl32.dll | <value> | Specifies the OpenGL driver dll file. |
| `gl_ext_bgra` | *,- | 1 | *write protected* | If enabled, the BGRA openGL extension will be used if supported. |
| `gl_ext_blend_func_separate` | *,- | 1 | *write protected* |  |
| `gl_ext_compressed_ETC1_RGB8_texture` |  | 1 |  |  |
| `gl_ext_depth24` |  | 1 |  |  |
| `gl_ext_depth_nonlinear` |  | 1 |  |  |
| `gl_ext_depth_texture` | *,L | 1 |  |  |
| `gl_ext_draw_instanced` | *,L | 1 |  |  |
| `gl_ext_draw_range_elements` | *,L | 1 | <0/1> | If enabled, DrawRangeElements (an opengl extension) will be used if it's supported. |
| `gl_ext_ES3_compatibility` | *,L | 1 |  |  |
| `gl_ext_fragment_precision_high` |  | 1 |  |  |
| `gl_ext_fragment_shader` | *,- | 1 | *write protected* |  |
| `gl_ext_framebuffer_blit` | *,L | 1 |  |  |
| `gl_ext_framebuffer_object` | *,- | 1 | *write protected* |  |
| `gl_ext_gamma_control` |  | 1 |  |  |
| `gl_ext_get_program_binary` | *,L | 1 |  |  |
| `gl_ext_GLSL` | *,- | 1 | *write protected* |  |
| `gl_ext_GLSL130` | *,L | 1 |  |  |
| `gl_ext_GLSL_core` | *,- | 1 | *write protected* |  |
| `gl_ext_gpu_memory_info` | *,- | 1 | *write protected* |  |
| `gl_ext_gpu_shader5` | *,L | 1 |  |  |
| `gl_ext_half_float_vertex` | *,L | 1 |  |  |
| `gl_ext_instanced_arrays` | *,L | 1 |  |  |
| `gl_ext_meminfo` | *,- | 1 | *write protected* |  |
| `gl_ext_multitexture` | *,- | 1 | *write protected* |  |
| `gl_ext_packed_depth_stencil` | *,L | 1 |  |  |
| `gl_ext_rgb8_rgba8` |  | 1 |  |  |
| `gl_ext_shader_objects` | *,- | 1 | *write protected* |  |
| `gl_ext_shading_language_100` | *,- | 1 | *write protected* |  |
| `gl_ext_shading_language_130` |  | 1 |  |  |
| `gl_ext_shadow` | *,L | 1 |  |  |
| `gl_ext_shadow_samplers` |  | 1 |  |  |
| `gl_ext_swap_control` | *,- | 1 | *write protected* |  |
| `gl_ext_texture3D` | *,L | 1 | <0/1> | If enabled, the Texture3D (an opengl extension) will be used if it's supported. |
| `gl_ext_texture_array` | *,L | 1 |  |  |
| `gl_ext_texture_compression` | *,L | 1 |  |  |
| `gl_ext_texture_cube_map` | *,- | 1 | *write protected* | If enabled, Texture Cube Mapping (an opengl extension) will be used if it's supported. |
| `gl_ext_texture_edge_clamp` | *,- | 1 | *write protected* |  |
| `gl_ext_texture_filter_anisotropic` | *,- | 1 | *write protected* |  |
| `gl_ext_texture_lod` | *,L | 1 |  |  |
| `gl_ext_texture_non_power_of_two` | *,L | 1 |  |  |
| `gl_ext_texture_npot` |  | 1 |  |  |
| `gl_ext_vertex_buffer_object` | *,- | 1 | *write protected* | If enabled, opengl vertex buffer objects will be utilized if supported. |
| `gl_ext_vertex_buffer_object_hack` | *,- | 0 | *write protected* |  |
| `gl_ext_vertex_half_float` |  | 1 |  |  |
| `gl_ext_vertex_shader` | *,- | 1 | *write protected* |  |
| `gl_finish` |  | 0 | <0/1> | If enabled, the CPU will wait for the GPU at the end of each rendered frame. |
| `gl_max_texture_size` |  | 0 | *write protected* |  |

## http

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `http_proxy` | * |  |  |  |
| `http_proxyuserpwd` | * |  |  |  |

## in

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `in_debug` |  | 0 |  |  |
| `in_dinput` |  | 1 |  |  |
| `in_grabinconsole` | * | 0 |  |  |
| `in_initmouse` |  | 1 | *write protected* |  |
| `in_mouse` | * | 1 | <0/1> | Enables mouse input |

## irc

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `irc_nick` | * | WarforkPlayer | <value> | Sets your nickname. |
| `irc_password` | * | <undefined> | <value> | Specifies a password for IRC Servers which require one to connect. |
| `irc_port` | * | 6667 | <value> | Specifies a port for the IRC Server you're connecting to. |
| `irc_server` | * | irc.quakenet.org | <value> | Specifies a ip\hostname for the IRC Server you're connecting to. |
| `irc_user` | * | WarforkUser | <value> | Specifies a username for IRC Servers which require one to connect. |

## logconsole

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `logconsole` | * |  |  |  |
| `logconsole_append` | * | 1 |  |  |
| `logconsole_flush` | * | 0 |  |  |
| `logconsole_timestamp` | * | 0 |  |  |

## m

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `m_accel` | * | 0 | <value> | Mouse acceleration multiplier. |
| `m_accelOffset` | * | 0 | <value> | Enables different mouse acceleration styles. |
| `m_accelPow` | * | 2 | <value> | Determines the rate of acceleration for m_accelStyle = 2. |
| `m_accelStyle` | * | 0 | <value> | Style of mouse acceleration. |
| `m_filter` | * | 0 | <0-2> | If enabled the type of filtering applied to your mouse input will be changed. |
| `m_filterStrength` | * | 0.5 | <value> | Controls the strength of m_filter. |
| `m_forward` |  | 1 | <value> | Changes your mouse sensitivity when moving forward and back. |
| `m_pitch` | * | <undefined> | <value> | The sensitivity for looking up and down with the mouse. |
| `m_raw` | * | 1 | <0/1> | Enables raw mouse data input. |
| `m_sensCap` | * | 0 | <value> | Affects the maximum limit for m_accelStyle = 2. |
| `m_side` |  | 1 | <value> | Changes your mouse sensitivity when moving left and right. |
| `m_yaw` | * | 0.022 | <value> | Changes speed scale of X axis. |

## r

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `r_brightness` | * | 0 | <0-1.0> | Sets the brightness level on your screen. |
| `r_coronascale` |  | 0.4 |  |  |
| `r_detailtextures` | * | 1 | <0/1> | If enabled, detailed textures will be shown. |
| `r_drawelements` |  | 1 | <0/1> | Enables drawing elements. |
| `r_drawentities` | C | 1 | <0/1> | Enables drawing entities. |
| `r_drawflat` | * | 0 | <0/1> | If enabled, will draw the floor and walls as solid colors. |
| `r_draworder` | C | 0 |  |  |
| `r_drawworld` | C | 1 | <0/1> | Enables drawing the world. |
| `r_dynamiclight` | * | 1 | <0/1> | Enables dynamic light. |
| `r_environment_color` |  | 0 0 0 |  | Changes the background color if r_drawworld is 0 |
| `r_faceplanecull` |  | 1 | <0/1> | If enabled, only the polygons of the face will be rendered. |
| `r_fastsky` | * | 0 | <0/1> | If enabled, only a basic skybox will be drawn. |
| `r_floorcolor` | * | 255 153 0 | <R G B> | The color of floor if r_drawflat = 1. |
| `r_fullbright` | L | 0 | <0/1> | Sets maximum brightness to all textures. |
| `r_fxaa` | * | 1 | <0/1> | Enables FXAA antialiasing. |
| `r_gamma` | * | 1.0 | <value> | Changes the gamma. |
| `r_ignorehwgamma` |  | 0 |  |  |
| `r_leafvis` | C | 0 |  |  |
| `r_lerpmodels` |  | 1 |  |  |
| `r_lighting_ambientscale` |  | 1 |  |  |
| `r_lighting_deluxemapping` | *,L | 1 |  |  |
| `r_lighting_directedscale` |  | 1 |  |  |
| `r_lighting_glossexponent` | * | 24 |  |  |
| `r_lighting_glossintensity` | * | 1.5 |  |  |
| `r_lighting_grayscale` | *,L | 0 | <0/1> | Enables grayscale lighting. |
| `r_lighting_maxglsldlights` | * | 16 |  |  |
| `r_lighting_maxlmblocksize` | *,L | 2048 |  |  |
| `r_lighting_packlightmaps` | *,L | 1 |  |  |
| `r_lighting_specular` | *,L | 1 |  |  |
| `r_lighting_vertexlight` | *,L | 0 |  |  |
| `r_lightmap` |  | 0 | <0/1> | If enabled, all textures will not be displayed and only static lights will be visible. |
| `r_lockpvs` | C | 0 |  |  |
| `r_lodbias` | * | 0 |  |  |
| `r_lodscale` | * | 5.0 | <value> | This value adjusts the level of detail scale modifier. |
| `r_mapoverbrightbits` | *,L | 2 |  |  |
| `r_maxfps` | * | 250 | <24-1000> | Sets the FPS limit. |
| `r_maxglslbones` | L | 100 |  |  |
| `r_multithreading` | *,L | 1 | <0/1> | Enables multithreading. |
| `r_nobind` |  | 0 |  |  |
| `r_nocull` |  | 0 |  |  |
| `r_norefresh` |  | 0 |  |  |
| `r_novis` |  | 0 |  |  |
| `r_offsetmapping` | * | 2 |  |  |
| `r_offsetmapping_reliefmapping` | * | 0 |  |  |
| `r_offsetmapping_scale` | * | 0.02 |  |  |
| `r_outlines_cutoff` | * | 712 |  |  |
| `r_outlines_scale` | * | 1 |  |  |
| `r_outlines_world` | * | 1.8 |  |  |
| `r_overbrightbits` |  | 0 |  |  |
| `r_packlightmaps` |  | 1 |  |  |
| `r_picmip` | *,L | 0 | <0-16> | Overall image and texture quality. The highest the number the lower the quality level. |
| `r_polyblend` |  | 1 |  |  |
| `r_portalmaps` | *,L | 1 |  |  |
| `r_portalmaps_maxtexsize` | * | 1024 |  |  |
| `r_portalonly` |  | 0 |  |  |
| `r_screenshot_fmtstr` | * | wf_y%m%d_HM%S | <date format> | File name format of screenshots. |
| `r_screenshot_jpeg` | * | 1 | <0/1> | Enables .jpeg screenshots. |
| `r_screenshot_jpeg_quality` | * | 90 | <0-100> | Sets the quality of jpeg screenshots, in percentages. |
| `r_shadows` | * | 0 |  |  |
| `r_shadows_alpha` | * | 0.7 | <0-1> | Alpha of shadows. |
| `r_shadows_dither` | * | 0 |  |  |
| `r_shadows_maxtexsize` | * | 64 |  |  |
| `r_shadows_nudge` | * | 1 |  |  |
| `r_shadows_pcf` | * | 1 |  |  |
| `r_shadows_projection_distance` | C | 64 |  |  |
| `r_shadows_self_shadow` | * | 0 |  |  |
| `r_shownormals` | C | 0 |  |  |
| `r_showtris` | C | 0 |  |  |
| `r_skymip` | *,L | 0 | <0-16> | Overall image and texture quality of the skybox. The highest the number the lower the quality level. |
| `r_soft_particles` | * | 1 | <0/1> | Enables soft particles. |
| `r_soft_particles_available` |  | 0 | *write protected* |  |
| `r_soft_particles_scale` | * | 0.02 |  | Scale of soft particles. |
| `r_speeds` |  | 0 |  |  |
| `r_stencilbits` | *,L | 0 |  |  |
| `r_subdivisions` | *,L | 5 |  |  |
| `r_swapinterval` | * | 0 |  |  |
| `r_swapinterval_min` |  | 0 | *write protected* |  |
| `r_temp1` |  | 0 |  |  |
| `r_texturebits` | *,L | 0 | <0/1> | If enabled, vsync will be activated. |
| `r_texturecompression` | *,L | 0 | <0/1> | Enables texture compression. |
| `r_texturefilter` | * | 4 |  |  |
| `r_texturefilter_max` |  | 0 | *write protected* |  |
| `r_texturemode` | * | GL_LINEAR_MIPMAP_LINEAR |  |  |
| `r_usenotexture` | * | 0 | <0/1> | Disables textures. |
| `r_wallcolor` | * | 255 255 255 | <R G B> | The color of walls if r_drawflat = 1. |

## rcon

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `rcon_address` |  | <undefined> | <ip address> | Sets the IP address for rcon connection. |
| `rcon_password` |  | <undefined> | <password> | Sets the password for rcon connection. |

## s

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `s_doppler` | * | 1.0 | <value> | If enabled, Doppler effect will be used for sounds |
| `s_globalfocus` | * | 0 | <0/1> | Mutes the game when alt-tabbed. |
| `s_khz` | * | 44 | <value> | The sampling rate of the sounds in kilohertz. |
| `s_mixahead` | * | 0.14 | <value> | The specified time waited before mixing sound samples. |
| `s_module` | *,L | 1 | <0-2> | Specifies the default sound module. |
| `s_module_fallback` | L | 2 | <0-2> | Specifies a fallback sound module incase s_module cannot be loaded. |
| `s_musicvolume` | * | 0.15 | <0-1> | Global music volume. |
| `s_openAL_device` | *,L | Generic Software | <value> | Specifies the OpenAL device. |
| `s_pseudoAcoustics` | * | 0 | <0/1> | High quality spatialisation for the Qfusion Sound Module. |
| `s_separationDelay` | * | 1.0 |  |  |
| `s_stereo2mono` | * | 0 | <0/1> | Enables mono sound. |
| `s_swapstereo` | * | 0 | <0/1> | Swap the left and right sound channel. |
| `s_volume` | * | 0.8 | <0-1> | Global volume of the game. |
| `s_wavonly` | * | 0 | <0/1> | If enabled, only .wav sound files will be played. |

## scr

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `scr_consize` | * | 0.4 | <0.1-1.0> | size of the console "0.1-1.0" |
| `scr_conspeed` | * | 3 | <value> | Controls the console drop-down speed. |

## sv

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `sv_autoUpdate` |  | 0 | *write protected* |  |
| `sv_botpersonality` | * | 0 |  |  |
| `sv_cheats` | S,L | 0 | <0/1> | Enables cheats on the server. |
| `sv_debug_serverCmd` | * | 0 |  |  |
| `sv_defaultmap` | * | wfdm1 | <map> | Changes the default map of the server. |
| `sv_demodir` |  |  | *write protected* |  |
| `sv_enforcetime` |  | 1 |  |  |
| `sv_fps` |  | 62 | *write protected* |  |
| `sv_highchars` |  | 1 |  |  |
| `sv_hostname` | *,S |  | <name> | Name of the server. Appears in the server list. |
| `sv_http` | *,S,L | 1 | <0/1> | Enables an HTTP server that lets connecting players download missing files. |
| `sv_http_ip` | *,L |  | <ip address> | If set, binds the HTTP server to a specific IPv4 address. |
| `sv_http_ipv6` | *,L |  | <ip address> | If set, binds the HTTP server to a specific IPv6 address. |
| `sv_http_port` | *,L | 44444 | <port> | Changes the port of the HTTP server. |
| `sv_http_upstream_baseurl` | *,L |  |  |  |
| `sv_http_upstream_ip` | * |  |  |  |
| `sv_http_upstream_realip_header` | * |  |  |  |
| `sv_ip` | *,L |  | <ip address> | If set, binds the Warfork server to a specific IPv4 address. |
| `sv_ip6` | *,L | :: | <ip address> | If set, binds the Warfork server to a specific IPv6 address. |
| `sv_iplimit` | * | 3 | <value> | Maximum amount of connections from a single IP address. |
| `sv_lastAutoUpdate` | *,- | 0 | *write protected* |  |
| `sv_maxclients` | *,S,L |  | <value> | Maximum amount of players allowed on the server. |
| `sv_maxentities` | *,L | 1024 | <value> | Maximum amount of entities on the map. |
| `sv_maxmvclients` | *,S | 4 |  |  |
| `sv_mm_authkey` | * |  |  |  |
| `sv_mm_debug_reportbots` | C | 0 |  |  |
| `sv_mm_enable` | *,S,- | 0 | *write protected* |  |
| `sv_mm_loginonly` | *,S | 0 |  |  |
| `sv_modmanifest` |  |  | *write protected* |  |
| `sv_MOTD` | * | 0 | <0/1> | Enables Message Of The Day on the server. |
| `sv_MOTDFile` | * | <undefined> | <path> | Path to Message Of The Day file. |
| `sv_MOTDString` | * | <undefined> | <value> | A definable MOTD String that takes precedence over sv_MOTDFile. |
| `sv_port` | *,L | 44400 | <port> | Changes the IPv4 port of the Warfork server. |
| `sv_port6` | *,L | 44400 | <port> | Changes the IPv6 port of the Warfork server. |
| `sv_pps` | S | 20 | <value> | Packets per second a server sends to the client. |
| `sv_public` | * |  | <0/1> | If set to 1, the server will appear on the public server list. |
| `sv_pure` | *,S,L | 0 | <0/1> | If set to 1, the server will check the validity of client files with server. Kicks if invalid. |
| `sv_pure_forcemodulepk3` | L |  |  |  |
| `sv_reconnectlimit` | * | 3 | <value> | Seconds a client must wait until they can reconnect with a server. |
| `sv_showChallenge` |  | 0 |  |  |
| `sv_showclamp` |  | 0 |  |  |
| `sv_showInfoQueries` |  | 0 |  |  |
| `sv_showRcon` |  | 1 |  |  |
| `sv_skilllevel` | *,S,L | 2 | <0-2> | Defines the skill level of your server, which affects bots. |
| `sv_skillRating` | S,- | 0 | *write protected* |  |
| `sv_timeout` |  | 125 | <value> | Kicks players from server if connection is lost for more than x seconds. Takes priority over cl_timeout. |
| `sv_uploads` |  | 1 |  |  |
| `sv_uploads_baseurl` | * |  |  |  |
| `sv_uploads_demos` | * | 1 |  |  |
| `sv_uploads_demos_baseurl` | * |  |  |  |
| `sv_uploads_from_server` |  | 1 | <0/1> | If enabled, uploading is allowed directly from the server. |
| `sv_uploads_http` |  | 1 | *write protected* |  |
| `sv_zombietime` |  | 2 | <value> | Determines how long a connected client remains open after it has either timed out with sv_timeout or disconnected. |

## ui

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `ui_autobrowse_manual` | * | 0 | <0/1> | If enabled, servers will be suggested when you click "Play" and query the masterservers. |
| `ui_basepath` | * | ui/porkui | <value> | Defines the basepath of the user interface. |
| `ui_cachepurgedate` | * | <undefined> | <yyyy-mm-dd> | Purges the folder "cache/ui" on a specific date, which contains cache from asyncrhonous HTTP requests. |
| `ui_lighting` |  | 2 |  |  |
| `ui_preload` | * | 1 |  |  |
| `ui_serverbrowser_tab` | * |  |  |  |
| `ui_tutorial_taken` | * | 0 | <0/1> | If enabled, you will be prompted (once per game load) to complete the tutorial upon clicking "Play". |
| `ui_video_profile` | * | medium |  |  |

## vid

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `vid_displayfrequency` | *,L | 0 | <value> | Defines the refresh rate of your screen in Hz. |
| `vid_fullscreen` | * | 1 | <0/1> | If enabled, Warfork will run in full screen mode. |
| `vid_height` | *,L | 0 | <value> | Defines a custom screen resolution height. |
| `vid_multiscreen_head` | * | -1 | <value> | Changes the default monitor used. |
| `vid_parentwid` |  | 0 | *write protected* | Defines the parent window identifier. |
| `vid_ref` | *,L | ref_gl | <value> | Defines the video renderer driver. |
| `vid_width` | *,L | 0 | <value> | Defines a custom screen resolution width. |
| `vid_xpos` | * | 0 | <value> | Defines the X position of the game running in window mode. |
| `vid_ypos` | * | 0 | <value> | Defines the Y position of the game running in window mode. |

## win

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `win_noalttab` | * | 0 | <0/1> | If enabled, ALT+TAB will work. |
| `win_nowinkeys` | * | 1 | <0/1> | If enabled, Windows keys will work. |

## Prefixless

| Command | Flags | Default | Parameters | Description |
|---------|-------|---------|------------|-------------|
| `clan` | *,U |  | <name> | Sets the name of your clan. Appears on the scoreboard. |
| `color` | *,U | 255 255 255 | <R G B> | Sets your Player color. |
| `debuggraph` |  | 0 | <0/1> | If enabled, the debug graph will be displayed. |
| `dedicated` |  | 0 | *write protected* | Tells the game if it's a dedicated server. |
| `developer` | C | 0 |  | Level of developer information printed to the console. The higher the number, the more information is printed. |
| `developerMemory` |  | 0 | <0/1> | Prints memory allocation information to console if developer is enabled as well. |
| `favorites` | * | 0 |  | Amount of favorite servers. |
| `filterban` |  | 1 |  |  |
| `fixedtime` | C | 0 |  |  |
| `fov` | * | 100 | <value> | Changes your Field of view. |
| `gamedate` | S,L | Oct 8 2019 |  |  |
| `gamename` | S,- | Warfork | *write protected* | Name of the game. |
| `graphheight` |  | 32 |  | Changes the graph height for timegraph, netgraph, etc. |
| `graphscale` |  | 1 |  | Scales the graph (timegraph, netgraph, etc.) for resolutions with a width greather than 1024. |
| `graphshift` |  | 0 |  |  |
| `hand` | *,U | 0 | <0/1> | Changes weapon handedness. |
| `handicap` | *,U | 0 | <value> | Decreases your damage output by x% usefull for dueling players below your skill level |
| `host_speeds` |  | 0 | <0/1> | If enabled timing information will be printed to console. |
| `lang` | *,L |  | <language> | Sets the language of Warfork. |
| `lookspring` |  | 0 | <0/1> | If enabled, the screen will be automatically centered when using +mlook. |
| `lookstrafe` |  | 0 | <0/1> | If enabled, automatic strafing will be toggled when using +mlook. |
| `mapname` | S,- |  | *write protected* | The name of current map played. |
| `masterservers` | L | master1.forbidden.gg master1.icy.gg | <value> | Specifies the master servers used to query a list of Warfork servers. |
| `masterservers_steam` | L | <undefined> | <value> | Specifies the Steam master servers used to query a list of Warfork servers. |
| `mm_url` | *,- | https://mm.forbidden.gg:1338 | *write protected* | Specifies the Warfork Matchmaking Servers |
| `model` | *,U | bigvic | <model name> | Changes your Player model. |
| `name` | *,U |  | <name> | Changes your nickname. |
| `net_showfragments` |  | 0 |  |  |
| `netgraph` |  | 0 | <0/1> | If enabled, information will be displayed on the bottom of the screen about all network packets. |
| `nextmap` |  | match "advance" | <value> | Proceeds to the next map. |
| `password` | *,U |  | <password> | If a server requires a password, the client automatically tries to join with x password. |
| `protocol` | S,- | 22 | *write protected* |  |
| `revision` |  | Oct 8 2019 00:08:07 | *write protected* | Date when the game was compiled. |
| `sensitivity` | * | 3 | <value> | Changes sensitivity of your mouse. |
| `showdrop` |  | 0 | <0/1> | If enabled, information will be displayed in the console about dropped network packets. |
| `showpackets` |  | 0 | <0/1> | If enabled, information will be displayed in the console about all network packets. |
| `skin` | *,U | default |  |  |
| `timedemo` | C | 0 |  |  |
| `timegraph` |  | 0 | <0/1> | If enabled, a graph will be displayed, which visualizes the compression and expansion of game time, which is necessary maintain the overall game time constant. |
| `timescale` | C | 1.0 | <value> | Changes the time scale of the game. |
| `tv_server` |  | 0 | *write protected* | Tells the game if the server is a TV server. |
| `version` | S,- | 2.10 x64 Oct 8 2019 Win32 RELEASE | *write protected* | The version of the game. |
| `zoomfov` | * | 30 | <value> | Changes the field of view while zooming. |
| `zoomsens` | * | 0 | <value> | Changes your sensitivity while zooming. |

## Commands

| Command | Parameters | Description |
|---------|------------|-------------|
| `+attack` |  | Primary attack. |
| `+back` |  | Moves backward. |
| `+forward` |  | Moves forward. |
| `+klook` |  | Keyboard look; +forward +back serve as +lookup +lookdown. |
| `+left` |  | Turns left. |
| `+lookdown` |  | Looks down. |
| `+lookup` |  | Looks up. |
| `+movedown` |  | Moves backwards. |
| `+moveleft` |  | Moves left. |
| `+moveright` |  | Moves right. |
| `+moveup` |  | Moves up; In water, lava, etc. |
| `+quickmenu` |  | An easily accessible menu with basic commands such as Voice Says. |
| `+right` |  | Turns right. |
| `+scores` |  | Accesses the scoreboard. |
| `+speed` |  | Changes your speed. |
| `+strafe` |  | When used +left and +right are changed with +moveleft and +moveright. |
| `+use` |  | Uses an item. |
| `+zoom` |  | Zooms. |
| `-attack` |  | Stops primary attack. |
| `-back` |  | Stops moving backward. |
| `-forward` |  | Stops moving forward. |
| `-klook` |  | Stops Keyboard look; +forward +back serve as +lookup +lookdown. |
| `-left` |  | Stops looking left. |
| `-lookdown` |  | Stops looking down. |
| `-lookup` |  | Stops looking up. |
| `-movedown` |  | Stops moving backwards. |
| `-moveleft` |  | Stops moving left. |
| `-moveright` |  | Stops moving right. |
| `-moveup` |  | Stops moving up; In water, lava, etc. |
| `-quickmenu` |  | Stops the quick menu, an easily accessible menu with basic commands such as Voice Says. |
| `-right` |  | Stops turning right. |
| `-scores` |  | Stops accessing the scoreboard. |
| `-speed` |  | Stops changing your speed. |
| `-strafe` |  | Stops strafing, which When used +left and +right are changed with +moveleft and +moveright. |
| `-use` |  | Stops using an item. |
| `-zoom` |  | Stops zooming. |
| `addcam` | <type name> | Adds a camera to your democam path. Available camera types are: FirstPerson; ThirdPerson; Positional; Path_linear; Path_spline; orbital. |
| `addip` | <ip address> | Adds IP addresses to the filter list. |
| `alias` | <alias name> <command> | Creates an alias. |
| `aliaslist` |  | Lists all aliases. |
| `bind` | <key> <command> | Binds a key to a command. |
| `bindlist` |  | Lists all bound keys. |
| `callvote` | <vote> [argument] | Calls a vote. |
| `centerview` |  | Centers the players view. |
| `clear` |  | Clears the console. |
| `clearcams` |  | Clears all cameras in a camerapath. |
| `cmdlist` |  | Lists all console commands. |
| `coach` |  | Allows you to be a coach in some team based gametypes. |
| `cointoss` | <heads/tails> | Flips a coin based on your choice and announces if you won or lost. |
| `condump` | <filename> | Dumps the console log to a file. |
| `connect` | <ip address> | Connects to a server. |
| `cvarlist` |  | Lists all cvars. |
| `deletecam` |  | Deletes the current camera; only works in demoEditMode |
| `demo` | <filename> | Loads a specific demo. |
| `demoavi` |  | Starts recording video as frames or audio as .wav file depending on cl_demoavi_audio and cl_demoavi_video. Framerate depends on cl_demoavi_fps. |
| `demoEditMode` |  | Lets you add and edit cameras for camera paths. Displays additional information on cameras (e.g.: timecode, current camera, next camera, type, position, roll, pitch, yaw ,fov). |
| `demoFreeFly` |  | Enables free flying camera regardless of set camera paths; entities like players may disappear on single POV demos when camera moves too far from the player. |
| `demoget` | <ID> | Use with demolist to download recorded demos from a server |
| `demojump` |  | Jumps to a specified time in a demo. Time format is [minutes:]seconds. Use + or - in front of the time to specify it in relation to current position in the demo. |
| `demolist` |  | Lists all demos on the Server and their ID. Can be downloaded via demoget <ID> |
| `demopause` |  | Pauses or resumes the currently playing demo. |
| `disconnect` |  | Disconnects from current server. |
| `downloadcancel` |  | Cancels an active download. |
| `downloadstatus` |  | Displays download status information. |
| `echo` | <message> | Prints a message to the console. |
| `editcam` | <command> <variable> | Edits the current camera, you can edit: type <type name> eg. path_spline; track <entity number> (tracks entity; 0 for no track); fov; timeOffset; origin; angles; pitch; yaw; roll. |
| `exec` | <filename> | Executes a configuration file. |
| `gametype` |  | Lists information about current game type. |
| `give` | <all/health/weapons/ammo/armor> | Give items to a Player. Requires cheats to be enabled. |
| `god` |  | Toggles godmode. |
| `heartbeat` |  | Sends a manual heartbeat to the masterservers. |
| `help_hud` |  | Prints a list of HUD scripts commands, HUD scripts operators, HUD scripts CONSTANT names, and HUD scripts REFERENCE names to your console. |
| `imagelist` |  | Shows a list of all images loaded in your console. |
| `importcams` | <filename> | imports a .cam file. Filepath is relative to the demos directory. The cameras imported are merged with the previously existing, if any. |
| `join` | [team name] | Joins the game. Joins a specific team if specified. |
| `kick` | <player> | Kicks a player from the server. |
| `kill` |  | Kills the player. |
| `killserver` |  | Kills the server process. |
| `leavequeue` |  | Leaves the challengers queue. |
| `listip` |  | The current list of filters will be printed to console. |
| `listlocations` |  | Prints a list of all map locations (if available) to console. |
| `lockteam` |  | Locks the teams. |
| `map` | <map name> | Switches a map. |
| `maplist` |  | Lists all maps available. |
| `match` | <restart\advance\status> | Restarts, Advances, or gets the Status of your match. |
| `memlist` |  | Prints a memory pool list to your console. |
| `memstats` |  | Prints memory statistics to your console. |
| `messagemode` |  | Prompts you to write a message, which will be sent to everyone on the server. |
| `messagemode2` |  | Prompts you to write a message, which will be sent to everyone on your team. |
| `mm_login` |  | Logs you out of matchmaking. |
| `mm_logout` |  | Logs you in Matchmaking. |
| `modellist` |  | Prints a list of all models loaded in your console. |
| `noclip` |  | Toggles noclip. |
| `notready` |  | Changes status to "Not ready". |
| `op` | <password> | Makes the player a game operator. |
| `opcall` | <vote> [argument] | Calls an instant-passing vote. |
| `operator` | <password> | Makes the player a game operator. |
| `players` |  | Lists all players in-game. |
| `position` |  | Displays player's current position. |
| `purelist` |  | Displays a list of all Pure Files in your console. |
| `putaway` |  | Closes the scoreboard if open. |
| `quit` |  | Quits the game / server. |
| `racerestart` |  | Restarts the race. |
| `rcon` | <command> | Executes a server command as console. |
| `ready` |  | Makes the player ready. |
| `reconnect` |  | Reconnects the player to the current server. |
| `record` | <name> | Records a demo with the specified name(These are single POV demos, for multiPOV use serverrecord). |
| `removeip` | <ip address> | Removes IP addresses from the filter list. |
| `s_devices` |  | List of available OpenAL sound devices. |
| `s_restart` |  | Restarts the sound engine. |
| `saverecam` | <optional name> | Saves the .cam script file with the camera path data. If no name is provided, the demo name is used. |
| `say` | <message> | Sends a global message. |
| `say_team` | <message> | Sends a team message. |
| `score` |  | Toggles the scoreboard. |
| `screenshot` |  | Takes a screenshot of what you're looking at. |
| `serverinfo` |  | Displays Server info settings in console. |
| `serverrecord` | <name> | Records a multiPOV demo on the Server (can be downloaded by clients via demolist and demoget). |
| `set` | <cvar> <value> | Changes the value of x cvar to y. |
| `shaderlist` |  | Prints a list of shaders currently loaded in your console. |
| `showip` |  | Shows your local IP Address (reversed). |
| `showserverip` |  | Shows the server IP Address. |
| `sizedown` |  | Decreases the viewable area (affects cg_viewSize by -10) on your screen. |
| `sizeup` |  | Increases the viewable area (affects cg_viewSize by +10) on your screen. |
| `soundlist` |  | Prints a list of all sounds currently loaded in your console. |
| `spec` |  | Joins the SPECTATOR team. |
| `spectators` |  | Prints a list of spectators. |
| `stats` | <id\playername> | Prints your or a specified players stats. |
| `status` |  | Displays the server status in console. |
| `stop` |  | Stops your demo if it's currently recording. |
| `stopmusic` |  | Stops music that's currently playing. |
| `svscore` | <0/1> | If enabled, the scoreboard will be toggled. |
| `timein` |  | Resumes the match instantly. |
| `timeout` |  | Pauses the match for 180 seconds. |
| `toggle` | <cvar> <argument 1> [argument n] | Toggles a cvar's value between the arguments. |
| `toggleconsole` |  | Toggles the console. |
| `toggleready` |  | Toggles "ready" status. |
| `tvconnect` |  | Sends a command to connect to a TV server (with available slots) that has round robin balancing. |
| `ui_dumpapi` |  | Dumps API information to console. |
| `ui_printdocs` |  | Prints document cache to console. |
| `ui_reload` |  | Reloads the user interface. |
| `unalias` | <name> | Removes an alias. |
| `unaliasall` |  | Removes all aliases> |
| `unbind` | <key> | Unbinds a key. |
| `unbindall` |  | Unbinds all keys. |
| `unlockteam` |  | Unlocks the teams. |
| `unready` |  | Makes the player unready. |
| `upstate` |  | Updates your client on the current state of things. |
| `use` |  | Uses an object in the world. |
| `userinfo` |  | Prints a list of User Info Settings to your console. |
| `vid_modelist` |  | List of available video modes. |
| `vid_restart` |  | Restarts the video engine. |
| `vote` | <yes / no> | Casts a vote. |
| `vsay` | <name> | Says a voice message globally. Shows list of all voice messages if executed without the argument. |
| `vsay_team` | <name> | Says a voice message to the team. |
| `vstr` | <variable. | Execute a variable command. |
| `wait` |  | Delays the execution of a remaining command buffer until the next frame. |
| `weapcross` | <0-4> | Shows weapon sets near your crosshair, which can be toggled between. |
| `weaplast` |  | Switches to last weapon. |
| `weapnext` |  | Switches to next weapon. |
| `weapprev` |  | Switches to previous weapon. |
| `whois` | <player> | Provides player information if they're logged into Matchmaking. |
| `writeconfig` | <name> | Writes the current configuration to a file. |
| `writeip` |  | Writes addip\removeip <ip> commands to listip.cfg for future execution. By default filter lists are not saved\restored. |

## Config Locations

| OS | Path |
|----|------|
| Windows | `%USERPROFILE%/My Documents/My Games/Warfork 2.1/basewf/` |
| Mac | `~/Library/Application Support/Warfork-2.1/basewf/` |
| Linux | `~/.local/share/warfork-2.1/basewf/` |

`config.cfg` loads on startup. `autoexec.cfg` in the same folder runs after it and takes precedence.

## Related

- [[games/warfork/controls\|Controls]]
- [[games/warfork/modding/server-hosting\|Server Hosting]]