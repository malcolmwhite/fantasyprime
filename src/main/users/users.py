from abc import ABCMeta, abstractmethod


class BaseUser(object):
    __metaclass__ = ABCMeta

    def __init__(self, user_id, league, players):
        self.user_id = user_id
        self.league = league
        self.players = players

    def get_player_to_drop_if_adding_player(self,
                                            player_to_add,
                                            current_schedule_unit=0):
        worst_replacement_player = None
        worst_replacement_player_points = None
        for player_on_team in self.players:
            if self.league.players_can_start_for_each_other(
                    player_on_team,
                    player_to_add
            ):
                if not worst_replacement_player:
                    worst_replacement_player = player_on_team
                    remaining_stats = worst_replacement_player\
                        .get_remaining_stats(current_schedule_unit)
                    worst_replacement_player_points = \
                        self.league.convert_list_of_stats_to_points(
                            remaining_stats
                        )
                else:
                    remaining_stats = player_on_team\
                        .get_remaining_stats(current_schedule_unit)
                    player_on_team_points = \
                        self.league.convert_list_of_stats_to_points(
                            remaining_stats
                        )
                    if player_on_team_points < worst_replacement_player_points:
                        worst_replacement_player = player_on_team
                        worst_replacement_player_points = player_on_team_points
        return worst_replacement_player


class AuctionUser(BaseUser):

    def __init__(self, user_id, league, players, points_to_bid=50):
        super(AuctionUser, self).__init__(user_id, league, players)
        self.points_to_bid = points_to_bid