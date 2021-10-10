import io
import unittest
from unittest import mock

from sotonggame.GlassBridgeGameSim import GlassBridgeGameSim


class TestGlassBridgeGameSim(unittest.TestCase):
    """
    GlassBridgeGameSim calculates the probability of player survival
    by running simulations of players moving across the bridge, with
    randomised survival paths.

    - test calculation of individual player survival given complete sim
    - test calculation of survival for all players given complete sim
    - test correct printing of 1
    - test correct printing of 2
    - test survival status given fail and pass path
    """

    @mock.patch('sotonggame.GlassBridgeGameSim.GlassBridgeGameSim.break_panel')
    def test_record_player_survival(self, mock_break_panel):
        glass_bridge_game_sim = GlassBridgeGameSim(num_of_players=1,
                                                   num_of_steps=1,
                                                   num_of_itr=1)

        mock_break_panel.return_value = 0

        glass_bridge_game_sim.run_sim()

        mock_break_panel.assert_called()
        self.assertEqual(glass_bridge_game_sim.survivals[0], 1)

    @mock.patch('sotonggame.GlassBridgeGameSim.GlassBridgeGameSim.break_panel')
    def test_record_player_death(self, mock_break_panel):
        glass_bridge_game_sim = GlassBridgeGameSim(num_of_players=1,
                                                   num_of_steps=1,
                                                   num_of_itr=1)
        mock_break_panel.return_value = 1

        glass_bridge_game_sim.run_sim()

        mock_break_panel.assert_called()
        self.assertEqual(glass_bridge_game_sim.survivals[0], 0)

    def test_calculate_player_survival(self):
        glass_bridge_game_sim = GlassBridgeGameSim(num_of_itr=5)

        glass_bridge_game_sim.survivals = [4, 2, 3]

        self.assertEqual(0.8, glass_bridge_game_sim.calculate_player_survival(0))
        self.assertEqual(0.4, glass_bridge_game_sim.calculate_player_survival(1))
        self.assertEqual(0.6, glass_bridge_game_sim.calculate_player_survival(2))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_survival(self, mock_stdout):
        glass_bridge_game_sim = GlassBridgeGameSim(num_of_itr=5)
        glass_bridge_game_sim.survivals = [4, 2, 3]
        expected_output = "Player 1 has a 80.0% chance of survival.\n" \
                          "Player 2 has a 40.0% chance of survival.\n" \
                          "Player 3 has a 60.0% chance of survival.\n"

        glass_bridge_game_sim.print_survival_chances()

        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
