import arcade

from sword_hitbox_generator import SwordHitboxGenerator


class MapResources:    
    enemies_info = {
        "volcano_island" : [
            (656, 816, "volcano_orc"),
            (560, 432, "volcano_orc"),
            (592, 1008, "volcano_slime"),
            (816, 1072, "volcano_slime"),
            (816, 304, "volcano_slime"),
            (720, 208, "volcano_orc"),
            (1104, 1168, "volcano_orc"),
            (1488, 1136, "volcano_slime"),
            (1040, 144, "volcano_slime"),
            (1392, 112, "volcano_orc"),
            (1840, 1168, "volcano_orc"),
            (2096, 1072, "volcano_slime"),
            (1712, 176, "volcano_orc"),
            (2160, 144, "volcano_orc"),
            (2256, 432, "volcano_slime"),
            (2128, 656, "volcano_orc"),
            (2352, 848, "volcano_slime"),
            (1552, 432, "volcano_slime"),
            (1712, 912, "volcano_slime"),
            (1008, 656, "volcano_org"),
            (2416, 240, "volcano_orc"),
            (1232, 848, "volcano_orc"),
            (1040, 464, "volcano_slime"),
            (1392, 656, "volcano_orc")
        ],
        "snowy_plains" : [
            (240, 944, "winter_slime"),
            (208, 336, "winter_orc"),
            (624, 1072, "winter_orc"),
            (592, 240, "winter_slime"),
            (976, 1040, "winter_slime"),
            (944, 336, "winter_orc"),
            (496, 560, "winter_orc"),
            (784, 752, "winter_orc"),
            (1232, 784, "winter_slime"),
            (1584, 464, "winter_orc"),
            (1584, 848, "winter_orc"),
            (1584, 1136, "winter_orc"),
            (1840, 688, "winter_slime"),
            (2032, 1008, "winter_orc"),
            (1936, 272, "winter_slime"),
            (2192, 336, "winter_orc"),
            (2224, 720, "winter_slime"),
            (1264, 496, "winter_slime")
        ],
        "crystal_cave": [
            (400, 688, "cave_org"),
            (880, 688, "cave_org"),
            (304, 1296, "cave_slime"),
            (944, 1264, "cave_org"),
            (656, 1424, "cave_org"),
            (336, 1936, "cave_slime"),
            (880, 2032, "cave_slime"),
            (592, 1872, "cave_org"),
            (656, 2224, "cave_org"),
            (336, 2448, "cave_org"),
            (624, 2416, "cave_slime"),
            (912, 2480, "cave_org")
        ]
    }

    hidden_bows_info = {
        "lobby": (816, 848, "lobby_bow"),
        "volcano_island": (2320, 208, "volcano_bow"),
        "snowy_plains": None,
        "crystal_cave": None
    }

    @staticmethod
    def get_enemies_info(island_name):
        return MapResources.enemies_info[island_name]
    
    @staticmethod
    def get_hidden_bows_info(island_name):
        return MapResources.hidden_bows_info[island_name]


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
            "sword": {
                "up": arcade.load_texture("assets/player/attack_sword_up.png"),
                "down": arcade.load_texture("assets/player/attack_sword_down.png"),
                "left": arcade.load_texture("assets/player/attack_sword_left.png"),
                "right": arcade.load_texture("assets/player/attack_sword_right.png")
            },
            "spear": {
                "up": arcade.load_texture("assets/player/attack_spear_up.png"),
                "down": arcade.load_texture("assets/player/attack_spear_down.png"),
                "left": arcade.load_texture("assets/player/attack_spear_left.png"),
                "right": arcade.load_texture("assets/player/attack_spear_right.png")
            },
            "bow": {
                "up": arcade.load_texture("assets/player/attack_bow_up.png"),
                "down": arcade.load_texture("assets/player/attack_bow_down.png"),
                "left": arcade.load_texture("assets/player/attack_bow_left.png"),
                "right": arcade.load_texture("assets/player/attack_bow_right.png")
            },
            "wand": {
                "up": arcade.load_texture("assets/player/attack_wand_up.png"),
                "down": arcade.load_texture("assets/player/attack_wand_down.png"),
                "left": arcade.load_texture("assets/player/attack_wand_left.png"),
                "right": arcade.load_texture("assets/player/attack_wand_right.png")
            }
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
            },
            "death": {
                "up": arcade.load_texture("assets/enemies/slime/cave/death_up.png"),
                "down": arcade.load_texture("assets/enemies/slime/cave/death_down.png"),
                "left": arcade.load_texture("assets/enemies/slime/cave/death_left.png"),
                "right": arcade.load_texture("assets/enemies/slime/cave/death_right.png"),
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
    sword_hitbox_generator = SwordHitboxGenerator()
    # TODO: Spear hitbox generator

    weapons = {
        "cave_sword1": {
            "type": "melee",
            "damage": 5,
            "texture": arcade.load_texture("assets/weapons/melee/cave_sword1.png"),
            "hitbox_generator": sword_hitbox_generator
        },
        "water_wand": {
            "type": "ranged",
            "damage": 5,
            "texture": arcade.load_texture("assets/weapons/ranged/water_wand.png"),
            "projectile_texture": arcade.load_texture("assets/weapons/ranged/water_projectile.png"),
            "projectile_speed": 175
        },
        "ice_wand": {
            "type": "ranged",
            "damage": 10,
            "texture": arcade.load_texture("assets/weapons/ranged/ice_wand.png"),
            "projectile_texture": arcade.load_texture("assets/weapons/ranged/ice_projectile.png"),
            "projectile_speed": 150
        },
        "fire_wand": {
            "type": "ranged",
            "damage": 20,
            "texture": arcade.load_texture("assets/weapons/ranged/fire_wand.png"),
            "projectile_texture": arcade.load_texture("assets/weapons/ranged/magma_projectile.png"),
            "projectile_speed": 128
        },
        "lobby_bow": {
            "type": "ranged",
            "damage": 5,
            "texture": arcade.load_texture("assets/weapons/ranged/lobby_bow.png"),
            "projectile_texture": arcade.load_texture("assets/weapons/ranged/arrow.png"),
            "projectile_speed": 150
        },
        "volcano_bow": {
            "type": "ranged",
            "damage": 40,
            "texture": arcade.load_texture("assets/weapons/ranged/volcano_bow.png"),
            "projectile_texture": arcade.load_texture("assets/weapons/ranged/arrow.png"),
            "projectile_speed": 300
        },
        "volcano_sword1": {
            "type": "melee",
            "damage": 20,
            "texture": arcade.load_texture("assets/weapons/melee/volcano_sword1.png"),
            "hitbox_generator": sword_hitbox_generator
        }
    }

    @staticmethod
    def get_weapons():
        return WeaponResources.weapons
