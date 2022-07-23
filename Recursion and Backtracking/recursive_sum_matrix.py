mat = [[1, 2, 3,4], [1, 2, 3,4], [1, 2, 3,4]]


def sum_matrix(row, col, sum, mat):
    sum += mat[row][col]

    if row == len(mat) - 1 and col == len(mat[0]) - 1:
        print(sum)
        return

    if row >= len(mat) or col >= len(mat[0]):
        return

    if col < len(mat[0]) - 1:
        col += 1
    else:
        row += 1
        col = 0
    sum_matrix(row, col, sum, mat)


sum_matrix(0, 0, 0, mat)
