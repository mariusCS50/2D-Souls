import arcade
from game_resources import WeaponResources

class NamedSprite(arcade.Sprite):
    def __init__(self, name, texture, pos_x, pos_y):
        super().__init__(texture=texture)

        self.center_x = pos_x
        self.center_y = pos_y

        self.name = name