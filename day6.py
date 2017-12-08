def a(blocks):
    before = set()
    while tuple(blocks) not in before:
        before.add(tuple(blocks))
        i = max(range(len(blocks)), key=lambda i: blocks[i])
        n_blocks = blocks[i]
        blocks[i] = 0
        while n_blocks:
            i = (i+1) % len(blocks)
            blocks[i] += 1
            n_blocks -= 1
    return len(before)


def b(blocks):
    before = []
    while tuple(blocks) not in before:
        before.append(tuple(blocks))
        i = max(range(len(blocks)), key=lambda i: blocks[i])
        n_blocks = blocks[i]
        blocks[i] = 0
        while n_blocks:
            i = (i+1) % len(blocks)
            blocks[i] += 1
            n_blocks -= 1
    return len(before) - before.index(tuple(blocks))


if __name__ == '__main__':
    with open('input6.txt') as f:
        input = list(map(int, f.read().split('\t')))
        print(a(input))
