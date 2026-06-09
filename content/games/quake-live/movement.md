---
title: "Movement"
game: quake-live
layer: canon
type: mechanic
tags: [quake-live, movement, strafe-jump, rocket-jump, circle-jump, plasma-climb]
status: canon
promoted: 2026-06-09
---

## Base Speeds

| State | Speed |
|---|---|
| Walk | 161 UPS |
| Run | 320 UPS |
| AutoHop (hold jump + forward) | up to 640 UPS |
| Strafe jumping | up to 640 UPS in ~3 hops |

UPS = units per second.

---

## Physics Modes

Physics are server-determined.

**VQL (Vanilla Quake Live):** Default physics. Strafe jumping is the primary speed technique. Air control is limited.

**PQL (Pro mode, CPM-like physics):** Heavy air control. Pressing a movement key while airborne steers toward the look direction. To maintain speed while turning, hold forward only. To make tight corners or accelerate rapidly, hold only left or right while turning.

---

## Strafe Jumping (VQL)

- Jump while holding forward and either left or right.
- Guide the mouse in the same direction as the strafe key.
- Press jump just before landing.
- 640 UPS is reachable in approximately 3 hops.
- Combining with a circle jump at the start increases initial speed.

---

## Circle Jumping

- A fast mouse flick at the moment of the initial jump.
- Gains extra initial speed before a strafe jump sequence.
- Considered the hardest fundamental technique to execute consistently.

---

## Rocket Jumping

- Requires sufficient HP or armor to survive the self-damage.
- Minimum: approximately 35 HP with armor, or over 50 HP without.
- Look down or diagonally behind. Press jump, then fire within the same frame.
- Standard binding: jump to mouse2, fire to mouse1.
- Set `cl_packetdup 0` to prevent double-jump bugs.
- Costs health and armor but provides significant speed and height gain.

---

## Plasma Climbing

- Position against a wall, looking diagonally down at the floor-wall junction.
- Jump while holding forward, hold fire.
- In VQL: release jump after launching (critical). On some server configurations, holding is acceptable.
- Allows climbing vertical surfaces.

---

## Teleport Jumping

- Press jump while inside a teleporter to exit faster and travel extra distance.
- With `cg_autohop 1` active: hold the jump key.

---

## AutoHop

- Cvar: `cg_autohop 1`
- Holding the jump key automatically re-jumps on landing.
- Sustained speed up to 640 UPS.

---

## Speed Reference

Strafe jumping reaches ~2x normal run speed. At 320 UPS base run, sustained strafe jumping reaches 640 UPS in approximately 3 hops. This is fast enough that strafe jumping is effectively required to compete at any level — not just for advanced play.

---

## History

Strafe jumping and bunny hopping were not designed mechanics. They emerged as physics exploits from the id Tech 3 engine in Quake III Arena. John Carmack attempted to patch them out during Q3A development but was unsuccessful. They were preserved in Quake Live and later formalized through the VQL/PQL physics system, which treats them as core movement rather than exploits.

---

## Removed Mechanics

OverBounce (a Quake 3 physics exploit that preserved vertical velocity through specific landing angles) was removed from Quake Live.

---

## Related

- [Getting Started](../getting-started)
- [Weapons](../weapons/index)
