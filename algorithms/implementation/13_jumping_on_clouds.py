#!/bin/python3

import os


# Complete the jumpingOnClouds function below.
def jumping_on_clouds(c):
    steps = 0
    i = 0
    while i < len(c) - 1:
        if i+2 < len(c) and c[i+2] != 1:
            i += 1
        steps = steps + 1
        i += 1
    return steps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
