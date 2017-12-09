n_garbage = 0

def find_closing_angled(group, should_count=False):
    global n_garbage
    ignore = False
    for i, char in enumerate(group):
        if ignore:
            if should_count:
                n_garbage -= 2
            ignore = False
            continue
        if char == '!':
            ignore = True
        elif char == '>':
            if should_count:
                n_garbage += i - 1
            return i


def find_closing_brace(group):
    deep = 0
    i = 0
    while i < len(group):
        char = group[i]
        if char == '!':
            i += 1
        elif char == '<':
            i = i + find_closing_angled(group[i:])
        elif char == '{':
            deep += 1
        elif char == '}':
            deep -= 1
            if deep == 0:
                return i
        i += 1


def sum_nested_groups(group, level=1):
    if group.startswith('<'):
        return 0
    i = 0
    group = group[1:-1]
    sums = []
    while i < len(group):
        if group[i] == '{':
            end = i + find_closing_brace(group[i:])
            sums.append(sum_nested_groups(group[i:end+1], level + 1))
            i = end + 1
        elif group[i] == '<':
            end = i + find_closing_angled(group[i:], True)
            i = end + 1
        elif group[i] == ',':
            i += 1
        else:
            raise ValueError('Not opening char ' + group + ' at ' + str(i))
    return level + sum(sums)


with open('input9.txt') as f:
    top_group = f.read().strip()
    print(sum_nested_groups(top_group))
    print(n_garbage)
