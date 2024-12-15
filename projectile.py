import arcade

class Projectile(arcade.Sprite):
    def __init__(self, texture, pos_x, pos_y, dir_x, dir_y, speed, damage, scene, hit_layer_names):
        super().__init__()

        self.texture = texture

        self.center_x = pos_x
        self.center_y = pos_y

        self.dir_x = dir_x
        self.dir_y = dir_y

        self.speed = speed
        self.damage = damage

        self.scene = scene
        self.hit_layer_names = hit_layer_names

        self.timer = 15

        self.set_custom_hitbox()

    def set_custom_hitbox(self):
        hitbox = [
            (-self.width / 8, -self.height / 8),
            (self.width / 8, -self.height / 8),
            (self.width / 8, self.height / 8),
            (-self.width / 8, self.height / 8)
        ]
        self.set_hit_box(hitbox)

    def on_update(self, delta_time):
        self.change_x = self.dir_x * self.speed * delta_time
        self.change_y = self.dir_y * self.speed * delta_time

        self.center_x += self.change_x
        self.center_y += self.change_y

        if arcade.check_for_collision_with_list(self, self.scene["Collision Layer 3"]):
            self.scene["Projectiles"].remove(self)
            return

        for hit_layer_name in self.hit_layer_names:
            hit_list = arcade.check_for_collision_with_list(self, self.scene[hit_layer_name])
            for hit in hit_list:
                hit.take_damage(self.damage)
                self.scene["Projectiles"].remove(self)
                return

        self.timer -= delta_time
        if self.timer <= 0:
            self.scene["Projectiles"].remove(self)
            return