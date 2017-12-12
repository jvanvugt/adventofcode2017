from collections import defaultdict


def count_groups(connections):
    all_nodes = set(connections.keys())
    n_groups = 0
    while all_nodes:
        node = next(iter(all_nodes))
        connected = connected_to(connections, start=node)
        all_nodes -= connected
        n_groups += 1
    return n_groups


def connected_to(connections, start=0):
    seen = set()
    to_expand = [start]
    while to_expand:
        node = to_expand.pop(0)
        for child in connections[node]:
            if child not in seen:
                seen.add(child)
                to_expand.append(child)
    return seen


def n_connected_0(connections):
    return len(connected_to(connections, 0))


with open('input12.txt') as f:
    connections = defaultdict(list)
    for line in f.read().strip().splitlines():
        a, rest = line.split(' <-> ')
        a = int(a)
        for b in map(int, rest.split(', ')):
            connections[a].append(b)
            connections[b].append(a)
    print(n_connected_0(connections))
    print(count_groups(connections))
