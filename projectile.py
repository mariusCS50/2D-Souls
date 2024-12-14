import arcade

class Projectile(arcade.Sprite):
    def __init__(self, texture, pos_x, pos_y, dir_x, dir_y, speed, scene, hit_layer_name):
        super().__init__()

        self.texture = texture

        self.center_x = pos_x
        self.center_y = pos_y

        self.dir_x = dir_x
        self.dir_y = dir_y

        self.speed = speed

        self.scene = scene
        self.hit_layer_name = hit_layer_name

    def on_update(self, delta_time):
        self.change_x = self.dir_x * self.speed * delta_time
        self.change_y = self.dir_y * self.speed * delta_time

        self.center_x += self.change_x
        self.center_y += self.change_y

        if arcade.check_for_collision_with_list(self, self.scene["Collision Layer 2"]):
            self.scene["Projectiles"].remove(self)
            return
        
        hit_list = arcade.check_for_collision_with_list(self, self.scene[self.hit_layer_name])
        for hit in hit_list:
            # TODO: Damage the hits

            self.scene["Projectiles"].remove(self)
            return