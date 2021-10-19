import io
import unittest
from unittest import mock


from sotonggame.glass_bridge_game_sim.GlassBridgeGameSim import GlassBridgeGameSim


class TestGlassBridgeGameSim(unittest.TestCase):
    @mock.patch('sotonggame.glass_bridge_game_sim.GlassBridgeGameSim.GlassBridgeGameSim.break_panel')
    def test_record_player_survival(self, mock_break_panel):
        glass_bridge_game_sim = GlassBridgeGameSim(num_of_players=1,
                                                   num_of_steps=1,
                                                   num_of_itr=1)

        mock_break_panel.return_value = 0

        glass_bridge_game_sim.run_sim()

        mock_break_panel.assert_called()
        self.assertEqual(glass_bridge_game_sim.survivals[0], 1)

    @mock.patch('sotonggame.glass_bridge_game_sim.GlassBridgeGameSim.GlassBridgeGameSim.break_panel')
    def test_record_player_death(self, mock_break_panel):
        glass_bridge_game_sim = GlassBridgeGameSim(num_of_players=1,
                                                   num_of_steps=1,
                                                   num_of_itr=1)
        mock_break_panel.return_value = 1

        glass_bridge_game_sim.run_sim()

        mock_break_panel.assert_called()
        self.assertEqual(glass_bridge_game_sim.survivals[0], 0)

    def test_calculate_all_player_survival(self):
        expected_chances = [0.8, 0.4, 0.6]

        glass_bridge_game_sim = GlassBridgeGameSim(num_of_players=3, num_of_itr=5)
        glass_bridge_game_sim.survivals = [4, 2, 3]

        glass_bridge_game_sim.calculate_all_player_survival()

        self.assertEqual(expected_chances, glass_bridge_game_sim.chances)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_survival(self, mock_stdout):
        glass_bridge_game_sim = GlassBridgeGameSim(num_of_players=3, num_of_itr=5)
        glass_bridge_game_sim.chances = [0.8, 0.4, 0.6]
        expected_player_1_output = "Player 1 has a 80.0% chance of survival."
        expected_player_2_output = "Player 2 has a 40.0% chance of survival."
        expected_player_3_output = "Player 3 has a 60.0% chance of survival."

        glass_bridge_game_sim.print_survival_chances()
        mock_stdout_value = mock_stdout.getvalue()

        self.assertIn(expected_player_1_output, mock_stdout_value)
        self.assertIn(expected_player_2_output, mock_stdout_value)
        self.assertIn(expected_player_3_output, mock_stdout_value)

    @mock.patch('sotonggame.glass_bridge_game_sim.GlassBridgeGameSim.GlassBridgeGameSim.break_panel')
    def test_player_forgets_when_nervous(self, mock_break_panel):
        t_player_memory = 2
        t_panels = [0] * 3

        glass_bridge_game_sim = GlassBridgeGameSim(num_of_players=1,
                                                   num_of_steps=3,
                                                   num_of_itr=1,
                                                   player_memory=t_player_memory)

        glass_bridge_game_sim.panels = t_panels

        glass_bridge_game_sim.run_sim()

        mock_break_panel.assert_called()


if __name__ == '__main__':
    unittest.main()
