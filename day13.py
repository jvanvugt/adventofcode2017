def update_col(col, down, r):
    if not any(col):
        return down
    n = len(col)
    current = max(range(n), key=lambda i: col[i])
    new = current + (1 if down else -1)
    col[new] = 1
    col[current] = 0
    if new == 0 or new == r:
        down = not down
    return down


def update(firewall, down, ranges):
    for i in range(len(firewall)):
        down[i] = update_col(firewall[i], down[i], ranges[i])


def a(scanners):
    max_depth = max(s[1] for s in scanners)
    max_scanner = max(s[0] for s in scanners) + 1
    firewall = [[0 for _ in range(max_depth)] for _ in range(max_scanner)]
    down = [True]*max_scanner
    ranges = [0]*max_scanner
    for i, r in scanners:
        firewall[i][0] = 1
        ranges[i] = r - 1

    severity = 0
    for i in range(max_scanner):
        if firewall[i][0]:
            scanner = [s for s in scanners if s[0] == i][0]
            severity += scanner[1] * scanner[0]
        print(i)
        print(firewall)
        update(firewall, down, ranges)
    return severity


def b(scanners):
    wait = 0
    while True:
        if not any((i + wait) % ((r-1)*2) == 0 for i, r in scanners):
            return wait
        wait += 1


def main():
    with open('input13.txt') as f:
        scanners = [tuple(map(int, l.split(': '))) for l in f.read().rstrip().splitlines()]
    print(b(scanners))


if __name__ == '__main__':
    main()
