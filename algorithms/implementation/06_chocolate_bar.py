#!/bin/python3


def solve(n, s, d, m):
    groups = [s[i:i + m] for i in range(0, len(s))]
    return sum(1 for x in groups if sum(x) == d)

    # or
    # return sum([1 for i in range(n-m+1) if sum(s[i:i+m]) == d])

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
