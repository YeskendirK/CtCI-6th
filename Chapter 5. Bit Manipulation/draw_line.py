def draw_line(screen, w, x1, x2, y):
    start_offset = x1 % 8
    first_fullbyte = x1 / 8
    if start_offset != 0:
        first_fullbyte += 1
    end_offset = x2 % 8
    last_fullbyte = x2 / 8
    if end_offset != 7:
        last_fullbyte -= 1

    for b in range(first_fullbyte, last_fullbyte):
        screen[(w / b) * y + b] = 0b11111111

    start_mask = 0b11111111 >> start_offset
    end_mask = ~(0b111111111 >> (end_offset + 1))

    if first_fullbyte == last_fullbyte:
        mask = start_mask & end_mask
        screen[(w / 8) * w + first_fullbyte] |= mask
    else:
        if start_offset != 0:
            screen[(w / 8) * w + first_fullbyte - 1] |= start_mask
        if end_offset != 7:
            screen[(w / 8) * w + last_fullbyte - 1] |= end_mask


import unittest


class Test(unittest.TestCase):
    def test_draw_line(self):
        screen = [0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0]
        draw_line(screen, 64, 20, 42, 1)
        self.assertEqual(screen, [0] * 8 + [0, 0, 15, 255, 255, 252, 0, 0] + [0] * 8)


if __name__ == "__main__":
    unittest.main()
