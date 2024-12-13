import arcade
from weapon import Weapon

class MeleeWeapon(Weapon):
    def __init__(self, damage, melee_hitbox_generator):
        super().__init__(damage)
        self.melee_hitbox_generator = melee_hitbox_generator
        self.hitbox = None

    def update(self, facing_dir, scene, hit_layer_name):
        if not self.hitbox:
            self.hitbox = self.melee_hitbox_generator.generate(facing_dir)

        hit_list = arcade.check_for_collision_with_list(self.hitbox, scene[hit_layer_name])
        for hit in hit_list:
            pass

    def stop_update(self):
        self.hitbox = None
