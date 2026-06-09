#!/usr/bin/env python3
"""
Generate /llms.txt for the TARP wiki.

Reads every .md file in content/, pulls title + description from frontmatter,
and builds a structured llms.txt organized by game section.

Output: quartz/static/llms.txt  (served at /llms.txt by Quartz)

Usage:
    python3 scripts/generate_llms_txt.py
    python3 scripts/generate_llms_txt.py --content-dir /path/to/content
"""

import argparse
import re
import sys
from pathlib import Path

BASE_URL = "https://tonikwithak.github.io/tarp-wiki"

GAME_LABELS = {
    "warfork": "Warfork",
    "quake-live": "Quake Live",
    "reflex-arena": "Reflex Arena",
}

# Section order within a game — unlisted sections fall into "Other"
SECTION_ORDER = ["weapons", "gametypes", "movement", "modding"]


def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter fields (title, description) without a full YAML parser."""
    fm = {}
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return fm
    block = match.group(1)

    # title: value or title: "value"
    for key in ("title", "description"):
        m = re.search(rf'^{key}:\s*"?([^"\n]+)"?\s*$', block, re.MULTILINE)
        if m:
            fm[key] = m.group(1).strip()
    return fm


def md_path_to_url(path: Path, content_dir: Path) -> str:
    rel = path.relative_to(content_dir)
    # index.md -> folder URL, others -> slug URL
    parts = list(rel.parts)
    if parts[-1] == "index.md":
        parts = parts[:-1]
        slug = "/".join(parts) + "/" if parts else ""
    else:
        parts[-1] = parts[-1].removesuffix(".md")
        slug = "/".join(parts)
    return f"{BASE_URL}/{slug}"


def collect_pages(content_dir: Path) -> dict:
    """
    Returns:
        {
            "root": [{"url": ..., "title": ..., "description": ...}],
            "warfork": {
                "index": {...},
                "weapons": [...],
                "gametypes": [...],
                ...
            },
            ...
        }
    """
    result = {"root": [], "games": {}}

    for md_file in sorted(content_dir.rglob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        title = fm.get("title") or md_file.stem.replace("-", " ").title()
        description = fm.get("description", "")
        url = md_path_to_url(md_file, content_dir)

        rel = md_file.relative_to(content_dir)
        parts = rel.parts  # e.g. ("games", "warfork", "weapons", "rocket-launcher.md")

        if len(parts) == 1:
            # Root index
            result["root"].append({"url": url, "title": title, "description": description})
            continue

        if parts[0] != "games" or len(parts) < 3:
            continue

        game = parts[1]  # warfork / quake-live / etc.
        if game not in result["games"]:
            result["games"][game] = {"index": None, "sections": {}}

        if len(parts) == 3 and parts[2] == "index.md":
            result["games"][game]["index"] = {"url": url, "title": title, "description": description}
        elif len(parts) == 3:
            # Top-level page under a game (movement.md, controls.md, etc.)
            section = "general"
            result["games"][game]["sections"].setdefault(section, []).append(
                {"url": url, "title": title, "description": description}
            )
        else:
            # Subfolder page: parts[2] is the section (weapons, gametypes, modding...)
            section = parts[2]
            if parts[-1] == "index.md":
                # Section index — prepend it
                result["games"][game]["sections"].setdefault(section, []).insert(
                    0, {"url": url, "title": title, "description": description}
                )
            else:
                result["games"][game]["sections"].setdefault(section, []).append(
                    {"url": url, "title": title, "description": description}
                )

    return result


def format_entry(page: dict) -> str:
    line = f"- [{page['title']}]({page['url']})"
    if page.get("description"):
        line += f": {page['description']}"
    return line


def build_llms_txt(data: dict) -> str:
    lines = []

    lines.append("# TARP: The Arena Revival Project")
    lines.append("")
    lines.append("> A living knowledge base for competitive Arena FPS.")
    lines.append("> Covers mechanics, movement, weapons, gametypes, and modding for Warfork, Quake Live, and Reflex Arena.")
    lines.append("> All pages are verified against source material before publication.")
    lines.append("")
    lines.append(f"Site: {BASE_URL}")
    lines.append("")

    # Root pages
    if data["root"]:
        lines.append("## Overview")
        lines.append("")
        for page in data["root"]:
            lines.append(format_entry(page))
        lines.append("")

    # Per-game sections
    for game_key, game_label in GAME_LABELS.items():
        game_data = data["games"].get(game_key)
        if not game_data:
            continue

        lines.append(f"## {game_label}")
        lines.append("")

        if game_data["index"]:
            lines.append(format_entry(game_data["index"]))
            lines.append("")

        sections = game_data["sections"]

        # Emit in preferred order first, then remaining
        ordered_keys = [s for s in SECTION_ORDER if s in sections]
        remaining_keys = [s for s in sections if s not in SECTION_ORDER]

        for section_key in ordered_keys + remaining_keys:
            pages = sections[section_key]
            if not pages:
                continue
            label = section_key.replace("-", " ").title()
            lines.append(f"### {game_label}: {label}")
            lines.append("")
            for page in pages:
                lines.append(format_entry(page))
            lines.append("")

    lines.append("## Optional")
    lines.append("")
    lines.append(f"- [Graph view]({BASE_URL}/): Interactive graph showing how pages connect")
    lines.append(f"- [GitHub repository](https://github.com/TonikwithaK/tarp-wiki)")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate llms.txt for TARP wiki")
    parser.add_argument(
        "--content-dir",
        default=str(Path(__file__).parent.parent / "content"),
        help="Path to the content/ directory",
    )
    parser.add_argument(
        "--output",
        default=str(Path(__file__).parent.parent / "quartz/static/llms.txt"),
        help="Output file path",
    )
    args = parser.parse_args()

    content_dir = Path(args.content_dir)
    output_path = Path(args.output)

    if not content_dir.exists():
        print(f"Error: content directory not found: {content_dir}", file=sys.stderr)
        sys.exit(1)

    data = collect_pages(content_dir)
    txt = build_llms_txt(data)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(txt, encoding="utf-8")

    page_count = sum(
        len(pages)
        for game in data["games"].values()
        for pages in game["sections"].values()
    ) + len(data["root"])
    print(f"Generated {output_path} — {page_count} pages indexed")


if __name__ == "__main__":
    main()
