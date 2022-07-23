grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def print_grid(grid):
    for row in grid:
        print(*row)


def possible_solution(y, x, n):
    # Check if n exist in horizontal
    # If exist return False (Not possible solution)
    for i in range(9):
        if grid[y][i] == n:
            return False

    # Check if n exist in vertical
    # if exist return False (Not possible solution)
    for i in range(9):
        if grid[i][x] == n:
            return False

    # check the 3x3 local grid
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False

    # Return True if pass all checks
    return True


def solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible_solution(y, x, n):
                        grid[y][x] = n
                        solve(grid)
                        grid[y][x] = 0
                return

    print_grid(grid)
    input()


solve(grid)
