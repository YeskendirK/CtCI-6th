def sparse_search(arr, val, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        while arr[mid] == '':
            mid -= 1
        if val < arr[mid]:
            high = mid - 1
            while high >= 0 and arr[high] == '':
                high -= 1
        elif val > arr[mid]:
            low = mid + 1
            while low < len(arr) and arr[low] == '':
                low += 1
        else:
            return mid
    return -1


arr = ['all', '', '', '', 'ball', '', '', 'cell', '', '', 'door', '']


import unittest


class Test(unittest.TestCase):
    def test_sparse_search(self):
        array = ['all', '', '', '', 'ball', '', '', 'cell', '', '', 'door', '']
        self.assertEqual(sparse_search(array, 'all'), 0)
        self.assertEqual(sparse_search(array, 'ball'), 4)
        self.assertEqual(sparse_search(array, 'cell'), 7)
        self.assertEqual(sparse_search(array, 'door'), 10)
        self.assertEqual(sparse_search(array, 'key'), -1)


if __name__ == "__main__":
    unittest.main()
