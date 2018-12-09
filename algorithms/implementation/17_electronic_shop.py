#!/bin/python3

import os
import unittest


def get_money_spent(keyboards, drives, budget):
    max_spent = 0
    for k in keyboards:
        for d in drives:
            spent = k + d
            if spent <= budget and spent > max_spent:
                max_spent = spent

    return max_spent if max_spent else -1


def get_money_spent2(keyboards, drivers, budget):
    from itertools import product
    return max((k + d if k + d <= budget else -1 for k, d in product(keyboards, drivers)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])

    money_spent = get_money_spent(
        list(map(int, input().rstrip().split())),
        list(map(int, input().rstrip().split())),
        b)

    fptr.write(str(money_spent) + '\n')
    fptr.close()


class TestSolution(unittest.TestCase):
    def test_function(self):
        self.assertEquals(get_money_spent([3, 1], [5, 2, 8], 10), 9)
        self.assertEquals(get_money_spent([5], [4], 5), -1)
