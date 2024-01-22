def print_grid(grid):
    for row in grid:
        print('.'.join('#' if cell else ' ' for cell in row))