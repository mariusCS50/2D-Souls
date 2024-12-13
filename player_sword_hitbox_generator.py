import arcade
from melee_hitbox_generator import MeleeHitboxGenerator

class PlayerSwordHitboxGenerator(MeleeHitboxGenerator):
    def __init__(self, owner):
        super().__init__(owner)

    def generate(self, facing_dir):
        sword_width = 25
        sword_height = 45

        if facing_dir == "up":
            sword_hitbox = arcade.SpriteSolidColor(sword_width, sword_height, arcade.color.BLUE)
            sword_hitbox.center_x = self.owner.center_x - 5
            sword_hitbox.center_y = self.owner.center_y + 20

        elif facing_dir == "down":
            sword_hitbox = arcade.SpriteSolidColor(sword_width, sword_height, arcade.color.BLUE)
            sword_hitbox.center_x = self.owner.center_x + 5
            sword_hitbox.center_y = self.owner.center_y - 40

        elif facing_dir == "left":
            sword_hitbox = arcade.SpriteSolidColor(sword_height, sword_width, arcade.color.BLUE)
            sword_hitbox.center_x = self.owner.center_x - 40
            sword_hitbox.center_y = self.owner.center_y - 2

        elif facing_dir == "right":
            sword_hitbox = arcade.SpriteSolidColor(sword_height, sword_width, arcade.color.BLUE)
            sword_hitbox.center_x = self.owner.center_x + 40
            sword_hitbox.center_y = self.owner.center_y - 2

        return sword_hitbox