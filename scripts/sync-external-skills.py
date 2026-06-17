#!/usr/bin/env python3
"""Manage vendored external Codex skills.

The manifest is the source of truth. This script only touches files listed in
external-skills.yaml, so local wrapper files such as agents/openai.yaml stay
repo-owned.
"""

from __future__ import annotations

import hashlib
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

try:
    import yaml
except ImportError:  # pragma: no cover - depends on host environment
    print("Missing dependency: PyYAML. Install it with `python3 -m pip install pyyaml`.", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = REPO_ROOT / "external-skills.yaml"
NOTICE_PATH = REPO_ROOT / "THIRD_PARTY_NOTICES.md"


@dataclass(frozen=True)
class ExternalSkill:
    name: str
    repo: str
    ref: str
    upstream_path: str
    local_path: Path
    copyright: str
    license_url: str
    files: tuple[str, ...]


@dataclass(frozen=True)
class FileStatus:
    relpath: str
    state: str
    local_hash: str | None
    upstream_hash: str | None


@dataclass(frozen=True)
class SkillStatus:
    skill: ExternalSkill
    files: tuple[FileStatus, ...]
    notice_missing: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return all(file.state == "ok" for file in self.files) and not self.notice_missing


def usage() -> str:
    return """Usage:
  python3 scripts/sync-external-skills.py list
  python3 scripts/sync-external-skills.py check [skill-name|all]
  python3 scripts/sync-external-skills.py update <skill-name|all>

Commands:
  list    Show external skills declared in external-skills.yaml.
  check   Compare local vendored files and notices against upstream.
  update  Replace local vendored files with upstream files listed in the manifest.
"""


def die(message: str, code: int = 2) -> None:
    print(message, file=sys.stderr)
    sys.exit(code)


def load_manifest() -> tuple[ExternalSkill, ...]:
    if not MANIFEST_PATH.exists():
        die(f"Manifest not found: {MANIFEST_PATH}")

    data = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("external_skills"), list):
        die("Manifest must contain `external_skills` as a list.")

    skills: list[ExternalSkill] = []
    seen: set[str] = set()
    for index, item in enumerate(data["external_skills"], start=1):
        if not isinstance(item, dict):
            die(f"external_skills[{index}] must be a mapping.")

        missing = [
            key
            for key in (
                "name",
                "repo",
                "ref",
                "upstream_path",
                "local_path",
                "copyright",
                "license_url",
                "files",
            )
            if key not in item
        ]
        if missing:
            die(f"external_skills[{index}] is missing: {', '.join(missing)}")

        name = checked_string(item["name"], f"external_skills[{index}].name")
        if name in seen:
            die(f"Duplicate external skill name: {name}")
        seen.add(name)

        files = item["files"]
        if not isinstance(files, list) or not files:
            die(f"external_skills[{index}].files must be a non-empty list.")

        file_names = tuple(checked_relative_file(value, f"{name}.files") for value in files)
        skills.append(
            ExternalSkill(
                name=name,
                repo=checked_string(item["repo"], f"{name}.repo"),
                ref=checked_string(item["ref"], f"{name}.ref"),
                upstream_path=checked_relative_dir(item["upstream_path"], f"{name}.upstream_path"),
                local_path=Path(checked_relative_dir(item["local_path"], f"{name}.local_path")),
                copyright=checked_string(item["copyright"], f"{name}.copyright"),
                license_url=checked_string(item["license_url"], f"{name}.license_url"),
                files=file_names,
            )
        )

    return tuple(skills)


def checked_string(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        die(f"{field} must be a non-empty string.")
    return value.strip()


def checked_relative_dir(value: object, field: str) -> str:
    text = checked_string(value, field).strip("/")
    path = Path(text)
    if path.is_absolute() or ".." in path.parts:
        die(f"{field} must be a relative path inside the repo.")
    return text


def checked_relative_file(value: object, field: str) -> str:
    text = checked_string(value, field)
    path = Path(text)
    if path.is_absolute() or ".." in path.parts or text.endswith("/"):
        die(f"{field} entries must be relative file paths.")
    return text


def select_skills(skills: Iterable[ExternalSkill], target: str | None) -> tuple[ExternalSkill, ...]:
    all_skills = tuple(skills)
    if target is None or target == "all":
        return all_skills

    selected = tuple(skill for skill in all_skills if skill.name == target)
    if not selected:
        names = ", ".join(skill.name for skill in all_skills)
        die(f"Unknown external skill `{target}`. Known skills: {names}")
    return selected


def upstream_file_url(skill: ExternalSkill, relpath: str) -> str:
    full_path = f"{skill.upstream_path}/{relpath}".strip("/")
    quoted_path = urllib.parse.quote(full_path, safe="/")
    quoted_ref = urllib.parse.quote(skill.ref, safe="")
    return f"https://raw.githubusercontent.com/{skill.repo}/{quoted_ref}/{quoted_path}"


def fetch_upstream_file(skill: ExternalSkill, relpath: str) -> bytes:
    url = upstream_file_url(skill, relpath)
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "text/plain",
            "User-Agent": "codex-external-skill-sync",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        die(f"Failed to fetch {url}: HTTP {exc.code}", code=1)
    except urllib.error.URLError as exc:
        die(f"Failed to fetch {url}: {exc.reason}", code=1)


def digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def local_file_path(skill: ExternalSkill, relpath: str) -> Path:
    path = REPO_ROOT / skill.local_path / relpath
    resolved = path.resolve()
    local_root = (REPO_ROOT / skill.local_path).resolve()
    if not str(resolved).startswith(str(local_root)):
        die(f"Refusing path outside local skill directory: {path}")
    return path


def compare_skill(skill: ExternalSkill) -> SkillStatus:
    file_statuses: list[FileStatus] = []
    for relpath in skill.files:
        upstream_bytes = fetch_upstream_file(skill, relpath)
        upstream_hash = digest(upstream_bytes)
        path = local_file_path(skill, relpath)
        if not path.exists():
            file_statuses.append(FileStatus(relpath, "missing", None, upstream_hash))
            continue

        local_bytes = path.read_bytes()
        local_hash = digest(local_bytes)
        state = "ok" if local_hash == upstream_hash else "drift"
        file_statuses.append(FileStatus(relpath, state, local_hash, upstream_hash))

    return SkillStatus(
        skill=skill,
        files=tuple(file_statuses),
        notice_missing=missing_notice_tokens(skill),
    )


def missing_notice_tokens(skill: ExternalSkill) -> tuple[str, ...]:
    if not NOTICE_PATH.exists():
        return ("THIRD_PARTY_NOTICES.md",)

    notice = NOTICE_PATH.read_text(encoding="utf-8")
    required = (
        skill.name,
        skill.repo,
        skill.upstream_path,
        skill.copyright,
        skill.license_url,
    )
    return tuple(token for token in required if token not in notice)


def print_status(status: SkillStatus) -> None:
    skill = status.skill
    print(f"{skill.name}")
    print(f"  upstream: https://github.com/{skill.repo}/tree/{skill.ref}/{skill.upstream_path}")
    print(f"  local:    {skill.local_path}")
    for file in status.files:
        if file.state == "ok":
            print(f"  ok      {file.relpath} {short_hash(file.local_hash)}")
        elif file.state == "missing":
            print(f"  missing {file.relpath} upstream={short_hash(file.upstream_hash)}")
        else:
            print(
                f"  drift   {file.relpath} "
                f"local={short_hash(file.local_hash)} upstream={short_hash(file.upstream_hash)}"
            )

    if status.notice_missing:
        print("  notice  missing tokens: " + ", ".join(status.notice_missing))
    else:
        print("  notice  ok")


def short_hash(value: str | None) -> str:
    return "-" if value is None else value[:12]


def update_skill(skill: ExternalSkill) -> int:
    changed = 0
    print(f"{skill.name}")
    for relpath in skill.files:
        upstream_bytes = fetch_upstream_file(skill, relpath)
        path = local_file_path(skill, relpath)
        path.parent.mkdir(parents=True, exist_ok=True)

        if path.exists() and path.read_bytes() == upstream_bytes:
            print(f"  ok      {relpath}")
            continue

        path.write_bytes(upstream_bytes)
        changed += 1
        print(f"  updated {relpath}")

    notice_missing = missing_notice_tokens(skill)
    if notice_missing:
        print("  notice  missing tokens: " + ", ".join(notice_missing))
    else:
        print("  notice  ok")
    return changed


def command_list(skills: tuple[ExternalSkill, ...]) -> int:
    for skill in skills:
        print(f"{skill.name} -> {skill.repo}/{skill.upstream_path} @ {skill.ref}")
    return 0


def command_check(skills: tuple[ExternalSkill, ...], target: str | None) -> int:
    selected = select_skills(skills, target)
    statuses = [compare_skill(skill) for skill in selected]
    for index, status in enumerate(statuses):
        if index:
            print()
        print_status(status)
    return 0 if all(status.ok for status in statuses) else 1


def command_update(skills: tuple[ExternalSkill, ...], target: str | None) -> int:
    if target is None:
        die("update requires a skill name or `all`.")

    selected = select_skills(skills, target)
    total_changed = 0
    for index, skill in enumerate(selected):
        if index:
            print()
        total_changed += update_skill(skill)
    print()
    print(f"Changed files: {total_changed}")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in {"help", "-h", "--help"}:
        print(usage())
        return 0 if len(argv) >= 2 else 2

    command = argv[1]
    target = argv[2] if len(argv) > 2 else None
    if len(argv) > 3:
        die("Too many arguments.\n\n" + usage())

    skills = load_manifest()
    if command == "list":
        if target is not None:
            die("list does not accept a skill name.")
        return command_list(skills)
    if command == "check":
        return command_check(skills, target)
    if command == "update":
        return command_update(skills, target)

    die(f"Unknown command `{command}`.\n\n{usage()}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
