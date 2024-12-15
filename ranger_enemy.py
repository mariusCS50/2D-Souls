import arcade
import math
from enemy import Enemy
from projectile import Projectile

class RangerEnemy(Enemy):
    def __init__(self, enemy_type, weapon_name, pos_x, pos_y, speed, health, shoot_time, shoot_cooldown, vision_radius, drops, scene, collision_layers):
        super().__init__(enemy_type, pos_x, pos_y, speed, health, vision_radius, drops, scene, collision_layers)

        self.damage = self.weapons[weapon_name]["damage"]
        self.projectile_texture = self.weapons[weapon_name]["projectile_texture"]
        self.projectile_speed = self.weapons[weapon_name]["projectile_speed"]

        self.avoidance_distance = self.vision_radius / 2

        self.is_shooting = False
        self.can_shoot = True
        self.shot_projectile = False

        self.shoot_time = shoot_time
        self.shoot_timer = 0

        self.shoot_cooldown = shoot_cooldown
        self.shoot_cooldown_timer = 0

        self.shoot_dir_x = 0
        self.shoot_dir_y = 0

    def set_custom_hitbox(self):
        hitbox = [
            (-self.width / 4, -self.height / 4),
            (self.width / 4, -self.height / 4),
            (self.width / 4, self.height / 4),
            (-self.width / 4, self.height / 4)
        ]
        self.set_hit_box(hitbox)

    def walk(self, delta_time):
        diff_x = self.get_target().center_x - self.center_x
        diff_y = self.get_target().center_y - self.center_y
        distance = math.sqrt(diff_x ** 2 + diff_y ** 2)

        self.shoot_dir_x = diff_x / distance
        self.shoot_dir_y = diff_y / distance

        if abs(distance - self.avoidance_distance) < 10:
            self.dir_x = self.dir_y = 0
            self.texture = self.enemy_textures["idle"][self.current_facing_direction]
        else:
            self.dir_x = diff_x / distance
            self.dir_y = diff_y / distance

            self.current_facing_direction = self.get_facing_direction()

            if distance <= self.avoidance_distance:
                self.dir_x *= -1
                self.dir_y *= -1

            self.animate_walk(delta_time)

        self.change_x = self.dir_x * self.speed * delta_time
        self.change_y = self.dir_y * self.speed * delta_time

    def shoot(self, delta_time):
        if self.shoot_timer <= self.shoot_time:
            self.texture = self.enemy_textures["attack"][self.current_facing_direction]
            self.change_x = self.dir_x = 0
            self.change_y = self.dir_y = 0

            if not self.shot_projectile:
                projectile = Projectile(
                    self.projectile_texture,
                    self.center_x,
                    self.center_y,
                    self.shoot_dir_x,
                    self.shoot_dir_y,
                    self.projectile_speed,
                    self.damage,
                    self.scene,
                    "Player"
                )

                self.scene["Projectiles"].append(projectile)
                self.shot_projectile = True

        else:
            self.shot_projectile = False
            self.is_shooting = False
            self.shoot_timer = 0.0

        self.shoot_timer += delta_time

    def shoot_cooldown_update(self, delta_time):
        if not self.can_shoot:
            self.shoot_cooldown_timer += delta_time
            if self.shoot_cooldown_timer > self.shoot_cooldown:
                self.can_shoot = True
                self.shoot_cooldown_timer = 0

    def on_update(self, delta_time):
        self.physics_engine.update()

        if self.is_shooting:
            self.shoot(delta_time)

        elif self.has_line_of_sight():
            self.walk(delta_time)

            if self.can_shoot:
                self.is_shooting = True
                self.can_shoot = False

                self.shoot(delta_time)
        else:
            self.wandering_logic(delta_time)

        self.shoot_cooldown_update(delta_time)
        self.invincible_timer_update(delta_time)