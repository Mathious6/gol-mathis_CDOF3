import random
import shutil

from calculation import get_neighbour_count
def create_grid(rows, cols):
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

def update_grid(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            count = get_neighbour_count(grid, row, col)
            if grid[row][col]:
                if count == 2 or count == 3:
                    new_grid[row][col] = 1
            else:
                if count == 3:
                    new_grid[row][col] = 1
    return new_grid

def get_user_grid_size():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    return rows, cols



def get_terminal_size():
    cols, rows = shutil.get_terminal_size()
    return rows, cols  # Note: get_terminal_size returns (columns, rows)

