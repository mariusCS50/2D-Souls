import arcade

class Projectile(arcade.Sprite):
    def __init__(self, texture, pos_x, pos_y, dir_x, dir_y, speed, damage, scene, hit_layer_name):
        super().__init__()

        self.texture = texture

        self.center_x = pos_x
        self.center_y = pos_y

        self.dir_x = dir_x
        self.dir_y = dir_y

        self.speed = speed
        self.damage = damage

        self.ignore_collision_layer = True
        self.ignore_collision_layer_time = speed / 16

        self.scene = scene
        self.hit_layer_name = hit_layer_name

    def on_update(self, delta_time):
        self.change_x = self.dir_x * self.speed * delta_time
        self.change_y = self.dir_y * self.speed * delta_time

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.ignore_collision_layer_time <= 0:
            self.ignore_collision_layer_time = 0
            self.ignore_collision_layer = False

        if not self.ignore_collision_layer:
            if arcade.check_for_collision_with_list(self, self.scene["Collision Layer 2"]):
                self.scene["Projectiles"].remove(self)
                return
        
        hit_list = arcade.check_for_collision_with_list(self, self.scene[self.hit_layer_name])
        for hit in hit_list:
            hit.take_damage(self.damage)
            self.scene["Projectiles"].remove(self)
            return