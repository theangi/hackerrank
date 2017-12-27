#!/bin/python3

s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
fallen_apples = [int(apple_temp) for apple_temp in input().strip().split(' ')]
fallen_oranges = [int(orange_temp) for orange_temp in input().strip().split(' ')]

# One-liner pythonic...
# print(sum(1 for x in fallen_apples if s <= (a + x) <= t))
# print(sum(1 for x in fallen_oranges if s <= (a + x) <= t))

# Explicit version:
number_of_apples = 0
number_of_oranges = 0

for x in fallen_apples:
    if s <= (a + x) <= t:
        number_of_apples = number_of_apples + 1

for x in fallen_oranges:
    if s <= (b + x) <= t:
        number_of_oranges = number_of_oranges + 1

print(number_of_apples)
print(number_of_oranges)
