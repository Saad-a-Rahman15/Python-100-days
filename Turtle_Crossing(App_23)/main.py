import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

class CrossyRoad():
    def __init__(self):
        self.screen = Screen()
        self.player = Player()
        self.car_manager = CarManager()
        self.scoreboard = Scoreboard()
        self.game_is_on = True
        self.setup_game()
        self.canvas = self.screen.getcanvas()
        self.root = self.canvas.winfo_toplevel()
        self.root.resizable(False, False)

    def setup_game(self):
        """Resets all game components to their initial state."""
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("gray20")
        self.screen.title("Crossy Road")
        self.screen.tracer(0)

        self.player.go_to_start()
        self.car_manager.reset()
        self.scoreboard.reset()

        self.screen = Screen()
        self.screen.listen()
        self.screen.onkey(self.player.up, "Up")

    def restart(self):
        answer = self.screen.textinput("Game Over", "You died! Play again? Click 'r' to restart or 'n' to end game: ")
        if answer and answer.lower().strip() == 'r':
            self.setup_game()
            self.run_game()
        else:
            self.screen.bye()

    def run_game(self):
        game_is_on = True
        while game_is_on:
            time.sleep(0.1)
            self.screen.update()

            self.car_manager.create_car()
            self.car_manager.move_car()

            for car in self.car_manager.cars:
                if car.distance(self.player) <= 20:
                    self.scoreboard.game_over()
                    game_is_on = False
                    self.scoreboard.level = 1
                    self.restart()
                    return

            if self.player.at_finish():
                self.player.go_to_start()
                self.car_manager.level_up()
                self.scoreboard.increase_level()

if __name__ == "__main__":
    game = CrossyRoad()
    game.setup_game()
    game.run_game()

