#!/bin/python3

import os
import unittest


def cat_and_mouse(cat_a, cat_b, mouse_c):
    ac = abs(cat_a - mouse_c)
    bc = abs(cat_b - mouse_c)

    if ac == bc:
        return 'Mouse C'
    elif ac < bc:
        return 'Cat A'
    return 'Cat B'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])

        result = cat_and_mouse(x, y, z)
        fptr.write(result + '\n')

    fptr.close()


class TestSolution(unittest.TestCase):
    def test_function(self):
        self.assertEquals(cat_and_mouse(1, 2, 3), 'Cat B')
        self.assertEquals(cat_and_mouse(1, 3, 2), 'Mouse C')
