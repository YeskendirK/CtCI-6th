import unittest


def get_next(n):
    c = n
    c0 = 0  # number of trailing zeros
    c1 = 0

    while (c & 1 == 0) and (c != 0):
        c = c >> 1
        c0 += 1

    while c & 1 == 1:
        c1 += 1
        c = c >> 1

    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    p = c0 + c1
    n = n | (1 << p)  # Flip rightmost non-trailing zero
    n = n & ~((1 << p) - 1)  # clear all bits to the right of p
    n = n | ((1 << (c1 - 1)) - 1)

    return n


def get_prev(n):
    temp = n
    c0 = 0
    c1 = 0

    while temp & 1 == 1:
        c1 += 1
        temp = temp >> 1
    if temp == 0:
        return -1

    while temp & 1 == 0 and temp != 0:
        c0 += 1
        temp = temp >> 1

    p = c0 + c1
    n = n & ((~0) << (p + 1))
    mask = (1 << (c1 + 1)) - 1
    n = n | (mask << (c0 - 1))

    return n


def next_numbers(n):
    return get_prev(n), get_next(n)


class Test(unittest.TestCase):
    def test_next_numbers(self):
        self.assertEqual(next_numbers(8), (4, 16))
        self.assertEqual(next_numbers(12), (10, 17))
        self.assertEqual(next_numbers(143), (124, 151))
        self.assertEqual(next_numbers(159), (126, 175))


if __name__ == "__main__":
    unittest.main()
