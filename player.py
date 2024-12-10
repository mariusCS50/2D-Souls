import arcade
import math

class Player(arcade.Sprite):
    def __init__(self, pos_x = 0, pos_y = 0):
        # temporary sprite
        super().__init__("assets/temp_player.png", scale=0.0625)

        self.center_x = pos_x
        self.center_y = pos_y

        self.speed = 3

        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

        self.dir_x = 0
        self.dir_y = 0

        self.lock_dir = False

        self.is_dodging = False

        self.dodge_speed = 6

        self.dodge_time = 0.3
        self.dodge_timer = 0.2

    def is_moving(self):
        return self.move_up or self.move_down or self.move_left or self.move_right

    def update_dir(self):
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

        self.dir_x = dir_x
        self.dir_y = dir_y

    def move(self, delta_time):
        self.center_x += self.change_x * delta_time
        self.center_y += self.change_y * delta_time

    def walk_logic(self, delta_time):
        self.update_dir()

        self.change_x = self.dir_x * self.speed
        self.change_y = self.dir_y * self.speed

        self.move(delta_time)

    def dodge_logic(self, delta_time):
        if not self.lock_dir:
            self.update_dir()
            self.lock_dir = True

            self.change_x = self.dir_x * self.dodge_speed
            self.change_y = self.dir_y * self.dodge_speed

        self.move(delta_time)

        self.dodge_timer += delta_time
        if self.dodge_timer > self.dodge_time:
            self.is_dodging = False
            self.dodge_timer = 0
            self.lock_dir = False
            return

    def on_update(self, delta_time):
        if self.is_dodging:
            self.dodge_logic(delta_time)
        else:
            self.walk_logic(delta_time)
