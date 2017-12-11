import itertools

def a(passphrases):
    n_valid = 0
    for phrase in passphrases:
        if len(phrase.split(' ')) == len(set(phrase.split(' '))):
            n_valid += 1
    return n_valid


def is_anagram(w, o):
    return w in (''.join(c) for c in itertools.permutations(o))


def b(passphrases):
    n_valid = 0
    for phrase in passphrases:
        seen = set()
        valid = True
        for word in phrase.split(' '):
            if not any(is_anagram(word, o) for o in seen):
                seen.add(word)
            else:
                valid = False
                break
        if valid:
            n_valid += 1
    return n_valid


if __name__ == '__main__':
    with open('input04.txt') as f:
        print(b(f.read().split('\n')))
