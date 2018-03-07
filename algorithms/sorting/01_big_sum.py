#!/bin/python3


def big_sorting(arr):
    return sorted(arr, key=lambda x: len(x) and int(x))

if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
        arr_t = str(input().strip())
        arr.append(arr_t)
    result = big_sorting(arr)
    print ("\n".join(map(str, result)))