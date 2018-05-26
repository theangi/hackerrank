#!/bin/python3


def staircase(n):
    for i in range(n):
        print(''.join([' ' * (n - i - 1), '#' * (i + 1)]))

if __name__ == "__main__":
    m = int(input().strip())
    staircase(m)
