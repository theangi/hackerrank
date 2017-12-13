#!/bin/python3


def adjust_grade(number, multiple=5, bias=3, min_mark=40):
    to_round_up = multiple - (number % multiple)
    if to_round_up >= bias:
        return number
    else:
        rounded = number + to_round_up
        return rounded if rounded >= min_mark else number


grades = [int(input()) for x in range(int(input()))]
for x in grades:
    print(adjust_grade(x))
