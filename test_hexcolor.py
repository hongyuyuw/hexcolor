import unittest

from hexcolor import brightness, channel, channel_gap, from_rgb, invert, is_black, is_dark, is_gray, is_light, is_white, normalize_hex, same_color, to_rgb, flat_color, wide_gap


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
        self.assertTrue(is_black("#000000"))
        self.assertFalse(is_black("#CCCCCC"))
        self.assertTrue(is_white("#FFFFFF"))
        self.assertFalse(is_white("#000000"))
        self.assertEqual(brightness("#000000"), 0)
        self.assertEqual(brightness("#FFFFFF"), 255)
        self.assertTrue(is_dark("#000000"))
        self.assertFalse(is_dark("#FFFFFF"))
        self.assertTrue(is_light("#FFFFFF"))
        self.assertFalse(is_light("#000000"))
        self.assertEqual(channel_gap("#FF0000"), 255)
        self.assertEqual(channel_gap("#FFFFFF"), 0)
        with self.assertRaises(ValueError):
            channel("#00FF00", "a")
        self.assertEqual(invert(invert("#00FF00")), "#00FF00")

    def test_reject(self) -> None:
        with self.assertRaises(ValueError):
            normalize_hex("#gg0000")


        self.assertTrue(flat_color("#FFFFFF"))
        self.assertFalse(flat_color("#FF0000"))

        self.assertTrue(wide_gap("#FF0000"))
        self.assertFalse(wide_gap("#010101"))

if __name__ == "__main__":
    unittest.main()
