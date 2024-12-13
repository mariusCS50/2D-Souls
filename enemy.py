import arcade
from abc import ABC, abstractmethod

class Enemy(arcade.Sprite, ABC):
    def __init__(self, sprite, pos_x, pos_y, speed, target, vision_radius, collision_layers):
        # temporary sprite
        super().__init__(sprite, scale=0.0625)

        self.center_x = pos_x
        self.center_y = pos_y

        self.speed = speed

        self.dir_x = 0
        self.dir_y = 0

        self.target = target
        self.vision_radius = vision_radius

        self.wandering = True
        self.found_target = False

        self.physics_engine = arcade.PhysicsEngineSimple(self, collision_layers)

    def wandering_logic(self, delta_time):
        self.change_x = 0
        self.change_y = 0

    @abstractmethod
    def found_target_logic(self, delta_time):
        pass

    def on_update(self, delta_time):
        self.physics_engine.update()

        distance = arcade.get_distance_between_sprites(self, self.target)

        if distance <= self.vision_radius:
            self.found_target_logic(delta_time)
        else:
            self.wandering_logic(delta_time)