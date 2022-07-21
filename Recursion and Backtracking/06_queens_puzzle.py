rows_count = 8
cols_count = 8
puzzle = [['-'] * cols_count for _ in range(rows_count)]


def print_result(result):
    for r in puzzle:
        print(*r)
    print()


def can_place_queen(row, col, rows, cols, right_diagonals, left_diagonals):
    if row in rows:
        return False
    if col in cols:
        return False
    if (col + row) in right_diagonals:
        return False
    if (col - row) in left_diagonals:
        return False
    return True


def set_queen(row, col, puzzle, rows, cols, right_diagonals, left_diagonals):
    puzzle[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_diagonals.add(col - row)
    right_diagonals.add(col + row)


def remove_queen(row, col, puzzle, rows, cols, right_diagonals, left_diagonals):
    puzzle[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_diagonals.remove(col - row)
    right_diagonals.remove(col + row)


def queen_puzzle(row, col, puzzle, rows, cols, right_diagonals, left_diagonals):
    if row >= rows_count:
        print_result(puzzle)
        return

    for col in range(cols_count):
        if can_place_queen(row, col, rows, cols, right_diagonals, left_diagonals):
            set_queen(row, col, puzzle, rows, cols, right_diagonals, left_diagonals)

            queen_puzzle(row + 1, col, puzzle, rows, cols, right_diagonals, left_diagonals)

            remove_queen(row, col, puzzle, rows, cols, right_diagonals, left_diagonals)


queen_puzzle(0, 0, puzzle, set(), set(), set(), set())
