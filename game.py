import arcade
from player import Player

class Game(arcade.Window):
    def __init__(self, width = 800, height = 600, title = "2D Souls"):
        super().__init__(width, height, title)

    def setup(self):
        self.player = Player(200, 200)

    def on_update(self, delta_time):
        self.player.on_update(delta_time)

    def on_draw(self):
        self.clear()
        self.player.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.D:
            self.player.move_right = True
        elif key == arcade.key.A:
            self.player.move_left = True
        elif key == arcade.key.W:
            self.player.move_up = True
        elif key == arcade.key.S:
            self.player.move_down = True
        elif key == arcade.key.SPACE:
            if self.player.is_moving():
                self.player.is_dodging = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.D:
            self.player.move_right = False
        elif key == arcade.key.A:
            self.player.move_left = False
        elif key == arcade.key.W:
            self.player.move_up = False
        elif key == arcade.key.S:
            self.player.move_down = False

if __name__ == "__main__":
    game = Game()
    game.setup()
    game.run()