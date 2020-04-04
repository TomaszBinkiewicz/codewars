class SudokuSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.possibilities = {}

    def set_value(self, x, y, value):
        self.puzzle[x][y] = value
        self.possibilities[f'{x}{y}'] = []
        self.update_possibilities()

    def check_possibility(self, x, y, value):
        # line possibilities
        for i in range(9):
            if self.puzzle[x][i] == value:
                return False
            if self.puzzle[i][y] == value:
                return False
        # square possibilities
        square_row = y % 3
        square_col = x % 3
        for i in range(-square_col, 3 - square_col):
            for j in range(-square_row, 3 - square_row):
                if self.puzzle[x + i][y + j] == value:
                    return False
        return True

    def check_exclusive_possibility(self, x, y, value):
        for i in range(9):
            if i != y and self.possibilities[f'{x}{i}'].count(value) > 0:
                return False
            if i != x and self.possibilities[f'{i}{y}'].count(value) > 0:
                return False
        return True

    def set_from_exclusive_possibility(self, x, y):
        for value in self.possibilities[f'{x}{y}']:
            if self.check_exclusive_possibility(x, y, value):
                self.set_value(x, y, value)

    def update_possibilities(self):
        self.possibilities.clear()
        for x, row in enumerate(self.puzzle):
            for y, number in enumerate(row):
                self.possibilities[f'{x}{y}'] = []
                if number == 0:
                    for value in range(1, 10):
                        if self.check_possibility(x, y, value):
                            self.possibilities[f'{x}{y}'].append(value)
                    if len(self.possibilities[f'{x}{y}']) == 1:
                        self.set_value(x, y, self.possibilities[f'{x}{y}'][0])

    def count_empty(self):
        counter = 0
        for row in self.puzzle:
            counter += row.count(0)
        return counter

    def count_possibilities(self):
        counter = 0
        for x in range(9):
            for y in range(9):
                counter += len(self.possibilities[f'{x}{y}'])
        return counter

    def solve(self):
        empty_count = 81
        poss_count = 81 * 9
        while empty_count != 0:
            self.update_possibilities()
            for x in range(9):
                for y in range(9):
                    self.set_from_exclusive_possibility(x, y)
            empty_count = self.count_empty()
            new_poss_count = self.count_possibilities()
            if poss_count == new_poss_count:
                print("I can't solve this")
                break
            poss_count = new_poss_count


def sudoku(puzzle):
    solver = SudokuSolver(puzzle)
    for row in puzzle:
        print(row)
    solver.solve()
    print("Solved")
    for row in puzzle:
        print(row)


if __name__ == '__main__':
    new_puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
                  [0, 0, 0, 4, 1, 9, 0, 0, 5],
                  [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    sudoku(new_puzzle)
