import re

def sum_depth(group, level=1):
    return level + sum(sum_depth(c, level+1) for c in group if isinstance(c, list))

def count_garbage(group):
    if not group:
        return 0
    if isinstance(group, str):
        return len(group)
    return sum(count_garbage(c) for c in group)

with open('input9.txt') as f:
    top_group = re.sub('!.', '', f.read().strip().replace('"', '_').replace('{', '[').replace('}', ']'))
    i = 0
    while i < len(top_group):
        if top_group[i] == '<':
            end = top_group.find('>', i+1)
            top_group = top_group[:i] + '"' + top_group[i+1:end] + '"' + top_group[end+1:]
            i = end
        i += 1
    top_group = eval(top_group)
    print(sum_depth(top_group))
    print(count_garbage(top_group))
    