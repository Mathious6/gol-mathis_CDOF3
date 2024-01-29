import time
import os
import random


def create_grid(rows, cols):
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]


def print_grid(grid, dead, live):
    for row in grid:
        print('.'.join(live if cell else dead for cell in row))


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


def main():
    rows, cols = 10, 10
    grid = create_grid(rows, cols)

    print("Please enter a marker for dead cells or press enter for default. The default is an empty space")
    dead = input("Dead marker : ")
    if dead == '':
        dead = ' '


    print("Please enter a marker for alive cells. The default is #")
    live = input("Live marker : ")
    if live == '':
        live = '#'

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_grid(grid, dead, live)
        grid = update_grid(grid)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
