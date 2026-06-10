---
title: "Powerups"
game: open-arena
layer: canon
type: reference
tags: [open-arena, powerups, items]
status: canon
promoted: 2026-06-10
---

Powerups last approximately 30 seconds and respawn 2 minutes after pickup. First spawn occurs 30-60 seconds after match start. Dropped on death with remaining duration. Same type can be stacked.

## Powerups

| Item | Effect |
|------|--------|
| Battle Suit | Full protection from drowning, lava, slime, splash damage, and fall damage. Halves normal damage received. |
| Flight | Free flight for 60 seconds. No speed gain from strafe jumping. Jump pads ignored. |
| Haste | +30% movement speed and fire rate. |
| Invisibility | Nearly invisible to enemies. Quad's blue ground light still visible. |
| Quad Damage | Damage multiplied by 3 (default). Multiplier set by `g_quadfactor`. |
| Regeneration | Auto-regenerates health up to 200. |

Quad Damage default multiplier is 3, not 4. The name is carried over from Quake 1/2.

## Holdable Items

Activated with the Use Item key (default: Enter). One at a time. Respawn after 1 minute.

| Item | Effect |
|------|--------|
| Medkit | Restores health to 125. Cannot activate if already at or above 125. |
| Personal Teleporter | Teleports to a random spawn point. Drops any carried flag. |
| Kamikaze | Suicide explosion damaging nearby players. Ignores friendly fire settings. If holder dies without activating, explodes 3 seconds later unless gibbed. |
| Invulnerability | Energy shield for ~10 seconds. Cannot move. Shots reflected. Proximity mines penetrate and kill. |

## Runes

From Quake III Team Arena. Disabled by default. Enable with `g_runes 1`. Held until death. One at a time. Do not spawn in Double Domination.

| Rune | ID | Effect |
|------|----|--------|
| Doubler | D | Doubles all weapon damage, including self-damage. |
| Ammo Regen | A | Auto-regenerates ammo up to weapon cap. Slight fire rate boost. |
| Scout | S | Faster than Haste, faster fire rate. Prevents wearing armor. |
| Guard | G | Grants 200 HP + 200 armor instantly. Auto-regens health to 200. Maintains armor at 200. |

Guard + Medkit: Medkit heals to 225 HP instead of 125.

Scout + Haste: does not stack beyond Scout's speed.

## Related

- [[games/open-arena/health-and-armor\|Health and Armor]]
- [[games/open-arena/gametypes\|Gametypes]]
