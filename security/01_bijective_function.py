def is_function_bijective():
    if int(input()) == len(set(input().split())):
        print('YES')
    else:
        print('NO')

    # print(['NO', 'YES'][int(input()) == len(set(input().split()))])
