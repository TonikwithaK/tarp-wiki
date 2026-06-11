---
title: Console
game: reflex
layer: canon
type: reference
tags: [reflex, console, config, cvars, binds]
confidence: high
sources: [phylum-cfg-guide, xytaglyph-guide, reflex-console-commands-aeon]
promoted: 2026-06-10
canon_attempts: 2
---

# Console

Source: [AEon's Reflex Console Command Reference](https://docs.google.com/document/d/1_rI85VlQJNKKsErot1S99niGkoEpuI79YNn_3FDmlvA/edit?tab=t.0) (v0.30.4)

Open with tilde (`~`). On German keyboards: `^`.

Start typing a command name and press Tab to autocomplete. Press Tab twice for a full list of matching commands. Typing a CVAR name alone and pressing Enter shows its current value.

## Config Files

Config files live in the game directory:
- 32-bit Windows: `C:\Program Files\Steam\steamapps\common\Reflex\`
- 64-bit Windows: `C:\Program Files (x86)\Steam\steamapps\common\Reflex\`

`saveconfig game` saves current settings to `game.cfg`. `loadconfig NAME` loads `NAME.cfg` (omit the `.cfg` extension).

Recommended setup: create a personal `.cfg`, clear `game.cfg`, replace its contents with `loadconfig NAME`.

## Bind Syntax

```
bind <key> <command> [value]
addbind <key> <command>
unbind <key>
unbindall
bindResetToDefaults
```

Commands starting with `+` have a paired `-` release. `addbind` adds to an existing bind without replacing it. Run `keylist` in the console for a full list of bindable key names.

## Client CVARs

### Camera / Spectator

| CVAR | Description |
|------|-------------|
| `cl_camera_freecam` | Free camera mode |
| `cl_camera_next_player` | Advance to next player POV |
| `cl_camera_prev_player` | Go to previous player POV |
| `cl_camera_player` | Attach to specific player |
| `cl_playerstate <1\|2\|3>` | 1=playing, 2=spectating, 3=editing |

### Display / HUD

| CVAR | Values | Description |
|------|--------|-------------|
| `cl_show_gun` | `0\|1` | Show/hide weapon model |
| `cl_show_hud` | `0\|1` | Show/hide HUD |
| `cl_show_lagmeter` | `0\|1` | Show lag meter |
| `cl_show_profiler` | `0\|1` | Show profiler |
| `cl_show_traffic` | `0\|1` | Show network traffic |
| `cl_events` | `0\|1` | Toggle event effects |
| `cl_gibs_maxcount` | int (default: 128) | Max gib count; set to 1 for performance |
| `cl_gibs_expire_time` | float (default: 10.0) | Gib lifetime in seconds |
| `cl_ragdoll_expire_time` | float | Ragdoll lifetime in seconds |
| `cl_text_group` | `0\|1` | Group burst/shotgun/ioncannon damage numbers into one value |
| `cl_text_time` | float | How long damage numbers stay on screen |
| `hud_vote_x` | int (default: 20) | Vote HUD x position |
| `hud_vote_y` | int (default: 300) | Vote HUD y position |

### Gameplay

| CVAR | Values | Description |
|------|--------|-------------|
| `cl_predict_items` | `0\|1` | 0 prevents false item pickups before server confirmation |
| `cl_input_subframe` | `0\|1` | 1 sets input polling to 1000 Hz, independent of framerate |
| `cl_weaponcycle` | `0\|1` | Allow weaponnext/weaponprev to cycle past first/last weapon |
| `cl_color_enemy` | color | Enemy player color |
| `cl_color_friend` | color | Friendly player color |
| `cl_color_relative` | color | Player color relative to self |
| `cl_country` | string | Country flag |

### Crosshair

| CVAR | Values | Description |
|------|--------|-------------|
| `cl_crosshair` | `1-16` | Crosshair style (0 = off) |
| `cl_show_crosshair` | `0\|1` | Show/hide crosshair |
| `cl_crosshair_colour` | `1-6` | 1=Green, 2=Teal, 3=Red, 4=Purple, 5=Yellow, 6=White |
| `ui_crosshairs_type` | int | Crosshair type index |
| `ui_crosshairs_typehit` | int | Crosshair type on hit |
| `ui_crosshairs_r` | int | Crosshair red channel |
| `ui_crosshairs_g` | int | Crosshair green channel |

For custom crosshairs, edit `game.cfg` under `ui_define Crosshairs` and modify the type/r/g/b values.

### Weapon Model

| CVAR | Default | Description |
|------|---------|-------------|
| `cl_weapon_offset_x` | `5.0` | Horizontal offset (0=center, negative=left) |
| `cl_weapon_offset_y` | `-10.0` | Vertical offset |
| `cl_weapon_offset_z` | `5.0` | Depth offset (-100 hides gun) |
| `cl_weapon_bob` | `0\|1` | Weapon bob while moving |
| `cl_weapon_kickback` | `0\|1` | Weapon kickback on firing |
| `cl_weapon_rotation` | `0\|1` | Weapon sway while moving/jumping |

To hide the weapon model without `cl_show_gun 0`: set `offset_x 0`, `offset_y -10`, `offset_z -100`.

### Player Customization

| CVAR | Description |
|------|-------------|
| `cl_playerhead` | Head model |
| `cl_playertorso` | Torso model |
| `cl_playerlegs` | Legs model |
| `cl_playerarms` | Arms model |
| `cl_playermelee` | Melee model |
| `cl_playerburstgun` | Burstgun model |
| `cl_playershotgun` | Shotgun model |
| `cl_playergrenadelauncher` | Grenade Launcher model |
| `cl_playerplasmarifle` | Plasma Rifle model |
| `cl_playerrocketlauncher` | Rocket Launcher model |
| `cl_playerplayerioncannon` | Ion Cannon model |
| `cl_playerboltrifle` | Bolt Rifle model |
| `cl_playerplayercolor1` | Player color slot 1 |
| `cl_playerplayercolor2` | Player color slot 2 |
| `cl_playerplayercolor3` | Player color slot 3 |
| `cl_playerteam` | Team assignment |

### Matchmaking

| CVAR | Description |
|------|-------------|
| `cl_mm_start` | Start matchmaking |
| `cl_mm_stop` | Stop matchmaking |
| `cl_mm_lobby` | Matchmaking lobby |
| `cl_mm_playlists` | Available playlists |
| `cl_mm_regions` | Matchmaking regions |
| `cl_mm_include_bots` | Include bots in matchmaking |
| `cl_mm_proving_grounds` | Proving grounds mode |
| `cl_mm_turbo` | Turbo matchmaking |

## Graphics CVARs

| CVAR | Values | Description |
|------|--------|-------------|
| `r_fullscreen` | `0\|1` | Fullscreen mode |
| `r_windowed_fullscreen` | `0\|1` | Borderless windowed fullscreen |
| `r_fullscreen_forcestretched` | `0\|1` | Force stretched resolution in fullscreen |
| `r_resolution_fullscreen <x> <y>` | integers | Fullscreen resolution |
| `r_resolution_windowed <x> <y>` | integers | Windowed resolution |
| `r_refreshrate` | float (default: 60.0) | Monitor refresh rate |
| `r_vsync` | `0\|1` | Vsync |
| `r_fov` | float (default: 110) | Field of view |
| `r_bloom` | `0\|1` | Bloom effect |
| `r_fxaa` | `0\|1\|2\|3` | FXAA anti-aliasing; 1-3 = low to high |
| `r_smaa` | `0\|1\|2\|3` | SMAA spatial anti-aliasing; 1-3 = low to high |
| `r_dynamic_lights` | `0\|1` | Real-time dynamic lights (expensive) |
| `r_dynamic_shadows` | `0\|1` | Dynamic shadows |
| `r_shadow_quality` | `0\|1\|2` | Shadow quality; 2 = very expensive |
| `r_shadow_resolution` | int | Shadow map resolution |
| `r_decals` | `0\|1` | Blood and impact decals |
| `r_effect_quality` | `0\|1\|2` | Game effects quality |
| `r_mesh_quality` | `0\|1\|2` | Mesh quality |
| `r_shader_quality` | `0\|1\|2` | Shader quality |
| `r_texture_quality` | int | Texture quality |
| `r_texture_resolution` | int | Texture resolution |
| `r_fog` | `0\|1` | Depth fog |
| `r_hbao` | `0\|1` | HBAO ambient occlusion |
| `r_sun` | `0\|1` | Sun lighting |
| `r_sun_intensity` | float | Sun intensity |
| `r_high_vis` | `0\|1` | High-visibility render mode (removes block effect) |
| `r_gamma` | float | Gamma |
| `r_occlusion` | `0\|1` | Occlusion culling |
| `r_silhouette` | `0\|1` | Player silhouettes through walls (spectating/team) |
| `r_showfps` | `0\|1` | FPS counter in HUD |
| `r_stats 1` | — | Real-time stats: lights, materials, drawcalls, shadowmaps, fps |
| `r_showlights` | `0\|1` | Debug: dark map with light entities visible |
| `r_profiler` | `0\|1` | CPU/GPU render timing (not working per dev) |
| `r_adapter` | int | Video adapter selection |
| `r_lm_build` | — | Compile lightmap for current map (bind: F4) |
| `r_lm_clear` | — | Clear lightmap file |
| `r_lm_showprobes` | `0\|1` | Show light probe spheres |
| `r_lm_stats` | `0\|1` | Show lightmap compile stats |
| `com_maxfps` | int | FPS cap |

## Mouse CVARs

| CVAR | Default | Description |
|------|---------|-------------|
| `m_speed` | 32.0 | Mouse sensitivity |
| `m_invert` | `0\|1` | Invert Y-axis |
| `m_advanced` | `0\|1` | Enable advanced mouse acceleration settings |
| `m_advanced_acceleration` | float | Amount of acceleration |
| `m_advanced_angle` | float | Acceleration angle |
| `m_advanced_offset` | float | Acceleration offset |
| `m_advanced_power` | float (default: 2) | Acceleration curve (2 = linear) |
| `m_advanced_sensitivity_cap` | float | Max sensitivity cap |
| `m_advanced_sensitivity_cap_min` | float | Min sensitivity cap |
| `m_advanced_postscale_x` | float | Post-scale for x-axis |
| `m_advanced_postscale_y` | float | Post-scale for y-axis |
| `m_advanced_input_frequency` | int | Mouse input frequency |

KovaaK's mouse acceleration wizard: http://mouseaccel.blogspot.com/2015/12/reflex-mouse-accel-configuration-wizard.html

## Sound CVARs

| CVAR | Default | Description |
|------|---------|-------------|
| `s_volume` | 0.4 | Master volume |
| `s_effects_volume` | float | Effects volume |
| `s_music_volume` | float | Music volume |
| `s_announcer_volume` | float | Announcer volume |
| `s_rot` | — | Sound rotation |

## Server CVARs

| CVAR | Default | Description |
|------|---------|-------------|
| `sv_hostname <name>` | — | Server name shown in browser |
| `sv_maxclients` | 8 | Max clients |
| `sv_gameport` | 25787 | Server port |
| `sv_password` | — | Server password |
| `sv_refpassword` | — | Referee password |
| `sv_startmap` | — | Map to load on launch |
| `sv_startmode` | — | Mode to start with |
| `sv_startruleset` | — | Ruleset to start with |
| `sv_startmutators` | — | Mutators to start with |
| `sv_startrotation` | — | Starting map rotation |
| `sv_startwmap` | — | Workshop map ID to start on |
| `sv_ruleset` | — | Active ruleset |
| `sv_mode` | — | Active mode |
| `sv_mutators` | — | Active mutators |
| `sv_allowmodes` | — | Whitelist of allowed modes |
| `sv_allowrulesets` | — | Whitelist of allowed rulesets |
| `sv_allowcallvote` | `0\|1` | Allow callvotes |
| `sv_allowcallvotemapmode` | `0\|1` | Allow map/mode callvotes |
| `sv_allowcallvotemutators` | `0\|1` | Allow mutator callvotes |
| `sv_allowedit` | `0\|1` | Allow players to edit maps on server |
| `sv_autorecord` | 1 | Auto-record replays |
| `sv_timelimit` | 600 | Match time limit in seconds |
| `sv_timelimit_round` | 90 | Round time limit (Arena modes) |
| `sv_timelimit_round_override` | int | Override round time limit |
| `sv_country` | — | Server country flag |
| `sv_steam` | `0\|1` | Enable Steam integration |
| `sv_addbot` | — | Add a bot |
| `sv_kickallbots` | — | Remove all bots |
| `sv_matchmaking_game` | — | Matchmaking game token |
| `sv_matchmaking_key` | — | Matchmaking auth key |
| `rcon` | — | Remote console command |
| `rcon_address` | — | rcon server address |
| `rcon_password` | — | rcon password |

## Replay Commands

| Command | Description |
|---------|-------------|
| `play` | Play a replay file |
| `re_speed <#>` | Set replay playback speed (0 = pause) |
| `re_seek_to <time>` | Jump to specific time |
| `re_next_frame` | Advance one frame (bind: `]`) |
| `re_prev_frame` | Back one frame (bind: `[`) |
| `re_next_marker` | Jump to next marker |
| `re_prev_marker` | Jump to previous marker |
| `re_next_keyframe` | Jump to next keyframe |
| `re_prev_keyframe` | Jump to previous keyframe |
| `re_add_keyframe` | Add camera keyframe |
| `re_remove_keyframe` | Delete current keyframe |
| `re_edit_toggle` | Toggle keyframe editor |
| `re_set_position` | Set camera position |
| `re_set_angle` | Set camera angle |
| `re_set_fov` | Set camera FOV |
| `re_set_player_attached_to` | Attach camera to player |
| `re_set_player_looking_towards` | Aim camera toward player |
| `re_set_position_lerp` | Set position interpolation method |
| `re_set_angle_lerp` | Set angle interpolation method |
| `re_set_fov_lerp` | Set FOV interpolation method |
| `re_zero_roll` | Reset camera roll to 0 |
| `re_spline_visible_travel_time` | Show camera path waypoints |
| `re_export` | Dump frames to disk as TGAs |
| `re_export_depth` | Export depth pass |
| `re_export_frame_rate` | Set export framerate |
| `re_save` | Save keyframe/telemetry file |
| `cl_replaymarker` | Add marker to replay (bind: `m`) |
| `profileplay` | Play replay and report average FPS |

## Map Editor Commands

| Command | Description |
|---------|-------------|
| `toggleeditor` | Toggle between game and editor (bind: Mouse3) |
| `editorclone` | Duplicate selected brush (bind: Space) |
| `editordelete` | Delete selected brush (bind: Backspace, Q) |
| `editorundo` | Undo last operation (bind: Z) |
| `editorredo` | Redo operation (bind: X) |
| `editortogglevertexmode` | Toggle vertex mode (bind: V) |
| `editortoggleclipmode` | Clip mode (unimplemented) |
| `me_showproperties 1` | Open properties window for selected item (bind: N) |
| `me_showclip` | `0\|1` — Show/hide clip brushes |
| `me_snapangle <#>` | Rotation snap angle in degrees |
| `me_snapdistance` | Grid snap distance |
| `me_getmaterial` | Get texture from active brush (bind: Mouse5, K) |
| `me_setmaterial` | Apply texture to active brush (bind: Mouse4, M) |
| `me_activealbedo <HEX>` | Set material color |
| `me_activematerial <mat>` | Set active material by path |
| `me_createtype` | Create entity of given type |
| `me_setentityproperty <id> <prop> <val>` | Set entity property |
| `me_createprefab <name>` | Create prefab from selected items (avoid including pickups) |
| `me_breakprefab` | Break prefab into components |
| `me_updateprefab <name>` | Update prefab with selected objects |
| `me_listprefabs` | List prefabs in map |
| `me_purgeprefabs` | Purge unused prefabs |
| `me_destroyprefab` | Destroy prefab |
| `me_volumeselect_apply` | Apply volumeselect brush selection |
| `me_startbridge` | Start bridge tool |
| `me_segments` / `me_segments_inc` / `me_segments_dec` | Segment count |
| `me_rotate_inc` / `me_rotate_dec` | Rotate selected object |
| `me_texcoords_*` | Texture coordinate manipulation (offset, scale, rotation, flip) |
| `savemap` | Quicksave current map (bind: F5) |
| `savemap <name>` | Save map as `<name>.map` |
| `map <name>` | Load `<name>.map` as a server |
| `wmap <id>` | Load workshop map by ID |
| `r_lm_build` | Compile lightmap (bind: F4) |

## UI CVARs

| CVAR | Description |
|------|-------------|
| `ui_list_widgets` | List installed HUD widgets |
| `ui_show_widget <name>` | Show a widget |
| `ui_hide_widget <name>` | Hide a widget |
| `ui_hide_all` | Hide all widgets |
| `ui_reset` | Reset UI to defaults |
| `ui_set_widget_anchor <name> <x> <y>` | Set widget grid anchor |
| `ui_set_widget_offset <name> <x> <y>` | Set widget x/y offset |
| `ui_set_widget_scale <#>` | Set widget scale |
| `ui_set_widget_zindex <#>` | Set widget draw priority |
| `ui_show_axis` | Show widget axis guides |
| `ui_show_mouse_regions` | Show clickable UI regions |
| `ui_viewport_height` | Set viewport height |
| `ui_scoreboard_leaderboard` | Scoreboard leaderboard view |

## In-Game Commands

| Command | Description |
|---------|-------------|
| `callvote map <name>` | Vote to change map |
| `callvote mode <mode>` | Vote to change mode (1v1, ffa, tdm, ctf, 2v2, AFFA, ATDM, A1v1) |
| `callvote restart` | Vote to restart match |
| `callvote ruleset <name>` | Vote to switch ruleset |
| `vote_yes` | Accept vote (bind: F1) |
| `vote_no` | Reject vote (bind: F2) |
| `ready` | Ready up (bind: F3) |
| `notready` | Un-ready |
| `forfeit` | Forfeit current match |
| `connect <ip>` | Direct connect to server |
| `disconnect` | Return to menu (bind: F12) |
| `reconnect` | Reconnect to last server |
| `name <name>` | Change display name |
| `suicide` | Kill yourself (use in Race to reset) |
| `say` | Open chat (bind: T) |
| `sayteam` | Open team chat (bind: Y) |
| `sayparty` | Party chat |
| `roll` | Roll a random number |
| `referee` | Enter referee mode |
| `unreferee` | Exit referee mode |
| `screenshot` | Save screenshot as TGA |
| `screenshotClean` | Screenshot without HUD |
| `screenshotWithDepth` | Screenshot + depth pass |
| `loadconfig <name>` | Load `<name>.cfg` |
| `saveconfig [name]` | Save config (optionally to named file) |
| `reset_vars` | Reset all settings to defaults |
| `keylist` | List all bindable key names |
| `ip` | Show server IP |
| `quit` | Exit the game |

## Weapon Selection

| Command | Weapon |
|---------|--------|
| `weapon 1` | Melee (Axe) |
| `weapon 2` | Burstgun |
| `weapon 3` | Shotgun |
| `weapon 4` | Grenade Launcher |
| `weapon 5` | Plasma Rifle |
| `weapon 6` | Rocket Launcher |
| `weapon 7` | Ion Cannon |
| `weapon 8` | Bolt Rifle |
| `weapon 9` | Stake Launcher (disabled) |
| `weaponnext` | Next available weapon |
| `weaponprev` | Previous available weapon |

## High-Performance Config Block

```
cl_gibs_maxcount 1
cl_gibs_expire_time 1
r_dynamic_shadows 0
r_bloom 0
r_fxaa 0
r_dynamic_lights 0
r_decals 0
```

## Related

- [[games/reflex/getting-started|Getting Started]]
- [[games/reflex/server-hosting|Server Hosting]]
