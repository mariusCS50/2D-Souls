import arcade
import math
from game_resources import EnemyResources, ItemResources

class VolcanoBoss(arcade.Sprite):
    def __init__(self, pos_x, pos_y, scene):
        super().__init__(scale=1)

        self.boss_textures = EnemyResources.get_textures("volcano_orc")

        self.damage = ItemResources.get_weapons()["volcano_sword1"]["damage"]

        self.center_x = pos_x
        self.center_y = pos_y

        self.stats_multiplier = 1.0

        self.speed = 144

        self.max_health = self._health = 150

        self.ability_name = "volcano_boss"

        self.scene = scene
        self.physics_engine = arcade.PhysicsEngineSimple(self, scene["Collision Layer"])

        self.is_attacking = False
        self.can_attack = True
        self.is_invincible = False
        self.is_dying = False

        self.invincible_time = 1
        self.invincible_timer = 0

        self.attack_time = 0.2
        self.attack_timer = 0

        self.attack_cooldown = 0.8
        self.attack_cooldown_timer = 0

        self.death_time = 0.4
        self.death_timer = 0

        self.current_facing_direction = "down"
        self.texture = self.boss_textures["idle"][self.current_facing_direction]

        self.walk_texture_index = 0
        self.animation_walk_time = 0.2
        self.animation_walk_timer = 0

        self.normal_time = 8
        self.rage_time = 2

        self.is_raged = False
        self.timer = 0

        self.set_custom_hitbox()

    def set_custom_hitbox(self):
        hitbox = [
            (-self.width / 6, -self.height / 6 - 40),
            (self.width / 6, -self.height / 6 - 40),
            (self.width / 6, self.height / 6 - 40),
            (-self.width / 6, self.height / 6 - 40)
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
            self.texture = self.boss_textures["walk"][self.current_facing_direction][self.walk_texture_index]
            self.animation_walk_timer = 0

    def follow_target(self, delta_time):
        diff_x = self.get_target().center_x - self.center_x
        diff_y = self.get_target().center_y - self.center_y
        distance = math.sqrt(diff_x ** 2 + diff_y ** 2)

        dir_x = diff_x / distance
        dir_y = diff_y / distance

        self.current_facing_direction = self.get_facing_direction(dir_x, dir_y)

        if distance > 60:
            self.dir_x = dir_x
            self.dir_y = dir_y

            self.animate_walk(delta_time)
        else:
            self.dir_x = self.dir_y = 0
            self.texture = self.boss_textures["idle"][self.current_facing_direction]

        self.change_x = self.dir_x * (self.speed * self.stats_multiplier) * delta_time
        self.change_y = self.dir_y * (self.speed * self.stats_multiplier) * delta_time

        return distance

    def attack(self, delta_time):
        if self.attack_timer == 0 and not self.get_target().is_dodging:
            self.get_target().take_damage(self.damage * self.stats_multiplier)

        self.attack_timer += delta_time
        if self.attack_timer <= self.attack_time / self.stats_multiplier:
            self.texture = self.boss_textures["attack"][self.current_facing_direction]
            self.change_x = 0
            self.change_y = 0
        else:
            self.is_attacking = False
            self.attack_timer = 0.0
            self.texture = self.boss_textures["idle"][self.current_facing_direction]

    def attack_cooldown_update(self, delta_time):
        if not self.can_attack:
            self.attack_cooldown_timer += delta_time
            if self.attack_cooldown_timer >= self.attack_cooldown / self.stats_multiplier:
                self.can_attack = True
                self.attack_cooldown_timer = 0.0

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
                self.get_target().grant_ability(self.ability_name)
                self.get_target().bosses_defeated += 1
                self.death_timer = 0
                self.is_dying = False

    def rage_state_update(self, delta_time):
        self.timer += delta_time

        if not self.is_raged:
            self.color = (255, 255, 255)
            if self.timer >= self.normal_time:
                self.is_raged = True
                self.stats_multiplier = 2
                self.timer = 0
        else:
            self.color = (255, 80, 80)
            if self.timer >= self.rage_time:
                self.is_raged = False
                self.stats_multiplier = 1
                self.timer = 0

    def on_update(self, delta_time):
        self.physics_engine.update()

        if self.is_dying:
            self.death_timer_update(delta_time)
        elif self.is_attacking:
            self.attack(delta_time)
        else:
            distance = self.follow_target(delta_time)

            if distance <= 60 and self.can_attack:
                self.is_attacking = True
                self.can_attack = False

        self.attack_cooldown_update(delta_time)
        self.invincible_timer_update(delta_time)
        self.rage_state_update(delta_time)