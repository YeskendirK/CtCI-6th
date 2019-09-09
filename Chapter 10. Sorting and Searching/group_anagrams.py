def group_anagrams(strings):
    pairs = [(s, sorted(s)) for s in strings]
    pairs.sort(key=lambda x: x[1])

    return [x[0] for x in pairs]

import unittest

class Test(unittest.TestCase):
  def test_group_anagrams(self):
    strings = ["cat", "bat", "rat", "arts", "tab", "tar", "car", "star"]
    self.assertEqual(group_anagrams(strings),
              ["bat", "tab", "car", "cat", "arts", "star", "rat", "tar"])

if __name__ == "__main__":
  unittest.main()
