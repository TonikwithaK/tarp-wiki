---
title: "Gametype Scripting Reference"
game: warfork
layer: canon
type: reference
tags: [warfork, modding, angelscript, api, scripting]
status: canon
source: source/gameshared/gs_pmove.c, assets/data0_21pure/progs/gametypes/
promoted: 2026-06-09
---

# Gametype Scripting Reference

AngelScript API reference for Warfork gametype development. All types and functions are available in gametype scripts unless noted.

## Core Types

### Vec3
3D vector used for positions, directions, and velocities.

```angelscript
Vec3 v(x, y, z);
float v.x, v.y, v.z;
float v.length();
float v.distance(Vec3 other);
Vec3 v.normalized();
// Operators: +, -, *, /, dot product
```

### String
```angelscript
String s = "text";
int s.len();
String s.getToken(int index);  // splits on whitespace, returns nth token
int s.toInt();
float s.toFloat();
bool s.empty();
```

### Array / Dictionary
```angelscript
array<int> arr(maxClients);
arr[i] = value;
arr.size();
dictionary<String, int> dict;
dict.set("key", value);
dict.get("key", value);
```

---

## Game Entity Types

### Entity
```angelscript
Entity @ent;
int ent.team;           // TEAM_ALPHA, TEAM_BETA, TEAM_PLAYERS, TEAM_SPECTATOR
Vec3 ent.origin;
float ent.health;
int ent.solid;          // SOLID_NOT, SOLID_TRIGGER, SOLID_BBOX, etc.
int ent.svflags;        // SVF_FORCETEAM, SVF_NOCLIENT, etc.
bool ent.isGhosting();  // true if player is dead/spectating
int ent.playerNum;
Client @ent.client;     // null for non-player entities
void ent.client.respawn(bool ghost);
void ent.respawnEffect(); // teleport visual
```

### Client
```angelscript
Client @client;
String client.name;
String client.clanName;
int client.ping;
float client.armor;
int client.playerNum;
bool client.isReady();
Bot @client.getBot();   // null if not a bot
Entity @client.getEnt();

// Inventory
void client.inventoryClear();
void client.inventoryGiveItem(int itemTag);
void client.inventorySetCount(int ammoTag, int count);
void client.selectWeapon(int weapTag);  // -1 = auto-select best
int client.pendingWeapon;

// Stats
client.stats.score;
client.stats.frags;
client.stats.totalDamageGiven;
void client.stats.clear();
void client.stats.addScore(int n);
void client.stats.addRound();

// Awards
void client.addAward(String text);

// HUD
void client.setHUDStat(int stat, int value);
```

### Team
```angelscript
Team @team = @G_GetTeam(TEAM_ALPHA);
bool team.lock();
void team.stats.clear();
team.stats.score;
team.ping;
Entity @team.ent(int index);  // iterate: for(j=0; @team.ent(j) != null; j++)
```

---

## Match Object

```angelscript
int match.getState();
// States: MATCH_STATE_WARMUP, MATCH_STATE_COUNTDOWN, MATCH_STATE_PLAYTIME, MATCH_STATE_POSTMATCH

void match.launchState(int newState);
bool match.scoreLimitHit();
bool match.timeLimitHit();
bool match.suddenDeathFinished();
void match.startAutorecord();
void match.stopAutorecord();
void match.setClockOverride(uint milliseconds);
```

---

## Gametype Object

```angelscript
gametype.title = "My Gametype";
gametype.version = "1.0";
gametype.author = "Name";
gametype.name;          // short name used in config paths

gametype.isTeamBased = true;
gametype.isRace = false;
gametype.hasChallengersQueue = false;
gametype.isInstagib;    // read-only, set by g_instagib cvar

gametype.shootingDisabled = false;
gametype.readyAnnouncementEnabled = true;
gametype.scoreAnnouncementEnabled = true;
gametype.countdownEnabled = true;
gametype.infiniteAmmo = false;
gametype.canForceModels = true;
gametype.removeInactivePlayers = true;
gametype.mmCompatible = false;

gametype.spawnableItemsMask = 0;    // IT_WEAPON, IT_AMMO, IT_ARMOR, IT_HEALTH, etc.
gametype.respawnableItemsMask = 0;
gametype.dropableItemsMask = 0;
gametype.pickableItemsMask = 0;

gametype.ammoRespawn = 20;
gametype.armorRespawn = 25;
gametype.weaponRespawn = 15;
gametype.healthRespawn = 25;
gametype.powerupRespawn = 90;
gametype.megahealthRespawn = 20;
gametype.ultrahealthRespawn = 60;

gametype.spawnpointRadius = 256;

void gametype.setTeamSpawnsystem(int team, int type, int delay, int maxCount, bool deadcam);
// Types: SPAWNSYSTEM_INSTANT, SPAWNSYSTEM_HOLD, SPAWNSYSTEM_WAVE, SPAWNSYSTEM_TEAMWAVE

bool G_FileExists(String path);
void G_WriteFile(String path, String content);
void G_CmdExecute(String cmd);
void G_RegisterCommand(String cmd);
```

---

## Global Functions

```angelscript
// Entities
Entity @G_GetEntity(int entNum);
Client @G_GetClient(int playerNum);
Team @G_GetTeam(int teamNum);
array<Entity @> @G_FindByClassname(String classname);
Item @G_GetItemByName(String name);

// Messages
void G_PrintMsg(Entity @ent, String msg);   // null = all players
void G_CenterPrintMsg(Entity @ent, String msg);
void G_AnnouncerSound(Entity @ent, int soundIndex, int team, bool queued, Entity @except);
int G_SoundIndex(String path);

// World
void G_RemoveDeadBodies();
void G_RemoveAllProjectiles();
void G_ConfigString(int index, String value);

// Spawns
Entity @GENERIC_SelectBestRandomSpawnPoint(Entity @self, String className);

// Utilities
float random();     // 0.0 to 1.0
int rand();         // integer random
float rint(float);  // round to nearest int
uint levelTime;     // current level time in ms
int maxClients;     // max client slots
```

---

## Constants

```angelscript
// Teams
TEAM_SPECTATOR, TEAM_PLAYERS, TEAM_ALPHA, TEAM_BETA
GS_MAX_TEAMS  // total team count

// Weapons (WEAP_*)
WEAP_NONE, WEAP_GUNBLADE, WEAP_MACHINEGUN, WEAP_RIOTGUN,
WEAP_GRENADELAUNCHER, WEAP_ROCKETLAUNCHER, WEAP_PLASMAGUN,
WEAP_LASERGUN, WEAP_ELECTROBOLT, WEAP_INSTAGUN

// Ammo (AMMO_*)
AMMO_GUNBLADE, AMMO_BULLETS, AMMO_SHELLS, AMMO_GRENADES,
AMMO_ROCKETS, AMMO_PLASMA, AMMO_LASERS, AMMO_BOLTS, AMMO_INSTAS
// AMMO_WEAK_* variants exist for each

// Item types (IT_*)
IT_WEAPON, IT_AMMO, IT_ARMOR, IT_HEALTH, IT_POWERUP

// Match states
MATCH_STATE_WARMUP, MATCH_STATE_COUNTDOWN,
MATCH_STATE_PLAYTIME, MATCH_STATE_POSTMATCH

// Spawnsystems
SPAWNSYSTEM_INSTANT, SPAWNSYSTEM_HOLD,
SPAWNSYSTEM_WAVE, SPAWNSYSTEM_TEAMWAVE

// HUD stats (STAT_*)
STAT_MESSAGE_ALPHA, STAT_MESSAGE_BETA, STAT_IMAGE_BETA
CS_GENERAL  // config string index for custom HUD data
```

## Related

- [[custom-gametypes]] — how to structure a gametype, file layout, mandatory callbacks
- [[server-hosting]] — deploying and configuring a server
