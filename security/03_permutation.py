def print_permutation():
    _ = input()
    values = list(map(int, input().split()))

    for i, x in enumerate(values):
        print(values[values[i] - 1])
