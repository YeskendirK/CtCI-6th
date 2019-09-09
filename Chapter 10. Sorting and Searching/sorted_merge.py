def sorted_merge(A, B):
    b = len(B) - 1
    a = len(A) - len(B) - 1
    while a >= 0 and b >= 0:
        if A[a] >= B[b]:
            A[a+b+1] = A[a]
            a -= 1
        else:
            A[a+b+1] = B[b]
            b -= 1
    while b >= 0:
        A[b] = B[b]
        b -= 1
    return

import unittest

class Test(unittest.TestCase):
  def test_sorted_merge(self):
    a = [33, 44, 55, 66, 88, 99, None, None, None]
    b = [11, 22, 77]
    sorted_merge(a, b)
    self.assertEqual(a, [11, 22, 33, 44, 55, 66, 77, 88, 99])
    a = [11, 22, 55, 66, 88, None, None, None]
    b = [33, 44, 99]
    sorted_merge(a, b)
    self.assertEqual(a, [11, 22, 33, 44, 55, 66, 88, 99])

if __name__ == "__main__":
  unittest.main()

