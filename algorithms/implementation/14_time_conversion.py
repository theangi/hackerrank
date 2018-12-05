#!/bin/python3

import os
import unittest


def time_conversion(time):
    hour, minute, seconds = map(int, time[:-2].split(':'))
    meridian = time[-2:]

    if meridian == 'PM' and hour != 12:
        hour = hour + 12
    elif meridian == 'AM' and hour == 12:
        hour = 0

    return '{:02d}:{:02d}:{:02d}'.format(hour, minute, seconds)


class TestSolution(unittest.TestCase):
    def test_function(self):
        self.assertEquals(time_conversion('07:05:45PM'), '19:05:45')
        self.assertEquals(time_conversion('12:45:54PM'), '12:45:54')

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = time_conversion("07:05:45PM")

    f.write(result + '\n')

    f.close()


