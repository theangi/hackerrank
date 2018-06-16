#!/bin/python3

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    print(sum(sorted(arr)[:-1]), sum(sorted(arr, reverse=True)[:-1]))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    