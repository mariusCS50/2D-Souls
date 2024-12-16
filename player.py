import arcade
import math
from game_resources import PlayerResources, ItemResources, AbilitiesResources
from health_bar import HealthBar
from inventory import Inventory
from abilities import Abilities
from projectile import Projectile
from drop_sprite import DropSprite

class Player(arcade.Sprite):
    def __init__(self, pos_x, pos_y, scene):
        super().__init__(texture=arcade.load_texture("assets/player/walk_up_1.png"), scale=0.5)

        self.scene = scene

        self.center_x = pos_x
        self.center_y = pos_y

        self.speed = 200

        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

        self.dir_x = 0
        self.dir_y = 0

        self.max_health = 100

        self._health = 100
        self.health_bar = HealthBar(16, 16, 200, 16, 2, self._health, self.max_health)

        self.inventory = Inventory(8, 32, 6, 800, 600)
        self.ability_inventory = Abilities(3, 32, 6, 800, 600)

        self.current_ability = None
        self.stats_multiplier = 1.0

        self.direction_lock = False

        self.is_dodging = False
        self.is_attacking = False
        self.is_invincible = False
        self.is_using_ability = False

        self.can_dodge = True
        self.can_attack = True
        self.can_use_ability = True

        self.attack_time = 0.2
        self.attack_timer = 0
        self.attack_cooldown = 0.5
        self.attack_cooldown_timer = 0

        self.dodge_speed = 400
        self.dodge_time = 0.3
        self.dodge_timer = 0
        self.dodge_cooldown = 1.5
        self.dodge_cooldown_timer = 0

        self.ability_time = 0
        self.ability_timer = 0
        self.ability_cooldown_time = 0
        self.ability_cooldown_timer = 0

        self.action_textures = PlayerResources.get_textures()
        self.weapons = ItemResources.get_weapons()

        self.current_facing_direction = "up"
        self.last_facing_direction = ""

        self.walk_texture_index = 0
        self.animation_walk_time = 0.2
        self.animation_walk_timer = 0

        self.invincible_time = 1
        self.invincible_timer = 0

        self.weapon_name = None

        self.melee_hitbox = None
        self.shot_projectile = False

        self.mouse_x = 0
        self.mouse_y = 0

        self.set_custom_hitbox()

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, val):
        if val < 0:
            val = 0

        self._health = val
        self.health_bar.update_bar(self._health, self.max_health)

    def set_custom_hitbox(self):
        hitbox = [
            (-self.width / 1.5, -self.height),
            (self.width / 1.5, -self.height),
            (self.width / 1.5, 10),
            (-self.width / 1.5, 10)
        ]
        self.set_hit_box(hitbox)

    def is_moving(self):
        return self.dir_x != 0 or self.dir_y != 0

    def update_dir(self):
        dir_x = 0
        dir_y = 0

        if self.move_right:
            dir_x += 1
        if self.move_left:
            dir_x -= 1

        if self.move_up:
            dir_y += 1
        if self.move_down:
            dir_y -= 1

        # normalize directions
        if (abs(dir_x) == 1 and abs(dir_y) == 1):
            factor = 1 / math.sqrt(2)

            dir_x *= factor
            dir_y *= factor

        self.last_facing_direction = self.current_facing_direction

        if dir_y > 0:
            self.current_facing_direction = "up"
        elif dir_y < 0:
            self.current_facing_direction = "down"
        elif dir_x < 0:
            self.current_facing_direction = "left"
        elif dir_x > 0:
            self.current_facing_direction = "right"

        self.dir_x = dir_x
        self.dir_y = dir_y

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
        if self.is_moving():
            if self.animation_walk_timer > self.animation_walk_time:
                self.walk_texture_index = (self.walk_texture_index + 1) % 2
                self.texture = self.action_textures["walk"][self.current_facing_direction][self.walk_texture_index]
                self.animation_walk_timer = 0

            elif self.current_facing_direction != self.last_facing_direction:
                self.walk_texture_index = 0
                self.texture = self.action_textures["walk"][self.current_facing_direction][0]
                self.animation_walk_timer = 0

            self.animation_walk_timer += delta_time
        else:
            self.texture = self.action_textures["idle"][self.current_facing_direction]
            self.animation_walk_timer = 0

    def walk(self, delta_time):
        self.update_dir()
        self.animate_walk(delta_time)

        self.change_x = self.dir_x * (self.speed * self.stats_multiplier) * delta_time
        self.change_y = self.dir_y * (self.speed * self.stats_multiplier) * delta_time

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

    def attack(self, delta_time):
        if not self.weapon_name:
            self.is_attacking = False
            return

        if self.attack_timer <= self.attack_time / self.stats_multiplier:
            self.change_x = self.dir_x = 0
            self.change_y = self.dir_y = 0

            attack_x_dir = self.mouse_x - self.center_x
            attack_y_dir = self.mouse_y - self.center_y
            distance = math.sqrt(attack_x_dir ** 2 + attack_y_dir ** 2)

            if distance == 0:
                attack_x_dir = 0
                attack_y_dir = 1

            attack_x_dir /= distance
            attack_y_dir /= distance

            attack_facing_direction = self.get_facing_direction(attack_x_dir, attack_y_dir)

            if self.weapons[self.weapon_name]["type"] == "melee":
                if not self.melee_hitbox:
                    if "sword" in self.weapon_name:
                        self.texture = self.action_textures["attack"]["sword"][attack_facing_direction]
                    elif "spear" in self.weapon_name:
                        self.texture = self.action_textures["attack"]["spear"][attack_facing_direction]

                    hitbox_generator = self.weapons[self.weapon_name]["hitbox_generator"]
                    self.melee_hitbox = hitbox_generator.generate(self, attack_facing_direction)

                hit_list = arcade.check_for_collision_with_list(self.melee_hitbox, self.scene["Enemies"])
                for hit in hit_list:
                    hit.take_damage(self.weapons[self.weapon_name]["damage"] * self.stats_multiplier)

                hit_list = arcade.check_for_collision_with_list(self.melee_hitbox, self.scene["Boss"])
                for hit in hit_list:
                    hit.take_damage(self.weapons[self.weapon_name]["damage"] * self.stats_multiplier)

            elif self.weapons[self.weapon_name]["type"] == "ranged":
                if not self.shot_projectile:
                    if "bow" in self.weapon_name:
                        self.texture = self.action_textures["attack"]["bow"][attack_facing_direction]
                    elif "wand" in self.weapon_name:
                        self.texture = self.action_textures["attack"]["wand"][attack_facing_direction]

                    center_projectile = Projectile(
                        self.weapons[self.weapon_name]["projectile_texture"],
                        self.center_x,
                        self.center_y,
                        attack_x_dir,
                        attack_y_dir,
                        self.weapons[self.weapon_name]["projectile_speed"],
                        self.weapons[self.weapon_name]["damage"] * self.stats_multiplier,
                        self.scene,
                        ["Enemies", "Boss"]
                    )

                    self.scene["Projectiles"].append(center_projectile)

                    if self.ability_timer > 0 and "wand" in self.weapon_name and self.current_ability["name"] == "multi_projectiles":
                        angle_offset = math.radians(15)
                        cos_angle = math.cos(angle_offset)
                        sin_angle = math.sin(angle_offset)

                        left_x_dir = attack_x_dir * cos_angle - attack_y_dir * sin_angle
                        left_y_dir = attack_x_dir * sin_angle + attack_y_dir * cos_angle
                        left_projectile = Projectile(
                            self.weapons[self.weapon_name]["projectile_texture"],
                            self.center_x,
                            self.center_y,
                            left_x_dir,
                            left_y_dir,
                            self.weapons[self.weapon_name]["projectile_speed"],
                            self.weapons[self.weapon_name]["damage"] * self.stats_multiplier,
                            self.scene,
                            ["Enemies", "Boss"]
                        )
                        self.scene["Projectiles"].append(left_projectile)

                        right_x_dir = attack_x_dir * cos_angle + attack_y_dir * sin_angle
                        right_y_dir = -attack_x_dir * sin_angle + attack_y_dir * cos_angle
                        right_projectile = Projectile(
                            self.weapons[self.weapon_name]["projectile_texture"],
                            self.center_x,
                            self.center_y,
                            right_x_dir,
                            right_y_dir,
                            self.weapons[self.weapon_name]["projectile_speed"],
                            self.weapons[self.weapon_name]["damage"] * self.stats_multiplier,
                            self.scene,
                            ["Enemies", "Boss"]
                        )
                        self.scene["Projectiles"].append(right_projectile)

                    self.shot_projectile = True

        else:
            self.melee_hitbox = None
            self.shot_projectile = False

            self.is_attacking = False
            self.attack_timer = 0.0
            self.texture = self.action_textures["idle"][self.current_facing_direction]

        self.attack_timer += delta_time

    def attack_cooldown_update(self, delta_time):
        if not self.can_attack:
            self.attack_cooldown_timer += delta_time
            if self.attack_cooldown_timer > self.attack_cooldown / self.stats_multiplier:
                self.can_attack = True
                self.attack_cooldown_timer = 0

    def take_damage(self, damage):
        if not self.is_invincible:
            self.health -= damage
            self.is_invincible = True

    def invincible_timer_update(self, delta_time):
        if self.is_invincible:
            if self.current_ability:
                if self.current_ability["name"] != "shield_bubble":
                    self.alpha = (255 + 128) - self.alpha
            self.invincible_timer += delta_time

            if self.invincible_timer > self.invincible_time:
                self.is_invincible = False
                self.invincible_timer = 0
                self.alpha = 255

    def update_item(self):
        item_name = self.inventory.items[self.inventory.index]
        if item_name:
            self.weapon_name = item_name
        else:
            self.weapon_name = None

    def pick_up_item(self):
        drops = arcade.check_for_collision_with_list(self, self.scene["Drops"])
        for drop in drops:
            if drop.name == "health_potion":
                self.health = 100 if self.health >= 90 else self.health + 10
                self.scene["Drops"].remove(drop)
                return

            if self.inventory.add_item(drop.name):
                self.scene["Drops"].remove(drop)

    def drop_item(self):
        item_name = self.inventory.items[self.inventory.index]
        if item_name:
            if self.inventory.remove_item():
                weapon_texture = ItemResources.get_weapons()[item_name]["texture"]
                drop = DropSprite(
                    name=item_name,
                    texture=weapon_texture,
                    pos_x=self.center_x,
                    pos_y=self.center_y,
                    scene=self.scene,
                    is_permanent=False
                )

                self.scene["Drops"].append(drop)


    def grant_ability(self, ability_name):
        self.ability_inventory.learn_ability(ability_name)

    def use_ability(self, delta_time):
        if self.ability_timer == 0:
            ability_name = self.ability_inventory.abilities[self.ability_inventory.index]
            if ability_name:
                self.current_ability = AbilitiesResources.get_abilities()[ability_name]
                self.can_use_ability = False

            if not self.current_ability:
                self.is_using_ability = False
                return

        if self.current_ability["name"] == "shield_bubble":
            self.is_invincible = True
            self.ability_sprite = self.current_ability["sprite"]
            self.ability_sprite.alpha = 128
            self.ability_sprite.center_x = self.center_x
            self.ability_sprite.center_y = self.center_y
            if not self.ability_sprite in self.scene["Ability"]:
                self.scene["Ability"].append(self.ability_sprite)

        if self.current_ability["name"] == "berserk":
            self.stats_multiplier = 1.5
            self.color = (255, 80, 80)

        self.ability_timer += delta_time
        if self.ability_timer > self.current_ability["ability_time"]:
            self.is_using_ability = False
            self.ability_timer = 0
            if self.current_ability["name"] == "shield_bubble":
                self.is_invincible = False
                self.scene["Ability"].remove(self.ability_sprite)

            if self.current_ability["name"] == "berserk":
                self.stats_multiplier = 1.0
                self.color = (255, 255, 255)

    def ability_cooldown_update(self, delta_time):
        if not self.can_use_ability:
            self.ability_cooldown_timer += delta_time
            if self.ability_cooldown_timer > self.current_ability["cooldown"]:
                self.current_ability = None
                self.can_use_ability  = True
                self.ability_cooldown_timer = 0

    def on_update(self, delta_time):
        self.update_item()
        if self.is_using_ability:
            self.use_ability(delta_time)

        if self.is_dodging:
            self.dodge(delta_time)
        elif self.is_attacking:
            self.attack(delta_time)
        else:
            self.walk(delta_time)

        self.ability_cooldown_update(delta_time)
        self.dodge_cooldown_update(delta_time)
        self.attack_cooldown_update(delta_time)
        self.invincible_timer_update(delta_time)