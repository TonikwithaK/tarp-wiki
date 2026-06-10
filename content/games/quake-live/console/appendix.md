---
title: "Console Reference: Appendix"
game: quake-live
layer: canon
type: reference
tags: [quake-live, console, cvars, colors, reference]
status: canon
promoted: 2026-06-10
source: https://www.euere.eu/ql/
---

# Console Appendix

Sourced from euere.eu/ql/ — updated September 2025.

---

## CVAR Flag Legend

| Flag | Name | Description |
|------|------|-------------|
| `[A]` | Archive | Saved to vars.rc |
| `[C]` | Cheat-Protected | Only usable in cheat-enabled servers or localhost |
| `[I]` | Init | Cannot be set from console; command line only |
| `[L]` | Latched | Requires server restart to apply |
| `[R]` | Read-Only | Display only; cannot be set |
| `[S]` | Server Info | Server broadcasts to clients |
| `[U]` | User Info | Client broadcasts to server on connect or change |
| `[T]` | QL Database | Saved to QL database |
| `[W]` | Write-Protected | Cannot be set by user at all |

---

## CVAR Prefix Reference

| Prefix | Domain |
|--------|--------|
| `BOT_` | Bot settings |
| `CG_` | Client game settings |
| `CL_` | Client-side settings |
| `CM_` | Collision map settings |
| `COM_` | Common settings |
| `FS_` | Game files settings |
| `G_` | Server-side game settings |
| `GT_` | Connection settings |
| `IN_` | General input device settings |
| `JOY_` | Joystick input settings |
| `M_` | Mouse input settings |
| `NET_` | Network settings |
| `PMOVE_` | Player movement server settings |
| `R_` | Video rendering settings |
| `S_` | Sound system settings |
| `SV_` | Server-side settings |
| `SYS_` | System configuration settings |
| `UI_` | User interface settings |
| `WEB_` | Website settings |

---

## Color System

QL uses three separate color systems:

| Palette | Use Case |
|---------|----------|
| 8-Color | Text: clan tags and player names. Black unavailable for names |
| 26-Color | Weapons: railgun trail color, grenade color |
| Hex | Skins, grenade color, fast sky color, and other uses |

### Color Chart

| 8-Color # | 26-Color # | Name | Hex | R | G | B |
|-----------|------------|------|-----|---|---|---|
| 1 | 1 | Red | FF0000 | 255 | 0 | 0 |
| | 2 | Orange-Red | FF4000 | 255 | 64 | 0 |
| | 3 | Dark Orange | FF8000 | 255 | 128 | 0 |
| | 4 | Orange | FFC000 | 255 | 192 | 0 |
| 3 | 5 | Yellow | FFFF00 | 255 | 255 | 0 |
| | 6 | Green-Yellow | C0FF00 | 192 | 255 | 0 |
| | 7 | Chartreuse | 80FF00 | 128 | 255 | 0 |
| | 8 | Green 1 | 40FF00 | 64 | 255 | 0 |
| 2 | 9 | Green 2 | 00FF00 | 0 | 255 | 0 |
| | 10 | Spring Green 1 | 00FF40 | 0 | 255 | 64 |
| | 11 | Spring Green 2 | 00FF80 | 0 | 255 | 128 |
| | 12 | Green-Cyan | 00FFC0 | 0 | 255 | 192 |
| 5 | 13 | Cyan | 00FFFF | 0 | 255 | 255 |
| | 14 | Deep Sky Blue | 00C0FF | 0 | 192 | 255 |
| | 15 | Azure | 0080FF | 0 | 128 | 255 |
| | 16 | Cobalt | 0040FF | 0 | 64 | 255 |
| 4 | 17 | Blue | 0000FF | 0 | 0 | 255 |
| | 18 | Electric Ultramarine | 4000FF | 64 | 0 | 255 |
| | 19 | Electric Purple | 8000FF | 128 | 0 | 255 |
| | 20 | Lilac | C000FF | 192 | 0 | 255 |
| 6 | 21 | Magenta 1 | FF00FF | 255 | 0 | 255 |
| | 22 | Magenta 2 | FF00C0 | 255 | 0 | 192 |
| | 23 | Bright Pink | FF0080 | 255 | 0 | 128 |
| | 24 | Folly | FF0040 | 255 | 0 | 64 |
| 7 | 25 | White | FFFFFF | 255 | 255 | 255 |
| | 26 | Medium Grey | 808080 | 128 | 128 | 128 |
| 8/0 | — | Black | 000000 | 0 | 0 | 0 |

## Related

- [[console|Console Overview]]
- [[console/cvars-a-c|CVars A–C]]
- [[console/cvars-d-p|CVars D–P]]
- [[console/cvars-r-t|CVars R–T]]
- [[console/cvars-u-w|CVars U–W]]
