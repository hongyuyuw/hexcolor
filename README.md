# hexcolor

Normalize `#abc` and `00ff00` to `#AABBCC`, then split the color into RGB integers.

Accepts 3 or 6 hex digits, with or without a leading `#`. Alpha channels are rejected.

```python
from hexcolor import normalize_hex, to_rgb, from_rgb, same_color, invert, channel

normalize_hex("#abc")  # "#AABBCC"
to_rgb("#00ff00")       # (0, 255, 0)
from_rgb(0, 255, 0)     # "#00FF00"
same_color("#abc", "AABBCC")  # True
invert("#000000")              # "#FFFFFF"
```

```bash
python -m unittest test_hexcolor.py
```

MIT
