def naive_matrix_search(matrix, val):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == val:
            return row, col
        elif val < matrix[row][col]:
            col -= 1
        else:
            row += 1

    return -1


def find_element(matrix, origin, dest, x):
    if not origin.in_bounds(matrix) or not dest.in_bounds(matrix):
        return None

    if matrix[origin.row][origin.column] == x:
        return origin
    elif not origin.is_before(dest):
        return None

    start = origin.clone()
    diag_dist = min(dest.row - origin.row, dest.column - origin.column)
    end = Coordinate(start.row + diag_dist, start.column + diag_dist)
    p = Coordinate(0, 0)

    while start.is_before(end):
        p.set_to_average(start, end)
        if x > matrix[p.row][p.column]:
            start.row = p.row + 1
            start.column = p.column + 1
        else:
            end.row = p.row - 1
            end.column = p.column - 1

    return partition_and_search(matrix, origin, dest, start, x)


def partition_and_search(matrix, origin, dest, pivot, x):
    lower_left_origin = Coordinate(pivot.row, origin.column)
    lower_left_dest = Coordinate(dest.row, pivot.column - 1)
    upper_right_origin = Coordinate(origin.row, pivot.column)
    upper_right_dest = Coordinate(pivot.row - 1, dest.column)

    lower_left = find_element(matrix, lower_left_origin, lower_left_dest, x)
    if lower_left is None:
        return find_element(matrix, upper_right_origin, upper_right_dest, x)
    return lower_left


def matrix_search(matrix, x):
    origin = Coordinate(0, 0)
    dest = Coordinate(len(matrix) - 1, len(matrix[0]) - 1)
    result = find_element(matrix, origin, dest, x)
    return result.row, result.column


class Coordinate:
    def __init__(self, r, c):
        self.row = r
        self.column = c

    def in_bounds(self, matrix):
        return 0 <= self.row < len(matrix) and 0 <= self.column < len(matrix[0])

    def is_before(self, p):
        return self.column <= p.column and self.row <= p.row

    def clone(self):
        return Coordinate(self.row, self.column)

    def set_to_average(self, min, max):
        self.row = (min.row + max.row) // 2
        self.column = (min.column + max.column) // 2


import unittest


class Test(unittest.TestCase):
    def test_sorted_matrix_search(self):
        mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
               [5, 10, 15, 20, 25, 30, 35, 40, 45],
               [11, 21, 31, 41, 51, 61, 71, 81, 91],
               [13, 23, 33, 43, 53, 63, 73, 83, 93],
               [14, 24, 34, 44, 54, 64, 74, 84, 94],
               [15, 25, 35, 45, 55, 65, 75, 85, 95],
               [16, 26, 36, 46, 56, 66, 77, 88, 99]]
        self.assertEqual(matrix_search(mat, 10), (1, 1))
        self.assertEqual(matrix_search(mat, 13), (3, 0))
        self.assertEqual(matrix_search(mat, 14), (4, 0))
        self.assertEqual(matrix_search(mat, 16), (6, 0))
        self.assertEqual(matrix_search(mat, 56), (6, 4))
        self.assertEqual(matrix_search(mat, 65), (5, 5))
        self.assertEqual(matrix_search(mat, 74), (4, 6))
        self.assertEqual(matrix_search(mat, 99), (6, 8))


if __name__ == "__main__":
    unittest.main()
