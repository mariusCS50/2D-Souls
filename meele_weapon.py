import arcade
from weapon import Weapon

class MeeleWeapon(Weapon):
    def __init__(self, damage):
        super().__init__(damage)

    def generate_collider(self, owner, looking_dir_x, looking_dir_y):
        collider = arcade.Sprite()
        if looking_dir_x == 0:
            collider.width = owner.width
            collider.height = owner.height // 2

            if looking_dir_y == 1:
                collider.top = owner.center_y + owner.height // 2
            else:
                collider.bottom = owner.center_y - owner.height // 2

            collider.center_x = owner.center_x

        elif looking_dir_y == 0:
            collider.width = owner.width // 2
            collider.height = owner.height

            if looking_dir_x == 1:
                collider.right = owner.center_x + owner.width // 2
            else:
                collider.left = owner.center_x - owner.width // 2

            collider.center_y = owner.center_y
        
        return collider

    def update(self, owner, looking_dir_x, looking_dir_y, sprites_to_hit):
        collider = self.generate_collider(owner, looking_dir_x, looking_dir_y)

        hit_list = arcade.check_for_collision_with_list(collider, sprites_to_hit)
        for hit in hit_list:
            hit.damage()
