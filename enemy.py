import arcade
import random
from abc import ABC, abstractmethod
from game_resources import EnemyResources

class Enemy(arcade.Sprite, ABC):
    def __init__(self, sprite, pos_x, pos_y, speed, vision_radius, scene, collision_layers):
        super().__init__(sprite, scale=0.0625)

        self.center_x = pos_x
        self.center_y = pos_y

        self.speed = speed

        self.dir_x = 0
        self.dir_y = 0

        self.target = scene["Player"][0]
        self.vision_radius = vision_radius

        self.timer = 0
        self.wandering_time = 2
        self.staying_idle_time = 2

        self.is_idle = True
        self.directions = EnemyResources().get_walking_directions()

        self.collision_layers = collision_layers
        self.physics_engine = arcade.PhysicsEngineSimple(self, self.collision_layers)

    def wandering_logic(self, delta_time):
        self.timer += delta_time

        if self.is_idle:
            if self.timer > self.staying_idle_time:
                self.timer = 0
                self.is_idle = False
                self.dir_x, self.dir_y = self.directions[random.randint(0, 3)]

        else:
            self.change_x = self.dir_x * self.speed * delta_time
            self.change_y = self.dir_y * self.speed * delta_time

            if self.timer > self.wandering_time:
                self.timer = 0
                self.is_idle = True
                self.change_x = 0
                self.change_y = 0

    def has_line_of_sight(self):
        return arcade.has_line_of_sight(
            self.position,
            self.target.position,
            self.collision_layers,
            self.vision_radius
        )

    @abstractmethod
    def found_target_logic(self, delta_time):
        pass

    def on_update(self, delta_time):
        self.physics_engine.update()

        if self.has_line_of_sight():
            self.found_target_logic(delta_time)
        else:
            self.wandering_logic(delta_time)