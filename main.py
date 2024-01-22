import time
import os
import random
from grid import get_user_grid_size, get_terminal_size
def create_grid(rows, cols):
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]


def print_grid(grid):
    for row in grid:
        print('.'.join('#' if cell else ' ' for cell in row))


def get_neighbour_count(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_row, new_col = row + i, col + j
            if 0 <= new_row < rows and 0 <= new_col < cols:
                count += grid[new_row][new_col]
    return count


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


def all_cells_dead(grid):
    """Check if all cells in the grid are dead."""
    return all(cell == 0 for row in grid for cell in row)


def main():
    mode = int(input("To load grid size dynamically type 1, otherwise enter another number: "))
    if mode == 1 :
        rows, cols = get_terminal_size()
    else : 
        rows, cols = get_user_grid_size()
    
    grid = create_grid(rows, cols)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_grid(grid)
        if all_cells_dead(grid):
            print("All cells are dead. Game Over.")
            break
        grid = update_grid(grid)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
