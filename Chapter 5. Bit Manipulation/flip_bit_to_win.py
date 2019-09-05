# Solution-1: Brute Force

def longest_seq(n):
    seq = get_alternate_seq(n)
    out = get_longest_seq(seq)
    return out


def get_alternate_seq(n):
    searching = 0
    counter = 0
    seq = []
    i = n.bit_length()
    while i >= 0:
        if n & 1 != searching:
            seq.append(counter)
            counter = 0
            searching = n & 1
        counter += 1
        n = n >> 1
        i -= 1
    return seq


def get_longest_seq(seq):
    max_seq = 1
    i = 0
    while i < len(seq):
        this = seq[i]
        left = seq[i - 1] if i > 0 else 0
        right = seq[i + 1] if i < len(seq) else 0
        if this == 1:
            current = left + 1 + right
        elif this >= 1:
            current = 1 + max(left, right)
        elif this == 0:
            current = max(left, right)
        max_seq = max(current, max_seq)
        i += 2
    return max_seq


# Solution-2: Optimized

def flip_bit(n):
    max_seq = 1
    prev_seq = 0
    current_seq = 0
    i = n.bit_length()
    while i >= 0:
        if n & 1 == 1:
            current_seq += 1
        elif n & 1 == 0:
            prev_seq = 0 if n & 2 == 0 else current_seq
            current_seq = 0
        max_seq = max(max_seq, prev_seq + 1 + current_seq)
        n = n >> 1
        i -= 1
    return max_seq


import unittest


class Test(unittest.TestCase):
    def test_longest_sequence_after_flip(self):
        self.assertEqual(flip_bit(0b1111100), 6)
        self.assertEqual(flip_bit(0b0111111), 7)
        self.assertEqual(flip_bit(0b1011110111001111110), 8)


if __name__ == "__main__":
    unittest.main()
