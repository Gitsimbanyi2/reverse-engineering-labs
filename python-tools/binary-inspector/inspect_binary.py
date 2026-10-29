#!/usr/bin/env python3
"""Print magic bytes and classify ELF / PE / other. No disassembly, no unpacking."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def classify(data: bytes) -> str:
    if data.startswith(b"\x7fELF"):
        return "ELF"
    if data.startswith(b"MZ"):
        return "PE/DOS MZ (Windows PE likely)"
    if data.startswith(b"\xfe\xed\xfa\xce") or data.startswith(b"\xcf\xfa\xed\xfe"):
        return "Mach-O"
    if data.startswith(b"/*") or b"int main" in data[:400]:
        return "C source (not an executable yet)"
    return "unknown / other"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    data = args.path.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    print(f"path:   {args.path}")
    print(f"size:   {len(data)}")
    print(f"sha256: {sha}")
    print(f"magic:  {data[:4].hex()}")
    print(f"class:  {classify(data)}")


if __name__ == "__main__":
    main()
