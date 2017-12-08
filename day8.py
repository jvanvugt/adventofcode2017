from collections import defaultdict
import re

def a(instructions):
    for line in instructions:
        var, _, _, _, var2, *_ = line.split(' ')
        if var not in dir():
            exec(f'{var} = 0')
        if var2 not in dir():
            exec(f'{var2} = 0')
        if eval(line.split(' if ')[1]):
            exec(f"{var} = {line.split(' if ')[0].replace('inc', '+').replace('dec', '-')}")
    return max(v for v in locals().values() if isinstance(v, int))


def b(instructions):
    variables = defaultdict(int)
    max_all_time = 0
    for line in instructions:
        var, what, amount, _, var2, op, num = line.split(' ')
        if eval(f'{variables[var2]} {op} {num}'):
            if what == 'inc':
                variables[var] += int(amount)
            else:
                variables[var] -= int(amount)
        max_all_time = max(max_all_time, max(variables.values()))
    return max_all_time


with open('input8.txt') as f:
    instructions = f.read().strip().splitlines()
    print(b(instructions))
