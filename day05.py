def a(nums):
    ip = 0
    n_steps = 0
    while 0 <= ip < len(nums):
        instr = nums[ip]
        nums[ip] += 1
        ip += instr
        n_steps += 1
    return n_steps


def b(nums):
    ip = 0
    n_steps = 0
    while 0 <= ip < len(nums):
        instr = nums[ip]
        nums[ip] += -1 if instr >= 3 else 1
        ip += instr
        n_steps += 1
    return n_steps


if __name__ == '__main__':
    with open('input05.txt') as f:
        instructions = list(map(int, f.read().strip().split('\n')))
        print(b(instructions))
