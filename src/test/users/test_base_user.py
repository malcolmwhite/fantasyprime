import unittest
from src.main.user_league.simplest_user_league import SimplestUserLeague
from src.main.players.simplest_player import SimplestPlayer
from src.main.users.users import BaseUser


class TestBaseUser(unittest.TestCase):
    def test_get_player_to_drop_with_simplest_league_and_simplest_player(self):
        league = SimplestUserLeague()

        # Test with players that have 0 and positive points
        player_with_no_points = SimplestPlayer(stats=[0, 0])
        player_with_many_points = SimplestPlayer(stats=[100, 100])
        player_to_add = SimplestPlayer()
        players = [
            player_with_no_points,
            player_with_many_points
        ]
        user = BaseUser(user_id=0, league=league, players=players)
        self.assertEqual(
            player_with_no_points,
            user.get_player_to_drop_if_adding_player(player_to_add)
        )

        # Repeat test with players in different order
        player_with_no_points = SimplestPlayer(stats=[0, 0])
        player_with_many_points = SimplestPlayer(stats=[100, 100])
        player_to_add = SimplestPlayer()
        players = [
            player_with_many_points,
            player_with_no_points
        ]
        user = BaseUser(user_id=0, league=league, players=players)
        self.assertEqual(
            player_with_no_points,
            user.get_player_to_drop_if_adding_player(player_to_add)
        )

        # Test with player that has negative points
        player_with_negative_points = SimplestPlayer(stats=[-5, -5])
        player_with_no_points = SimplestPlayer(stats=[0, 0])
        player_with_many_points = SimplestPlayer(stats=[100, 100])
        player_to_add = SimplestPlayer()
        players = [
            player_with_no_points,
            player_with_negative_points,
            player_with_many_points
        ]
        user = BaseUser(user_id=0, league=league, players=players)
        self.assertEqual(
            player_with_negative_points,
            user.get_player_to_drop_if_adding_player(player_to_add)
        )

        # Test with player that has very many points
        player_with_negative_points = SimplestPlayer(stats=[-5, -5])
        player_with_no_points = SimplestPlayer(stats=[0, 0])
        player_with_many_points = SimplestPlayer(stats=[100, 100])
        player_with_very_many_points = SimplestPlayer(stats=[1000, 1000])
        player_to_add = SimplestPlayer()
        players = [
            player_with_no_points,
            player_with_negative_points,
            player_with_very_many_points,
            player_with_many_points
        ]
        user = BaseUser(user_id=0, league=league, players=players)
        self.assertEqual(
            player_with_negative_points,
            user.get_player_to_drop_if_adding_player(player_to_add)
        )


if __name__ == '__main__':
    unittest.main()
