import arcade
import math
from enemy import Enemy

class MeleeEnemy(Enemy):
    def __init__(self, enemy_type, weapon_name, pos_x, pos_y, speed, vision_radius, scene, collision_layers):
        super().__init__(enemy_type, pos_x, pos_y, speed, vision_radius, scene, collision_layers)
        
        self.damage = self.weapons[weapon_name]["damage"]

    def attack(self, delta_time):
        if self.attack_timer == 0:
            self.target.take_damage(self.damage)

        self.attack_timer += delta_time
        if self.attack_timer <= self.attack_speed:
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
        diff_x = self.target.center_x - self.center_x
        diff_y = self.target.center_y - self.center_y
        distance = math.sqrt(diff_x ** 2 + diff_y ** 2)

        if distance > 50:
            self.dir_x = diff_x / distance
            self.dir_y = diff_y / distance

            new_x = self.center_x + self.dir_x * self.speed * delta_time
            new_y = self.center_y + self.dir_y * self.speed * delta_time

            self.center_x = new_x
            collides_x = arcade.check_for_collision(self, self.target)
            self.center_x = self.center_x - self.dir_x * self.speed * delta_time

            self.center_y = new_y
            collides_y = arcade.check_for_collision(self, self.target)
            self.center_y = self.center_y - self.dir_y * self.speed * delta_time

            if not collides_x:
                self.change_x = self.dir_x * self.speed * delta_time
            else:
                self.change_x = 0

            if not collides_y:
                self.change_y = self.dir_y * self.speed * delta_time
            else:
                self.change_y = 0

            self.current_facing_direction = self.get_facing_direction()
            self.animate_walk(delta_time)

        return distance

    def on_update(self, delta_time):
        self.physics_engine.update()

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
