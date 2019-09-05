def coins(n):
    denoms = [25, 10, 5, 1]
    map = [[0] * len(denoms) for j in range(n + 1)]
    return make_change(n, denoms, 0, map)


def make_change(amount, denoms, index, map):
    if map[amount][index] > 0:
        return map[amount][index]
    if index >= len(denoms) - 1:
        return 1
    denom_amount = denoms[index]
    ways = 0
    i = 0
    while i * denom_amount <= amount:
        amount_remain = amount - i * denom_amount
        ways += make_change(amount_remain, denoms, index + 1, map)
        i += 1
    map[amount][index] = ways
    return ways


import unittest


class Test(unittest.TestCase):
    def test_coins(self):
        self.assertEqual(coins(0), 1)
        self.assertEqual(coins(1), 1)
        self.assertEqual(coins(4), 1)
        self.assertEqual(coins(5), 2)
        self.assertEqual(coins(15), 6)
        self.assertEqual(coins(17), 6)
        self.assertEqual(coins(20), 9)
        self.assertEqual(coins(25), 13)
        self.assertEqual(coins(52), 49)


if __name__ == "__main__":
    unittest.main()
