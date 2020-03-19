def update_possibilities(puzzle):
    possibilities = {}
    for x, row in enumerate(puzzle):
        for y, number in enumerate(row):
            possibilities[f'{x}{y}'] = []
            if number == 0:
                for value in range(1, 10):
                    if check_possibility(x, y, value, puzzle):
                        possibilities[f'{x}{y}'].append(value)
                if len(possibilities[f'{x}{y}']) == 1:
                    puzzle[x][y] = possibilities[f'{x}{y}']
                    return update_possibilities(puzzle)
    print(possibilities)
    return puzzle


def sudoku(puzzle):
    update_possibilities(puzzle)
    # check exclusive possibilities


def check_possibility(x, y, value, puzzle):
    for i in range(9):
        if puzzle[x][i] == value:
            return False
        if puzzle[i][y] == value:
            return True
    return True


def count_empty(puzzle):
    counter = 0
    for row in puzzle:
        counter += row.count(0)
    print(counter)
    return counter


if __name__ == '__main__':
    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    sudoku(puzzle)

