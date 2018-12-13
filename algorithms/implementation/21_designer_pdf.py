#!/bin/python3

import unittest
import os


def designer_pdf_viewer(alphabet_heigths, word):
    mapping = dict(zip([chr(x) for x in range(ord('a'), ord('z') + 1)], alphabet_heigths))
    return len(word) * max([mapping[letter] for letter in word])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designer_pdf_viewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()


class TestSolution(unittest.TestCase):
    def test_function(self):
        self.assertEqual(designer_pdf_viewer(
            [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            'abc'), 9)
        self.assertEqual(designer_pdf_viewer(
            [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7],
            'zaba'), 28)
