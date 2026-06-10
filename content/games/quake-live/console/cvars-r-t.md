---
title: "CVars: R–T"
game: quake-live
layer: canon
type: reference
tags: [quake-live, console, cvars, rendering, sound, server, reference]
status: canon
promoted: 2026-06-10
source: https://www.euere.eu/ql/
---

# Console Variables: R–T

Full reference sourced from euere.eu/ql/ — updated September 2025.

---

## R — Rendering

### Resolution & Display
| CVar | Default | Description |
|------|---------|-------------|
| `r_mode` | -2 | Screen resolution: -2=desktop, -1=custom, 0–27=presets |
| `r_customwidth` | 1600 | Custom horizontal resolution (when r_mode -1) |
| `r_customheight` | 1024 | Custom vertical resolution (when r_mode -1) |
| `r_fullscreen` | 0 | 0=Windowed, 1=Fullscreen |
| `r_aspectRatio` | 0 | 0=4:3, 1=16:9, 2=16:10, 3=5:4 |
| `r_displayRefresh` | 0 | Monitor refresh rate (Hz) |
| `r_colorbits` | 32 | Color depth (16 or 32) |
| `r_texturebits` | 32 | Texture quality (16 or 32) |
| `r_noFastRestart` | 0 | 0=attempt fullscreen/windowed switch without full reload |

### Textures
| CVar | Default | Description |
|------|---------|-------------|
| `r_picmip` | 0 | Texture detail: 0=highest quality, 16=near solid colors; requires vid_restart |
| `r_roundImagesDown` | 1 | Round images down; boosts performance, lowers quality |
| `r_simpleMipMaps` | 1 | Simple MIP mapping; boosts performance |
| `r_intensity` | 1 | Brightness added to textures and model skins |
| `r_fullbright` | 0 | 1=all map textures render at full brightness |
| `r_detailtextures` | 1 | Detail texturing stages |

### Lighting
| CVar | Default | Description |
|------|---------|-------------|
| `r_gamma` | 1 | Image luminance |
| `r_contrast` | 1.0 | Contrast level |
| `r_overBrightBits` | 1 | Ambient lighting on entities (0–4) |
| `r_mapOverBrightBits` | 2 | Ambient lighting on map geometry (0–10) |
| `r_ambientScale` | 10 | Ambient light among players |
| `r_dynamiclight` | 1 | Dynamic lights (rockets, etc.) |
| `r_vertexlight` | 0 | 0=light maps, 1=vertex lighting |
| `r_lightmap` | 0 | Light data lighting model |
| `r_teleporterFlash` | 1 | 0=black frame instead of white flash on teleport |
| `r_flares` | 0 | Projectile flare effects |
| `r_flareSize` | 40 | Size of flares |
| `r_drawSun` | 0 | Sunlight simulation on models (0 recommended) |

### Post-Processing
| CVar | Default | Description |
|------|---------|-------------|
| `r_enablePostProcess` | 1 | Post-processing pipeline (performance hit) |
| `r_enableBloom` | 0 | Bloom (requires r_enablePostProcess 1) |
| `r_enableColorCorrect` | 1 | Color correction (requires r_enablePostProcess 1) |
| `r_BloomBrightThreshold` | 0.125 | Lower=more bloom drawn (0–1) |
| `r_BloomIntensity` | 0.750 | Bloom intensity (0–10) |
| `r_BloomSaturation` | 0.800 | Bloom color saturation (0–10) |
| `r_BloomSceneIntensity` | 1.000 | Non-bloomed world brightness (0–10) |
| `r_BloomPasses` | 1 | Rendering passes for bloom |

### Performance
| CVar | Default | Description |
|------|---------|-------------|
| `r_facePlaneCull` | 1 | Brush face culling; boosts performance |
| `r_lodbias` | 0 | Geometric detail: 0=High, 1=Medium, 2=Low |
| `r_subdivisions` | 4 | Patch subdivisions; 80=angled surfaces, better performance |
| `r_fastsky` | 0 | 1=disable sky boxes |
| `r_fastSkyColor` | 0x000000 | Solid sky color when r_fastsky 1 (hex) |
| `r_drawentities` | 1 | Draw world entities (weapons, items, models) |

---

## S — Sound

| CVar | Default | Description |
|------|---------|-------------|
| `s_volume` [A] | 0.8 | Master volume (0.0–1.0) |
| `s_musicvolume` [A] | 0.25 | Music volume (0=mute) |
| `s_doppler` | 1 | Doppler effect (0=off) |
| `s_khz` [I] | 22 | Sampling rate (11, 22, or 44 kHz) |
| `s_mixahead` | 0.2 | Sound mixing ahead time |
| `s_ambient` | 1 | Ambient sounds |
| `s_separation` | 0.5 | Stereo separation |

---

## SV — Server

| CVar | Default | Description |
|------|---------|-------------|
| `sv_maxclients` [I] | 8 | Maximum clients |
| `sv_hostname` [S,A] | noname | Server name |
| `sv_fps` | 20 | Server frame rate |
| `sv_timeout` | 200 | Client timeout (seconds) |
| `sv_pure` | 1 | Pure server (clients must match server pk3s) |
| `sv_cheats` [S,I] | 0 | Enable cheat cvars on server |
| `sv_maxRate` | 0 | Maximum client data rate cap |
| `sv_minPing` [S] | 0 | Minimum client ping filter |
| `sv_maxPing` [S] | 0 | Maximum client ping filter |
| `sv_allowDownload` | 0 | Allow clients to download missing files |
| `sv_floodprotect` | 1 | Flood protection |
| `sv_password` | — | Server password |
| `sv_rconPassword` | — | RCON password |
| `sv_privateClients` | 0 | Reserved player slots |
| `sv_privatePassword` | — | Password for reserved slots |
| `sv_keywords` [S] | — | Keywords for server browser filtering |

---

## T — Timing

| CVar | Default | Description |
|------|---------|-------------|
| `timelimit` [S,A] | 0 | Match time limit in minutes |
| `timescale` [C] | 1 | Game speed multiplier (cheat) |

## Related

- [[console|Console Overview]]
- [[console/cvars-a-c|CVars A–C]]: bots, crosshair, HUD, client settings
- [[console/cvars-d-p|CVars D–P]]: game settings, weapon values, physics
- [[console/cvars-u-w|CVars U–W]]: UI variables
- [[console/appendix|Appendix]]: flag legend, color chart
