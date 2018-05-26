#!/bin/python3

import sys

def staircase(n):
    for i in range(n):
        print(''.join([' ' * (n - i - 1), '#' * (i + 1)]))

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
