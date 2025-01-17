import arcade
import math
from game_resources import EnemyResources, AbilitiesResources

class CaveBoss(arcade.Sprite):
    def __init__(self, pos_x, pos_y, scene):
        super().__init__(scale=1)

        self.boss_textures = EnemyResources.get_textures("cave_bat")

        self.damage = 5

        self.center_x = pos_x
        self.center_y = pos_y

        self.speed = 144

        self.max_health = self._health = 50

        self.scene = scene
        self.physics_engine = arcade.PhysicsEngineSimple(self, scene["Collision Layer"])

        self.ability_name = "cave_boss"

        self.ability = AbilitiesResources.get_abilities()[self.ability_name]

        self.ability_sprite = self.ability["sprite"]
        self.ability_sprite.alpha = 128
        self.scene["Ability"].append(self.ability_sprite)

        self.is_attacking = False
        self.can_attack = True
        self.is_invincible = False
        self.is_dying = False

        self.invincible_time = 5
        self.invincible_timer = 0

        self.attack_time = 0.4
        self.attack_timer = 0

        self.attack_cooldown = 0.8
        self.attack_cooldown_timer = 0

        self.death_time = 0.4
        self.death_timer = 0

        self.current_facing_direction = "down"
        self.texture = self.boss_textures["fly"][self.current_facing_direction][0]

        self.fly_texture_index = 0
        self.animation_walk_time = 0.2
        self.animation_walk_timer = 0

        self.set_custom_hitbox()

    def set_custom_hitbox(self):
        hitbox = [
            (-self.width / 6, -self.height / 6),
            (self.width / 6, -self.height / 6),
            (self.width / 6, self.height / 6),
            (-self.width / 6, self.height / 6)
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
        self.scene["Ability"].remove(self.ability_sprite)
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

    def animate_fly(self, delta_time):
        self.animation_walk_timer += delta_time
        if self.animation_walk_timer > self.animation_walk_time:
            self.fly_texture_index = (self.fly_texture_index + 1) % 2
            self.texture = self.boss_textures["fly"][self.current_facing_direction][self.fly_texture_index]
            self.animation_walk_timer = 0

    def follow_target(self, delta_time):
        diff_x = self.get_target().center_x - self.center_x
        diff_y = self.get_target().center_y - self.center_y
        distance = math.sqrt(diff_x ** 2 + diff_y ** 2)

        self.dir_x = diff_x / distance
        self.dir_y = diff_y / distance

        self.change_x = self.dir_x * self.speed * delta_time
        self.change_y = self.dir_y * self.speed * delta_time

        self.current_facing_direction = self.get_facing_direction(self.dir_x, self.dir_y)
        self.animate_fly(delta_time)

    def attack(self, delta_time):
        if self.attack_timer == 0:
            self.get_target().take_damage(self.damage)

        self.attack_timer += delta_time
        if self.attack_timer <= self.attack_time:
            self.change_x = 0
            self.change_y = 0
        else:
            self.is_attacking = False
            self.attack_timer = 0.0

    def attack_cooldown_update(self, delta_time):
        if not self.can_attack:
            self.attack_cooldown_timer += delta_time
            if self.attack_cooldown_timer >= self.attack_cooldown:
                self.can_attack = True
                self.attack_cooldown_timer = 0.0

    def take_damage(self, damage):
        if not self.is_invincible:
            self.health -= damage
            self.is_invincible = True

    def invincible_timer_update(self, delta_time):
        if self.is_invincible:
            self.ability_sprite.visible = True
            self.ability_sprite.center_x = self.center_x
            self.ability_sprite.center_y = self.center_y + 10
            self.ability_sprite.alpha = 128

            if self.invincible_timer <= 1.0:
                self.alpha = (255 + 128) - self.alpha

            if self.invincible_timer > self.invincible_time:
                self.ability_sprite.visible = False
                self.is_invincible = False
                self.invincible_timer = 0
                self.alpha = 255

        self.invincible_timer += delta_time

    def death_timer_update(self, delta_time):
        if self.is_dying:
            self.death_timer += delta_time
            if self.death_timer >= self.death_time:
                self.scene["Boss"].remove(self)
                self.get_target().grant_ability(self.ability_name)
                self.get_target().bosses_defeated += 1
                self.death_timer = 0
                self.is_dying = False

    def on_update(self, delta_time):
        self.physics_engine.update()

        if self.is_dying:
            self.death_timer_update(delta_time)
        elif self.is_attacking:
            self.attack(delta_time)
        else:
            self.follow_target(delta_time)

            if self.can_attack and arcade.check_for_collision(self, self.get_target()):
                self.is_attacking = True
                self.can_attack = False

        self.attack_cooldown_update(delta_time)
        self.invincible_timer_update(delta_time)