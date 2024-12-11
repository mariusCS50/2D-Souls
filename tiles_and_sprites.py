import arcade

class MapTransitions:
    def __init__(self):
        self.transitions = {
            "assets/maps/lobby.tmx": {
                "right": ("assets/maps/volcano_island.tmx", "left"),
                "left": ("assets/maps/snowy_plains.tmx", "right"),
                "up": ("assets/maps/crystal_cave.tmx", "down"),
            },
            "assets/maps/volcano_island.tmx": {
                "left": ("assets/maps/lobby.tmx", "right")
            },
            "assets/maps/snowy_plains.tmx": {
                "right": ("assets/maps/lobby.tmx", "left")
            },
            "assets/maps/crystal_cave.tmx": {
                "down": ("assets/maps/lobby.tmx", "up")
            }
        }

    def get_transitions(self):
        return self.transitions


class PlayerTextures:
    def __init__(self):
        self.idle_textures = {
            "up": arcade.load_texture("assets/player/stay_idle_up.png"),
            "down": arcade.load_texture("assets/player/stay_idle_down.png"),
            "left": arcade.load_texture("assets/player/stay_idle_left.png"),
            "right": arcade.load_texture("assets/player/stay_idle_right.png"),
        }

        self.walking_textures = {
            "up": [
                arcade.load_texture("assets/player/walk_up_1.png"),
                arcade.load_texture("assets/player/walk_up_2.png")
            ],
            "down": [
                arcade.load_texture("assets/player/walk_down_1.png"),
                arcade.load_texture("assets/player/walk_down_2.png")
            ],
            "left": [
                arcade.load_texture("assets/player/walk_left_1.png"),
                arcade.load_texture("assets/player/walk_left_2.png")
            ],
            "right": [
                arcade.load_texture("assets/player/walk_right_1.png"),
                arcade.load_texture("assets/player/walk_right_2.png")
            ],
        }

        self.attack_textures = {
            "up": arcade.load_texture("assets/player/attack_up.png"),
            "down": arcade.load_texture("assets/player/attack_down.png"),
            "left": arcade.load_texture("assets/player/attack_left.png"),
            "right": arcade.load_texture("assets/player/attack_right.png"),
        }

    def get_idle_textures(self):
        return self.idle_textures

    def get_walking_textures(self):
        return self.walking_textures

    def get_attack_textures(self):
        return self.attack_textures
