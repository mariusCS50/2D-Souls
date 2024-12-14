import arcade
import math
from enemy import Enemy

class RangerEnemy(Enemy):
    def __init__(self, enemy_type, weapon_name, pos_x, pos_y, speed, vision_radius, scene, collision_layers):
        super().__init__(enemy_type, pos_x, pos_y, speed, vision_radius, scene, collision_layers)

        self.damage = self.weapons[weapon_name]["damage"]
        self.projectile_texture = self.weapons[weapon_name]["projectile"]

        self.avoidance_distance = 150

        self.shoot_dir_x = 0
        self.shoot_dir_y = 0

    def follow_target(self, delta_time):
        diff_x = self.target.center_x - self.center_x
        diff_y = self.target.center_y - self.center_y
        distance = math.sqrt(diff_x ** 2 + diff_y ** 2)

        self.shoot_dir_x = diff_x / distance
        self.shoot_dir_y = diff_y / distance

        if distance > self.avoidance_distance:
            self.dir_x = self.shoot_dir_x
            self.dir_y = self.shoot_dir_y
        elif abs(distance - self.avoidance_distance) < 1:
            self.dir_x = self.dir_y = 0
        else:
            self.dir_x = -self.shoot_dir_x
            self.dir_y = -self.shoot_dir_y

        self.change_x = self.dir_x * self.speed * delta_time
        self.change_y = self.dir_y * self.speed * delta_time

        # TODO: shoot player with arrows
        pass