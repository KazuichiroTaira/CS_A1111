# Y1 SUMMER 2021
# Basic Course in Programming Y1
# Author: Vilma Kahri
# Template for exercise 6.3

from grids import GRID_NAMES, GRID_RETURNS, GRIDS, GRIDS_BIG, GRIDS_SMALL

GRID_SIZE = 9  # Length of one side of the sudoku
SUBGRID_SIZE = 3  # Length of one side of a cell of the sudoku


def check_part(list_of_num):

    for num in list_of_num:

        if num is None:
            continue

        count_num = list_of_num.count(num)
        if count_num != 1:
            return False

    return True


def check_sudoku_grid(grid):

    """
    Parameter : GRID_SIZE * GRID_SIZE two-dimensional list
    Return value : Boolean (True/False)

    Checks whether a sudoku grid is valid
    ie. doesn't contain any duplicates (besides None)
    in any row, column or cell.
    """
    # Implement your code here

    # Check line
    for line in grid:
        correct = check_part(line)
        if correct is False:
            return False

    # Check column
    for i in range(GRID_SIZE):  # len(grid[0]): GRID_SIZE
        column = []
        for line in grid:
            column.append(line[i])

        correct = check_part(column)
        if correct is False:
            return False

    # Check cube
    for row_idx in range(0, GRID_SIZE, SUBGRID_SIZE):
        for col_idx in range(0, GRID_SIZE, SUBGRID_SIZE):
            # print(f'NEW CUBE starting at {row_idx}, {col_idx}')
            cube = []
            for i in range(row_idx, row_idx + SUBGRID_SIZE):
                for j in range(col_idx, col_idx + SUBGRID_SIZE):
                    cube.append(grid[i][j])

            correct = check_part(cube)
            if correct is False:
                return False

    return True


def print_grid(grid):
    for i in range(GRID_SIZE):
        row = ""
        for j in range(GRID_SIZE):
            try:
                val = int(grid[i][j])
            except TypeError:
                val = "_"
            except ValueError:
                val = grid[i][j]
            row += "{} ".format(val)
            if j % SUBGRID_SIZE == SUBGRID_SIZE - 1:
                row += " "
        print(row)
        if i % SUBGRID_SIZE == SUBGRID_SIZE - 1:
            print()


def main():
    i = 0
    for grid in GRIDS:
        is_valid = check_sudoku_grid(grid)
        print(f"This grid {GRID_NAMES[i]}.")
        print(f"Your function should return:{GRID_RETURNS[i]}")
        print(f"Your function returns:{is_valid}")
        print_grid(grid)
        i += 1


    """ 
    Extra challenge: 

    If you want to try your check_sudoku_grid with a different sized grid,
    you can change the GRID_SIZE and SUBGRID_SIZE and the list to go 
    through in the main function.

    Big grids :         GRID_SIZE = 16
                        SUBGRID_SIZE = 4
    list of grids:      GRIDS_BIG

    Small grids:        GRID_SIZE = 4
                        SUBGRID_SIZE = 2
    list of grids:      GRIDS_SMALL

    """


main()