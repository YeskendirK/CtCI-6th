def insertion(N, M, i, j):
    all_ones = ~0
    left = all_ones << (j + 1)
    right = (1 << i) - 1
    mask = left | right

    n_cleared = N & mask
    m_shifted = M << i
    return n_cleared | m_shifted


import unittest


class Test(unittest.TestCase):
    def test_insertion(self):
        self.assertEqual(insertion(0b11111111, 0b10, 2, 5), 0b11001011)
        self.assertEqual(insertion(0b00000000, 0b1010, 4, 7), 0b10100000)


if __name__ == "__main__":
    unittest.main()
