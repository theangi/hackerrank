#!/bin/python3
import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(' '.join([str(arr[i-1]) for i in range(n, 0, -1)]))
