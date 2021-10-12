import random
from enum import Enum


class PanelStatus(Enum):
    BROKEN = 0
    STEPPED = 1
    NOT_STEPPED = 2


class GlassBridgeGameSim:
    def __init__(self, num_of_players=16,
                 num_of_steps=18,
                 num_of_itr=1000,
                 player_memory=18):

        self.survivals = [0] * num_of_players
        self.num_of_steps = num_of_steps
        self.num_of_itr = num_of_itr
        self.player_memory = player_memory
        self.panels = [PanelStatus.NOT_STEPPED] * num_of_steps

    def run_sim(self):
        for itr in range(self.num_of_itr):
            print("Simulating iteration {} out of {}".format(itr, self.num_of_itr))
            for player_num in range(len(self.survivals)):
                player_is_alive = True
                player_num_memory = self.player_memory

                for step in range(self.num_of_steps):
                    panel_status = self.panels[step]
                    if (panel_status == PanelStatus.NOT_STEPPED) or (player_num_memory == 0):
                        self.panels[step] = PanelStatus.STEPPED
                        panel_is_broken = self.break_panel()

                        if panel_is_broken:
                            self.panels[step] = PanelStatus.BROKEN
                            player_is_alive = False
                        if not player_is_alive:
                            print("Player {} is eliminated.".format(player_num))
                            break
                    elif panel_status == PanelStatus.BROKEN:
                        continue
                    else:
                        player_num_memory -= 1
                        continue

                if player_is_alive:
                    self.survivals[player_num] += 1
            self.panels = [PanelStatus.NOT_STEPPED] * self.num_of_steps

        self.print_survival_chances()

    @staticmethod
    def break_panel():
        return random.randrange(0, 2)

    def calculate_player_survival(self, player_num):
        return self.survivals[player_num] / self.num_of_itr

    def print_survival_chances(self):
        for player_num in range(len(self.survivals)):
            player_chances = round(100 * self.calculate_player_survival(player_num), 2)
            print("Player {} has a {}% chance of survival.".format(player_num + 1, player_chances))


if __name__ == "__main__":
    glass_bridge_game_sim = GlassBridgeGameSim(player_memory=10)
    glass_bridge_game_sim.run_sim()
