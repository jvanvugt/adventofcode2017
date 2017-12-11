from math import floor, ceil


# Thanks to https://www.redblobgames.com/grids/hexagons/#conversions
DIRECTIONS = {'n': [1, 0, -1], 'ne': [1, -1, 0], 'se': [0, -1, 1],
              's': [-1, 0, 1], 'sw': [-1, 1, 0], 'nw': [0, 1, -1]}


def get_lost(dirs):
    cur = [0, 0, 0]
    max_distance = 0
    for d in dirs:
        move = DIRECTIONS[d]
        for i in range(3):
            cur[i] += move[i]
            max_distance = max(max_distance, calc_dist(cur))
    return cur, max_distance


def calc_dist(coor):
    return sum(abs(c) for c in coor) / 2


def a(dirs):
    """
    >>> a(['ne']*3)
    3
    >>> a(['ne', 'ne', 'sw', 'sw'])
    0
    >>> a(['ne', 'ne', 's', 's'])
    2
    >>> a(['se', 'sw', 'se', 'sw', 'sw'])
    3
    """
    pos, md = get_lost(dirs)
    return calc_dist(pos), md

def main():
    with open('input11.txt') as f:
        dirs = f.read().strip().split(',')
    print(a(dirs))


if __name__ == '__main__':
    main()
