import arcade
import math

class Player(arcade.Sprite):
    def __init__(self, pos_x = 0, pos_y = 0):
        # temporary sprite
        super().__init__(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png")

        self.center_x = pos_x
        self.center_y = pos_y

        self.speed = 100

        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

    def update_speed(self):
        dir_x = 0
        dir_y = 0

        if self.move_right:
            dir_x += 1
        if self.move_left:
            dir_x -= 1

        if self.move_up:
            dir_y += 1
        if self.move_down:
            dir_y -= 1

        # normalize directions
        if (abs(dir_x) == 1 and abs(dir_y) == 1):
            factor = 1 / math.sqrt(2)

            dir_x *= factor
            dir_y *= factor

        self.change_x = dir_x * self.speed
        self.change_y = dir_y * self.speed

    def on_update(self, delta_time):
        self.update_speed()
        
        self.center_x += self.change_x * delta_time
        self.center_y += self.change_y * delta_time
    