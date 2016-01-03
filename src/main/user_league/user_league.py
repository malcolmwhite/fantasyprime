from abc import ABCMeta, abstractmethod


class BaseUserLeague:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def convert_list_of_stats_to_points(self, stats):
        return sum([self.convert_stats_to_points(stat) for stat in stats])

    @abstractmethod
    def convert_stats_to_points(self, stats):
        pass

    @abstractmethod
    def players_can_start_for_each_other(self, player1, player2):
        pass