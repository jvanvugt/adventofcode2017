from collections import defaultdict


def a(grid, iters=10000):
    x, y = 0, 0
    direction = 0
    n_infected = 0
    for _ in range(iters):
        direction = (direction + int((int(grid[x, y]) - 0.5) * 2)) % 4
        grid[x, y] = not grid[x, y]
        n_infected += int(grid[x, y])
        if direction == 0: y -= 1
        elif direction == 1: x += 1
        elif direction == 2: y += 1
        elif direction == 3: x -= 1
    return n_infected


def b(grid, iters=10000000):
    x, y = 0, 0
    direction = 0
    n_infected = 0
    for _ in range(iters):
        if grid[x, y] == 0: turn = -1
        elif grid[x, y] == 1: turn = 0
        elif grid[x, y] == 2: turn = 1
        elif grid[x, y] == 3: turn = 2
        direction = (direction + turn) % 4
        grid[x, y] = (grid[x, y] + 1) % 4
        n_infected += int(grid[x, y] == 2)
        if direction == 0: y -= 1
        elif direction == 1: x += 1
        elif direction == 2: y += 1
        elif direction == 3: x -= 1
    return n_infected


def main():
    grid = defaultdict(int)
    with open('input22.txt') as f:
        data = f.read().rstrip().splitlines()
    width, height = len(data[0]), len(data)
    hw, hh = width // 2, height // 2
    for y in range(height):
        for x in range(width):
            grid[(x-hw, y-hh)] = 2 * int(data[y][x] == '#')
    print(b(grid))


if __name__ == '__main__':
    main()