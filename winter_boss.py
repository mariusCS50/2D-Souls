import math
import arcade
from game_resources import EnemyResources, ItemResources
from projectile import Projectile

class WinterBoss(arcade.Sprite):
    def __init__(self, pos_x, pos_y, scene):
        super().__init__(scale=1)

        self.boss_textures = EnemyResources.get_textures("winter_slime")

        ice_wand = ItemResources.get_weapons()["ice_wand"]
        self.projectile_damage = ice_wand["damage"]
        self.projectile_texture = ice_wand["projectile_texture"]
        self.projectile_speed = ice_wand["projectile_speed"]

        self.collision_damage = self.projectile_damage / 2

        self.center_x = pos_x
        self.center_y = pos_y

        self.speed = 96

        self.max_health = self._health = 100

        self.scene = scene
        self.physics_engine = arcade.PhysicsEngineSimple(self, scene["Collision Layer"])

        self.is_shooting = False
        self.can_shoot = False
        self.is_invincible = False
        self.is_dying = False

        self.invincible_time = 1
        self.invincible_timer = 0

        self.shot_projectiles = False

        self.shoot_time = 0.3
        self.shoot_timer = 0
        self.shoot_cooldown = 2.5
        self.shoot_cooldown_timer = 0

        self.death_time = 0.4
        self.death_timer = 0

        self.current_facing_direction = "down"
        self.texture = self.boss_textures["idle"][self.current_facing_direction]

        self.walk_texture_index = 0
        self.animation_walk_time = 0.2
        self.animation_walk_timer = 0

        self.all_dirs = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0),
            (1 / math.sqrt(2), 1 / math.sqrt(2)),
            (1 / math.sqrt(2), -1 / math.sqrt(2)),
            (-1 / math.sqrt(2), -1 / math.sqrt(2)),
            (-1 / math.sqrt(2), 1 / math.sqrt(2))
        ]

        self.set_custom_hitbox()

    def set_custom_hitbox(self):
        hitbox = [
            (-self.width / 8, -self.height / 8),
            (self.width / 8, -self.height / 8),
            (self.width / 8, self.height / 8),
            (-self.width / 8, self.height / 8)
        ]
        self.set_hit_box(hitbox)

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
        self.texture = self.boss_textures["death"][self.current_facing_direction]

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
        if self.animation_walk_timer > self.animation_walk_time:
            self.walk_texture_index = (self.walk_texture_index + 1) % 2
            self.texture = self.boss_textures["walk"][self.current_facing_direction][self.walk_texture_index]
            self.animation_walk_timer = 0

    def walk(self, delta_time):
        diff_x = self.get_target().center_x - self.center_x
        diff_y = self.get_target().center_y - self.center_y
        distance = math.sqrt(diff_x ** 2 + diff_y ** 2)

        self.dir_x = diff_x / distance
        self.dir_y = diff_y / distance

        self.change_x = self.dir_x * self.speed * delta_time
        self.change_y = self.dir_y * self.speed * delta_time

        self.current_facing_direction = self.get_facing_direction()
        self.animate_walk(delta_time)

    def shoot(self, delta_time):
        if self.shoot_timer <= self.shoot_time:
            self.texture = self.boss_textures["attack"][self.current_facing_direction]
            self.change_x = self.dir_x = 0
            self.change_y = self.dir_y = 0

            if not self.shot_projectiles:
                for dir in self.all_dirs:
                    projectile = Projectile(
                        self.projectile_texture,
                        self.center_x,
                        self.center_y,
                        dir[0],
                        dir[1],
                        self.projectile_speed,
                        self.projectile_damage,
                        self.scene,
                        ["Player"]
                    )

                    self.scene["Projectiles"].append(projectile)

                self.shot_projectiles = True
        else:
            self.shot_projectiles = False
            self.is_shooting = False
            self.shoot_timer = 0.0

        self.shoot_timer += delta_time

    def shoot_cooldown_update(self, delta_time):
        if not self.can_shoot:
            self.shoot_cooldown_timer += delta_time
            if self.shoot_cooldown_timer > self.shoot_cooldown:
                self.can_shoot = True
                self.is_shooting = True
                self.shoot_cooldown_timer = 0

    def take_damage(self, damage):
        if not self.is_invincible:
            self.health -= damage
            self.is_invincible = True

    def invincible_timer_update(self, delta_time):
        if self.is_invincible:
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
                self.scene["Boss"].remove(self)
                self.death_timer = 0
                self.is_dying = False

    def on_update(self, delta_time):
        self.physics_engine.update()

        if self.is_dying:
            self.death_timer_update(delta_time)
        elif self.is_shooting:
            self.can_shoot = False
            self.shoot(delta_time)
        else:
            self.walk(delta_time)

        if arcade.check_for_collision(self, self.get_target()):
            self.get_target().take_damage(self.collision_damage)

        self.shoot_cooldown_update(delta_time)
        self.invincible_timer_update(delta_time)


