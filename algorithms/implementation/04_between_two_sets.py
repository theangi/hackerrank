#!/bin/python3

import sys

def getTotalX(a=[2, 4], b=[16, 32, 96]):
    return sum(1 for x in range(a[-1], b[0] + 1) if all_divisibile(x, a) and evenly_divides(x, b))


def all_divisibile(num, serie):
    for x in serie:
        if num % x != 0:
            return False
    return True


def evenly_divides(num, serie):
    for x in serie:
        if x % num != 0:
            return False
    return True

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)