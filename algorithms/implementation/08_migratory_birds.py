import collections


def migratoryBirds(n, ar):
    counter = collections.Counter(ar)
    return sorted(counter.most_common(1), key=lambda x: x[1])[0][0]


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
