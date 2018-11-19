#!/bin/python3

import os

from collections import Counter


# Complete the sockMerchant function below.
def sock_merchant(n, ar):
    counter = Counter(ar)
    matching_pairs = 0
    for x in counter:
        matching_pairs = matching_pairs + counter[x]//2
    return matching_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
