import arcade
import math
from enemy import Enemy

class MeleeEnemy(Enemy):
    def __init__(self, enemy_type, weapon_name, pos_x, pos_y, speed, health, attack_time, attack_cooldown, vision_radius, drops, scene, collision_layers):
        super().__init__(enemy_type, pos_x, pos_y, speed, health, vision_radius, drops, scene, collision_layers)

        self.damage = self.weapons[weapon_name]["damage"]

        self.is_attacking = False
        self.can_attack = True

        self.attack_time = attack_time
        self.attack_timer = 0
        self.attack_cooldown = attack_cooldown
        self.attack_cooldown_timer = 0

    def set_custom_hitbox(self):
        hitbox = [
            (-self.width / 2, -self.height),
            (self.width / 2, -self.height),
            (self.width / 2, 0),
            (-self.width / 2, 0)
        ]
        self.set_hit_box(hitbox)

    def attack(self, delta_time):
        if self.attack_timer == 0 and not self.get_target().is_dodging:
            self.get_target().take_damage(self.damage)

        self.attack_timer += delta_time
        if self.attack_timer <= self.attack_time:
            self.texture = self.enemy_textures["attack"][self.current_facing_direction]
            self.change_x = 0
            self.change_y = 0
        else:
            self.is_attacking = False
            self.attack_timer = 0.0
            self.texture = self.enemy_textures["idle"][self.current_facing_direction]

    def attack_cooldown_update(self, delta_time):
        if not self.can_attack:
            self.attack_cooldown_timer += delta_time
            if self.attack_cooldown_timer >= self.attack_cooldown:
                self.can_attack = True
                self.attack_cooldown_timer = 0.0

    def follow_target(self, delta_time):
        diff_x = self.get_target().center_x - self.center_x
        diff_y = self.get_target().center_y - self.center_y
        distance = math.sqrt(diff_x ** 2 + diff_y ** 2)

        self.change_x = 0
        self.change_y = 0

        if distance > 40:
            self.dir_x = diff_x / distance
            self.dir_y = diff_y / distance

            self.change_x = self.dir_x * self.speed * delta_time
            self.change_y = self.dir_y * self.speed * delta_time

            self.current_facing_direction = self.get_facing_direction()
            self.animate_walk(delta_time)

        return distance

    def on_update(self, delta_time):
        self.physics_engine.update()

        if self.is_dying:
            self.death_timer_update(delta_time)
            return

        if self.is_attacking:
            self.attack(delta_time)

        elif self.has_line_of_sight():
            distance = self.follow_target(delta_time)

            if self.can_attack and distance <= 50:
                self.is_attacking = True
                self.can_attack = False

        else:
            self.wandering_logic(delta_time)

        self.attack_cooldown_update(delta_time)
        self.invincible_timer_update(delta_time)
