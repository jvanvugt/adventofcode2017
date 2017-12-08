import sys
from math import sqrt, ceil


def a(number):
    minh = maxh = minv = maxv = 0
    cur = [0, 0]
    i = 1
    while True:
        while cur[0] <= maxh:
            if i == number: return cur
            cur[0] += 1
            i += 1
        maxh += 1
        while cur[1] <= maxv:
            if i == number: return cur
            cur[1] += 1
            i += 1
        maxv += 1
        while cur[0] >= minh:
            if i == number: return cur
            cur[0] -= 1
            i += 1
        minh -= 1
        while cur[1] >= minv:
            if i == number: return cur
            cur[1] -= 1
            i += 1
        minv -= 1


def neighbours(coord):
    return [[coord[0], coord[1]+1],
            [coord[0]+1, coord[1]],
            [coord[0]+1, coord[1]+1],
            [coord[0], coord[1]-1],
            [coord[0]-1, coord[1]],
            [coord[0]-1, coord[1]-1],
            [coord[0]+1, coord[1]-1],
            [coord[0]-1, coord[1]+1]]

def b(number):
    s = round(ceil(sqrt(number)))
    grid = [[0 for _ in range(s)] for _ in range(s)]
    half = s // 2
    cur = [half, half]
    minh = maxh = minv = maxv = half
    while True:
        while cur[0] <= maxh:
            n = max(1, sum(grid[c[0]][c[1]] for c in neighbours(cur)))
            grid[cur[0]][cur[1]] = n
            if n > number: return n
            cur[0] += 1
        maxh += 1
        while cur[1] <= maxv:
            n = sum(grid[c[0]][c[1]] for c in neighbours(cur))
            grid[cur[0]][cur[1]] = n
            if n > number: return n
            cur[1] += 1
        maxv += 1
        while cur[0] >= minh:
            n = sum(grid[c[0]][c[1]] for c in neighbours(cur))
            grid[cur[0]][cur[1]] = n
            if n > number: return n
            cur[0] -= 1
        minh -= 1
        while cur[1] >= minv:
            n = sum(grid[c[0]][c[1]] for c in neighbours(cur))
            grid[cur[0]][cur[1]] = n
            if n > number: return n
            cur[1] -= 1
        minv -= 1


def manhattan(coord):
    return sum(abs(c) for c in coord)


if __name__ == '__main__':
        # print(manhattan(a(int(sys.argv[1]))))
    print(b(int(sys.argv[1])))
