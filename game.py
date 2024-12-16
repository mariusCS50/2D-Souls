import arcade
import arcade.key
import arcade.gui
from player import Player
from island_scene import IslandScene

class StartScreenView(arcade.View):
    def on_show_view(self):
        self.game_view = GameView()
        self.game_view.setup()

        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        self.background_texture = arcade.load_texture("assets/backgrounds/start_screen_background.png")

    def on_play_button_click(self, event):
        self.window.show_view(self.game_view)

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rectangle(
            self.window.width // 2,
            self.window.height // 2,
            self.window.width,
            self.window.height,
            self.background_texture
        )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.window.show_view(self.game_view)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.show_view(self.game_view)

class DeathScreenView(arcade.View):
    def on_show_view(self):
        self.game_view = GameView()
        self.game_view.setup()

        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        self.background_texture = arcade.load_texture("assets/backgrounds/death_screen_background.png")

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rectangle(
            self.window.width // 2,
            self.window.height // 2,
            self.window.width,
            self.window.height,
            self.background_texture
        )

        arcade.draw_text("Click or press Enter to respawn", self.window.width / 2, self.window.height / 2-150,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.window.show_view(self.game_view)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.show_view(self.game_view)

class WinScreenView(arcade.View):
    def on_show_view(self):
        self.game_view = GameView()
        self.game_view.setup()

        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        self.background_texture = arcade.load_texture("assets/backgrounds/win_screen_background.png")

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rectangle(
            self.window.width // 2,
            self.window.height // 2,
            self.window.width,
            self.window.height,
            self.background_texture
        )

        arcade.draw_text("Click or press Enter to respawn", self.window.width / 2, self.window.height / 2-150,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.window.show_view(self.game_view)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.show_view(self.game_view)

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.ui_manager = None
        self.player = None
        self.current_island_status = None
        self.no_bosses = 3

    def setup(self):
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()

        self.camera = arcade.Camera(self.window.width, self.window.height)

        self.current_scene = IslandScene("lobby", is_lobby=True)

        self.player = Player(640, 32, self.current_scene)
        self.current_scene["Player"].append(self.player)

        self.ui_manager.add(self.player.health_bar)
        self.ui_manager.add(self.player.inventory)
        self.ui_manager.add(self.player.ability_inventory)

        collision_layers = self.current_scene.get_collision_layers()
        self.player_physics_engine = arcade.PhysicsEngineSimple(self.player, collision_layers)

        snowy_plains = IslandScene("snowy_plains", is_lobby=False)
        snowy_plains.set_right_scene(self.current_scene)
        self.current_scene.set_left_scene(snowy_plains)

        snowy_plains["Player"].append(self.player)

        crystal_cave = IslandScene("crystal_cave", is_lobby=False)
        crystal_cave.set_down_scene(self.current_scene)
        self.current_scene.set_up_scene(crystal_cave)

        crystal_cave["Player"].append(self.player)

        volcano_island = IslandScene("volcano_island", is_lobby=False)
        volcano_island.set_left_scene(self.current_scene)
        self.current_scene.set_right_scene(volcano_island)

        volcano_island["Player"].append(self.player)

    def check_map_transition(self):
        new_scene = None

        if self.player.center_x < 0:
            new_scene = self.current_scene.get_left_scene()
            self.player.center_x = new_scene.map_width - 32

        elif self.player.center_x > self.current_scene.map_width:
            new_scene = self.current_scene.get_right_scene()
            self.player.center_x = 32

        elif self.player.center_y < 0:
            new_scene = self.current_scene.get_down_scene()
            self.player.center_y = new_scene.map_height - 32

        elif self.player.center_y > self.current_scene.map_height:
            new_scene = self.current_scene.get_up_scene()
            self.player.center_y = 32

        if new_scene:
            self.current_scene["Projectiles"].clear()

            self.player.scene = new_scene

            new_collision_layers = new_scene.get_collision_layers()
            self.player_physics_engine = arcade.PhysicsEngineSimple(self.player, new_collision_layers)

            self.current_scene = new_scene

            if self.current_island_status:
                self.ui_manager.remove(self.current_island_status)

            self.current_island_status = new_scene.island_status

            if self.current_island_status:
                self.ui_manager.add(self.current_island_status)

    def center_camera_to_player(self):
        target_x = self.player.center_x - self.window.width // 2
        target_y = self.player.center_y - self.window.height // 2

        target_x = max(0, min(target_x, self.current_scene.map_width - self.window.width))
        target_y = max(0, min(target_y, self.current_scene.map_height - self.window.height))

        self.camera.move_to((target_x, target_y), speed=0.2)

    def on_update(self, delta_time):
        self.check_map_transition()
        self.player_physics_engine.update()
        self.current_scene.on_update(delta_time)
        self.center_camera_to_player()
        self.check_player_dead()
        self.check_player_won()

    def check_player_dead(self):
        if self.player.health == 0:
            death_view = DeathScreenView()
            self.window.show_view(death_view)

    def check_player_won(self):
        if self.player.bosses_defeated == self.no_bosses:
            win_view = WinScreenView()
            self.window.show_view(win_view)


    def reset(self):
        self.player = None
        self.setup()

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.current_scene.on_draw()
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
        elif key == arcade.key.E:
            self.player.pick_up_item()
        elif key == arcade.key.R:
            self.player.drop_item()
        elif key == arcade.key.Q and self.player.can_use_ability:
            self.player.is_using_ability = True
        elif key == arcade.key.SPACE:
            if self.player.is_moving() and self.player.can_dodge and not self.player.is_attacking:
                self.player.is_dodging = True
                self.player.can_dodge = False
        elif key == arcade.key.KEY_1 or key == arcade.key.KEY_2 or key == arcade.key.KEY_3:
            ability_index = key - arcade.key.KEY_1
            self.player.ability_inventory.select_ability(ability_index)

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
            self.player.mouse_x = x + self.camera.position[0]
            self.player.mouse_y = y + self.camera.position[1]

            self.player.is_attacking = True
            self.player.can_attack = False

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        if scroll_y < 0:
            self.player.inventory.select_next()
        elif scroll_y > 0:
            self.player.inventory.select_previous()


if __name__ == "__main__":
    window = arcade.Window(800, 600, "2D Souls")
    start_view = StartScreenView()
    window.show_view(start_view)
    arcade.run()