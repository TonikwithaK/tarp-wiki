---
title: "CVars: A–C"
game: quake-live
layer: canon
type: reference
tags: [quake-live, console, cvars, reference]
status: canon
promoted: 2026-06-10
source: https://www.euere.eu/ql/
---

# Console Variables: A–C

Full reference sourced from euere.eu/ql/ — 1,079 CVARs documented, updated September 2025.

For the flag legend and CVAR prefix reference, see [[console/appendix|Appendix]].

---

## A

| CVar | Default | Description |
|------|---------|-------------|
| `activeAction` | — | Executed on client's first active frame; used to script timedemo start after loading |
| `appendlogfile` | 0 | Append to log file (0=disabled, 1=enabled) |
| `armor_tiered` | 0 | QW-inspired tiered armor rules (server-side) |

---

## B — Bot Variables

### Core
| CVar | Default | Description |
|------|---------|-------------|
| `bot_enable` [R] | 1 | Enable/disable bots on server/offline match |
| `bot_minplayers` [S] | 0 | Auto-fill disconnected player slots with bots |
| `bot_challenge` | 0 | Makes bots slightly more challenging |
| `bot_dynamicSkill` [A] | 0 | 0=fixed skill, 1=matches "My Skill" setting |
| `bot_startingSkill` [A] | 1 | 1=Easy, 2=Bring It On, 3=Medium, 4=Hardcore, 5=Nightmare |
| `bot_thinktime` [C] | 100 | AI frame interval in ms |

### Behavior
| CVar | Default | Description |
|------|---------|-------------|
| `bot_rocketjump` | 1 | Allow bots to rocket jump |
| `bot_teamkill` | 0 | Bots shoot teammates |
| `bot_followMe` [A] | 0 | Bots follow you in debug mode |
| `bot_followDist` | 250 | Following distance when bot_followMe 1 |
| `bot_training` [A] | 0 | Training mode (like Crash match) |
| `bot_instaGibAimSkill` | 0.4 | Bot aim in instagib (0.0–1.0) |
| `bot_nochat` | 0 | Disable bot chat |
| `bot_gauntlet` [A] | 0 | Force bots to use gauntlet only |

### Pathfinding / AAS
| CVar | Default | Description |
|------|---------|-------------|
| `bot_predictobstacles` | 1 | Enable bot obstacle prediction |
| `bot_aasoptimize` | 0 | Optimize bot AI for specific map |
| `bot_forceclustering` | 0 | Force recalculation of AAS clustering |
| `bot_forcereachability` | 0 | Force recalculation of AAS reachabilities |

---

## C

### Game Rules
| CVar | Default | Description |
|------|---------|-------------|
| `capturelimit` [S,A] | 8 | Captures needed to win CTF |

### Crosshair
| CVar | Default | Description |
|------|---------|-------------|
| `cg_drawCrosshair` [A] | 5 | Crosshair style 0–10 (0=off) |
| `cg_crosshairSize` [A,T] | 32 | Size in pixels |
| `cg_crosshairColor` [A,T] | 7 | Color (1–26, see [[console/appendix|color chart]]) |
| `cg_crosshairBrightness` [A,T] | 1.0 | Brightness (0.0–1.0) |
| `cg_crosshairHealth` [A,T] | 0 | Color crosshair by health (overrides color setting) |
| `cg_crosshairX` [A,T] | 0 | X offset from center (-300 to 300) |
| `cg_crosshairY` [A,T] | 0 | Y offset from center (-220 to 220) |
| `cg_crosshairPulse` [A,T] | 1 | Pulse on item pickup |
| `cg_crosshairHitStyle` [A,T] | 2 | Hit indicator style (0–8) |
| `cg_crosshairHitColor` [A,T] | 1 | Hit indicator color (1–26) |
| `cg_crosshairHitTime` [A,T] | 200 | Duration of hit effect (ms) |
| `cg_drawCrosshairNames` [A] | 1 | 0=off, 1=names, 2=names+teammate health/armor |
| `cg_drawCrosshairNamesOpacity` [A,T] | 0.75 | Opacity of crosshair names (0.0–1.0) |
| `cg_drawCrosshairTeamHealth` [A,T] | 2 | Show teammate health/armor when targeted |

### HUD
| CVar | Default | Description |
|------|---------|-------------|
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
| `cg_fov` [A,T] | 100 | Field of view (10–130) |
| `cg_zoomfov` [A,T] | 22.5 | Zoomed FOV (10–130) |

### Visual / Client Game
| CVar | Default | Description |
|------|---------|-------------|
| `cg_autoswitch` [A] | 1 | Auto-switch to picked-up weapon (0=off recommended) |
| `cg_predictItems` [A] | 1 | Client-side item pickup prediction |
| `cg_simpleItems` [A] | 0 | Simple 2D icons instead of 3D models |
| `cg_gibs` [A] | 1 | Gib effects |
| `cg_blood` [A] | 1 | Blood effects |
| `cg_brassTime` [A] | 2500 | Bullet casings duration (0=off) |
| `cg_noProjectileTrail` [A] | 0 | Disable projectile trails (1=off) |
| `cg_forceModel` [A] | 0 | Force all players to use your model |
| `cg_enemyModel` [A] | — | Model override for enemies |
| `cg_enemyColors` [A] | — | Hex color for enemies |
| `cg_teamModel` [A] | — | Model override for teammates |
| `cg_teamColors` [A] | — | Hex color for teammates |
| `cg_teamChatsOnly` [A] | 0 | Filter chat to team only |

### Client Network
| CVar | Default | Description |
|------|---------|-------------|
| `cl_maxpackets` [A] | 30 | Outgoing packet rate (125 recommended) |
| `cl_timenudge` [A] | 0 | Packet timing offset (-1 to -30 range; negative = earlier) |
| `cl_mouseAccelStyle` [A] | 0 | Acceleration style (0=Quake3, 1=simple) |
| `com_maxfps` [A] | 85 | Max rendered FPS (125 recommended for physics) |
| `com_hunkMegs` [I] | 96 | Memory reserved for gameplay (MB) |
| `com_soundMegs` [I] | 16 | Memory for sounds (MB) |
| `com_allowConsole` | 0 | Allow ~ to open console (set to 1 after first Ctrl+Alt+~ access) |

## Related

- [[console|Console Overview]]: config files, how to access console
- [[console/cvars-d-p|CVars D–P]]: game settings, weapon values, physics
- [[console/cvars-r-t|CVars R–T]]: rendering, sound, server
- [[console/cvars-u-w|CVars U–W]]: UI variables
- [[console/appendix|Appendix]]: flag legend, prefix reference, color chart
