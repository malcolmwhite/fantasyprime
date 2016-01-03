from random import randint
from players import BasePlayer


class SimplestPlayer(BasePlayer):

    def __init__(self, stats=None):
        super(SimplestPlayer, self).__init__()
        if not stats:
            self.stats = []
            self.stats.append(randint(0, 10))
            self.stats.append(randint(0, 10))
        else:
            self.stats = stats

    def get_stats_for_schedule_unit(self, schedule_unit):
        return self.stats[schedule_unit]