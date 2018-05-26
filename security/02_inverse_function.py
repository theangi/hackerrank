def print_inverse_function():
    _ = input()
    values = input().split()

    for i, _ in enumerate(values):
        print(values.index(str(i + 1)) + 1)
