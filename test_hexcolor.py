import unittest

from hexcolor import normalize_hex, to_rgb


class HexcolorTest(unittest.TestCase):
    def test_expand(self) -> None:
        self.assertEqual(normalize_hex("#abc"), "#AABBCC")
        self.assertEqual(normalize_hex("00ff00"), "#00FF00")
        self.assertEqual(to_rgb("#abc"), (170, 187, 204))

    def test_reject(self) -> None:
        with self.assertRaises(ValueError):
            normalize_hex("#gg0000")


if __name__ == "__main__":
    unittest.main()
