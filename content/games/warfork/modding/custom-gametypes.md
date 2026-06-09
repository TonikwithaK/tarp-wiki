---
title: "Custom Gametypes"
game: warfork
layer: canon
type: reference
tags: [warfork, modding, angelscript, gametypes]
status: canon
promoted: 2026-06-09
---

Warfork gametypes are written in AngelScript. They live in:

```
[assets/data0_21pure/progs/gametypes/](https://github.com/TeamForbiddenLLC/warfork-qfusion/tree/master/assets/data0_21pure/progs/gametypes)
```

## File Structure

Each gametype uses three files:

| File | Purpose |
|---|---|
| `<name>.as` | Main script |
| `<name>.gt` | Includes list: which `.as` files to load |
| `<name>.gtd` | Gametype descriptor: title, author, version |

### Example: ca.gt

```
/shared/constants.as;
/shared/utils.as;
/shared/files.as;
generic/quickmenu.as;
generic/matchstates.as;
generic/bots.as;
generic/awards.as;
ca.as;
legacy/quake1.as;
```

Files are loaded in order. Shared utilities in `/shared/` and `generic/` are available to all gametypes.

## Required Callback Functions

Every gametype must implement these functions. The engine calls them at defined points in the match lifecycle.

| Function | When called |
|---|---|
| `GT_InitGametype()` | Before any entity spawns. Set gametype properties, register commands, write default config. |
| `GT_SpawnGametype()` | After map entities spawn. |
| `GT_MatchStateStarted()` | On match state transition: warmup, countdown, playtime, postmatch. |
| `GT_MatchStateFinished(int incomingState)` | Return `true` to allow the state transition to proceed. |
| `GT_ThinkRules()` | Every frame. Check win conditions, manage timers. |
| `GT_PlayerRespawn(Entity @ent, int old_team, int new_team)` | Give inventory at spawn. |
| `GT_SelectSpawnPoint(Entity @self)` | Return the spawn entity to use. |
| `GT_ScoreEvent(Client @client, const String &event, const String &args)` | Handle scoring events: kills, damage, awards. |
| `GT_ScoreboardMessage(uint maxlen)` | Build and return the scoreboard string. |
| `GT_UpdateBotStatus(Entity @ent)` | Set bot goal weights and AI state. |
| `GT_Command(Client @client, const String &cmd, const String &args, int argc)` | Handle custom client commands. |
| `GT_Shutdown()` | Cleanup on map change or restart. |

## Gametype Properties

Set these in `GT_InitGametype()` via the `gametype` global object.

| Property | Type | Description |
|---|---|---|
| `gametype.title` | string | Display name in server browser |
| `gametype.isTeamBased` | bool | Enable team logic |
| `gametype.isRace` | bool | Enable race mode behavior |
| `gametype.hasChallengersQueue` | bool | Queue system for pickup-style play |
| `gametype.spawnableItemsMask` | int | Bitmask of item types that spawn on map |
| `gametype.infiniteAmmo` | bool | Disable ammo consumption |
| `gametype.canForceModels` | bool | Allow model forcing for fullbright visibility |
| `gametype.shootingDisabled` | bool | Disable all weapon fire |
| `gametype.mmCompatible` | bool | Eligible for matchmaking |

## Inventory Setup (GT_PlayerRespawn)

CA-style spawn with weapons from a cvar list:

```angelscript
// Clear existing inventory
ent.client.inventoryClear();

// Give each weapon from the cvar string
String itemList = g_noclass_inventory.string; // "gb mg rg gl rl pg lg eb ..."
for( int i = 0; i < itemList.numTokens(); i++ )
{
    Item @item = @G_GetItemByName( itemList.getToken( i ) );
    if( @item != null )
        ent.client.inventoryGiveItem( item.tag );
}

// Set ammo counts from cvar
// g_class_strong_ammo: "1 75 20 20 40 125 180 15" (GB MG RG GL RL PG LG EB)
String ammoCounts = g_class_strong_ammo.string;
// ... iterate and call inventorySetCount per weapon ammo item

// Give armor
ent.client.armor = 150;

// Default weapon selection
ent.client.selectWeapon( WEAP_ROCKETLAUNCHER );
```

## Spawning System

Control when players respawn after death or round start.

| Constant | Behavior |
|---|---|
| `SPAWNSYSTEM_INSTANT` | Spawn immediately on death |
| `SPAWNSYSTEM_HOLD` | Hold in ghost state until round begins |

Set per team in `GT_InitGametype()`:

```angelscript
gametype.setTeamSpawnsystem( TEAM_ALPHA, SPAWNSYSTEM_HOLD, 0, 0, true );
gametype.setTeamSpawnsystem( TEAM_BETA,  SPAWNSYSTEM_HOLD, 0, 0, true );
```

## Installing a Custom Gametype

1. Place `mygametype.as`, `mygametype.gt`, and `mygametype.gtd` in `basewf/progs/gametypes/`
2. Set `g_gametype mygametype` on the server
3. Restart the map: `map <mapname>`

The engine compiles the AngelScript on load. Compile errors appear in the server console.

## See Also

- [[gametype-scripting-reference]]: full AngelScript API: Vec3, Trace, Match, Gametype, Team, Entity, Client
- [[server-hosting]]: running a server and setting cvars
