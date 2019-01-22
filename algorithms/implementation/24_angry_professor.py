import unittest


def angry_professor(threshold, times):
    return 'NO' if sum(1 for x in filter(lambda x: x <= 0, times)) >= threshold else 'YES'


class Solution(unittest.TestCase):
    def test_angry_professor(self):
        self.assertEqual('YES', angry_professor(3, [-1, -3, 4, 2]))
        self.assertEqual('NO', angry_professor(2, [0, -1, 2, 1]))
