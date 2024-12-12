import arcade
from weapon import Weapon

class MeleeWeapon(Weapon):
    def __init__(self, damage):
        super().__init__(damage)

    def create_sword_hitbox(self, player):
        sword_width = 25
        sword_height = 45

        if player.current_facing_direction == "up":
            sword_hitbox = arcade.SpriteSolidColor(sword_width, sword_height, arcade.color.BLUE)
            sword_hitbox.center_x = player.center_x - 5
            sword_hitbox.center_y = player.center_y + 20

        elif player.current_facing_direction == "down":
            sword_hitbox = arcade.SpriteSolidColor(sword_width, sword_height, arcade.color.BLUE)
            sword_hitbox.center_x = player.center_x + 5
            sword_hitbox.center_y = player.center_y - 40

        elif player.current_facing_direction == "left":
            sword_hitbox = arcade.SpriteSolidColor(sword_height, sword_width, arcade.color.BLUE)
            sword_hitbox.center_x = player.center_x - 40
            sword_hitbox.center_y = player.center_y - 2

        elif player.current_facing_direction == "right":
            sword_hitbox = arcade.SpriteSolidColor(sword_height, sword_width, arcade.color.BLUE)
            sword_hitbox.center_x = player.center_x + 40
            sword_hitbox.center_y = player.center_y - 2

        return sword_hitbox

    # def update(self, owner, looking_dir_x, looking_dir_y, sprites_to_hit):
    #     collider = self.create_sword_hitbox(owner, looking_dir_x, looking_dir_y)

    #     hit_list = arcade.check_for_collision_with_list(collider, sprites_to_hit)
    #     for hit in hit_list:
    #         hit.damage()
