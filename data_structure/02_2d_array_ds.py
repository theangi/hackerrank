#!/bin/python3
# Calculate Hourglass maximum sum
# -9 -9 -9  1 1 1
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0
#
#
#
#

import os

HOURGLASS = [[0, 0], [0, 1], [0, 2], [1, 1], [2, 0], [2, 1], [2, 2]]


def sum_hourglass(arr, i, j):
    return sum([arr[i + x[0]][j + x[1]] for x in HOURGLASS])


def maximum_sum(arr):
    return max(sum_hourglass(arr, i, j) for i in range(4) for j in range(4))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)
    result = maximum_sum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
