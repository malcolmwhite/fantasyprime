from abc import ABCMeta, abstractmethod


class BasePlayer:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass


    @abstractmethod
    def get_stats_for_schedule_unit(self, schedule_unit):
        pass