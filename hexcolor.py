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


def same_color(left: str, right: str) -> bool:
    return normalize_hex(left) == normalize_hex(right)


def channel(text: str, name: str) -> int:
    index = {"r": 0, "g": 1, "b": 2}.get(name)
    if index is None:
        raise ValueError("通道只能是 r g b")
    return to_rgb(text)[index]


def is_gray(text: str) -> bool:
    red, green, blue = to_rgb(text)
    return red == green == blue


def invert(text: str) -> str:
    red, green, blue = to_rgb(text)
    return from_rgb(255 - red, 255 - green, 255 - blue)


def from_rgb(red: int, green: int, blue: int) -> str:
    for channel in (red, green, blue):
        if channel < 0 or channel > 255:
            raise ValueError("通道超出 0..255")
    return f"#{red:02X}{green:02X}{blue:02X}"
