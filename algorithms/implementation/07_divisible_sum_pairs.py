#!/bin/python3


# Brute force approach
def divisible_sum_pairs(n=6, k=3, ar=(1, 3, 2, 6, 1, 2)):
    return sum(1 for i in range(n) for j in range(n) if i < j and (ar[i] + ar[j]) % k == 0)
    # return sum(0.5 for a1, a2 in groups if (a1 + a2) % k == 0)


# n, k = input().strip().split(' ')
# n, k = [int(n), int(k)]
# ar = list(map(int, input().strip().split(' ')))
# result = divisibleSumPairs(n, k, ar)
result = divisible_sum_pairs()
print(int(result))
