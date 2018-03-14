from collections import defaultdict


def a(rules, start, n_steps):
    tape = defaultdict(int)
    pointer = 0
    state = start
    for _ in range(n_steps):
        to_do = rules[state+str(tape[pointer])]
        for action in to_do:
            if action.startswith('Write the value'):
                value = int(action.split(' ')[-1].rstrip('.'))
                tape[pointer] = value
            elif action.startswith('Move one slot to'):
                direction = action.split(' ')[-1].rstrip('.')
                pointer += 1 if direction == 'right' else -1
            elif action.startswith('Continue with state'):
                state = action.split(' ')[-1].rstrip('.')
    return sum(tape.values())
            


def main():
    with open('input25.txt') as f:
        text = f.read().rstrip().splitlines()
    
    start_state = None
    n_steps = None
    rules = defaultdict(list)
    current_state = current_value = None
    for line in text:
        if line.startswith('Begin in state'):
            start_state = line.split(' ')[-1].rstrip('.')
        elif line.startswith('Perform a diagnostic'):
            n_steps = int(line.split(' ')[-2])
        elif line.startswith('In state'):
            current_state = line.split(' ')[-1].rstrip(':')
        elif line.strip().startswith('If the current value'):
            current_value = line.split(' ')[-1].rstrip(':')
        elif line.strip().startswith('-'):
            rules[current_state+current_value].append(line.strip('- '))
    print(a(rules, start_state, n_steps))
    

if __name__ == '__main__':
    main()
