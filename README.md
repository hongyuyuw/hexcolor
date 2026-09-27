# hexcolor

Normalize `#abc` and `00ff00` to `#AABBCC`, then split the color into RGB integers.

Accepts 3 or 6 hex digits, with or without a leading `#`. Alpha channels are rejected.

```python
from hexcolor import normalize_hex, to_rgb

normalize_hex("#abc")  # "#AABBCC"
to_rgb("#00ff00")       # (0, 255, 0)
```

```bash
python -m unittest test_hexcolor.py
```

MIT
