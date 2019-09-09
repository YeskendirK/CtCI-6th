class Listy(object):
    def __init__(self, array):
        self.array = array

    def __getitem__(self, ix):
        if ix < len(self.array):
            return self.array[ix]
        else:
            return -1


def search(listy, value):
    index = 1
    while listy[index] != -1 and listy[index] < value:
        index = index * 2
    return binary_search(listy, value, index // 2, index)


def binary_search(listy, value, low, high):
    while low <= high:
        mid = (low + high) // 2
        middle = listy[mid]
        if middle > value or middle == -1:
            high = mid - 1
        elif middle < value:
            low = mid + 1
        else:
            return mid
    return -1


import unittest


class Test(unittest.TestCase):
    def test_search_listy(self):
        listy = Listy([0, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(search(listy, 5), 5)
        self.assertEqual(search(listy, 7), 7)
        self.assertEqual(search(listy, 10), -1)


if __name__ == "__main__":
    unittest.main()
