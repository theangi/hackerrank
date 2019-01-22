import unittest


def hurlde_race(normal_jump, heigts):
    n_potions = max(heigts) - normal_jump
    return n_potions if n_potions > 0 else 0


class Solution(unittest.TestCase):
    def test_hurlde_race(self):
        self.assertEqual(2, hurlde_race(4, [1, 6, 3, 5, 2]))
