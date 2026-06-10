---
title: "Gameplay"
game: xonotic
layer: canon
type: mechanic
tags:
- gameplay
- xonotic
- health
- armor
- sound
- console
- competitive-settings
status: canon
promoted: 2026-06-10
---

# Gameplay

General mechanics and competitive practice for vanilla Xonotic.

Source: Halogene's Newbie Corner (https://xonotic.org/guide/)

## Health and Armor

Starting health is 100. An experienced player can kill in 2 shots via a weapon combo.

Mega Armor and Mega Health each grant +100 of their respective stat. Both respawn 30 seconds after pickup.

Above 100: health and armor both rot back down to 100 over time. The further above 100, the faster the rot.

Below 100 health: health auto-regenerates after a short delay since last damage. The lower the health, the faster the regen. Armor does not regenerate.

Pick up health and armor whenever the path doesn't put you in a worse position. Megas in particular are worth routing around.

## Sound Awareness

Each pickup size has a distinct audio cue audible at distance — more reliable than footsteps for tracking opponents across the map. Knowing pickup locations and recognizing their sounds tells you where players are before you see them.

Hit sounds change when a player's health is critically low. The low-health groan tells you a follow-up with a fast spread weapon (Shotgun, MachineGun) or fast splash (Crylink) will finish them. Important in duel.

## Splash Damage Through Walls

All splash weapons — Mortar, Devastator, Electro combo — deal damage through thin walls and ceilings. The hit indicator beep confirms a hit. The opponent cannot retaliate simultaneously, making this a safe damage option when you know their position.

## Console

Open with Shift+ESC. Tab completes commands; partial matches show all completions along with current value, default value, and description.

`search <term>` lists all commands with that text in the name or description.

Vote commands: `vhelp` lists allowed votes on the current server. `vcall <vote>` calls a vote (e.g., `vcall endmatch`).

## Competitive Settings

Settings used to reduce visual noise and improve readability. Commands via in-game console.

```
hud_damage_blur 0               ; disable damage blur on hit
hud_damage 0.4                  ; reduce damage flash intensity
fov 120                         ; field of view (default 90)

playermodel "models/player/megaerebus.iqm"  ; fullbright player model
cl_forceplayermodels 1          ; force your model on all players
cl_forceplayercolors 1          ; force your color on all players

cl_gentle_gibs 1                ; disable gibs (requires reconnect)
cl_particles_alpha 0.2          ; reduce explosion particle opacity
cl_particles_sparks 0
cl_particles_blood 0
r_coronas 0
r_bloom 0

gl_picmip_world 10              ; degrade world textures (requires vid_restart)
gl_texturecompression 1
cl_simple_items 1               ; 2D sprites for pickups (server must allow)

r_drawviewmodel 0               ; hide first-person weapon model
cl_reticle 0                    ; disable zoom overlay mask
cl_zoomspeed -1                 ; instant zoom transition
cl_unpress_zoom_on_weapon_switch 0  ; keep zoom through weapon switches

cl_bobfall 0
cl_bobmodel 0
cl_bobup 0

cl_deathscoreboard 0            ; watch action instead of scoreboard when dead
```

Fullbright model note: the Mega Erebus model was removed from the model selection menu in 0.8.2 but is still available via console. Setting `cl_forceplayermodels 1` makes all other players appear as your chosen model.

## Related

- [[games/xonotic/index|Xonotic]]: overview
- [[games/xonotic/movement|Movement]]: bunny hopping, Blaster jumping, ramp jumping
- [[games/xonotic/weapons|Weapons]]: weapon details and comboing
