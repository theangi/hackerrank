#!/bin/python3

import unittest


def bon_appetit(bill, item_to_exclude, proposed_amount):
    fair_share = (sum(bill) - bill[item_to_exclude]) // 2

    if fair_share == proposed_amount:
        return 'Bon Appetit'
    else:
        return proposed_amount - fair_share

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bon_appetit(bill, k, b)


class TestSolution(unittest.TestCase):
    def test_function(self):
        self.assertEquals(bon_appetit([3, 10, 2, 9], 1, 12), 5)
        self.assertEquals(bon_appetit([3, 10, 2, 9], 1, 7), 'Bon Appetit')
