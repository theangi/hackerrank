#!/bin/python3

def breakingRecords(score):
    highest = lowest = score[0]
    h = l = 0
    for x in score:
        if x > highest:
            highest = x
            h = h + 1
        if x < lowest:
            lowest = x
            l = l + 1
    return h, l

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))
