import arcade
import math
from enemy import Enemy

class MeleeEnemy(Enemy):
    def __init__(self, sprite, pos_x, pos_y, speed, vision_radius, scene, collision_layers, melee_weapon):
        super().__init__(sprite, pos_x, pos_y, speed, vision_radius, scene, collision_layers)
        
        self.melee_weapon = melee_weapon

    def found_target_logic(self, delta_time):
        diff_x = self.target.center_x - self.center_x
        diff_y = self.target.center_y - self.center_y
        distance = math.sqrt(diff_x ** 2 + diff_y ** 2)

        self.dir_x = diff_x / distance
        self.dir_y = diff_y / distance

        self.change_x = self.dir_x * self.speed * delta_time
        self.change_y = self.dir_y * self.speed * delta_time

        # TODO: attack player when is attacking with meele weapon
        pass