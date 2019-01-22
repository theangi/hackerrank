import unittest
from bisect import bisect_left


def get_rankings(leaderboard):
    rankings = [1]
    current_ranking = 1

    for i in range(1, len(leaderboard)):
        if leaderboard[i] != leaderboard[i-1]:
            current_ranking += 1

        rankings.append(current_ranking)

    return rankings


def climbing_leaderboard_2(leaderboard, alice_scores):
    steps = []
    rev_leaderboard = list(reversed(leaderboard))

    for score in alice_scores:
        step = bisect_left(rev_leaderboard, score)
        new_position = len(leaderboard) - step
        leaderboard.insert(new_position, score)
        steps.append(get_rankings(leaderboard)[len(leaderboard) - step - 1])
        del leaderboard[new_position]
    return steps


def climbing_leaderboard(leaderboard, alice_scores):
    steps = []
    for score in alice_scores:
        leaderboard.append(score)
        new_lead = list(sorted(set(leaderboard), reverse=True))
        steps.append(new_lead.index(score) + 1)
    return steps


def climbing_leaderboard(leaderboard, alice_scores):
    # Alice's scores are in ACENDING order already!!!
    steps = []
    ranking = 0
    last_score = None
    i = 0

    for score in reversed(leaderboard):
        if score != last_score:
            ranking += 1

        if alice_scores[i] <= score:
            steps.append(ranking)
            i += 1

    return steps


class Solution(unittest.TestCase):

    def test_climbining_leaderboard(self):
        self.assertEqual(
            [6, 4, 2, 1],
            climbing_leaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
        )

        self.assertEqual(
            [6, 5, 4, 2, 1],
            climbing_leaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
        )
