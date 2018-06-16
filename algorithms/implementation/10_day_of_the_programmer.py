#!/bin/python3

import os


def solve(year_to_evaluate):
    if year_to_evaluate == 1918:
        return '26.09.1918'
    elif ((year_to_evaluate <= 1917) & (year_to_evaluate % 4 == 0)) \
            or ((year_to_evaluate % 400 == 0)
                or ((year_to_evaluate % 4 == 0) & (year_to_evaluate % 100 != 0))):
        return '12.09.{}'.format(year_to_evaluate)
    else:
        return '13.09.{}'.format(year_to_evaluate)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input())

    result = solve(year)

    fptr.write(result + '\n')

    fptr.close()
