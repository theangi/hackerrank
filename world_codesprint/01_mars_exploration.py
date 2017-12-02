def solve_challange():
    signal_received = input().strip()

    count = 0

    groups = [signal_received[i:i + 3] for i in range(0, len(signal_received), 3)]
    for x in groups:
        if x[0] != 'S':
            count += 1
        if x[1] != 'O':
            count += 1
        if x[2] != 'S':
            count += 1

    print(count)
