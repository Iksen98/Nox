#!/usr/bin/env python3
"""Inspect COEMatrix.csv without external dependencies."""

from __future__ import annotations

import csv
from pathlib import Path

CSV_PATH = Path("COEMatrix.csv")


def main() -> None:
    if not CSV_PATH.exists():
        raise SystemExit(f"File not found: {CSV_PATH}")

    with CSV_PATH.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        columns = reader.fieldnames or []

    print(f"shape: ({len(rows)}, {len(columns)})")
    print("columns:")
    for index, name in enumerate(columns, start=1):
        print(f"  {index:>2}. {name}")

    print("\nhead (first 5 rows):")
    for row in rows[:5]:
        preview = {key: row[key] for key in columns[:6]}
        print(preview)


if __name__ == "__main__":
    main()
