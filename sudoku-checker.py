from sudoku import make_puzzle, solve, puzzle_to_grid_alt


def verify_line(line):
    return len(line) == 9 and sum(line) == sum(set(line))


def check_sudoku(grid):
    bad_rows = [row for row in grid if not verify_line(row)]
    grid = list(zip(*grid))
    bad_cols = [col for col in grid if not verify_line(col)]
    squares = []

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [item for items in [row[j:j + 3] for row in grid[i:i + 3]] for item in items]
            squares.append(square)

    bad_squares = [square for square in squares if not verify_line(square)]

    return not (bad_rows or bad_cols or bad_squares)


if __name__ == '__main__':
    puzzle = make_puzzle()
    solution = solve(puzzle)
    sudoku_grid = puzzle_to_grid_alt(solution)

    print(f"Puzzle:\n{puzzle}")
    print(f"Solution:\n{solution}")
    print(f"Sudoku grid:\n{sudoku_grid}")
    print(f"Is solvable: {check_sudoku(sudoku_grid)}")
