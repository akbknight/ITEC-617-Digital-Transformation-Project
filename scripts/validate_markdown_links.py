#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# ///

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


MARKDOWN_LINK_RE = re.compile(r"(?<!!)(?:\[[^\]]*\])\(([^)]+)\)")
IGNORED_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:")


@dataclass
class BrokenLink:
    source_file: Path
    line_number: int
    raw_target: str
    resolved_path: Path


def discover_markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts
    )


def parse_markdown_links(text: str) -> list[tuple[int, str]]:
    links: list[tuple[int, str]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for match in MARKDOWN_LINK_RE.finditer(line):
            links.append((line_number, match.group(1).strip()))
    return links


def is_local_target(target: str) -> bool:
    if not target:
        return False
    lowered = target.lower()
    return not lowered.startswith(IGNORED_SCHEMES)


def resolve_target(source_file: Path, raw_target: str, repo_root: Path) -> Path | None:
    target = raw_target.strip().strip("<>")
    if not is_local_target(target):
        return None

    path_part = target.split("#", 1)[0].strip()
    if not path_part:
        return source_file

    decoded = unquote(path_part)
    if decoded.startswith("/"):
        candidate = (repo_root / decoded.lstrip("/")).resolve()
    else:
        candidate = (source_file.parent / decoded).resolve()
    return candidate


def collect_broken_links(repo_root: Path) -> tuple[list[BrokenLink], int]:
    markdown_files = discover_markdown_files(repo_root)
    broken: list[BrokenLink] = []
    checked_links = 0

    for markdown_file in markdown_files:
        content = markdown_file.read_text(encoding="utf-8")
        for line_number, raw_target in parse_markdown_links(content):
            resolved = resolve_target(markdown_file, raw_target, repo_root)
            if resolved is None:
                continue

            checked_links += 1
            if not resolved.exists():
                broken.append(
                    BrokenLink(
                        source_file=markdown_file,
                        line_number=line_number,
                        raw_target=raw_target,
                        resolved_path=resolved,
                    )
                )

    return broken, checked_links


def generate_report_markdown(
    repo_root: Path,
    checked_links: int,
    broken_links: list[BrokenLink],
    title: str,
) -> str:
    lines: list[str] = [
        f"# {title}",
        "",
        f"- Repository root: `{repo_root}`",
        f"- Internal local links checked: **{checked_links}**",
        f"- Broken links found: **{len(broken_links)}**",
        "",
    ]

    if not broken_links:
        lines.append("## Result")
        lines.append("")
        lines.append("All checked internal links resolved successfully.")
        return "\n".join(lines) + "\n"

    lines.append("## Broken Links")
    lines.append("")
    for issue in broken_links:
        relative_source = issue.source_file.relative_to(repo_root)
        relative_resolved = (
            issue.resolved_path.relative_to(repo_root)
            if issue.resolved_path.is_relative_to(repo_root)
            else issue.resolved_path
        )
        lines.append(
            f"- `{relative_source}:{issue.line_number}` -> `{issue.raw_target}` "
            f"(resolved: `{relative_resolved}`)"
        )

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate internal local links across markdown files."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root to scan (default: current directory).",
    )
    parser.add_argument(
        "--report",
        default=None,
        help="Optional path to write markdown test report.",
    )
    parser.add_argument(
        "--title",
        default="Markdown Internal Link Validation Report",
        help="Report title when --report is provided.",
    )
    args = parser.parse_args()

    repo_root = Path(args.root).resolve()
    broken_links, checked_links = collect_broken_links(repo_root)

    print(f"Checked internal links: {checked_links}")
    print(f"Broken links: {len(broken_links)}")
    for issue in broken_links:
        source = issue.source_file.relative_to(repo_root)
        print(f"- {source}:{issue.line_number} -> {issue.raw_target}")

    if args.report:
        report_path = Path(args.report)
        if not report_path.is_absolute():
            report_path = (repo_root / report_path).resolve()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_text = generate_report_markdown(
            repo_root=repo_root,
            checked_links=checked_links,
            broken_links=broken_links,
            title=args.title,
        )
        report_path.write_text(report_text, encoding="utf-8")
        print(f"Report written: {report_path}")

    return 1 if broken_links else 0


if __name__ == "__main__":
    raise SystemExit(main())
