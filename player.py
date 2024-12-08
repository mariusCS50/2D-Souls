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

        self.dir_x = 0
        self.dir_y = 0

    def update_dir(self):
        if self.move_right:
            self.dir_x += 1
        if self.move_left:
            self.dir_x -= 1

        if self.move_up:
            self.dir_y += 1
        if self.move_down:
            self.dir_y -= 1

        # normalize directions
        if (abs(self.dir_x) == 1 and abs(self.dir_y) == 1):
            factor = 1 / math.sqrt(2)

            self.dir_x *= factor
            self.dir_y *= factor

    def on_update(self, delta_time):
        self.update_dir()
        
        self.change_x = self.dir_x * self.speed
        self.change_y = self.dir_y * self.speed

        self.center_x += self.change_x * delta_time
        self.center_y += self.change_y * delta_time
    