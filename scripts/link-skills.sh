#!/usr/bin/env bash
# Keep both agents on the same checkout without replacing unrelated skills.
set -euo pipefail
repo=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
names=(baa baa-apple baa-android baa-windows)
targets=("$HOME/.claude/skills" "$HOME/.agents/skills")
for target in "${targets[@]}"; do
  for name in "${names[@]}"; do
    source_path="$repo/skills/$name"
    link_path="$target/$name"
    if [[ ! -f "$source_path/SKILL.md" ]]; then
      printf 'Missing public skill: %s\n' "$source_path" >&2
      exit 1
    fi
    if [[ -e "$link_path" || -L "$link_path" ]]; then
      if [[ ! -L "$link_path" || ! "$link_path" -ef "$source_path" ]]; then
        printf 'Refusing to replace existing path: %s\n' "$link_path" >&2
        exit 1
      fi
    fi
  done
done
for target in "${targets[@]}"; do
  mkdir -p "$target"
  for name in "${names[@]}"; do
    link_path="$target/$name"
    if [[ ! -L "$link_path" ]]; then
      ln -s "$repo/skills/$name" "$link_path"
    fi
    printf '%s\n' "$link_path"
  done
done
