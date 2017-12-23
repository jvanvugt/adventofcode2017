def a(instructions):
    registers = {l:0 for l in 'abcdefgh'}
    i = 0
    get_value = lambda s: registers[s] if s in registers else int(s)
    n_mul = 0
    while i >= 0 and i < len(instructions):
        ins = instructions[i]
        if ins[0] == 'set':
            registers[ins[1]] = get_value(ins[2])
        elif ins[0] == 'sub':
            registers[ins[1]] -= get_value(ins[2])
        elif ins[0] == 'mul':
            registers[ins[1]] *= get_value(ins[2])
            n_mul += 1
        elif ins[0] == 'jnz':
            if get_value(ins[1]):
                i += get_value(ins[2]) - 1
        i += 1
    return n_mul


def is_prime(n):
    """Returns True if n is prime."""
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def b():
    return sum(not is_prime(n) for n in range(106500, 123500+1, 17))


def main():
    with open('input23.txt') as f:
        instructions = [ins.split() for ins in f.read().rstrip().splitlines()]
    print(a(instructions))
    print(b())


if __name__ == '__main__':
    main()
