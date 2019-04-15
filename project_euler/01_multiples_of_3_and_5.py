import unittest


def sum_of_multiples(n):
    return sum((x for x in range(n) if int(x) % 3 == 0 or int(x) % 5 == 0))


def sum_of_multiples_2(n):
    a = [x for x in range(0, n, 3)]
    b = [x for x in range(0, n, 5)]
    c = [x for x in range(0, n, 15)]
    return sum(a) + sum(b) - sum(c)


def sum_of_multiples_3(n):
    n_of_threes = (n - 1) // 3
    n_of_fives = (n - 1) // 5
    n_of_fifteens = (n - 1) // 15

    sum_of_threes = 3 * n_of_threes * (n_of_threes + 1) // 2
    sum_of_fives = 5 * n_of_fives * (n_of_fives + 1) // 2
    sum_of_fifteens = 15 * n_of_fifteens * (n_of_fifteens + 1) // 2

    return sum_of_threes + sum_of_fives - sum_of_fifteens


class Solution(unittest.TestCase):
    def test_sum_of_multiples(self):
        self.assertEqual(23, sum_of_multiples(10))
        self.assertEqual(2318, sum_of_multiples(100))
        self.assertEqual(233168, sum_of_multiples(1000))

    def test_sum_of_multiples_2(self):
        self.assertEqual(23, sum_of_multiples_2(10))
        self.assertEqual(2318, sum_of_multiples_2(100))
        self.assertEqual(233168, sum_of_multiples_2(1000))

    def test_sum_of_multiples_3(self):
        self.assertEqual(23, sum_of_multiples_3(10))
        self.assertEqual(2318, sum_of_multiples_3(100))
        self.assertEqual(233168, sum_of_multiples_3(1000))
        self.assertEqual(2333333316666668, sum_of_multiples_3(100000000))
