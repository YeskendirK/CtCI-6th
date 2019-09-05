def pairwise_swap(x):
    even_mask = 0b10101010101010101010101010101010
    odd_mask = 0b01010101010101010101010101010101
    return (x & even_mask) >> 1 | (x & odd_mask) << 1


import unittest


class Test(unittest.TestCase):
    def test_swap_odd_even_bits(self):
        self.assertEqual(pairwise_swap(42), 21)
        self.assertEqual(pairwise_swap(21), 42)
        self.assertEqual(pairwise_swap(43), 23)
        self.assertEqual(pairwise_swap(511), 767)
        self.assertEqual(pairwise_swap(1023), 1023)


if __name__ == "__main__":
    unittest.main()
