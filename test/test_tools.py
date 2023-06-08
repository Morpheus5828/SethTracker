from unittest import TestCase
import tools as tl


class Test(TestCase):
    def test_exist(self):
        pass

    def test_array_to_bin(self):
        self.assertEqual(
            "01000010011010100101110000101001001000010111010100110000000000000011000010011101100001111010111000",
            str(tl.array_to_bin([58.59, 117.1875, -61.53]))
        )

    def test_float_to_bin(self):
        self.assertEqual("01000010011010100101110000101001", str(tl.float_to_bin(58.59)))
        self.assertEqual("01000010111010100110000000000000", str(tl.float_to_bin(117.1875)))
        self.assertEqual("11000010011101100001111010111000", str(tl.float_to_bin(-61.53)))
