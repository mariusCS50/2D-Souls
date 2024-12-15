import arcade

class SwordHitboxGenerator():
    def __init__(self):
        pass

    def generate(self, owner, facing_dir):
        sword_width = 25
        sword_height = 50

        if facing_dir == "up":
            sword_hitbox = arcade.SpriteSolidColor(sword_width, sword_height, arcade.color.BLUE)
            sword_hitbox.center_x = owner.center_x - 5
            sword_hitbox.center_y = owner.center_y + 20

        elif facing_dir == "down":
            sword_hitbox = arcade.SpriteSolidColor(sword_width, sword_height, arcade.color.BLUE)
            sword_hitbox.center_x = owner.center_x + 5
            sword_hitbox.center_y = owner.center_y - 40

        elif facing_dir == "left":
            sword_hitbox = arcade.SpriteSolidColor(sword_height, sword_width, arcade.color.BLUE)
            sword_hitbox.center_x = owner.center_x - 40
            sword_hitbox.center_y = owner.center_y - 2

        elif facing_dir == "right":
            sword_hitbox = arcade.SpriteSolidColor(sword_height, sword_width, arcade.color.BLUE)
            sword_hitbox.center_x = owner.center_x + 40
            sword_hitbox.center_y = owner.center_y - 2

        return sword_hitbox

import arcade

class SpearHitboxGenerator():
    def __init__(self):
        pass

    def generate(self, owner, facing_dir):
        spear_width = 25
        spear_height = 75

        if facing_dir == "up":
            spear_hitbox = arcade.SpriteSolidColor(spear_width, spear_height, arcade.color.BLUE)
            spear_hitbox.center_x = owner.center_x - 5
            spear_hitbox.center_y = owner.center_y + 40

        elif facing_dir == "down":
            spear_hitbox = arcade.SpriteSolidColor(spear_width, spear_height, arcade.color.BLUE)
            spear_hitbox.center_x = owner.center_x + 5
            spear_hitbox.center_y = owner.center_y - 60

        elif facing_dir == "left":
            spear_hitbox = arcade.SpriteSolidColor(spear_height, spear_width, arcade.color.BLUE)
            spear_hitbox.center_x = owner.center_x - 45
            spear_hitbox.center_y = owner.center_y - 2

        elif facing_dir == "right":
            spear_hitbox = arcade.SpriteSolidColor(spear_height, spear_width, arcade.color.BLUE)
            spear_hitbox.center_x = owner.center_x + 45
            spear_hitbox.center_y = owner.center_y - 2

        return spear_hitbox