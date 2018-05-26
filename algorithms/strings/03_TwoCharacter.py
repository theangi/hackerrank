#!/bin/python3

import collections


def twoCharaters(s):
    counter = collections.Counter(s)
    while len(counter) > 0:
        first, second = counter.most_common(2)
        new_string = s.replace(first).replace(second)
        expected = ''.join([first, second]) * int(len(new_string) / 2)
        if new_string == expected:
            return len(new_string)

        counter[first] = 0


if __name__ == "__main__":
    # l = int(input().strip())
    # s = input().strip()
    s = 'beabeefeab'
    result = twoCharaters(s)
    print(result)
