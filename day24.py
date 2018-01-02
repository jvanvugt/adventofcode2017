def a(cables, chain=[[0, 0]], strength=0):
    children = []
    for cable in cables[:]:
        matching_ports = [side for side in cable if side in chain[-1]]
        if matching_ports:
            matching_port = matching_ports[0]
            cables.remove(cable)
            new_strength = strength + sum(cable)
            cable.remove(matching_port)
            children.append(a(cables, chain + [cable], new_strength))
            cable.append(matching_port)
            cables.append(cable)

    return max(children) if children else strength


def b(cables, chain=[[0, 0]], strength=0):
    children = []
    for cable in cables[:]:
        matching_ports = [side for side in cable if side in chain[-1]]
        if matching_ports:
            matching_port = matching_ports[0]
            cables.remove(cable)
            new_strength = strength + sum(cable)
            cable.remove(matching_port)
            children.append(b(cables, chain + [cable], new_strength))
            cable.append(matching_port)
            cables.append(cable)
    return max(children) if children else (len(chain), strength)


def main():
    with open('input24.txt') as f:
        cables = [list(map(int, line.split('/'))) for line in f.read().rstrip().splitlines()]
    print(a(cables))
    print(b(cables)[1])


if __name__ == '__main__':
    main()
