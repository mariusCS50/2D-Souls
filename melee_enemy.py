import arcade
from enemy import Enemy

class MeleeEnemy(Enemy):
    def __init__(self, pos_x, pos_y, speed, target, vision_radius):
        super().__init__(pos_x, pos_y, speed, target, vision_radius)

    def found_target_logic(self, delta_time):
        # TODO: attack player with sword
        pass