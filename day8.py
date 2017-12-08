from collections import defaultdict
import re


def a(instructions):
    variables = defaultdict(int)
    for line in instructions:
        var, what, amount, _, var2, op, num = line.split(' ')
        if var not in variables:
            variables[var] = 0
        if var2 not in variables:
            variables[var2] = 0
        if eval(f'{variables[var2]} {op} {num}'):
            if what == 'inc':
                variables[var] += int(amount)
            else:
                variables[var] -= int(amount)
    return max(variables.values())


def b(instructions):
    variables = defaultdict(int)
    max_all_time = 0
    for line in instructions:
        var, what, amount, _, var2, op, num = line.split(' ')
        if var not in variables:
            variables[var] = 0
        if var2 not in variables:
            variables[var2] = 0
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
