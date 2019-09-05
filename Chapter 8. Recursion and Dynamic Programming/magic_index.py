def magic_index(arr):
    return find_index(arr, 0, len(arr) - 1)


def find_index(arr, start, end):
    if end < start:
        return -1
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return find_index(arr, start, mid - 1)
    else:
        return find_index(arr, mid + 1, end)


def magic_index2(arr):
    return find_index2(arr, 0, len(arr) - 1)


def find_index2(arr, start, end):
    if end < start:
        return -1
    midIndex = (start + end) // 2
    midValue = arr[midIndex]

    if midValue == midIndex:
        return midIndex
    else:
        leftIndex = min(midIndex - 1, midValue)
        left = find_index2(arr, start, leftIndex)
        if left > 0:
            return left

        rightIndex = max(midValue, midIndex + 1)
        right = find_index2(arr, rightIndex, end)

        return right


import unittest


class Test(unittest.TestCase):
    def test_magic_index_distinct(self):
        self.assertEqual(magic_index([3, 4, 5]), -1)
        self.assertEqual(magic_index([-2, -1, 0, 2]), -1)
        self.assertEqual(magic_index([-20, 0, 1, 2, 3, 4, 5, 6, 20]), -1)
        self.assertEqual(magic_index([-20, 0, 1, 2, 3, 4, 5, 7, 20]), 7)
        self.assertEqual(magic_index([-20, 1, 2, 3, 4, 5, 6, 20]), 3)

    def test_magic_index(self):
        self.assertEqual(magic_index2([3, 4, 5]), -1)
        self.assertEqual(magic_index2([-2, -1, 0, 2]), -1)
        self.assertEqual(magic_index2([-20, 0, 1, 2, 3, 4, 5, 6, 20]), -1)
        self.assertEqual(magic_index2([-20, 0, 1, 2, 3, 4, 5, 7, 20]), 7)
        self.assertEqual(magic_index2([-20, 0, 1, 3, 4, 5, 6, 20]), 3)
        self.assertEqual(magic_index2([-20, 5, 5, 5, 5, 5, 7, 20]), 5)


if __name__ == "__main__":
    unittest.main()
