"""Tests for scripts/validate_markdown_links.py."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

# Import the module under test
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import validate_markdown_links as vml


# ---------------------------------------------------------------------------
# parse_markdown_links
# ---------------------------------------------------------------------------


class TestParseMarkdownLinks:
    def test_simple_link(self):
        text = "See [guide](README.md) for details."
        result = vml.parse_markdown_links(text)
        assert result == [(1, "README.md")]

    def test_multiple_links_same_line(self):
        text = "Read [A](a.md) and [B](b.md)."
        result = vml.parse_markdown_links(text)
        assert result == [(1, "a.md"), (1, "b.md")]

    def test_multiple_lines(self):
        text = "First [one](one.md)\nSecond [two](two.md)\nThird line."
        result = vml.parse_markdown_links(text)
        assert result == [(1, "one.md"), (2, "two.md")]

    def test_link_with_anchor(self):
        text = "See [section](doc.md#heading)."
        result = vml.parse_markdown_links(text)
        assert result == [(1, "doc.md#heading")]

    def test_anchor_only_link(self):
        text = "See [above](#overview)."
        result = vml.parse_markdown_links(text)
        assert result == [(1, "#overview")]

    def test_image_link_excluded(self):
        text = "![alt](image.png)"
        result = vml.parse_markdown_links(text)
        assert result == []

    def test_external_link_still_parsed(self):
        """External URLs are parsed; filtering happens in is_local_target."""
        text = "Visit [site](https://example.com)."
        result = vml.parse_markdown_links(text)
        assert result == [(1, "https://example.com")]

    def test_empty_text(self):
        assert vml.parse_markdown_links("") == []

    def test_no_links(self):
        text = "Just some plain text with no links at all."
        assert vml.parse_markdown_links(text) == []

    def test_link_with_spaces_stripped(self):
        text = "See [doc]( path/to/file.md )."
        result = vml.parse_markdown_links(text)
        assert result == [(1, "path/to/file.md")]


# ---------------------------------------------------------------------------
# is_local_target
# ---------------------------------------------------------------------------


class TestIsLocalTarget:
    def test_relative_path(self):
        assert vml.is_local_target("docs/guide.md") is True

    def test_anchor_only(self):
        assert vml.is_local_target("#section") is True

    def test_http(self):
        assert vml.is_local_target("http://example.com") is False

    def test_https(self):
        assert vml.is_local_target("https://example.com") is False

    def test_mailto(self):
        assert vml.is_local_target("mailto:user@example.com") is False

    def test_tel(self):
        assert vml.is_local_target("tel:+1234567890") is False

    def test_data(self):
        assert vml.is_local_target("data:text/plain;base64,abc") is False

    def test_empty(self):
        assert vml.is_local_target("") is False

    def test_case_insensitive_scheme(self):
        assert vml.is_local_target("HTTPS://example.com") is False
        assert vml.is_local_target("Http://example.com") is False


# ---------------------------------------------------------------------------
# resolve_target
# ---------------------------------------------------------------------------


class TestResolveTarget:
    def test_relative_path(self, tmp_path):
        source = tmp_path / "docs" / "guide.md"
        source.parent.mkdir()
        source.touch()
        target_file = tmp_path / "docs" / "other.md"
        target_file.touch()

        result = vml.resolve_target(source, "other.md", tmp_path)
        assert result == target_file.resolve()

    def test_absolute_path_from_root(self, tmp_path):
        source = tmp_path / "docs" / "guide.md"
        source.parent.mkdir()
        source.touch()
        target_file = tmp_path / "README.md"
        target_file.touch()

        result = vml.resolve_target(source, "/README.md", tmp_path)
        assert result == target_file.resolve()

    def test_anchor_only_returns_source(self, tmp_path):
        source = tmp_path / "guide.md"
        source.touch()

        result = vml.resolve_target(source, "#section", tmp_path)
        assert result == source

    def test_path_with_anchor_strips_fragment(self, tmp_path):
        source = tmp_path / "guide.md"
        source.touch()
        target_file = tmp_path / "other.md"
        target_file.touch()

        result = vml.resolve_target(source, "other.md#heading", tmp_path)
        assert result == target_file.resolve()

    def test_external_url_returns_none(self, tmp_path):
        source = tmp_path / "guide.md"
        source.touch()

        result = vml.resolve_target(source, "https://example.com", tmp_path)
        assert result is None

    def test_angle_brackets_stripped(self, tmp_path):
        source = tmp_path / "guide.md"
        source.touch()
        target_file = tmp_path / "other.md"
        target_file.touch()

        result = vml.resolve_target(source, "<other.md>", tmp_path)
        assert result == target_file.resolve()

    def test_url_encoded_path(self, tmp_path):
        source = tmp_path / "guide.md"
        source.touch()
        target_file = tmp_path / "my file.md"
        target_file.touch()

        result = vml.resolve_target(source, "my%20file.md", tmp_path)
        assert result == target_file.resolve()


# ---------------------------------------------------------------------------
# discover_markdown_files
# ---------------------------------------------------------------------------


class TestDiscoverMarkdownFiles:
    def test_finds_md_files(self, tmp_path):
        (tmp_path / "a.md").touch()
        (tmp_path / "sub").mkdir()
        (tmp_path / "sub" / "b.md").touch()

        result = vml.discover_markdown_files(tmp_path)
        assert len(result) == 2
        assert tmp_path / "a.md" in result
        assert tmp_path / "sub" / "b.md" in result

    def test_excludes_git_directory(self, tmp_path):
        (tmp_path / "a.md").touch()
        (tmp_path / ".git").mkdir()
        (tmp_path / ".git" / "README.md").touch()

        result = vml.discover_markdown_files(tmp_path)
        assert len(result) == 1
        assert tmp_path / "a.md" in result

    def test_ignores_non_md_files(self, tmp_path):
        (tmp_path / "a.md").touch()
        (tmp_path / "b.txt").touch()
        (tmp_path / "c.py").touch()

        result = vml.discover_markdown_files(tmp_path)
        assert len(result) == 1

    def test_empty_directory(self, tmp_path):
        assert vml.discover_markdown_files(tmp_path) == []


# ---------------------------------------------------------------------------
# collect_broken_links
# ---------------------------------------------------------------------------


class TestCollectBrokenLinks:
    def test_all_links_valid(self, tmp_path):
        (tmp_path / "target.md").write_text("# Target", encoding="utf-8")
        (tmp_path / "index.md").write_text(
            "See [target](target.md).", encoding="utf-8"
        )

        broken, checked = vml.collect_broken_links(tmp_path)
        assert checked == 1
        assert broken == []

    def test_broken_link_detected(self, tmp_path):
        (tmp_path / "index.md").write_text(
            "See [missing](does-not-exist.md).", encoding="utf-8"
        )

        broken, checked = vml.collect_broken_links(tmp_path)
        assert checked == 1
        assert len(broken) == 1
        assert broken[0].raw_target == "does-not-exist.md"
        assert broken[0].line_number == 1

    def test_external_links_skipped(self, tmp_path):
        (tmp_path / "index.md").write_text(
            "Visit [site](https://example.com).", encoding="utf-8"
        )

        broken, checked = vml.collect_broken_links(tmp_path)
        assert checked == 0
        assert broken == []

    def test_mixed_valid_and_broken(self, tmp_path):
        (tmp_path / "exists.md").write_text("# Exists", encoding="utf-8")
        (tmp_path / "index.md").write_text(
            "Good [link](exists.md) and bad [link](nope.md).",
            encoding="utf-8",
        )

        broken, checked = vml.collect_broken_links(tmp_path)
        assert checked == 2
        assert len(broken) == 1
        assert broken[0].raw_target == "nope.md"

    def test_subdirectory_relative_link(self, tmp_path):
        sub = tmp_path / "docs"
        sub.mkdir()
        (sub / "a.md").write_text("See [b](b.md).", encoding="utf-8")
        (sub / "b.md").write_text("# B", encoding="utf-8")

        broken, checked = vml.collect_broken_links(tmp_path)
        assert checked == 1
        assert broken == []

    def test_parent_directory_link(self, tmp_path):
        (tmp_path / "root.md").write_text("# Root", encoding="utf-8")
        sub = tmp_path / "docs"
        sub.mkdir()
        (sub / "child.md").write_text(
            "See [root](../root.md).", encoding="utf-8"
        )

        broken, checked = vml.collect_broken_links(tmp_path)
        assert checked == 1
        assert broken == []

    def test_anchor_only_not_broken(self, tmp_path):
        (tmp_path / "guide.md").write_text(
            "See [above](#overview).", encoding="utf-8"
        )

        broken, checked = vml.collect_broken_links(tmp_path)
        assert checked == 1
        assert broken == []


# ---------------------------------------------------------------------------
# generate_report_markdown
# ---------------------------------------------------------------------------


class TestGenerateReportMarkdown:
    def test_clean_report(self, tmp_path):
        report = vml.generate_report_markdown(
            repo_root=tmp_path,
            checked_links=10,
            broken_links=[],
            title="Test Report",
        )
        assert "# Test Report" in report
        assert "**10**" in report
        assert "**0**" in report
        assert "All checked internal links resolved successfully." in report

    def test_broken_links_report(self, tmp_path):
        source = tmp_path / "docs" / "guide.md"
        broken = [
            vml.BrokenLink(
                source_file=source,
                line_number=5,
                raw_target="missing.md",
                resolved_path=tmp_path / "docs" / "missing.md",
            )
        ]
        report = vml.generate_report_markdown(
            repo_root=tmp_path,
            checked_links=3,
            broken_links=broken,
            title="Test Report",
        )
        assert "## Broken Links" in report
        assert "**1**" in report
        assert "missing.md" in report
        assert "guide.md:5" in report


# ---------------------------------------------------------------------------
# main (CLI integration)
# ---------------------------------------------------------------------------


class TestMainCLI:
    def test_exit_code_zero_clean(self, tmp_path):
        (tmp_path / "a.md").write_text(
            "See [b](b.md).", encoding="utf-8"
        )
        (tmp_path / "b.md").write_text("# B", encoding="utf-8")

        result = subprocess.run(
            [sys.executable, "-m", "validate_markdown_links", "--root", str(tmp_path)],
            capture_output=True,
            text=True,
            cwd=str(Path(__file__).resolve().parent.parent / "scripts"),
        )
        assert result.returncode == 0
        assert "Broken links: 0" in result.stdout

    def test_exit_code_one_broken(self, tmp_path):
        (tmp_path / "a.md").write_text(
            "See [missing](nope.md).", encoding="utf-8"
        )

        result = subprocess.run(
            [sys.executable, "-m", "validate_markdown_links", "--root", str(tmp_path)],
            capture_output=True,
            text=True,
            cwd=str(Path(__file__).resolve().parent.parent / "scripts"),
        )
        assert result.returncode == 1
        assert "Broken links: 1" in result.stdout

    def test_report_flag_writes_file(self, tmp_path):
        (tmp_path / "a.md").write_text("No links here.", encoding="utf-8")
        report_path = tmp_path / "report.md"

        subprocess.run(
            [
                sys.executable, "-m", "validate_markdown_links",
                "--root", str(tmp_path),
                "--report", str(report_path),
                "--title", "CI Report",
            ],
            capture_output=True,
            text=True,
            cwd=str(Path(__file__).resolve().parent.parent / "scripts"),
        )
        assert report_path.exists()
        content = report_path.read_text(encoding="utf-8")
        assert "# CI Report" in content
