import arcade
import random
from abc import ABC, abstractmethod
from game_resources import EnemyResources, WeaponResources

class Enemy(arcade.Sprite, ABC):
    def __init__(self, enemy_type, pos_x, pos_y, speed, vision_radius, scene, collision_layers):
        super().__init__(texture=arcade.load_texture("assets/temp_player.png"), scale=0.5)

        self.scene = scene

        self.center_x = pos_x
        self.center_y = pos_y

        self.speed = speed

        self.dir_x = 0
        self.dir_y = 0

        self.target = scene["Player"][0]
        self.vision_radius = vision_radius

        self.timer = 0
        self.wandering_time = 2
        self.staying_idle_time = 2

        self.can_attack = False

        self.is_attacking = False
        self.is_idle = True
        self.directions = EnemyResources.get_walking_directions()

        self.collision_layers = collision_layers
        self.physics_engine = arcade.PhysicsEngineSimple(self, self.collision_layers)

        self.enemy_textures = EnemyResources.get_textures(enemy_type)
        self.weapons = WeaponResources.get_weapons()

        self.current_facing_direction = "down"
        self.texture = self.enemy_textures["idle"][self.current_facing_direction]

        self.attack_speed = 0.4
        self.attack_timer = 0
        self.attack_cooldown = 0.6
        self.attack_cooldown_timer = 0

        self.walk_texture_index = 0
        self.animation_walk_speed = 0.2
        self.animation_walk_timer = 0

        self.set_custom_hitbox()

    def set_custom_hitbox(self):
        hitbox = [
            (-self.width / 2, -self.height),
            (self.width / 2, -self.height),
            (self.width / 2, 0),
            (-self.width / 2, 0)
        ]
        self.set_hit_box(hitbox)

    def get_facing_direction(self):
        if abs(self.dir_x) > abs(self.dir_y):
            if self.dir_x > 0:
                return "right"
            else:
                return "left"
        else:
            if self.dir_y > 0:
                return "up"
            else:
                return "down"

    def animate_walk(self, delta_time):
        self.animation_walk_timer += delta_time
        if self.animation_walk_timer > self.animation_walk_speed:
            self.walk_texture_index = (self.walk_texture_index + 1) % 2
            self.texture = self.enemy_textures["walk"][self.current_facing_direction][self.walk_texture_index]
            self.animation_walk_timer = 0

    def wandering_logic(self, delta_time):
        self.timer += delta_time

        self.change_x = 0
        self.change_y = 0

        if self.is_idle:
            self.texture = self.enemy_textures["idle"][self.current_facing_direction]

            if self.timer > self.staying_idle_time:
                self.timer = 0
                self.is_idle = False
                self.dir_x, self.dir_y = self.directions[random.randint(0, 3)]
                self.current_facing_direction = self.get_facing_direction()

        else:
            self.change_x = self.dir_x * 50 * delta_time
            self.change_y = self.dir_y * 50 * delta_time
            self.animate_walk(delta_time)

            if self.timer > self.wandering_time:
                self.timer = 0
                self.is_idle = True

    def has_line_of_sight(self):
        return arcade.has_line_of_sight(
            self.position,
            self.target.position,
            self.collision_layers,
            self.vision_radius
        )

    @abstractmethod
    def on_update(self, delta_time):
        pass