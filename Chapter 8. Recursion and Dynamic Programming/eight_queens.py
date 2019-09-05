GRID_SIZE = 8


def place_queens(row, columns, results):
    if row == GRID_SIZE:
        results.append(columns)
    else:
        for col in range(0, GRID_SIZE):
            if check_valid(columns, row, col):
                columns[row] = col
                place_queens(row + 1, columns, results)
    return


def check_valid(columns, row1, col1):
    for row2 in range(0, row1):
        col2 = columns[row2]
        if col1 == col2:
            return False

        col_distance = abs(col1 - col2)
        row_distance = row1 - row2
        if row_distance == col_distance:
            return False

        return True
