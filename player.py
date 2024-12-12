import arcade
import math
from game_resources import PlayerResources
from melee_weapon import MeleeWeapon

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

        self.can_dodge = True
        self.can_attack = True

        self.attack_speed = 0.35
        self.attack_timer = 0
        self.attack_cooldown = 0.45
        self.attack_cooldown_timer = 0

        self.dodge_speed = 400
        self.dodge_time = 0.3
        self.dodge_timer = 0
        self.dodge_cooldown = 1.2
        self.dodge_cooldown_timer = 0

        self.idle_textures = PlayerResources().get_idle_textures()
        self.walking_textures = PlayerResources().get_walking_textures()
        self.attack_textures = PlayerResources().get_attack_textures()

        self.current_facing_direction = "up"
        self.last_facing_direction = ""

        self.walk_texture_index = 0
        self.animation_walk_speed = 0.2
        self.animation_walk_timer = 0

        self.set_custom_hitbox()

        self.sword = MeleeWeapon(10)
        self.weapon_hitbox = None

    def set_custom_hitbox(self):
        hitbox = [
            (-self.width / 1.5, -self.height),
            (self.width / 1.5, -self.height),
            (self.width / 1.5, 0),
            (-self.width / 1.5, 0)
        ]
        self.set_hit_box(hitbox)

    def is_moving(self):
        return self.dir_x != 0 or self.dir_y != 0

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

        self.last_facing_direction = self.current_facing_direction

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

    def animate_walk(self, delta_time):
        if self.is_moving():
            if self.animation_walk_timer > self.animation_walk_speed:
                self.walk_texture_index = (self.walk_texture_index + 1) % 2
                self.texture = self.walking_textures[self.current_facing_direction][self.walk_texture_index]
                self.animation_walk_timer = 0

            elif self.current_facing_direction != self.last_facing_direction:
                self.walk_texture_index = 0
                self.texture = self.walking_textures[self.current_facing_direction][0]
                self.animation_walk_timer = 0

            self.animation_walk_timer += delta_time
        else:
            self.texture = self.idle_textures[self.current_facing_direction]
            self.animation_walk_timer = 0

    def walk(self, delta_time):
        self.update_dir()
        self.animate_walk(delta_time)

        self.change_x = self.dir_x * self.speed * delta_time
        self.change_y = self.dir_y * self.speed * delta_time

    def dodge(self, delta_time):
        if not self.direction_lock:
            self.update_dir()
            self.animate_walk(delta_time)
            self.direction_lock = True

        self.change_x = self.dir_x * self.dodge_speed * delta_time
        self.change_y = self.dir_y * self.dodge_speed * delta_time

        self.dodge_timer += delta_time
        if self.dodge_timer > self.dodge_time:
            self.is_dodging = False
            self.dodge_timer = 0
            self.direction_lock = False
            return

    def dodge_cooldown_update(self, delta_time):
        if not self.can_dodge:
            self.dodge_cooldown_timer += delta_time
            if self.dodge_cooldown_timer > self.dodge_cooldown:
                self.can_dodge = True
                self.dodge_cooldown_timer = 0

    def attack(self, delta_time, enemies):
        self.weapon_hitbox = self.sword.create_sword_hitbox(self)

        self.attack_timer += delta_time

        if self.attack_timer <= self.attack_speed:
            self.texture = self.attack_textures[self.current_facing_direction]
            self.change_x = 0
            self.change_y = 0

            enemies_hit = arcade.check_for_collision_with_list(self.weapon_hitbox, enemies)
            for enemy in enemies_hit:
                enemies.remove(enemy)

        else:
            self.is_attacking = False
            self.can_attack = False
            self.attack_timer = 0.0
            self.texture = self.idle_textures[self.current_facing_direction]
            self.set_custom_hitbox()
            self.weapon_hitbox = None

    def attack_cooldown_update(self, delta_time):
        if not self.can_attack:
            self.attack_cooldown_timer += delta_time
            if self.attack_cooldown_timer > self.attack_cooldown:
                self.can_attack = True
                self.attack_cooldown_timer = 0

    def attack_cooldown_update(self, delta_time):
        if not self.can_attack:
            self.attack_cooldown_timer += delta_time
            if self.attack_cooldown_timer > self.attack_cooldown:
                self.can_attack = True
                self.attack_cooldown_timer = 0

    def on_update(self, delta_time, enemies):
        if self.is_dodging:
            self.dodge(delta_time)
        elif self.is_attacking:
            self.attack(delta_time, enemies)
        else:
            self.walk(delta_time)

        self.dodge_cooldown_update(delta_time)
        self.attack_cooldown_update(delta_time)