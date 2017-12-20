from collections import namedtuple
from functools import cmp_to_key
import re

Point = namedtuple('Point', ['x', 'y', 'z'])
Particle = namedtuple('Particle', ['p', 'v', 'a'])

def distance(point):
    return sum(abs(p) for p in point)

def compare(a, b):
    a_acc = distance(a.a)
    b_acc = distance(b.a)
    if a_acc != b_acc:
        return 1 if a_acc > b_acc else -1

    a_vel = distance(a.v)
    b_vel = distance(b.v)
    if a_vel != b_vel:
        return 1 if a_vel > b_vel else -1

    a_pos = distance(a.p)
    b_pos = distance(b.p)
    if a_pos != b_pos:
        return 1 if a_pos > b_pos else -1

    return 0


def a(particles):
    key_fn = cmp_to_key(compare)
    return min(range(len(particles)), key=lambda i: key_fn(particles[i]))


def add(p1, p2):
    return Point(p1.x+p2.x, p1.y+p2.y, p1.z+p2.z)


def b(particles):
    for _ in range(100000):
        for i in range(len(particles)):
            particle = particles[i]
            new_vel = add(particle.v, particle.a)
            new_pos = add(particle.p, new_vel)
            particles[i] = Particle(new_pos, new_vel, particle.a)
        collided = set()
        for i in range(len(particles)):
            for j in range(i+1, len(particles)):
                p1, p2 = particles[i].p, particles[j].p
                if p1.x == p2.x and p1.y == p2.y and p1.z == p2.z:
                    collided.add(i)
                    collided.add(j)
        for idx in sorted(collided, reverse=True):
            particles.pop(idx)
        print(len(particles))
    return len(particles)


def main():
    with open('input20.txt') as f:
        lines = f.read().rstrip().splitlines()
    particles = []
    for line in lines:
        numbers = re.findall(r'\<(-?\d+),(-?\d+),(-?\d+)\>', line)
        particles.append(Particle(
            Point(*map(int, numbers[0])),
            Point(*map(int, numbers[1])),
            Point(*map(int, numbers[2]))
        ))
    print(a(particles))
    print(b(particles))

if __name__ == '__main__':
    main()
