#!/bin/python3

import sys

def plusMinus(arr):
    positive, negative, zeros = 0, 0, 0
    for x in arr:
        if x > 0:
            positive += 1
        elif x == 0:
            zeros += 1
        else:
            negative += 1
    print('{0:.6f}\n{1:.6f}\n{2:.6f}'.format(positive / len(arr), negative / len(arr), zeros / len(arr)))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)