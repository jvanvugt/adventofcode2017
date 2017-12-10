from functools import reduce
from operator import xor


def a(input):
    lengths = [int(s.strip()) for s in input.split(',')]
    nums = list(range(256))
    offset = 0
    current = 0
    n = len(nums)
    for length in lengths:
        copy = nums[:]
        end = current + length
        for i in range(length):
            nums[(end-i-1)%n] = copy[(i+current)%n]
        current = (current + length + offset)
        offset += 1
    return nums[0] * nums[1]


def b(input):
    lengths = list(input.encode('ascii'))
    lengths += [17, 31, 73, 47, 23]
    offset = 0
    current = 0
    nums = list(range(256))
    n = len(nums)
    for _ in range(64):
        for length in lengths:
            copy = nums[:]
            end = current + length
            for i in range(length):
                nums[(end-i-1)%n] = copy[(i+current)%n]
            current = (current + length + offset)
            offset += 1
    dense_hash = [reduce(xor, nums[i:i+16]) for i in range(0, 256, 16)]
    return ('{:02x}'*16).format(*dense_hash)


def main():
    with open('input10.txt') as f:
        input = f.read()
    print(b(input))

if __name__ == '__main__':
    main()