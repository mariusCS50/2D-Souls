import arcade
import math
from enemy import Enemy

class SimpleEnemy(Enemy):
    def __init__(self, enemy_type, pos_x, pos_y, speed, vision_radius, scene, collision_layers, damage):
        super().__init__(enemy_type, pos_x, pos_y, speed, vision_radius, scene, collision_layers)

        self.damage = damage

    def follow_target(self, delta_time):
        diff_x = self.target.center_x - self.center_x
        diff_y = self.target.center_y - self.center_y
        distance = math.sqrt(diff_x ** 2 + diff_y ** 2)

        if distance > 50:
            self.dir_x = diff_x / distance
            self.dir_y = diff_y / distance

            new_x = self.center_x + self.dir_x * self.speed * delta_time
            new_y = self.center_y + self.dir_y * self.speed * delta_time

            self.center_x = new_x
            collides_x = arcade.check_for_collision(self, self.target)
            self.center_x = self.center_x - self.dir_x * self.speed * delta_time

            self.center_y = new_y
            collides_y = arcade.check_for_collision(self, self.target)
            self.center_y = self.center_y - self.dir_y * self.speed * delta_time

            if not collides_x:
                self.change_x = self.dir_x * self.speed * delta_time
            else:
                self.change_x = 0

            if not collides_y:
                self.change_y = self.dir_y * self.speed * delta_time
            else:
                self.change_y = 0

            self.current_facing_direction = self.get_facing_direction()
            self.animate_walk(delta_time)

        else:
            self.change_x = 0
            self.change_y = 0

        # if arcade.check_for_collision(self, self.target):
            # self.target.take_damage(self.damage)