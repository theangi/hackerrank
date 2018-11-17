#!/bin/python3

def mini_max_sum(arr):
    print(sum(sorted(arr)[:-1]), sum(sorted(arr, reverse=True)[:-1]))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    mini_max_sum(arr)
