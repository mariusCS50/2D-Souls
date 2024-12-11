import arcade
from abc import ABC, abstractmethod

class Enemy(arcade.Sprite, ABC):
    def __init__(self, pos_x, pos_y, speed, target, vision_radius):
        # temporary sprite
        super().__init__("assets/temp_player.png", scale=0.0625)

        self.center_x = pos_x
        self.center_y = pos_y

        self.speed = speed

        self.dir_x = 0
        self.dir_y = 0

        self.target = target
        self.vision_radius = vision_radius

        self.wandering = True
        self.found_target = False

    def wandering_logic(self, delta_time):
        # TODO: wandering logic
        pass

    @abstractmethod
    def found_target_logic(self, delta_time):
        pass

    def on_update(self, delta_time):
        distance = arcade.get_distance_between_sprites(self, self.target)

        if distance <= self.vision_radius:
            self.wandering = False
            self.found_target = True
        else:
            self.wandering = True
            self.found_target = False

        if self.wandering:
            self.wandering_logic(delta_time)
        elif self.found_target:
            self.found_target_logic(delta_time)
