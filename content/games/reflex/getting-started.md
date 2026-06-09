---
title: Getting Started
game: reflex
layer: canon
type: overview
tags: [reflex, getting-started, setup, hud, rulesets]
confidence: high
sources: [reflex-cr2-ruleset-source, reflex-casual-ruleset-source, reflex-sushi-ruleset-source, reflex-wikipedia-pcgamingwiki, xytaglyph-guide]
promoted: 2026-06-10
canon_attempts: 1
---

# Getting Started

Reflex has three distinct rulesets that change weapon behavior, movement constants, and match settings simultaneously. The same game mode on different rulesets plays differently enough that choosing a ruleset is a prerequisite to finding the right server.

## Finding Games

Matchmaking exists but is not used by the active playerbase. Use the Server Browser in-game and the community Discords.

- Official Discord: discord.gg/reflex (1,574 members)
- Revival community: discord.gg/VnMmsazekU

Primary activity is in Duel. FFA and TDM servers are more active in evenings and on weekends.

## Rulesets

Three rulesets are active:

| Ruleset | Region | Notes |
|---|---|---|
| Competitive | EU dominant | CR2 values. 10-minute duels. |
| Sushi | NA dominant | Higher jump height, higher gravity, lower friction. Tighter weapon trace radii. Authored by Soh. |
| Casual | Mixed | Competitive movement values. 5-minute matches. Item timers visible. |

The Server Browser displays the ruleset for each listed server.

## HUD

GoaHud is the standard community HUD.

Install path: Options > Addons > Explore Workshop > search "GoaHud" > Download > restart the game > Options > Widgets > GoaHud > Quick Enable GoaHud.

## Recommended Settings

| CVAR | Value | Effect |
|---|---|---|
| `r_bloom` | `0` | Disables bloom |
| `cl_predict_items` | `0` | Prevents false item pickups not yet confirmed by server |
| `cl_input_subframe` | `1` | Input polling at 1000 Hz, independent of framerate |

## Jump Binding

Mouse2 (right-click) is the community-standard jump key. Jump queuing is supported: holding jump before landing registers the jump on ground contact.

## Related

- [[rulesets]]
- [[console]]
