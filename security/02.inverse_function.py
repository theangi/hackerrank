def print_inverse_function():
    n = input()
    values = input().split()

    for i, x in enumerate(values):
        print(values.index(str(i + 1)) + 1)
