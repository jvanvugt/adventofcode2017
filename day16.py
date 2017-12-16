from functools import lru_cache


def a(letters, moves):
    order = list(letters)
    for move in moves:
        if move.startswith('s'):
            amount = int(move[1:])
            order = order[-amount:] + order[:-amount]
        elif move.startswith('x'):
            a, b = list(map(int, move[1:].split('/')))
            order[a], order[b] = order[b], order[a]
        elif move.startswith('p'):
            a, b = move[1:].split('/')
            a = order.index(a)
            b = order.index(b)
            order[a], order[b] = order[b], order[a]
    return ''.join(order)


def b(letters, moves):
    seen = {letters: 0}
    i = 0
    total = 1000000000
    while i < total:
        letters = a(letters, moves)
        i += 1
        if letters not in seen:
            seen[letters] = i
        else:
            cycle_length = i - seen[letters]
            number_of_cycles = ((total - i) // cycle_length)
            left = (total - number_of_cycles * cycle_length) % cycle_length
            return [k for k, v in seen.items() if v == seen[letters] + left][0]

    return letters


def main():
    with open('input16.txt') as f:
        moves = f.read().rstrip().split(',')
    print(b('abcdefghijklmnop', moves))


if __name__ == '__main__':
    main()