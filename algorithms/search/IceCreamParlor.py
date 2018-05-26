#!/bin/python3


def improved(money, flavors):
    import collections
    counter = collections.Counter(flavors)

    for i, _ in enumerate(flavors):
        if counter[money - flavors[i]]:
            # nope! [1 2 . . 2 . 1 ] # Counter does not store original position :(
            return [i + 1, counter + 1]

# 1.0258732159854844
def icecreamParlor(money, flavors):
    for i, _ in enumerate(flavors):
        for j, _ in enumerate(flavors):
            if i != j and flavors[i] + flavors[j] == money:
                return [i + 1, j + 1]


if __name__ == "__..main__":
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = icecreamParlor(m, arr)
        print (" ".join(map(str, result)))

        # import timeit
        # print(timeit.timeit(stmt='xxx()', setup='from __main__ import ciao', number=100000))


