import arcade

class DropSprite(arcade.Sprite):
    def __init__(self, name, texture, pos_x, pos_y, scene, is_permanent=False):
        super().__init__(texture=texture)

        self.center_x = pos_x
        self.center_y = pos_y

        self.name = name
        self.timer = 15

        self.is_permanent = is_permanent

        self.scene = scene

    def on_update(self, delta_time):
        if not self.is_permanent:
            self.timer -= delta_time

            if self.timer <= 5:
                self.alpha = (255 + 64) - self.alpha

            if self.timer <= 0:
                self.scene["Drops"].remove(self)