#!/usr/bin/env python3
"""Validate this repository's Agent Skills catalog."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MANIFEST = SKILLS_DIR / "manifest.json"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

TEXT_EXTENSIONS = {
    ".md",
    ".py",
    ".yaml",
    ".yml",
    ".json",
    ".txt",
    ".sh",
}

QUALITY_PATTERNS = [
    r"\b" + "TO" + r"DO\b",
    r"\b" + "FIX" + r"ME\b",
    r"\b" + "place" + r"holder\b",
    r"\b" + "dum" + r"my\b",
    r"\b" + "stu" + r"b\b",
    r"\b" + "lor" + r"em\b",
    r"\b" + "enterprise" + r"-grade\b",
    r"\b" + "production" + r"-ready\b",
    r"\b" + "revolution" + r"ary\b",
]

SIGNATURE_PATTERNS = [
    r"generated\s+by",
    r"created\s+by\s+chatgpt",
    r"written\s+by\s+chatgpt",
    r"ai" + r"[- ]generated",
    r"vibe\s+coded",
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        fail(errors, f"{path}: missing YAML frontmatter")
        return {}

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(errors, f"{path}: invalid frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def check_openai_yaml(skill_dir: Path, errors: list[str]) -> None:
    metadata = skill_dir / "agents" / "openai.yaml"
    if not metadata.exists():
        fail(errors, f"{skill_dir}: missing agents/openai.yaml")
        return

    text = metadata.read_text(encoding="utf-8")
    required = ("display_name:", "short_description:", "default_prompt:")
    for marker in required:
        if marker not in text:
            fail(errors, f"{metadata}: missing {marker}")
    if f"${skill_dir.name}" not in text:
        fail(errors, f"{metadata}: default_prompt must mention ${skill_dir.name}")


def check_skill(skill_dir: Path, errors: list[str]) -> None:
    if not NAME_RE.fullmatch(skill_dir.name):
        fail(errors, f"{skill_dir}: invalid skill folder name")

    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        fail(errors, f"{skill_dir}: missing SKILL.md")
        return

    data = parse_frontmatter(skill_file, errors)
    if data.get("name") != skill_dir.name:
        fail(errors, f"{skill_file}: name must match folder")

    description = data.get("description", "")
    if len(description) < 80:
        fail(errors, f"{skill_file}: description is too short to route reliably")
    if len(description) > 1024:
        fail(errors, f"{skill_file}: description exceeds 1024 characters")
    if "Use when" not in description and "use when" not in description:
        fail(errors, f"{skill_file}: description must include use triggers")

    check_openai_yaml(skill_dir, errors)


def check_manifest(skill_dirs: list[Path], errors: list[str]) -> None:
    if not MANIFEST.exists():
        fail(errors, f"{MANIFEST}: missing manifest")
        return

    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        fail(errors, f"{MANIFEST}: cannot read valid JSON: {exc}")
        return
    if not isinstance(data, dict) or not isinstance(data.get("skills"), list):
        fail(errors, f"{MANIFEST}: root must contain a skills list")
        return
    items = data["skills"]
    malformed_items = [index for index, item in enumerate(items) if not isinstance(item, dict)]
    if malformed_items:
        fail(
            errors,
            f"{MANIFEST}: skill entries must be objects (indexes: "
            f"{', '.join(map(str, malformed_items))})",
        )
        return
    listed = [item.get("name", "") for item in items]
    duplicates = sorted({name for name in listed if listed.count(name) > 1})
    if duplicates:
        fail(errors, f"{MANIFEST}: duplicate skill names: {', '.join(duplicates)}")
    actual = [path.name for path in skill_dirs]
    for item in data.get("skills", []):
        if not NAME_RE.fullmatch(item.get("name", "")):
            fail(errors, f"{MANIFEST}: invalid skill name {item.get('name')!r}")
        if not item.get("summary"):
            fail(errors, f"{MANIFEST}: missing summary for {item.get('name')!r}")
    if listed != actual:
        fail(errors, f"{MANIFEST}: skill order or names do not match skills directory")


def check_readme(skill_dirs: list[Path], errors: list[str]) -> None:
    readme = ROOT / "README.md"
    if not readme.exists():
        fail(errors, f"{readme}: missing README")
        return

    text = readme.read_text(encoding="utf-8")
    for skill_dir in skill_dirs:
        if f"`{skill_dir.name}`" not in text:
            fail(errors, f"{readme}: missing README entry for {skill_dir.name}")


def iter_public_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        parts = set(path.relative_to(ROOT).parts)
        if ".git" in parts or ".specs" in parts:
            continue
        if path.suffix.lower() in TEXT_EXTENSIONS:
            files.append(path)
    return files


def check_public_text(errors: list[str]) -> None:
    quality_res = [re.compile(pattern, re.IGNORECASE) for pattern in QUALITY_PATTERNS]
    signature_res = [re.compile(pattern, re.IGNORECASE) for pattern in SIGNATURE_PATTERNS]

    for path in iter_public_text_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for regex in quality_res:
            if regex.search(text):
                fail(errors, f"{rel}: contains filler or unfinished-work language")
                break
        for regex in signature_res:
            if regex.search(text):
                fail(errors, f"{rel}: contains a generator signature")
                break


def main() -> int:
    errors: list[str] = []
    try:
        manifest_data = (
            json.loads(MANIFEST.read_text(encoding="utf-8"))
            if MANIFEST.exists()
            else {"skills": []}
        )
    except (json.JSONDecodeError, OSError):
        manifest_data = {"skills": []}
    raw_items = manifest_data.get("skills", []) if isinstance(manifest_data, dict) else []
    items = raw_items if isinstance(raw_items, list) else []
    manifest_order = {
        item.get("name"): index
        for index, item in enumerate(items)
        if isinstance(item, dict)
    }
    skill_dirs = sorted(
        [path for path in SKILLS_DIR.iterdir() if path.is_dir()],
        key=lambda path: manifest_order.get(path.name, len(manifest_order) + 1),
    )

    if not skill_dirs:
        fail(errors, f"{SKILLS_DIR}: no skill directories found")

    for skill_dir in skill_dirs:
        check_skill(skill_dir, errors)
    check_manifest(skill_dirs, errors)
    check_readme(skill_dirs, errors)
    check_public_text(errors)

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        print(f"{len(errors)} validation error(s)", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
