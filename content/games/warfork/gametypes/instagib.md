---
title: "Instagib"
game: warfork
layer: canon
type: mechanic
tags: [warfork, instagib, game-mode, instagun]
status: canon
promoted: 2026-06-09
---

# Instagib

Instagib is a modifier, not a standalone gametype. It is enabled via the server cvar `g_instagib 1` and requires a restart. It can be applied to FFA, TDM, CTF, CA, and Duel.

## Effect

When active, all weapons are replaced with the Instagun. All players have infinite ammo.

## Instagun Stats

| Parameter | Value |
|---|---|
| Damage | 200 |
| Cooldown | 1300ms |
| Travel | instant |
| Splash radius | 80 units |
| Self-damage | 0.1 |
| Knockback | 95 |

One hit kills any player at full health.

## Optional Sub-modifiers

| Modifier | Cvar | Effect |
|---|---|---|
| Instashield | `g_instashield 1` | Temporary invulnerability |
| Instajump | `g_instajump 1` | Enhanced jump height and speed |

Both can be enabled via server callvote or cvar.

## Related

- [[games/warfork/weapons/instagun|Instagun]]
- [[games/warfork/movement|Movement]]
- [[games/warfork/weapons/index|Index]]
