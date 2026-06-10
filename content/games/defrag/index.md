---
title: Defrag
game: defrag
type: index
tags: [defrag, movement, speedrun, vq3, cpm, quake3]
status: canon
created: 2026-06-10
updated: 2026-06-10
---

DeFRaG is a movement-focused mod for Quake 3 Arena. Players complete movement courses -- reaching a finish trigger from a start trigger in the shortest possible time. Maps range from straightforward strafe-jump tracks to complex multi-path routes requiring precise technique.

The mod runs both VQ3 and CPM physics. Every map has separate leaderboards for each physics mode.

The community hub is [defrag.racing](https://defrag.racing): 15,400 maps, 653,100 records, active servers, a launcher, and a 73-page wiki covering physics, techniques, CVARs, mapping, and history. The [forum archive](https://defrag.racing/forum-archive) preserves 275 topics and 1,364 posts from the defunct q3df.org phpBB forum.

For detailed documentation, defrag.racing is the authoritative source. This page covers what Defrag is and how it relates to the broader Q3 ecosystem.

## Physics Modes

DeFRaG uses the same two physics modes as CPMA:

- **VQ3**: Vanilla Q3 physics. Strafe-jumping with near-zero air control. The per-axis speed check exploit is the primary movement technique.
- **CPM**: Challenge ProMode physics. Full air control. Higher acceleration. Bunny hopping, double jumping, enhanced ramp jumping.

VQ3 and CPM require different techniques and produce different optimal routes on the same map. Most competitive records are contested in both modes independently.

## Game Modes

| Mode | Description |
|---|---|
| Run | Race from start to finish trigger. Linear maps. Primary competitive mode. |
| Accuracy | Hit Railgun targets while moving. |
| Tricks / Freestyle | Creativity-judged trick execution. No fixed goal. |
| Fast Capture | CTF flag carrier time. Tests movement on standard Q3 CTF maps. |
| Training | Technique-focused courses with incremental difficulty sections. |

## Physics Framerate

Server-side physics run at 125fps in DeFRaG. This is significant: certain techniques (overbounces, specific jump heights) are frame-dependent. Running the client at 125fps aligns client and server frames, which affects timing.

## Engines

DeFRaG runs on ioquake3 and Quake3e. The defrag.racing launcher bundles everything needed. See [defrag.racing/wiki/engines](https://defrag.racing/wiki/engines) for a full breakdown of client options and their differences.

## Documentation

Full technique documentation, CVAR reference, HUD tools, mapping guides, and history are at [defrag.racing/wiki](https://defrag.racing/wiki). Key pages:

- [Physics](https://defrag.racing/wiki/physics) -- VQ3 vs CPM, strafe math, jump heights
- [Strafe Mechanics](https://defrag.racing/wiki/strafe-mechanics) -- the deep dive
- [Weapon Jumps](https://defrag.racing/wiki/weapon-jumps) -- rocket, plasma, grenade jump reference
- [Techniques](https://defrag.racing/wiki/techniques) -- groundboosting, overbounce, wallbugs
- [Console Commands](https://defrag.racing/wiki/console-commands) -- full CVAR reference

## Related

- [[games/quake-3/index|Quake III Arena]]
- [[games/quake-3/movement|Q3 Movement]]
- [[games/cpma/index|CPMA]]
