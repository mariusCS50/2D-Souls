import arcade

from sword_hitbox_generator import SwordHitboxGenerator

class MapResources:
    transitions = {
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
    
    @staticmethod
    def get_transitions():
        return MapResources.transitions


class PlayerResources:
    action_textures = {
        "idle" : {
            "up": arcade.load_texture("assets/player/idle_up.png"),
            "down": arcade.load_texture("assets/player/idle_down.png"),
            "left": arcade.load_texture("assets/player/idle_left.png"),
            "right": arcade.load_texture("assets/player/idle_right.png"),
        },
        "walk" : {
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
        },
        "attack" : {
            "up": arcade.load_texture("assets/player/attack_up.png"),
            "down": arcade.load_texture("assets/player/attack_down.png"),
            "left": arcade.load_texture("assets/player/attack_left.png"),
            "right": arcade.load_texture("assets/player/attack_right.png"),
        }
    }

    @staticmethod
    def get_textures():
        return PlayerResources.action_textures

class EnemyResources:
    walking_directions = [
        [0, 1],
        [0, -1],
        [-1, 0],
        [1, 0],
    ]

    textures = {
        "winter_orc": {
            "idle": {
                "up": arcade.load_texture("assets/enemies/orc/winter/idle_up.png"),
                "down": arcade.load_texture("assets/enemies/orc/winter/idle_down.png"),
                "left": arcade.load_texture("assets/enemies/orc/winter/idle_left.png"),
                "right": arcade.load_texture("assets/enemies/orc/winter/idle_right.png"),
            },
            "walk": {
                "up": [
                    arcade.load_texture("assets/enemies/orc/winter/walk_up_1.png"),
                    arcade.load_texture("assets/enemies/orc/winter/walk_up_2.png"),
                ],
                "down": [
                    arcade.load_texture("assets/enemies/orc/winter/walk_down_1.png"),
                    arcade.load_texture("assets/enemies/orc/winter/walk_down_2.png"),
                ],
                "left": [
                    arcade.load_texture("assets/enemies/orc/winter/walk_left_1.png"),
                    arcade.load_texture("assets/enemies/orc/winter/walk_left_2.png"),
                ],
                "right": [
                    arcade.load_texture("assets/enemies/orc/winter/walk_right_1.png"),
                    arcade.load_texture("assets/enemies/orc/winter/walk_right_2.png"),
                ],
            },
            "attack": {
                "up": arcade.load_texture("assets/enemies/orc/winter/attack_up.png"),
                "down": arcade.load_texture("assets/enemies/orc/winter/attack_down.png"),
                "left": arcade.load_texture("assets/enemies/orc/winter/attack_left.png"),
                "right": arcade.load_texture("assets/enemies/orc/winter/attack_right.png"),
            }
        },
    }

    @staticmethod
    def get_walking_directions():
        return EnemyResources.walking_directions
    
    @staticmethod
    def get_textures(enemy_type):
        return EnemyResources.textures[enemy_type]

class WeaponResources:
    weapons = {
        "sword": {
            "type": "melee",
            "damage": 5,
            "sprite": None,
            "hitbox_generator": SwordHitboxGenerator()
        },
        "wand": {
            "type": "ranged",
            "damage": 10,
            "sprite": None,
            "projectile_texture": arcade.load_texture("assets/projectile.png"),
            "projectile_speed": 128
        }
    }

    @staticmethod
    def get_weapons():
        return WeaponResources.weapons
