#!/bin/python3


def diagonalDifference(a):
    # for i, x in enumerate(a):
    #     print('Line {}, values {} and {}, difference {}'.format(i, x[i], x[-i-1], x[i] - x[-i-1]))
    return abs(sum(x[i] - x[-i - 1] for i, x in enumerate(a)))


if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        a.append(a_t)
    result = diagonalDifference(a)
    print(result)
