import arcade
import arcade.gui

class HealthBar(arcade.gui.UIWidget):
    def __init__(self, player):
        super().__init__()
        self.border = arcade.gui.UISpace(x=14, y=14, height=20, width=204, color=(0, 0, 0))
        self.bar = arcade.gui.UISpace(x=16, y=16, height=16, width=200, color=(255, 0, 0))

        self.add(self.border)
        self.add(self.bar)