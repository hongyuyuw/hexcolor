import unittest

from hexcolor import channel, from_rgb, invert, is_gray, normalize_hex, same_color, to_rgb


class HexcolorTest(unittest.TestCase):
    def test_expand(self) -> None:
        self.assertEqual(normalize_hex("#abc"), "#AABBCC")
        self.assertEqual(normalize_hex("00ff00"), "#00FF00")
        self.assertEqual(to_rgb("#abc"), (170, 187, 204))
        self.assertEqual(from_rgb(0, 255, 0), "#00FF00")
        self.assertEqual(to_rgb(from_rgb(170, 187, 204)), (170, 187, 204))
        self.assertTrue(same_color("#abc", "AABBCC"))
        self.assertFalse(same_color("#abc", "#000000"))
        self.assertEqual(invert("#000000"), "#FFFFFF")
        self.assertEqual(channel("#00FF00", "g"), 255)
        self.assertTrue(is_gray("#CCCCCC"))
        self.assertFalse(is_gray("#00FF00"))
        with self.assertRaises(ValueError):
            channel("#00FF00", "a")
        self.assertEqual(invert(invert("#00FF00")), "#00FF00")

    def test_reject(self) -> None:
        with self.assertRaises(ValueError):
            normalize_hex("#gg0000")


if __name__ == "__main__":
    unittest.main()
