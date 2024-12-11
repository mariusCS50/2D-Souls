import arcade
from tiles_and_sprites import map_transitions
from player import Player

class Game(arcade.Window):
    def __init__(self, width=800, height=600, title="2D Souls"):
        super().__init__(width, height, title)

    def setup(self, map_name="assets/maps/lobby.tmx", spawn_edge="down"):
        self.current_map = map_name
        scaling = 1.0
        tile_map = arcade.load_tilemap(map_name, scaling)
        self.scene = arcade.Scene.from_tilemap(tile_map)

        self.map_width = tile_map.width * tile_map.tile_width * scaling
        self.map_height = tile_map.height * tile_map.tile_height * scaling

        if spawn_edge == "left":
            player_spawn_x = tile_map.tile_width * scaling
            player_spawn_y = self.map_height / 2
        elif spawn_edge == "right":
            player_spawn_x = self.map_width - tile_map.tile_width * scaling
            player_spawn_y = self.map_height / 2
        elif spawn_edge == "up":
            player_spawn_x = self.map_width / 2
            player_spawn_y = self.map_height - tile_map.tile_height * scaling
        elif spawn_edge == "down":
            player_spawn_x = self.map_width / 2
            player_spawn_y = tile_map.tile_height * scaling

        self.player = Player(player_spawn_x, player_spawn_y)
        self.scene.add_sprite("Player", self.player)
        self.camera = arcade.Camera(self.width, self.height)

        collision_layers = arcade.SpriteList()
        collision_layers.extend(self.scene["Collision Layer"])
        collision_layers.extend(self.scene["Collision Layer 2"])

        self.physics_engine = arcade.PhysicsEngineSimple(self.player, collision_layers)

    def check_map_transition(self):
        transition = None
        spawn_edge = None

        if self.player.center_x < 0:
            transition = map_transitions.get(self.current_map, {}).get("left")
        elif self.player.center_x > self.map_width:
            transition = map_transitions.get(self.current_map, {}).get("right")
        elif self.player.center_y < 0:
            transition = map_transitions.get(self.current_map, {}).get("down")
        elif self.player.center_y > self.map_height:
            transition = map_transitions.get(self.current_map, {}).get("up")

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
        self.player.on_update(delta_time)
        self.center_camera_to_player()

    def on_draw(self):
        self.clear()
        self.camera.use()

        self.scene["Collision Layer"].draw()
        self.scene["Ground Layer"].draw()
        self.scene["Ground Layer 2"].draw()
        self.scene["Ground Layer 3"].draw()
        self.scene["Collision Layer 2"].draw()
        self.player.draw()
        self.scene["Top Layer"].draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.D:
            self.player.move_right = True
        elif key == arcade.key.A:
            self.player.move_left = True
        elif key == arcade.key.W:
            self.player.move_up = True
        elif key == arcade.key.S:
            self.player.move_down = True
        elif key == arcade.key.SPACE:
            if self.player.is_moving():
                self.player.is_dodging = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.D:
            self.player.move_right = False
        elif key == arcade.key.A:
            self.player.move_left = False
        elif key == arcade.key.W:
            self.player.move_up = False
        elif key == arcade.key.S:
            self.player.move_down = False

if __name__ == "__main__":
    game = Game()
    game.setup()
    arcade.run()
