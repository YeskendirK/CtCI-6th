# Solution -1: Brute Force
def triple_step(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return triple_step(n - 3) + triple_step(n - 2) + triple_step(n - 1)


# Solution-2: Using Memoization
def triple_step_memo(n):
    memo = [-1] * (n + 1)
    return count_ways(n, memo)


def count_ways(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = count_ways(n - 1, memo) + count_ways(n - 2, memo) + count_ways(n - 3, memo)
        return memo[n]


import unittest


class Test(unittest.TestCase):
    def test_triple_step(self):
        self.assertEqual(triple_step_memo(3), 4)
        self.assertEqual(triple_step_memo(7), 44)


if __name__ == "__main__":
    unittest.main()
