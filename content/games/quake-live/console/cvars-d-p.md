---
title: "CVars: D–P"
game: quake-live
layer: canon
type: reference
tags: [quake-live, console, cvars, reference, weapons, physics]
status: canon
promoted: 2026-06-10
source: https://www.euere.eu/ql/
---

# Console Variables: D–P

Full reference sourced from euere.eu/ql/ — updated September 2025.

---

## D

| CVar | Default | Description |
|------|---------|-------------|
| `dedicated` [L] | 0 | 0=Listen server, 1=Dedicated server |
| `developer` | 0 | Developer mode |
| `dmflags` [S,A] | 0 | Deathmatch flags: 4=no self splash on HP, 8=no self splash on armor, 16=no fall damage |

---

## F

| CVar | Default | Description |
|------|---------|-------------|
| `fraglimit` [S,A] | 30 | Frag limit (0=none) |
| `fs_homepath` [I] | — | Write access path; location for custom mods/content |

---

## G — Game Settings

### Gametype
| CVar | Default | Description |
|------|---------|-------------|
| `g_gametype` [S,L] | 0 | 0=FFA, 1=Tournament (Duel), 2=Race, 3=TDM, 4=Clan Arena, 5=CTF, 6=One-Flag CTF, 7=Overload, 8=Harvester, 9=Freeze Tag |
| `g_compmode` [S,I] | 0 | Competition mode |
| `g_training` | 0 | Training mode (skill placement match) |
| `g_quadHog` | 0 | Score only while holding Quad |

### Voting
| CVar | Default | Description |
|------|---------|-------------|
| `g_allowVote` [A] | 1 | Enable voting |
| `g_allowSpecVote` | 0 | Allow spectators to vote |
| `g_allowVoteMidGame` | 0 | Allow voting during match |
| `g_voteFlags` [S,A] | 0 | Bitmask of disabled vote commands: &1=map, &2=map_restart, &4=nextmap, &8=gametype, &16=kick, &64=timelimit, &128=fraglimit, &256=shuffle, &512=teamsize, &1024=cointoss, &2048=ruleset |

### Weapon Damage
| Weapon | Direct Damage | Splash Damage | Splash Radius |
|--------|--------------|---------------|---------------|
| BFG | 100 | 100 | 80 |
| Chaingun | 8/bullet | — | — |
| Gauntlet | 50 | — | — |
| Grenade Launcher | 100 | 100 | 150 |
| Lightning Gun | 7/tick | — | — |
| Machinegun | 5 (4 in TDM) | — | — |
| Nailgun | 12/nail | — | — |
| Plasmagun | 20/cell | 15 | 20 |
| Railgun | 80 | — | — |
| Rocket Launcher | 100 | 84 | 120 |
| Shotgun | 5/pellet (4 in TDM) | — | — |
| Prox Mine | 0 direct | 100 | 150 |

### Knockback
| CVar | Default | Description |
|------|---------|-------------|
| `g_knockback` | 1000 | General knockback base |
| `g_knockback_lg` | 1.50 | Lightning gun (highest) |
| `g_knockback_gl` | 1.10 | Grenades |
| `g_knockback_pg` | 1.10 | Plasma |
| `g_knockback_pg_self` | 1.30 | Plasma self-splash |
| `g_knockback_rl` | 0.90 | Rockets |
| `g_knockback_rg` | 0.85 | Railgun (lowest) |
| `g_knockback_z` | 24 | Vertical knockback offset (units) |
| `g_max_knockback` | 120 | Maximum knockback cap |

### Projectile Velocity
| CVar | Default (units/sec) |
|------|---------------------|
| `g_velocity_pg` | 2000 |
| `g_velocity_rl` | 1000 |
| `g_velocity_bfg` | 1800 |
| `g_velocity_gl` | 700 |

### Starting Weapons (Bitmask)
```
g_startingWeapons
  &1    = Gauntlet
  &2    = Machinegun
  &4    = Shotgun
  &8    = Grenade Launcher
  &16   = Rocket Launcher
  &32   = Lightning Gun
  &64   = Railgun
  &128  = Plasmagun
  &256  = BFG
  &512  = Grappling Hook
  &1024 = Nailgun
  &2048 = Prox Launcher
  &4096 = Chaingun
  &8192 = Map Default Weapons

  Default (Gauntlet + MG) = 3
  All weapons             = 8191
  Standard CA loadout     = 255
```

### Spawn Settings
| CVar | Default | Description |
|------|---------|-------------|
| `g_startingHealth` | 100 | Spawn health |
| `g_startingArmor` | 0 | Spawn armor |
| `g_startingHealthBonus` | 25 | Bonus health on spawn |
| `g_startingammo_mg` | 100 | MG ammo on spawn |
| `g_ca_startingHealth` | 200 | Clan Arena spawn health |
| `g_enableMachinegun` | 1 | Spawn with MG |

### Match Settings
| CVar | Default | Description |
|------|---------|-------------|
| `g_timelimit` [S,A] | 0 | Time limit in minutes (0=none) |
| `g_friendlyFire` [S,A] | 0 | Friendly fire |
| `g_allowKill` [A] | 1 | Allow kill command |
| `g_inactivity` | 0 | Kick inactive players after N seconds (0=disabled) |
| `g_warmup` | 20 | Warmup time (seconds) |
| `g_overtime` | 0 | Enable overtime |
| `g_doWarmup` | 0 | Enable warmup period |

### Teams
| CVar | Default | Description |
|------|---------|-------------|
| `g_teamForceBalance` | 0 | Force balanced teams |
| `g_teamAutoJoin` | 0 | Auto-assign team on connect |
| `g_redTeam` | Pagans | Red team name |
| `g_blueTeam` | Stroggs | Blue team name |

### Item Settings
| CVar | Default | Description |
|------|---------|-------------|
| `g_quadfactor` | 3 | Quad damage multiplier |
| `g_weaponRespawn` | 5 | Weapon respawn time (seconds) |
| `g_weaponTeamRespawn` | 30 | Team game weapon respawn |
| `g_healthRegenTime` | 0 | Health regen time (CA) |
| `g_armorRegenTime` | 0 | Armor regen time (CA) |

---

## N — Network

| CVar | Default | Description |
|------|---------|-------------|
| `net_port` [I] | 27960 | Network port |
| `net_ip` [I] | — | IP address to bind server to |
| `nextmap` | — | Map to load after current map ends |

---

## P — Physics

| CVar | Default | Description |
|------|---------|-------------|
| `pmove_fixed` | 0 | Fixed physics timestep (1=required for consistent physics/bunnyhopping) |
| `pmove_msec` | 8 | Physics timestep in ms (8=125Hz physics, recommended) |
| `pmove_float` | 0 | Floating point movement (1=smoother on high FPS) |
| `pm_bunnyhopping` | 1 | Enable bunny hopping |
| `pm_airstrafejump` | 1 | Enable air-strafing during jumps |
| `pm_maxStepSize` | 18 | Maximum step height |
| `pm_fallheight_damage` | 74 | Fall damage threshold (units/sec) |

## Related

- [[console|Console Overview]]
- [[console/cvars-a-c|CVars A–C]]: bots, crosshair, HUD, client settings
- [[console/cvars-r-t|CVars R–T]]: rendering, sound, server settings
- [[console/cvars-u-w|CVars U–W]]: UI variables
- [[console/appendix|Appendix]]: flag legend, color chart
