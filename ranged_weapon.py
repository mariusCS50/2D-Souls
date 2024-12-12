import arcade
from weapon import Weapon

class RangedWeapon(Weapon):
    def __init__(self, damage, projectile):
        super().__init__(damage)

        self.projectile = projectile

    def update(self, owner, looking_dir_x, looking_dir_y):
        # TODO: Implement ranged weapon update
        pass