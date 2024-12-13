import arcade
from projectile import Projectile
from weapon import Weapon

class RangerWeapon(Weapon):
    def __init__(self, owner, damage, projectile_sprite, projectile_speed):
        super().__init__(owner, damage)

        self.projectile_sprite = projectile_sprite
        self.projectile_speed = projectile_speed

        self.shot_projectile = False

    def update(self, facing_dir, scene, hit_layer_name):
        if not self.shot_projectile:
            projectile_x_dir = 0
            projectile_y_dir = 0

            if facing_dir == "up":
                projectile_y_dir = 1
            elif facing_dir == "down":
                projectile_y_dir = -1
            elif facing_dir == "right":
                projectile_x_dir = 1
            elif facing_dir == "left":
                projectile_x_dir = -1

            projectile = Projectile(
                self.projectile_sprite,
                self.owner.center_x,
                self.owner.center_y,
                projectile_x_dir,
                projectile_y_dir,
                self.projectile_speed,
                scene,
                hit_layer_name
            )

            scene["Projectiles"].append(projectile)

            self.shot_projectile = True

    def stop_update(self):
        self.shot_projectile = False