from user_league import BaseUserLeague


class SimplestUserLeague(BaseUserLeague):

    def __init__(self):
        super(BaseUserLeague, self).__init__()

    def convert_stats_to_points(self, stats):
        return stats

    def players_can_start_for_each_other(self, player1, player2):
        return True