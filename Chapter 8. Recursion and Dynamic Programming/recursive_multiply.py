# Solution-0

def multiply(a, b):
    if a == 1:
        return b
    else:
        return b + multiply(a - 1, b)


# Solution 1

def minProduct(a, b):
    bigger = b if a < b else a
    smaller = a if a < b else b
    return minProductHelper(smaller, bigger)


def minProductHelper(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    # Compute half. If uneven, compute other half. If even, double it
    s = smaller >> 1  # divide by 2
    side1 = minProduct(s, bigger)
    side2 = side1
    if smaller % 2 == 1:
        side2 = minProductHelper(smaller - s, bigger)

    return side1 + side2


# Solution 2

def minProduct2(a, b):
    bigger = b if a < b else a
    smaller = a if a < b else b
    return minProduct2Helper(smaller, bigger, {})


def minProduct2Helper(smaller, bigger, memo):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    elif smaller in memo:
        return memo[smaller]

    # Compute half. If uneven, compute other half. If even double it
    s = smaller >> 1
    side1 = minProduct2Helper(s, bigger, memo)
    side2 = side1
    if smaller % 2 == 1:
        side2 = minProduct2Helper(smaller - s, bigger, memo)
    # sum and cache
    memo[smaller] = side1 + side2
    return memo[smaller]


# Solution 3

def minProduct3(a, b):
    bigger = b if a < b else a
    smaller = a if a < b else b
    return minProduct3Helper(smaller, bigger)


def minProduct3Helper(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    s = smaller >> 1
    halfProd = minProduct3Helper(s, bigger)
    if smaller % 2 == 0:
        return halfProd + halfProd
    else:
        return halfProd + halfProd + bigger


import unittest


class Test(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(minProduct3(2, 2), 4)
        self.assertEqual(minProduct3(1, 125), 125)
        self.assertEqual(minProduct3(7, 11), 77)
        self.assertEqual(minProduct3(10000000010, 21), 210000000210)


if __name__ == "__main__":
    unittest.main()
