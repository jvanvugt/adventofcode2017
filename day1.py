def a(digits):
    N = len(digits)
    result = sum(digits[i] for i in range(N) if digits[i] == digits[(i+1)%N])
    return result


def b(digits):
    """
    >>> b([1,2,1,2])
    6
    >>> b([1, 2, 2, 1])
    0
    >>> b([1, 2, 3, 4, 2, 5])
    4
    """
    N = len(digits)
    half = N // 2
    result = sum(digits[i] for i in range(N) if digits[i] == digits[(i+half)%N])
    return result


if __name__ == '__main__':
    with open('input1.txt') as f:
        digits = list(map(int, f.read()))
    print(b(digits))
