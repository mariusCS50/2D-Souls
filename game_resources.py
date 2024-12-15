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

    enemies = {
        "volcano_island" : [
            (656, 848, "volcano_orc"),
            (560, 464, "volcano_orc"),
            (592, 1040, "volcano_slime"),
            (816, 1104, "volcano_slime"),
            (816, 336, "volcano_slime"),
            (720, 240, "volcano_orc"),
            (1104, 1200, "volcano_orc"),
            (1488, 1168, "volcano_slime"),
            (1040, 176, "volcano_slime"),
            (1392, 144, "volcano_orc"),
            (1840, 1200, "volcano_orc"),
            (2096, 1104, "volcano_slime"),
            (1712, 208, "volcano_orc"),
            (2160, 176, "volcano_orc"),
            (2256, 464, "volcano_slime"),
            (2128, 688, "volcano_orc"),
            (2352, 880, "volcano_slime"),
            (1552, 464, "volcano_slime"),
            (1712, 944, "volcano_slime"),
            (1008, 688, "volcano_org"),
            (2416, 272, "volcano_orc"),
            (1232, 880, "volcano_orc"),
            (1040, 496, "volcano_slime"),
            (1392, 688, "volcano_orc")
        ],
        "snowy_plains" : [
            (240, 976, "winter_slime"),
            (208, 368, "winter_orc"),
            (624, 1104, "winter_orc"),
            (592, 272, "winter_slime"),
            (976, 1072, "winter_slime"),
            (944, 368, "winter_orc"),
            (496, 592, "winter_orc"),
            (784, 784, "winter_orc"),
            (1232, 816, "winter_slime"),
            (1584, 496, "winter_orc"),
            (1584, 880, "winter_orc"),
            (1584, 1168, "winter_orc"),
            (1840, 720, "winter_slime"),
            (2032, 1040, "winter_orc"),
            (1936, 304, "winter_slime"),
            (2192, 368, "winter_orc"),
            (2224, 752, "winter_slime"),
            (1264, 528, "winter_slime")
        ],
        "crystal_cave": [
            (400, 720, "cave_org"),
            (880, 725, "cave_org"),
            (304, 1328, "cave_slime"),
            (944, 1296, "cave_org"),
            (656, 1456, "cave_org"),
            (336, 1968, "cave_slime"),
            (880, 2064, "cave_slime"),
            (592, 1904, "cave_org"),
            (656, 2256, "cave_org"),
            (336, 2480, "cave_org"),
            (624, 2448, "cave_slime"),
            (912, 2512, "cave_org")
        ]
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
        "cave_orc": {
            "idle": {
                "up": arcade.load_texture("assets/enemies/orc/cave/idle_up.png"),
                "down": arcade.load_texture("assets/enemies/orc/cave/idle_down.png"),
                "left": arcade.load_texture("assets/enemies/orc/cave/idle_left.png"),
                "right": arcade.load_texture("assets/enemies/orc/cave/idle_right.png"),
            },
            "walk": {
                "up": [
                    arcade.load_texture("assets/enemies/orc/cave/walk_up_1.png"),
                    arcade.load_texture("assets/enemies/orc/cave/walk_up_2.png"),
                ],
                "down": [
                    arcade.load_texture("assets/enemies/orc/cave/walk_down_1.png"),
                    arcade.load_texture("assets/enemies/orc/cave/walk_down_2.png"),
                ],
                "left": [
                    arcade.load_texture("assets/enemies/orc/cave/walk_left_1.png"),
                    arcade.load_texture("assets/enemies/orc/cave/walk_left_2.png"),
                ],
                "right": [
                    arcade.load_texture("assets/enemies/orc/cave/walk_right_1.png"),
                    arcade.load_texture("assets/enemies/orc/cave/walk_right_2.png"),
                ],
            },
            "attack": {
                "up": arcade.load_texture("assets/enemies/orc/cave/attack_up.png"),
                "down": arcade.load_texture("assets/enemies/orc/cave/attack_down.png"),
                "left": arcade.load_texture("assets/enemies/orc/cave/attack_left.png"),
                "right": arcade.load_texture("assets/enemies/orc/cave/attack_right.png"),
            },
            "death": {
                "up": arcade.load_texture("assets/enemies/orc/cave/death_up.png"),
                "down": arcade.load_texture("assets/enemies/orc/cave/death_down.png"),
                "left": arcade.load_texture("assets/enemies/orc/cave/death_left.png"),
                "right": arcade.load_texture("assets/enemies/orc/cave/death_right.png"),
            }
        },
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
            },
            "death": {
                "up": arcade.load_texture("assets/enemies/orc/winter/death_up.png"),
                "down": arcade.load_texture("assets/enemies/orc/winter/death_down.png"),
                "left": arcade.load_texture("assets/enemies/orc/winter/death_left.png"),
                "right": arcade.load_texture("assets/enemies/orc/winter/death_right.png"),
            }
        },
        "volcano_orc": {
            "idle": {
                "up": arcade.load_texture("assets/enemies/orc/volcano/idle_up.png"),
                "down": arcade.load_texture("assets/enemies/orc/volcano/idle_down.png"),
                "left": arcade.load_texture("assets/enemies/orc/volcano/idle_left.png"),
                "right": arcade.load_texture("assets/enemies/orc/volcano/idle_right.png"),
            },
            "walk": {
                "up": [
                    arcade.load_texture("assets/enemies/orc/volcano/walk_up_1.png"),
                    arcade.load_texture("assets/enemies/orc/volcano/walk_up_2.png"),
                ],
                "down": [
                    arcade.load_texture("assets/enemies/orc/volcano/walk_down_1.png"),
                    arcade.load_texture("assets/enemies/orc/volcano/walk_down_2.png"),
                ],
                "left": [
                    arcade.load_texture("assets/enemies/orc/volcano/walk_left_1.png"),
                    arcade.load_texture("assets/enemies/orc/volcano/walk_left_2.png"),
                ],
                "right": [
                    arcade.load_texture("assets/enemies/orc/volcano/walk_right_1.png"),
                    arcade.load_texture("assets/enemies/orc/volcano/walk_right_2.png"),
                ],
            },
            "attack": {
                "up": arcade.load_texture("assets/enemies/orc/volcano/attack_up.png"),
                "down": arcade.load_texture("assets/enemies/orc/volcano/attack_down.png"),
                "left": arcade.load_texture("assets/enemies/orc/volcano/attack_left.png"),
                "right": arcade.load_texture("assets/enemies/orc/volcano/attack_right.png"),
            },
            "death": {
                "up": arcade.load_texture("assets/enemies/orc/volcano/death_up.png"),
                "down": arcade.load_texture("assets/enemies/orc/volcano/death_down.png"),
                "left": arcade.load_texture("assets/enemies/orc/volcano/death_left.png"),
                "right": arcade.load_texture("assets/enemies/orc/volcano/death_right.png"),
            }
        },
        "cave_slime": {
            "idle": {
                "up": arcade.load_texture("assets/enemies/slime/cave/idle_up.png"),
                "down": arcade.load_texture("assets/enemies/slime/cave/idle_down.png"),
                "left": arcade.load_texture("assets/enemies/slime/cave/idle_left.png"),
                "right": arcade.load_texture("assets/enemies/slime/cave/idle_right.png"),
            },
            "walk": {
                "up": [
                    arcade.load_texture("assets/enemies/slime/cave/walk_up_1.png"),
                    arcade.load_texture("assets/enemies/slime/cave/walk_up_2.png"),
                ],
                "down": [
                    arcade.load_texture("assets/enemies/slime/cave/walk_down_1.png"),
                    arcade.load_texture("assets/enemies/slime/cave/walk_down_2.png"),
                ],
                "left": [
                    arcade.load_texture("assets/enemies/slime/cave/walk_left_1.png"),
                    arcade.load_texture("assets/enemies/slime/cave/walk_left_2.png"),
                ],
                "right": [
                    arcade.load_texture("assets/enemies/slime/cave/walk_right_1.png"),
                    arcade.load_texture("assets/enemies/slime/cave/walk_right_2.png"),
                ],
            },
            "attack": {
                "up": arcade.load_texture("assets/enemies/slime/cave/attack_up.png"),
                "down": arcade.load_texture("assets/enemies/slime/cave/attack_down.png"),
                "left": arcade.load_texture("assets/enemies/slime/cave/attack_left.png"),
                "right": arcade.load_texture("assets/enemies/slime/cave/attack_right.png"),
            }
        },
        "winter_slime": {
            "idle": {
                "up": arcade.load_texture("assets/enemies/slime/winter/idle_up.png"),
                "down": arcade.load_texture("assets/enemies/slime/winter/idle_down.png"),
                "left": arcade.load_texture("assets/enemies/slime/winter/idle_left.png"),
                "right": arcade.load_texture("assets/enemies/slime/winter/idle_right.png"),
            },
            "walk": {
                "up": [
                    arcade.load_texture("assets/enemies/slime/winter/walk_up_1.png"),
                    arcade.load_texture("assets/enemies/slime/winter/walk_up_2.png"),
                ],
                "down": [
                    arcade.load_texture("assets/enemies/slime/winter/walk_down_1.png"),
                    arcade.load_texture("assets/enemies/slime/winter/walk_down_2.png"),
                ],
                "left": [
                    arcade.load_texture("assets/enemies/slime/winter/walk_left_1.png"),
                    arcade.load_texture("assets/enemies/slime/winter/walk_left_2.png"),
                ],
                "right": [
                    arcade.load_texture("assets/enemies/slime/winter/walk_right_1.png"),
                    arcade.load_texture("assets/enemies/slime/winter/walk_right_2.png"),
                ],
            },
            "attack": {
                "up": arcade.load_texture("assets/enemies/slime/winter/attack_up.png"),
                "down": arcade.load_texture("assets/enemies/slime/winter/attack_down.png"),
                "left": arcade.load_texture("assets/enemies/slime/winter/attack_left.png"),
                "right": arcade.load_texture("assets/enemies/slime/winter/attack_right.png"),
            },
            "death": {
                "up": arcade.load_texture("assets/enemies/slime/winter/death_up.png"),
                "down": arcade.load_texture("assets/enemies/slime/winter/death_down.png"),
                "left": arcade.load_texture("assets/enemies/slime/winter/death_left.png"),
                "right": arcade.load_texture("assets/enemies/slime/winter/death_right.png"),
            }
        },
        "volcano_slime": {
            "idle": {
                "up": arcade.load_texture("assets/enemies/slime/volcano/idle_up.png"),
                "down": arcade.load_texture("assets/enemies/slime/volcano/idle_down.png"),
                "left": arcade.load_texture("assets/enemies/slime/volcano/idle_left.png"),
                "right": arcade.load_texture("assets/enemies/slime/volcano/idle_right.png"),
            },
            "walk": {
                "up": [
                    arcade.load_texture("assets/enemies/slime/volcano/walk_up_1.png"),
                    arcade.load_texture("assets/enemies/slime/volcano/walk_up_2.png"),
                ],
                "down": [
                    arcade.load_texture("assets/enemies/slime/volcano/walk_down_1.png"),
                    arcade.load_texture("assets/enemies/slime/volcano/walk_down_2.png"),
                ],
                "left": [
                    arcade.load_texture("assets/enemies/slime/volcano/walk_left_1.png"),
                    arcade.load_texture("assets/enemies/slime/volcano/walk_left_2.png"),
                ],
                "right": [
                    arcade.load_texture("assets/enemies/slime/volcano/walk_right_1.png"),
                    arcade.load_texture("assets/enemies/slime/volcano/walk_right_2.png"),
                ],
            },
            "attack": {
                "up": arcade.load_texture("assets/enemies/slime/volcano/attack_up.png"),
                "down": arcade.load_texture("assets/enemies/slime/volcano/attack_down.png"),
                "left": arcade.load_texture("assets/enemies/slime/volcano/attack_left.png"),
                "right": arcade.load_texture("assets/enemies/slime/volcano/attack_right.png"),
            },
            "death": {
                "up": arcade.load_texture("assets/enemies/slime/volcano/death_up.png"),
                "down": arcade.load_texture("assets/enemies/slime/volcano/death_down.png"),
                "left": arcade.load_texture("assets/enemies/slime/volcano/death_left.png"),
                "right": arcade.load_texture("assets/enemies/slime/volcano/death_right.png"),
            }
        }
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
        "water_wand": {
            "type": "ranged",
            "damage": 5,
            "sprite": None,
            "projectile_texture": arcade.load_texture("assets/weapons/ranged/water_projectile.png"),
            "projectile_speed": 175
        },
        "ice_wand": {
            "type": "ranged",
            "damage": 10,
            "sprite": None,
            "projectile_texture": arcade.load_texture("assets/weapons/ranged/ice_projectile.png"),
            "projectile_speed": 150
        },
        "fire_wand": {
            "type": "ranged",
            "damage": 20,
            "sprite": None,
            "projectile_texture": arcade.load_texture("assets/weapons/ranged/magma_projectile.png"),
            "projectile_speed": 128
        }
    }

    @staticmethod
    def get_weapons():
        return WeaponResources.weapons
