from collections import defaultdict
import string


register_names = set(string.ascii_lowercase)


def get_value(token, registers):
    if token in register_names:
        return registers[token]
    else:
        return int(token)


def a(instructions):
    registers = defaultdict(int)
    last_played = None
    recovered = None
    i = 0
    while i >= 0 and i < len(instructions):
        instr = instructions[i].split(' ')
        if instr[0] == 'snd':
            last_played = get_value(instr[1], registers)
        elif instr[0] == 'set':
            registers[instr[1]] = get_value(instr[2], registers)
        elif instr[0] == 'add':
            registers[instr[1]] += get_value(instr[2], registers)
        elif instr[0] == 'mul':
            registers[instr[1]] *= get_value(instr[2], registers)
        elif instr[0] == 'mod':
            registers[instr[1]] %= get_value(instr[2], registers)
        elif instr[0] == 'rcv':
            if get_value(instr[1], registers):
                recovered = last_played
        elif instr[0] == 'jgz':
            if get_value(instr[1], registers) > 0:
                i += get_value(instr[2], registers) - 1
        if recovered and recovered > 0:
            return recovered
        i += 1

def do_instruction(instructions, i, registers, own_q, other_q):
    if i < 0 or i >= len(instructions):
        return i, True
    instr = instructions[i].split(' ')
    blocked = False
    if instr[0] == 'snd':
        other_q.append(get_value(instr[1], registers))
    elif instr[0] == 'set':
        registers[instr[1]] = get_value(instr[2], registers)
    elif instr[0] == 'add':
        registers[instr[1]] += get_value(instr[2], registers)
    elif instr[0] == 'mul':
        registers[instr[1]] *= get_value(instr[2], registers)
    elif instr[0] == 'mod':
        registers[instr[1]] %= get_value(instr[2], registers)
    elif instr[0] == 'rcv':
        if own_q:
            registers[instr[1]] = own_q.pop(0)
        else:
            i -= 1
            blocked = True
    elif instr[0] == 'jgz':
        if get_value(instr[1], registers) > 0:
            i += get_value(instr[2], registers) - 1
    return i + 1, blocked

def b(instructions):
    registers_a = defaultdict(lambda: 0)
    registers_b = defaultdict(lambda: 1)
    queue_a = []
    queue_b = []
    i_a = i_b = 0
    blocked_a = blocked_b = False
    n_sent_b = 0
    while not (blocked_a and blocked_b):
        i_a, blocked_a = do_instruction(instructions, i_a, registers_a, queue_a, queue_b)

        len_before = len(queue_a)
        i_b, blocked_b = do_instruction(instructions, i_b, registers_b, queue_b, queue_a)
        if len(queue_a) > len_before:
            n_sent_b += 1

        if blocked_a and blocked_b:
            i_a, blocked_a = do_instruction(instructions, i_a, registers_a, queue_a, queue_b)
    return n_sent_b


def main():
    with open('input18.txt') as f:
        instructions = f.read().strip().splitlines()
    print(b(instructions))


if __name__ == '__main__':
    main()