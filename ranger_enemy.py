import arcade
from enemy import Enemy

class RangerEnemy(Enemy):
    def __init__(self, pos_x, pos_y, speed, target, vision_radius):
        super().__init__(pos_x, pos_y, speed, target, vision_radius)

    def found_target_logic(self, delta_time):
        # TODO: shoot player with arrows
        pass