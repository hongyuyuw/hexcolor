"""Normalize hex colors and split them into RGB channels."""
from __future__ import annotations

import re

_HEX = re.compile(r"#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})\Z")


def normalize_hex(text: str) -> str:
    match = _HEX.fullmatch((text or "").strip())
    if not match:
        raise ValueError(f"不是十六进制颜色: {text}")
    body = match.group(1)
    if len(body) == 3:
        body = "".join(ch * 2 for ch in body)
    return "#" + body.upper()


def to_rgb(text: str) -> tuple[int, int, int]:
    body = normalize_hex(text)[1:]
    return tuple(int(body[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def from_rgb(red: int, green: int, blue: int) -> str:
    for channel in (red, green, blue):
        if channel < 0 or channel > 255:
            raise ValueError("通道超出 0..255")
    return f"#{red:02X}{green:02X}{blue:02X}"
