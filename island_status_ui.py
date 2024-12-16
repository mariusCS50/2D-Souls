import arcade
import arcade.gui

class IslandStatusUI(arcade.gui.UILayout):
    def __init__(self, max_number_enemies):
        super().__init__()

        self.max_number_enemies = max_number_enemies

        self.space = arcade.gui.UISpace(16, 550, 230, 38, color=(0,0,0,128))
        self.enemies_label = arcade.gui.UILabel(24, 553, text=f"Enemies: {max_number_enemies}/{max_number_enemies}", font_size=20)
        self.boss_incoming_label = arcade.gui.UILabel(210, 400, text=f"Boss incoming...", font_size=36, text_color=arcade.color.RED)

        self.add(self.space)
        self.add(self.enemies_label)

        self.boss_incoming = False
        self.stop = False

        self.boss_incoming_label_countdown = 3

    def boss_incoming_label_countdown_update(self, delta_time):
        if self.boss_incoming:
            self.boss_incoming_label_countdown -= delta_time

            if self.boss_incoming_label_countdown <= 0:
                self.remove(self.space)
                self.remove(self.boss_incoming_label)
                self.stop = True

    def update(self, no_enemies, delta_time):
        if self.stop:
            return
        
        if no_enemies > 0:
            self.enemies_label.text = f"Enemies: {no_enemies}/{self.max_number_enemies}"
        elif not self.boss_incoming:
            self.boss_incoming = True

            self.remove(self.space)
            self.space = arcade.gui.UISpace(205, 395, 400, 60, color=(0,0,0,128))
            self.add(self.space)

            self.remove(self.enemies_label)
            self.add(self.boss_incoming_label)

        self.boss_incoming_label_countdown_update(delta_time)