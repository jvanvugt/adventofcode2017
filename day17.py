def a(steps):
    buffer = [0]
    pos = 0
    for i in range(1, 2018):
        pos = (pos + steps) % len(buffer)
        buffer.insert(pos + 1, i)
        pos = pos + 1
    return buffer[pos+1]


def b(steps):
    pos = 0
    zero_pos = 0
    after_zero = None
    length = 1
    for i in range(1, 50000000):
        pos = (pos + steps) % length
        if pos < zero_pos:
            zero_pos += 1
        elif pos == zero_pos:
            after_zero = i
        pos = pos + 1
        length += 1
    return after_zero


def main():
    with open('input17.txt') as f:
        steps = int(f.read().strip())
    start = time.time()


if __name__ == '__main__':
    main()