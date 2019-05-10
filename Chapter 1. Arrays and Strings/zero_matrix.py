def zeroMatrix(matrix):
    col_len = len(matrix[0])
    row_len = len(matrix)
    zeroes = []
    # find zeoes
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == 0:
                zeroes.append([i, j])

    # Nullify
    for elem in zeroes:
        row, col = elem[0], elem[1]
        matrix[row] = [0] * col_len
        for k in range(row_len):
            matrix[k][col] = 0

    return matrix


matrix = [[0, 2, 3], [4, 5, 6], [7, 8, 9]]
print(zeroMatrix(matrix))
