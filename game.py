import arcade
import arcade.key
import arcade.gui
from game_resources import MapResources
from player import Player
from ranger_enemy import RangerEnemy
from melee_enemy import MeleeEnemy


class Game(arcade.Window):
    def __init__(self, width=800, height=600, title="2D Souls"):
        super().__init__(width, height, title)

        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()

        self.map_transitions = MapResources().get_transitions()
        self.player = None

    def setup(self, map_name="assets/maps/lobby.tmx", spawn_edge="down"):
        self.current_map = map_name
        scaling = 1.0
        tile_map = arcade.load_tilemap(map_name, scaling)
        self.scene = arcade.Scene.from_tilemap(tile_map)

        self.map_width = tile_map.width * tile_map.tile_width * scaling
        self.map_height = tile_map.height * tile_map.tile_height * scaling

        if self.player is None:
            player_spawn_x = self.map_width / 2
            player_spawn_y = tile_map.tile_height * scaling
            self.player = Player(player_spawn_x, player_spawn_y, self.scene)
        else:
            self.player.scene = self.scene

            if spawn_edge == "left":
                self.player.center_x = tile_map.tile_width * scaling
            elif spawn_edge == "right":
                self.player.center_x = self.map_width - tile_map.tile_width * scaling
            elif spawn_edge == "up":
                self.player.center_y = self.map_height - tile_map.tile_height * scaling
            elif spawn_edge == "down":
                self.player.center_x = self.map_width / 2
                self.player.center_y = tile_map.tile_height * scaling

        self.scene.add_sprite_list_after("Player", "Collision Layer 2")
        self.scene["Player"].append(self.player)

        self.ui_manager.add(self.player.health_bar)

        self.collision_layers = arcade.SpriteList(use_spatial_hash=True)
        self.collision_layers.extend(self.scene["Collision Layer"])
        self.collision_layers.extend(self.scene["Collision Layer 2"])

        #self.enemies = self.generate_enemies(self.collision_layers)

        self.scene.add_sprite_list_after("Enemies", "Collision Layer 2")
        #self.scene["Enemies"].extend(self.enemies)

        self.scene.add_sprite_list_after("Projectiles", "Collision Layer 2")

        self.camera = arcade.Camera(self.width, self.height)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.collision_layers)

    def generate_enemies(self, collision_layers):
        enemies = arcade.SpriteList()

        enemy = RangerEnemy(
            enemy_type="winter_orc",
            pos_x=self.map_width / 2,
            pos_y=300,
            speed=100,
            scene=self.scene,
            vision_radius=200,
            collision_layers=collision_layers,
            ranger_weapon=RangerWeapon(10, "assets/projectile.png", 300)
        )
        enemies.append(enemy)


    def check_map_transition(self):
        transition = None
        spawn_edge = None

        if self.player.center_x < 0:
            transition = self.map_transitions.get(self.current_map, {}).get("left")
        elif self.player.center_x > self.map_width:
            transition = self.map_transitions.get(self.current_map, {}).get("right")
        elif self.player.center_y < 0:
            transition = self.map_transitions.get(self.current_map, {}).get("down")
        elif self.player.center_y > self.map_height:
            transition = self.map_transitions.get(self.current_map, {}).get("up")

        if transition:
            target_map, spawn_edge = transition
            self.setup(target_map, spawn_edge)

    def center_camera_to_player(self):
        target_x = self.player.center_x - self.width // 2
        target_y = self.player.center_y - self.height // 2

        target_x = max(0, min(target_x, self.map_width - self.width))
        target_y = max(0, min(target_y, self.map_height - self.height))

        self.camera.move_to((target_x, target_y), speed=0.2)

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.check_map_transition()
        self.scene.on_update(delta_time)
        self.center_camera_to_player()

        self.check_player_dead()

    def check_player_dead(self):
        if self.player.health == 0:
            self.reset()

    def reset(self):
        self.player = None
        self.setup()

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene["Collision Layer"].draw()
        self.scene["Ground Layer"].draw()
        self.scene["Ground Layer 2"].draw()
        self.scene["Ground Layer 3"].draw()
        self.scene["Collision Layer 2"].draw()

        draw_priority = arcade.SpriteList()
        draw_priority.extend(self.scene["Player"])
        draw_priority.extend(self.scene["Enemies"])
        sprite_priority = sorted(draw_priority, key=lambda sprite: sprite.center_y, reverse=True)

        for sprite in sprite_priority:
            sprite.draw()

        self.scene["Top Layer"].draw()

        # code to check the hitbox
        hitbox = self.player.get_hit_box()
        scaled_hitbox = [
            (self.player.center_x + point[0] * self.player.scale,
            self.player.center_y + point[1] * self.player.scale)
            for point in hitbox
        ]
        arcade.draw_polygon_outline(scaled_hitbox, arcade.color.RED, 2)

        # if self.player.is_attacking:
        #     sword_hitbox = self.player.weapon.melee_hitbox_generator.generate(self.player, self.player.current_facing_direction)
        #     sword_hitbox_vertices = sword_hitbox.get_hit_box()
        #     scaled_sword_hitbox = [
        #         (sword_hitbox.center_x + point[0],
        #         sword_hitbox.center_y + point[1])
        #         for point in sword_hitbox_vertices
        #     ]
        #     arcade.draw_polygon_outline(scaled_sword_hitbox, arcade.color.BLUE, 2)

        # for enemy in self.enemies:
        #         if arcade.has_line_of_sight(self.player.position,
        #                                     enemy.position,
        #                                     self.collision_layers,
        #                                     enemy.vision_radius):
        #             color = arcade.color.RED
        #         else:
        #             color = arcade.color.WHITE
        #         arcade.draw_line(self.player.center_x,
        #                          self.player.center_y,
        #                          enemy.center_x,
        #                          enemy.center_y,
        #                          color,
        #                          2)

        # for enemy in self.enemies:
        #     hitbox = enemy.get_hit_box()
        #     scaled_hitbox = [
        #         (enemy.center_x + point[0] * enemy.scale,
        #         enemy.center_y + point[1] * enemy.scale)
        #         for point in hitbox
        #     ]
        #     arcade.draw_polygon_outline(scaled_hitbox, arcade.color.PAKISTAN_GREEN, 2)

        self.ui_manager.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player.move_up = True
        elif key == arcade.key.A:
            self.player.move_left = True
        elif key == arcade.key.S:
            self.player.move_down = True
        elif key == arcade.key.D:
            self.player.move_right = True
        elif key == arcade.key.SPACE:
            if self.player.is_moving() and self.player.can_dodge and not self.player.is_attacking:
                self.player.is_dodging = True
                self.player.can_dodge = False
        elif key == arcade.key.K and self.player.can_attack:
            self.player.is_attacking = True
        elif key == arcade.key.G:
            self.player.health -= 10

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.player.move_up = False
        elif key == arcade.key.A:
            self.player.move_left = False
        elif key == arcade.key.S:
            self.player.move_down = False
        elif key == arcade.key.D:
            self.player.move_right = False

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and self.player.can_attack:
            self.player.is_attacking = True

if __name__ == "__main__":
    game = Game()
    game.setup()
    game.run()
