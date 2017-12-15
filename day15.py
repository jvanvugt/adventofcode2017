import time
def a(gen_a, gen_b):
    count = 0
    for _ in range(40000000):
        gen_a = (gen_a * 16807) % 2147483647
        gen_b = (gen_b * 48271) % 2147483647
        count += int(gen_a & 0xffff == gen_b & 0xffff)
    return count

def b(gen_a, gen_b):
    count = 0
    for _ in range(5000000):
        while True:
            gen_a = (gen_a * 16807) % 2147483647
            if gen_a % 4 == 0:
                break
        while True:
            gen_b = (gen_b * 48271) % 2147483647
            if gen_b % 8 == 0:
                break
        count += int(gen_a & 0xffff == gen_b & 0xffff)
    return count


def main():
    with open('input15.txt') as f:
        gen_a, gen_b = [int(l.split(' ')[-1]) for l in f.read().rstrip().splitlines()]
    cur = time.time()
    print(a(gen_a, gen_b))
    print(time.time() - cur)



if __name__ == '__main__':
    main()