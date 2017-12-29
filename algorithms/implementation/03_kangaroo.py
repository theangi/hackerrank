#!/bin/python3


def kangaroo(x1, v1, x2, v2):
    if v1 - v2 != 0:
        return 'YES' if (x2 - x1) / (v1 - v2) > 0 and (x2 - x1) % (v1 - v2) == 0 else 'NO'
    else:
        return 'NO'

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [float(x1), float(v1), float(x2), float(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
