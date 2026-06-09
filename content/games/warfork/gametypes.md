---
title: "Gametypes"
game: warfork
layer: canon
type: reference
tags: [warfork, gametypes, game-modes]
status: canon
promoted: 2026-06-09
---

# Gametypes

Warfork ships with 13 default gametypes covering competitive 1v1, team play, objective modes, and movement-focused formats. Custom gametypes can be written in AngelScript, which gives server operators and community developers the ability to extend or entirely replace the default ruleset.

Each mode has its own strategic demands. Knowing which gametype you're playing — and what it rewards — is the first step toward playing it well.

---

## Standard Gametypes

### [[duel]]
1v1. Win by reaching the frag limit or having the highest score when time expires. Players start with a basic loadout and acquire the full weapon set through map pickups. Item timing — tracking when Mega Health and armor respawn — is the defining skill at high levels. The most demanding test of individual mechanics in Warfork.

### [[clan-arena]]
Team elimination. The last team with players alive wins the round. Everyone spawns with a full loadout and abundant ammo; there are no items to scavenge mid-round. Self-damage from explosives is disabled. Rounds are short, coordination is mandatory, and movement knowledge determines which routes and angles are viable. The standard competitive format is 3v3.

### [[deathmatch]]
Free-for-all frag race. Every player is an opponent. First to the frag limit, or highest score at time expiry, wins. Continuous respawning keeps the pace high. The most accessible entry point into Warfork — lower barrier than Duel, less coordination overhead than team modes.

### [[team-deathmatch]]
Two teams race to accumulate frags. Every kill by any team member scores for that team. Respawning is continuous. Distinct from Clan Arena in that survival is not the objective — consistent fragging is. Controlling weapon and armor spawns gives a team a sustained output advantage.

### [[capture-the-flag]]
Teams must steal the enemy flag and return it to their own base while defending theirs. Requires split roles — offense, defense, and flag carrier support. Movement speed and routing knowledge are critical for both carrying and intercepting.

### [[bomb-and-defuse]]
Attackers plant a bomb at a designated site; defenders must defuse it before it detonates, or eliminate the attackers before the plant. Round-based, no respawning mid-round. Roles and map positioning are everything.

### [[race]]
Pure movement. No combat. Players run a map course and the fastest completion time wins. Race maps are built to test strafe-jumping, wall-jumping, and route optimization. If you want to develop movement fundamentals without combat pressure, Race is the place to do it.

### [[headhunt]]
One player is the designated target — the head. All others hunt them. The target scores points for surviving; the hunter who lands the kill becomes the new target. Free-for-all structure with no permanent teams. Being the head is high pressure. Hunting is competitive — other hunters are rivals as much as allies.

---

## Modifiers

### [[instagib]]
Instagib is not a standalone gametype but a modifier applicable to multiple modes. All players wield an instagun that kills in one hit, with infinite ammo. No other weapons. No armor. Every engagement is decided instantly, which makes movement and positioning the only variables. Can be layered onto Deathmatch, Duel, Clan Arena, and others.

---

## Community and Variant Gametypes

### Duel Arena
A queue-based variant of Duel. Players spawn with all weapons rather than acquiring them via pickups. The winner stays on, the next challenger enters, and the first player to reach 11 frags wins the match. Server-run, casual structure — good for high-volume practice against varied opponents.

### [[exhaustion-gametype]]
A community-created team elimination variant. Like Clan Arena in structure, but with an escalating respawn penalty — players who die face increasing delays before they can re-enter, raising the cost of dying as the round progresses. Not a default Warfork gametype; requires a custom server configuration.

---

## Extending Gametypes

Warfork's gametype system is scriptable via AngelScript. Server operators can modify spawn rules, scoring logic, item behavior, and win conditions without touching engine code. The default gametypes themselves are implemented in script and can serve as a reference for custom work.
