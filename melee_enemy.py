import arcade
import math
import random
from enemy import Enemy

class MeleeEnemy(Enemy):
    def __init__(self, sprite, pos_x, pos_y, speed, vision_radius, scene, collision_layers, melee_weapon):
        super().__init__(sprite, pos_x, pos_y, speed, vision_radius, scene, collision_layers)

        self.melee_weapon = melee_weapon

        # self.barrier_list = arcade.AStarBarrierList(self, collision_layers, 32, 0, 1280, 0, 1280)
        # self.path = None

    def found_target_logic(self, delta_time):
        # self.path = arcade.astar_calculate_path(self.position, self.target.position, self.barrier_list, diagonal_movement=True)

        # if self.path and len(self.path) > 1:
        #     if self.center_x < self.path[1][0]:
        #         self.center_x += min(self.speed, self.path[1][0] - self.center_x)
        #     elif self.center_x > self.path[1][0]:
        #         self.center_x -= min(self.speed, self.center_x - self.path[1][0])

        #     if self.center_y < self.path[1][1]:
        #         self.center_y += min(self.speed, self.path[1][1] - self.center_y)
        #     elif self.center_y > self.path[1][1]:
        #         self.center_y -= min(self.speed, self.center_y - self.path[1][1])
        diff_x = self.target.center_x - self.center_x
        diff_y = self.target.center_y - self.center_y
        distance = math.sqrt(diff_x ** 2 + diff_y ** 2)

        self.dir_x = diff_x / distance
        self.dir_y = diff_y / distance

        self.change_x = self.dir_x * self.speed * delta_time
        self.change_y = self.dir_y * self.speed * delta_time

        # TODO: attack player when is attacking with meele weapon
        pass