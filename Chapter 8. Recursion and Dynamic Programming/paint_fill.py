def paint_fill(screen, r, c, ncolor):
    if screen[r][c] == ncolor:
        return False
    paint_fill_color(screen, r, c, screen[r][c], ncolor)


def paint_fill_color(screen, r, c, ocolor, ncolor):
    if r < 0 or c < 0 or r >= len(screen) or c >= len(screen[0]):
        return False

    if screen[r][c] == ocolor:
        screen[r][c] = ncolor
        paint_fill_color(screen, r - 1, c, ocolor, ncolor)
        paint_fill_color(screen, r + 1, c, ocolor, ncolor)
        paint_fill_color(screen, r, c - 1, ocolor, ncolor)
        paint_fill_color(screen, r, c + 1, ocolor, ncolor)
    return True
