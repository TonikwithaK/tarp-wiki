---
title: "Custom Shaders"
game: warfork
layer: canon
type: reference
tags: [warfork, modding, shaders, graphics]
status: canon
promoted: 2026-06-09
---

Warfork uses a Q3-derived shader system. Shader scripts define visual properties for surfaces, models, and particle effects. Stock shaders live in:

```
Shader scripts live in [assets/data0_21pure/scripts/](https://github.com/TeamForbiddenLLC/warfork-qfusion/tree/master/assets/data0_21pure/scripts)
```

## Shader Script Format

A shader definition is a named block. The name is the shader identifier — not the filename.

```
shader/name
{
    // Global directives
    cull disable            // Face culling: disable, back, front
    nopicmip                // Ignore picmip quality reduction
    entityMergable          // Allow sprite batching
    softParticle            // Soft particle depth blending

    {
        // Stage (one texture pass)
        map path/to/texture.png             // Static texture
        clampmap path/to/texture.png        // Clamped (no UV repeat)
        animmap fps frame1 frame2 ...       // Animated texture sequence

        blendfunc blend                     // Shorthand: src_alpha / one_minus_src_alpha
        blendfunc GL_SRC_ALPHA GL_ONE_MINUS_SRC_ALPHA
        blendfunc add                       // Additive blending

        rgbGen vertex       // Color from vertex colors
        alphaGen vertex     // Alpha from vertex colors
        rgbGen entity       // Color from entity (team color, etc.)
        alphaGen entity
    }
}
```

A shader can have multiple stages. Stages are blended in order.

## Common Use Cases

### Player Visibility Shaders

Replace player model textures with flat fullbright colors for competitive visibility. Team colors are controlled by `cg_teamALPHAcolor` and `cg_teamBETAcolor`, but custom shaders can override individual model skins directly.

See the fullbright pattern below.

### Effect Shaders

Dash burst effects, smoke puffs, and projectile trails are defined in `effects.shader`. Effect shaders typically use additive blending and animated textures. Source path: `gfx/dash/` for dash-related effects.

### Map Geometry Shaders

Surface properties — slick floors, nodraw faces, clip brushes, trigger volumes — are defined in `solidfake.shader` and in per-map `.shader` files. These shaders control physics and visibility independently.

### Sky Shaders

Skybox definitions use the `sky` global directive. Defined in `sky.shader`.

## Shader Search Path

The engine loads shaders from:

```
basewf/scripts/
```

Custom shaders can be placed loose in that directory or packaged inside a `.pk3` file under `scripts/`. The `.shader` filename does not matter — shader names come from the block headers.

If two shaders share the same name, load order determines which wins. PK3 files loaded later take precedence over earlier ones.

## Fullbright / Visibility Shaders

For competitive play, a common pattern renders a model as a flat unlit color, ignoring map lighting entirely:

```
models/players/mymodel/skin
{
    {
        map $whiteimage
        rgbGen entity
    }
}
```

`$whiteimage` is a built-in 1x1 white texture. `rgbGen entity` pulls the color from the entity's assigned shader color — in practice, the team color set by the client. This produces a solid, fully lit silhouette regardless of map lighting.

Combined with `cg_forceMyTeamAlpha`, `cg_outlinePlayers`, and team color cvars, this is the basis of competitive visibility setups in Warfork.

## See Also

- [[../getting-started]] — client setup and graphics settings
- [[console]] — cvar reference for `cg_teamALPHAcolor`, `cg_teamBETAcolor`, `cg_outlinePlayers`
