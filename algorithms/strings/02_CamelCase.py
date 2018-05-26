#!/bin/python3


def camelcase(s):
    return sum([1 for x in s if x.isupper()]) + 1

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
