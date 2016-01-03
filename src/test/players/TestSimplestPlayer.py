import unittest

from src.main.players.simplest_player import SimplestPlayer


class TestSimplestPlayer(unittest.TestCase):
    def test_construction_with_stats(self):
        all_expected_stats = [
            [5, 6], [2], [6, 8, 2, 6], [], [0, 0, 0, 0]
        ]
        for expected_stats in all_expected_stats:
            player = SimplestPlayer(stats=expected_stats)
            for schedule_unit, expected_stat in enumerate(expected_stats):
                actual_stat = player.get_stats_for_schedule_unit(schedule_unit)
                self.assertEqual(expected_stat, actual_stat)




if __name__ == '__main__':
    unittest.main()
