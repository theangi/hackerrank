#!/bin/python3

import os


# Complete the countingValleys function below.
def counting_valleys(n, s):
    level = 0
    valleys = 0

    for x in s:
        level = level + 1 if x == 'U' else level - 1

        if level == 0 and x == 'U':
            valleys += 1

    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = counting_valleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
