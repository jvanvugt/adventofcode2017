from day10 import b as knot_hash
from skimage.morphology import label
import numpy as np


def a(word):
    filled = 0
    for i in range(128):
        w = f'{word}-{i}'
        h = knot_hash(w)
        b = f'{int(h, 16):#0128b}'[2:]
        filled += len([c for c in b if int(c)])
    return filled


def b(word):
    filled = 0
    rows = []
    for i in range(128):
        w = f'{word}-{i}'
        h = knot_hash(w)
        b = f'{int(h, 16):0128b}'
        rows.append([int(c) for c in b])
    memory = np.array(rows)
    _, num = label(memory, connectivity=1, return_num=True)
    return num


def main():
    with open('input14.txt') as f:
        word = f.read().rstrip()
    print(b(word))


if __name__ == '__main__':
    main()