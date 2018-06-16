#!/bin/python3

import os

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max_value = max(ar)
    return sum(1 for x in ar if x == max_value)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
