import arcade
import arcade.gui

class HealthBar(arcade.gui.UIWidget):
    def __init__(self, x, y, width, height, border_thickness, health, max_health):
        super().__init__()
        
        percentange = health / max_health
        
        self.health_bar = arcade.gui.UISpace(x, y, width, height, (127, 0, 0))
        self.fill = arcade.gui.UISpace(x, y, percentange * width, height, (255, 0, 0))

        self.border = arcade.gui.UISpace(
            x - border_thickness,
            y - border_thickness,
            width + 2 * border_thickness,
            height + 2 * border_thickness,
            (0, 0, 0))

        self.add(self.border)
        self.add(self.health_bar)
        self.add(self.fill)

    def update_bar(self, health, max_health):
        percentange = health / max_health
        new_width = self.health_bar.width * percentange

        new_fill = arcade.gui.UISpace(
            self.fill.x,
            self.fill.y,
            new_width,
            self.fill.height,
            self.fill.color
        )

        self.remove(self.fill)

        self.fill = new_fill
        self.add(self.fill)
