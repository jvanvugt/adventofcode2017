from collections import defaultdict, Counter


def find_other(weights):
    """
    >>> find_other([3, 3, 3])
    -1
    >>> find_other([3, 3, 2])
    2
    """
    c = Counter(weights)
    if c.most_common(1)[0][1] == len(weights):
        return -1
    return weights.index(c.most_common(2)[-1][0])


def a(discs):
    balance = defaultdict(list)
    for k, v in discs.items():
        for b in v[1]:
            balance[b].append(k)
    node = next(iter(balance.keys()))
    while node in balance:
        node = balance[node][0]
    return node


def b(discs):
    total_weights = {}
    balance = defaultdict(list)
    for k, v in discs.items():
        for b in v[1]:
            balance[b].append(k)
    to_expand = [k for k, v in discs.items() if not v[1]]
    while to_expand:
        node = to_expand.pop(0)
        try:
            weights = [total_weights[c] for c in discs[node][1]]
        except KeyError:
            to_expand.append(node)
            continue
        if weights:
            other = find_other(weights)
            if other != -1:
                should_be = len(weights)*weights[(other+1)%len(weights)]
                diff = should_be - sum(weights)
                return discs[discs[node][1][other]][0] + diff
        for child in balance[node]:
            to_expand.append(child)
        total_weights[node] = discs[node][0] + sum(weights)


if __name__ == '__main__':
    discs = {}
    with open('input07.txt') as f:
        for line in f.readlines():
            line = line.strip()
            name, weight, *_ = line.split(' ')
            weight = int(weight[1:-1])
            if '->' in line:
                balancers = line.split('->')[1].strip().split(', ')
            else:
                balancers = []
            discs[name] = (weight, balancers)
    print(b(discs))
