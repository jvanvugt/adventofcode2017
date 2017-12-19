import re
import string


def a(diagram):
    pos = [diagram[0].index('|'), 0]
    current_dir = 'D'
    directions = {
        'D': [ 0,  1],
        'U': [ 0, -1],
        'L': [-1,  0],
        'R': [ 1,  0]
    }
    dir_to_char = {
        'D': '|',
        'U': '|',
        'L': '-',
        'R': '-'
    }
    letters = []

    while True:
        if diagram[pos[1]][pos[0]] == ' ':
            break
        if diagram[pos[1]][pos[0]] in string.ascii_uppercase:
            letters.append(d(pos))
            diagram[pos[1]][pos[0]] = dir_to_char[current_dir]

        elif diagram[pos[1]][pos[0]] == '+':
            if current_dir in ('U', 'D'):
                sub = ''.join([diagram[pos[1]][i] for i in range(pos[0]-1, pos[0]+2)])
                side = re.search('[A-Z-]', sub).start()
                if side == 0:
                    current_dir = 'L'
                if side == 2:
                    current_dir = 'R'
            elif current_dir in ('L', 'R'):
                sub = ''.join([diagram[i][pos[0]] for i in range(pos[1]-1, pos[1]+2)])
                side = re.search('[A-Z\|]', sub).start()
                if side == 0:
                    current_dir = 'U'
                if side == 2:
                    current_dir = 'D'
        pos = [pos[0] + directions[current_dir][0], pos[1] + directions[current_dir][1]]
    return ''.join(letters)


def b(diagram):
    pos = [diagram[0].index('|'), 0]
    current_dir = 'D'
    directions = {
        'D': [ 0,  1],
        'U': [ 0, -1],
        'L': [-1,  0],
        'R': [ 1,  0]
    }
    dir_to_char = {
        'D': '|',
        'U': '|',
        'L': '-',
        'R': '-'
    }
    n_steps = 0

    while True:
        if diagram[pos[1]][pos[0]] == ' ':
            break
        if diagram[pos[1]][pos[0]] in string.ascii_uppercase:
            diagram[pos[1]][pos[0]] = dir_to_char[current_dir]

        elif diagram[pos[1]][pos[0]] == '+':
            if current_dir in ('U', 'D'):
                sub = ''.join([diagram[pos[1]][i] for i in range(pos[0]-1, pos[0]+2)])
                side = re.search('[A-Z-]', sub).start()
                if side == 0:
                    current_dir = 'L'
                if side == 2:
                    current_dir = 'R'
            elif current_dir in ('L', 'R'):
                sub = ''.join([diagram[i][pos[0]] for i in range(pos[1]-1, pos[1]+2)])
                side = re.search('[A-Z\|]', sub).start()
                if side == 0:
                    current_dir = 'U'
                if side == 2:
                    current_dir = 'D'
        pos = [pos[0] + directions[current_dir][0], pos[1] + directions[current_dir][1]]
        n_steps += 1
    return n_steps

def main():
    with open('input18.txt') as f:
        diagram = [list(l) for l in f.read().splitlines()]
    print(b(diagram))
    
