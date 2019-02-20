import unittest


def save_the_prisoner(number_of_prisoners, number_of_sweets, starting_position):
    end_position = (starting_position + number_of_sweets - 1) % number_of_prisoners
    return end_position if end_position != 0 else number_of_prisoners


class Solution(unittest.TestCase):
    def test_save_the_prisoner(self):
        self.assertEqual(save_the_prisoner(5, 2, 1), 2)
        self.assertEqual(save_the_prisoner(5, 2, 2), 3)
        self.assertEqual(save_the_prisoner(7, 19, 2), 6)
        self.assertEqual(save_the_prisoner(3, 7, 3), 3)
