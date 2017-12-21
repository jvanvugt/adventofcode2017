import numpy as np


def divide(grid, size):
    subgrids = []
    for i in range(0, len(grid), size):
        for j in range(0, len(grid), size):
            subgrids.append(grid[i:i+size, j:j+size])
    return subgrids


def to_grid_string(array):
    rows = [''.join(['#' if v else '.' for v in row]) for row in array]
    return '/'.join(rows)


def from_grid_string(s):
    rows = s.split('/')
    return np.array([[v == '#' for v in row] for row in rows])


def transform(grids, rules):
    new_grids = []
    for grid in grids:
        for orientation in (grid, 
                            np.fliplr(grid),
                            np.flipud(grid),
                            np.rot90(grid, k=1),
                            np.rot90(grid, k=2),
                            np.rot90(grid, k=3),
                            np.fliplr(np.rot90(grid, k=1)),
                            np.fliplr(np.rot90(grid, k=3))):
            s = to_grid_string(orientation)
            if s in rules:
                new_grids.append(from_grid_string(rules[s]))
                break
    return new_grids


def tile(grids):
    size = int(np.sqrt(len(grids)))
    grids = [np.hstack(grids[i:i+size]) for i in range(0, len(grids), size)]
    return np.vstack(grids)


def a(rules, iters=5):
    grid = np.array([[False, True, False],
                     [False, False, True],
                     [True, True, True]])
    for _ in range(iters):
        size = grid.shape[0]
        subgrids = divide(grid, 2 if size % 2 == 0 else 3)
        subgrids = transform(subgrids, rules)
        grid = tile(subgrids)
    return grid.sum()


def main():
    with open('input21.txt') as f:
        lines = f.read().rstrip().splitlines()
        rules = [line.split(' => ') for line in lines]
        rules = dict(rules)
    print(a(rules))
    print(a(rules, iters=18))
    


if __name__ == '__main__':
    main()