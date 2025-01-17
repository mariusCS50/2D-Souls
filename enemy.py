import arcade
import random
from abc import ABC, abstractmethod
from game_resources import EnemyResources, ItemResources
from drop_sprite import DropSprite

class Enemy(arcade.Sprite, ABC):
    def __init__(self, enemy_type, pos_x, pos_y, speed, health, vision_radius, drops, scene, collision_layers):
        super().__init__(scale=0.5)

        self.scene = scene

        self.center_x = pos_x
        self.center_y = pos_y

        self.speed = speed

        self.dir_x = 0
        self.dir_y = 0

        self.max_health = self._health = health

        self.vision_radius = vision_radius

        self.timer = 0
        self.wandering_time = 2
        self.staying_idle_time = 2

        self.is_idle = True

        self.is_invincible = False

        self.invincible_time = 0.6
        self.invincible_timer = 0

        self.directions = EnemyResources.get_walking_directions()

        self.collision_layers = collision_layers
        self.physics_engine = arcade.PhysicsEngineSimple(self, self.collision_layers)

        self.enemy_textures = EnemyResources.get_textures(enemy_type)
        self.weapons = ItemResources.get_weapons()

        self.current_facing_direction = "down"
        self.texture = self.enemy_textures["idle"][self.current_facing_direction]

        self.walk_texture_index = 0
        self.animation_walk_time = 0.2
        self.animation_walk_timer = 0

        self.is_dying = False
        self.death_time = 0.4
        self.death_timer = 0

        self.drops = drops

        self.set_custom_hitbox()

    def get_target(self):
        return self.scene["Player"][0]

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, val):
        if val <= 0:
            self.die()

        self._health = val

    def die(self):
        self.change_x = 0
        self.change_y = 0
        self.is_dying = True
        self.texture = self.enemy_textures["death"][self.current_facing_direction]

        drop = random.choices(list(self.drops.keys()), weights=list(self.drops.values()))[0]
        if drop is not None:
            self.scene["Drops"].append(DropSprite(drop, self.weapons[drop]["texture"], self.center_x, self.center_y, self.scene))

    @abstractmethod
    def set_custom_hitbox(self):
        pass

    def get_facing_direction(self, dir_x, dir_y):
        if abs(dir_x) > abs(dir_y):
            if dir_x > 0:
                return "right"
            else:
                return "left"
        else:
            if dir_y > 0:
                return "up"
            else:
                return "down"

    def animate_walk(self, delta_time):
        self.animation_walk_timer += delta_time
        if self.animation_walk_timer > self.animation_walk_time:
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
                self.current_facing_direction = self.get_facing_direction(self.dir_x, self.dir_y)

        else:
            next_x = self.center_x + self.dir_x * 10
            next_y = self.center_y + self.dir_y * 10

            original_x, original_y = self.center_x, self.center_y

            self.center_x, self.center_y = next_x, next_y
            collisions = arcade.check_for_collision_with_list(self, self.collision_layers)

            self.center_x, self.center_y = original_x, original_y

            if not collisions:
                self.change_x = self.dir_x * (self.speed / 2) * delta_time
                self.change_y = self.dir_y * (self.speed / 2) * delta_time
                self.animate_walk(delta_time)
            else:
                self.dir_x, self.dir_y = self.directions[random.randint(0, 3)]
                self.current_facing_direction = self.get_facing_direction(self.dir_x, self.dir_y)

            if self.timer > self.wandering_time:
                self.timer = 0
                self.is_idle = True

    def take_damage(self, damage):
        if not self.is_invincible and not self.is_dying:
            self.health -= damage
            self.is_invincible = True

    def invincible_timer_update(self, delta_time):
        if self.is_invincible and not self.is_dying:
            self.alpha = (255 + 128) - self.alpha
            self.invincible_timer += delta_time

            if self.invincible_timer > self.invincible_time:
                self.is_invincible = False
                self.invincible_timer = 0
                self.alpha = 255

    def death_timer_update(self, delta_time):
        if self.is_dying:
            self.death_timer += delta_time
            if self.death_timer >= self.death_time:
                self.scene["Enemies"].remove(self)
                self.death_timer = 0
                self.is_dying = False


    def has_line_of_sight(self):
        return arcade.has_line_of_sight(
            self.position,
            self.get_target().position,
            self.collision_layers,
            self.vision_radius
        )

    @abstractmethod
    def on_update(self, delta_time):
        pass