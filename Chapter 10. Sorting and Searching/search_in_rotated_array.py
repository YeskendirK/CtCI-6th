def rotated_search(arr, x, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if right < left:
        return -1

    mid = (left + right) // 2
    if x == arr[mid]:
        return mid

    if arr[left] < arr[mid]:
        if arr[left] <= x < arr[mid]:
            return rotated_search(arr, x, left, mid - 1)
        else:
            return rotated_search(arr, x, mid + 1, right)
    elif arr[mid] < arr[right]:
        if arr[mid] < x <= arr[right]:
            return rotated_search(arr, x, mid + 1, right)
        else:
            return rotated_search(arr, x, left, mid - 1)
    elif arr[mid] == left:
        if arr[mid] != arr[right]:
            return rotated_search(arr, x, mid + 1, right)
        else:
            result = rotated_search(arr, x, left, mid - 1)
            if result == -1:
                return rotated_search(arr, x, mid + 1, right)
            else:
                return result
    return -1


import unittest


class Test(unittest.TestCase):
    def test_rotated_search(self):
        array = [55, 60, 65, 70, 75, 80, 85, 90, 95, 15, 20, 25, 30, 35, 40, 45]
        self.assertEqual(rotated_search(array, 55), 0)
        self.assertEqual(rotated_search(array, 60), 1)
        self.assertEqual(rotated_search(array, 90), 7)
        self.assertEqual(rotated_search(array, 95), 8)
        self.assertEqual(rotated_search(array, 15), 9)
        self.assertEqual(rotated_search(array, 30), 12)
        self.assertEqual(rotated_search(array, 45), 15)


if __name__ == "__main__":
    unittest.main()
