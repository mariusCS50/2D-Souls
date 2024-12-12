import arcade
import math
from game_resources import PlayerResources

class Player(arcade.Sprite):
    def __init__(self, pos_x = 0, pos_y = 0):
        super().__init__(texture=arcade.load_texture("assets/player/walk_up_1.png"), scale=0.5)

        self.center_x = pos_x
        self.center_y = pos_y

        self.speed = 200

        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

        self.dir_x = 0
        self.dir_y = 0

        self.direction_lock = False
        self.is_dodging = False
        self.is_attacking = False

        self.attack_speed = 0.3
        self.attack_timer = 0

        self.dodge_speed = 300
        self.dodge_time = 0.3
        self.dodge_timer = 0

        self.idle_textures = PlayerResources().get_idle_textures()
        self.walking_textures = PlayerResources().get_walking_textures()
        self.attack_textures = PlayerResources().get_attack_textures()

        self.current_facing_direction = "up"
        self.texture_index = 0
        self.animation_timer = 0

        self.set_default_hitbox()

    def set_default_hitbox(self):
        hitbox = [
            (-self.width / 1.5, -self.height),
            (self.width / 1.5, -self.height),
            (self.width / 1.5, 0),
            (-self.width / 1.5, 0)
        ]
        self.set_hit_box(hitbox)

    def is_moving(self):
        return self.move_up or self.move_down or self.move_left or self.move_right

    def update_dir(self):
        offset_x = 0
        offset_y = 0

        if self.move_right:
            offset_x += 1
        if self.move_left:
            offset_x -= 1

        if self.move_up:
            offset_y += 1
        if self.move_down:
            offset_y -= 1

        # normalize directions
        if (abs(offset_x) == 1 and abs(offset_y) == 1):
            factor = 1 / math.sqrt(2)

            offset_x *= factor
            offset_y *= factor

        if offset_y > 0:
            self.current_facing_direction = "up"
        elif offset_y < 0:
            self.current_facing_direction = "down"
        elif offset_x < 0:
            self.current_facing_direction = "left"
        elif offset_x > 0:
            self.current_facing_direction = "right"

        self.dir_x = offset_x
        self.dir_y = offset_y

    def animate(self, delta_time):
        if self.is_moving():
            self.animation_timer += delta_time
            if self.animation_timer > 0.2:
                self.texture_index = (self.texture_index + 1) % 2
                self.texture =  self.walking_textures[self.current_facing_direction][self.texture_index]
                self.animation_timer = 0
        else:
            self.texture = self.idle_textures[self.current_facing_direction]

    def walk(self, delta_time):
        self.update_dir()

        self.change_x = self.dir_x * self.speed * delta_time
        self.change_y = self.dir_y * self.speed * delta_time

        self.animate(delta_time)

    def dodge(self, delta_time):
        if not self.direction_lock:
            self.update_dir()
            self.direction_lock = True

        self.change_x = self.dir_x * self.dodge_speed * delta_time
        self.change_y = self.dir_y * self.dodge_speed * delta_time

        self.dodge_timer += delta_time
        if self.dodge_timer > self.dodge_time:
            self.is_dodging = False
            self.dodge_timer = 0
            self.direction_lock = False
            return

    def attack(self, delta_time):
        self.attack_timer += delta_time

        if self.attack_timer <= self.attack_speed:
            self.texture = self.attack_textures[self.current_facing_direction]

        else:
            self.is_attacking = False
            self.attack_timer = 0.0
            self.scale = 0.5
            self.texture = self.idle_textures[self.current_facing_direction]
            self.set_default_hitbox()

    def on_update(self, delta_time):
        if self.is_attacking:
            self.attack(delta_time)
        elif self.is_dodging:
            self.dodge(delta_time)
        else:
            self.walk(delta_time)