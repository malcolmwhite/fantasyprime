import unittest

from src.main.user_league.simplest_user_league import SimplestUserLeague


class TestSimplestLeague(unittest.TestCase):
    def test_stats_to_points(self):
        league = SimplestUserLeague()
        stats = [5, 6, 9, 1, 100, 0, -1]
        expected_points = stats
        for stat, expected_point in zip(stats, expected_points):
            actual_point = league.convert_stats_to_points(stat)
            self.assertEqual(expected_point, actual_point)


if __name__ == '__main__':
    unittest.main()
