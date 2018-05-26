def involution():
    _ = input()
    values = list(map(int, input().split()))

    for i, _ in enumerate(values):
        first = [values[values[i] - 1]][0]
        second = i + 1
        if first != second:
            print('NO')
            exit()
    print('YES')
