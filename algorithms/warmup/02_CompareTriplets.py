#!/bin/python3


def solve(alice, bob):
    a, b = 0, 0
    for x, y in zip(alice, bob):
        if x > y:
            a = a + 1
        elif x < y:
            b = b + 1
    return [a, b]

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve([a0, a1, a2], [b0, b1, b2])

print(" ".join(map(str, result)))