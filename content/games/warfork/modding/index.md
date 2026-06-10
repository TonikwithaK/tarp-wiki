---
title: "Modding"
game: warfork
layer: canon
type: reference
tags: [warfork, modding]
status: canon
promoted: 2026-06-09
---

Warfork is built on QFusion, a Quake engine fork. Most gameplay logic is exposed to AngelScript: a statically-typed scripting language that handles gametypes, item definitions, bot AI, and match state. The shader system and HUD system are also scriptable without recompiling the engine.

Source repository: [TeamForbiddenLLC/warfork-qfusion](https://github.com/TeamForbiddenLLC/warfork-qfusion)

Gametypes: [assets/data0_21pure/progs/gametypes/](https://github.com/TeamForbiddenLLC/warfork-qfusion/tree/master/assets/data0_21pure/progs/gametypes)
HUDs: [assets/data0_21/huds/](https://github.com/TeamForbiddenLLC/warfork-qfusion/tree/master/assets/data0_21/huds)

## Sections

- [[games/warfork/modding/server-hosting|Server Hosting]]: running a dedicated server, port forwarding, cvars, RCON
- [[games/warfork/modding/custom-gametypes|Custom Gametypes]]: writing and installing AngelScript gametypes
- [[games/warfork/modding/custom-huds|Custom Huds]]: the `.hud` scripting format, available variables, the four default HUDs
- [[games/warfork/modding/custom-shaders|Custom Shaders]]: the shader script format for textures and visual effects
- [[games/warfork/modding/gametype-scripting-reference|Gametype Scripting Reference]]: AngelScript API types: Vec3, Trace, Match, Gametype, Team
