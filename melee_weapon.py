import arcade
from weapon import Weapon

class MeleeWeapon(Weapon):
    def __init__(self, owner, damage, melee_hitbox_generator):
        super().__init__(owner, damage)

        self.melee_hitbox_generator = melee_hitbox_generator
        self.hitbox = None

    def update(self, facing_dir, scene, hit_layer_name):
        if not self.hitbox:
            self.hitbox = self.melee_hitbox_generator.generate(self.owner, facing_dir)

        hit_list = arcade.check_for_collision_with_list(self.hitbox, scene[hit_layer_name])
        for hit in hit_list:
            # TODO: Damage the hits
            scene[hit_layer_name].remove(hit)
            pass

    def stop_update(self):
        self.hitbox = None
