"""
GlassBridgeGameSim calculates the probability of player survival
by running simulations of players moving across the bridge, with
randomised survival paths.

Default should be 16 players, 18 steps with 1000 sim iterations.


"""
import random


class GlassBridgeGameSim:
    def __init__(self, num_of_players=16,
                 num_of_steps=18,
                 num_of_itr=1000000):

        self.survivals = [0] * num_of_players
        self.num_of_steps = num_of_steps
        self.num_of_itr = num_of_itr

    def run_sim(self):
        for itr in range(self.num_of_itr):
            print("Simulating iteration ", itr)
            stepped = [0] * self.num_of_steps

            for player_num in range(len(self.survivals)):
                player_is_alive = True

                for step in range(self.num_of_steps):
                    if stepped[step]:
                        continue
                    else:
                        panel_is_broken = self.break_panel()
                        if not panel_is_broken:
                            player_is_alive = False
                        stepped[step] = 1
                        if not player_is_alive:
                            break

                if player_is_alive:
                    self.survivals[player_num] += 1

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
    glass_bridge_game_sim = GlassBridgeGameSim()
    glass_bridge_game_sim.run_sim()
