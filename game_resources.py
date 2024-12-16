import arcade

from melee_hitbox_generator import SwordHitboxGenerator, SpearHitboxGenerator

class MapResources:
    enemies_info = {
        "volcano_island" : [
            {"x": 656, "y": 816, "enemy_type": "volcano_orc"},
            {"x": 560, "y": 432, "enemy_type": "volcano_orc"},
            {"x": 592, "y": 1008, "enemy_type": "volcano_orc"},
            {"x": 816, "y": 1072, "enemy_type": "volcano_slime"},
            {"x": 816, "y": 304, "enemy_type": "volcano_slime"},
            {"x": 1104, "y": 1168, "enemy_type": "volcano_orc"},
            {"x": 1488, "y": 1136, "enemy_type": "volcano_slime"},
            {"x": 1040, "y": 144, "enemy_type": "volcano_orc"},
            {"x": 1392, "y": 112, "enemy_type": "volcano_orc"},
            {"x": 1840, "y": 1168, "enemy_type": "volcano_orc"},
            {"x": 2096, "y": 1072, "enemy_type": "volcano_slime"},
            {"x": 1712, "y": 176, "enemy_type": "volcano_orc"},
            {"x": 2256, "y": 432, "enemy_type": "volcano_slime"},
            {"x": 2128, "y": 656, "enemy_type": "volcano_orc"},
            {"x": 1552, "y": 432, "enemy_type": "volcano_slime"},
            {"x": 1712, "y": 912, "enemy_type": "volcano_slime"},
            {"x": 1008, "y": 656, "enemy_type": "volcano_orc"},
            {"x": 2416, "y": 240, "enemy_type": "volcano_orc"},
            {"x": 1232, "y": 848, "enemy_type": "volcano_orc"},
            {"x": 1392, "y": 656, "enemy_type": "volcano_orc"}
        ],
        "snowy_plains" : [
            {"x": 240, "y": 944, "enemy_type": "winter_slime"},
            {"x": 208, "y": 336, "enemy_type": "winter_orc"},
            {"x": 624, "y": 1072, "enemy_type": "winter_orc"},
            {"x": 592, "y": 240, "enemy_type": "winter_slime"},
            {"x": 976, "y": 1040, "enemy_type": "winter_slime"},
            {"x": 944, "y": 336, "enemy_type": "winter_orc"},
            {"x": 496, "y": 560, "enemy_type": "winter_orc"},
            {"x": 784, "y": 752, "enemy_type": "winter_orc"},
            {"x": 1232, "y": 784, "enemy_type": "winter_slime"},
            {"x": 1584, "y": 464, "enemy_type": "winter_orc"},
            {"x": 1584, "y": 848, "enemy_type": "winter_orc"},
            {"x": 1584, "y": 1136, "enemy_type": "winter_orc"},
            {"x": 2032, "y": 1008, "enemy_type": "winter_orc"},
            {"x": 1936, "y": 272, "enemy_type": "winter_slime"},
            {"x": 2224, "y": 720, "enemy_type": "winter_slime"},
            {"x": 1264, "y": 496, "enemy_type": "winter_slime"}
        ],
        "crystal_cave": [
            {"x": 400, "y": 688, "enemy_type": "cave_orc"},
            {"x": 880, "y": 688, "enemy_type": "cave_orc"},
            {"x": 304, "y": 1296, "enemy_type": "cave_slime"},
            {"x": 944, "y": 1264, "enemy_type": "cave_orc"},
            {"x": 656, "y": 1424, "enemy_type": "cave_orc"},
            {"x": 336, "y": 1936, "enemy_type": "cave_slime"},
            {"x": 880, "y": 2032, "enemy_type": "cave_slime"},
            {"x": 592, "y": 1872, "enemy_type": "cave_orc"},
            {"x": 656, "y": 2224, "enemy_type": "cave_orc"},
            {"x": 336, "y": 2448, "enemy_type": "cave_orc"},
            {"x": 624, "y": 2416, "enemy_type": "cave_slime"},
            {"x": 912, "y": 2480, "enemy_type": "cave_orc"}
        ]
    }

    hidden_bows_info = {
        "lobby": {"x": 816, "y": 848, "weapon_name": "lobby_bow"},
        "volcano_island": {"x": 2320, "y": 208, "weapon_name": "volcano_bow"},
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
        "cave_bat": {
            "fly": {
                "up": [
                    arcade.load_texture("assets/enemies/bat/fly_up_1.png"),
                    arcade.load_texture("assets/enemies/bat/fly_up_2.png"),
                ],
                "down": [
                    arcade.load_texture("assets/enemies/bat/fly_down_1.png"),
                    arcade.load_texture("assets/enemies/bat/fly_down_2.png"),
                ],
                "left": [
                    arcade.load_texture("assets/enemies/bat/fly_left_1.png"),
                    arcade.load_texture("assets/enemies/bat/fly_left_2.png"),
                ],
                "right": [
                    arcade.load_texture("assets/enemies/bat/fly_right_1.png"),
                    arcade.load_texture("assets/enemies/bat/fly_right_2.png"),
                ],
            },
            "death": {
                "up": arcade.load_texture("assets/enemies/bat/death_up.png"),
                "down": arcade.load_texture("assets/enemies/bat/death_down.png"),
                "left": arcade.load_texture("assets/enemies/bat/death_left.png"),
                "right": arcade.load_texture("assets/enemies/bat/death_right.png"),
            }
        },
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

    enemies_stats = {
        "cave_orc": {
            "attack_type": "melee",
            "weapon_name": "cave_sword1",
            "speed": 96,
            "health": 10,
            "attack_time": 0.5,
            "attack_cooldown": 2,
            "vision_radius": 288,
            "drops": {
                "cave_sword1": 0.30,
                "cave_sword2": 0.25,
                "cave_spear": 0.15,
                None: 0.3
            }
        },
        "cave_slime": {
            "attack_type": "ranger",
            "weapon_name": "water_wand",
            "speed": 64,
            "health": 10,
            "attack_time": 0.5,
            "attack_cooldown": 2,
            "vision_radius": 288,
            "drops": {
                "health_potion": 0.6,
                "water_wand": 0.3,
                None: 0.1
            }
        },
        "winter_orc": {
            "attack_type": "melee",
            "weapon_name": "winter_sword1",
            "speed": 128,
            "health": 20,
            "attack_time": 0.4,
            "attack_cooldown": 1.5,
            "vision_radius": 320,
            "drops": {
                "winter_sword1": 0.25,
                "winter_sword2": 0.20,
                "winter_spear": 0.15,
                None: 0.4
            }
        },
        "winter_slime": {
            "attack_type": "ranger",
            "weapon_name": "ice_wand",
            "speed": 96,
            "health": 20,
            "attack_time": 0.4,
            "attack_cooldown": 1.5,
            "vision_radius": 320,
            "drops": {
                "health_potion": 0.65,
                "ice_wand": 0.25,
                None: 0.1
            }
        },
        "volcano_orc": {
            "attack_type": "melee",
            "weapon_name": "volcano_sword1",
            "speed": 144,
            "health": 30,
            "attack_time": 0.2,
            "attack_cooldown": 1,
            "vision_radius": 336,
            "drops": {
                "volcano_sword1": 0.23,
                "volcano_sword2": 0.15,
                "volcano_spear": 0.12,
                None: 0.5
            }
        },
        "volcano_slime": {
            "attack_type": "ranger",
            "weapon_name": "magma_wand",
            "speed": 112,
            "health": 35,
            "attack_time": 0.2,
            "attack_cooldown": 1,
            "vision_radius": 336,
            "drops": {
                "health_potion": 0.75,
                "magma_wand": 0.15,
                None: 0.1
            }
        },
    }

    @staticmethod
    def get_walking_directions():
        return EnemyResources.walking_directions

    @staticmethod
    def get_textures(enemy_type):
        return EnemyResources.textures[enemy_type]

    def get_enemy_stats(enemy_type):
        return EnemyResources.enemies_stats[enemy_type]

class ItemResources:
    sword_hitbox_generator = SwordHitboxGenerator()
    spear_hitbox_generator = SpearHitboxGenerator()

    items = {
        "health_potion": {
            "type": "potion",
            "texture": arcade.load_texture("assets/potions/health_potion.png"),
        },
        "cave_sword1": {
            "type": "melee",
            "damage": 4,
            "texture": arcade.load_texture("assets/weapons/melee/cave_sword1.png"),
            "hitbox_generator": sword_hitbox_generator
        },
        "cave_sword2": {
            "type": "melee",
            "damage": 8,
            "texture": arcade.load_texture("assets/weapons/melee/cave_sword2.png"),
            "hitbox_generator": sword_hitbox_generator
        },
        "cave_spear": {
            "type": "melee",
            "damage": 6,
            "texture": arcade.load_texture("assets/weapons/melee/cave_spear.png"),
            "hitbox_generator": spear_hitbox_generator
        },
        "water_wand": {
            "type": "ranged",
            "damage": 3,
            "texture": arcade.load_texture("assets/weapons/ranged/water_wand.png"),
            "projectile_texture": arcade.load_texture("assets/weapons/ranged/water_projectile.png"),
            "projectile_speed": 192
        },
        "winter_sword1": {
            "type": "melee",
            "damage": 8,
            "texture": arcade.load_texture("assets/weapons/melee/winter_sword1.png"),
            "hitbox_generator": sword_hitbox_generator
        },
        "winter_sword2": {
            "type": "melee",
            "damage": 12,
            "texture": arcade.load_texture("assets/weapons/melee/winter_sword2.png"),
            "hitbox_generator": sword_hitbox_generator
        },
        "winter_spear": {
            "type": "melee",
            "damage": 10,
            "texture": arcade.load_texture("assets/weapons/melee/winter_spear.png"),
            "hitbox_generator": spear_hitbox_generator
        },
        "ice_wand": {
            "type": "ranged",
            "damage": 6,
            "texture": arcade.load_texture("assets/weapons/ranged/ice_wand.png"),
            "projectile_texture": arcade.load_texture("assets/weapons/ranged/ice_projectile.png"),
            "projectile_speed": 224
        },
        "volcano_sword1": {
            "type": "melee",
            "damage": 12,
            "texture": arcade.load_texture("assets/weapons/melee/volcano_sword1.png"),
            "hitbox_generator": sword_hitbox_generator
        },
        "volcano_sword2": {
            "type": "melee",
            "damage": 16,
            "texture": arcade.load_texture("assets/weapons/melee/volcano_sword2.png"),
            "hitbox_generator": sword_hitbox_generator
        },
        "volcano_spear": {
            "type": "melee",
            "damage": 14,
            "texture": arcade.load_texture("assets/weapons/melee/volcano_spear.png"),
            "hitbox_generator": spear_hitbox_generator
        },
        "magma_wand": {
            "type": "ranged",
            "damage": 10,
            "texture": arcade.load_texture("assets/weapons/ranged/magma_wand.png"),
            "projectile_texture": arcade.load_texture("assets/weapons/ranged/magma_projectile.png"),
            "projectile_speed": 224
        },
        "lobby_bow": {
            "type": "ranged",
            "damage": 3,
            "texture": arcade.load_texture("assets/weapons/ranged/lobby_bow.png"),
            "projectile_texture": arcade.load_texture("assets/weapons/ranged/arrow.png"),
            "projectile_speed": 350
        },
        "volcano_bow": {
            "type": "ranged",
            "damage": 10,
            "texture": arcade.load_texture("assets/weapons/ranged/volcano_bow.png"),
            "projectile_texture": arcade.load_texture("assets/weapons/ranged/arrow.png"),
            "projectile_speed": 400
        },
    }

    @staticmethod
    def get_weapons():
        return ItemResources.items

class AbilitiesResources:
    abilities = {
        "cave_boss": {
            "name" : "shield_bubble",
            "texture" : arcade.load_texture("assets/abilities/cave_boss.png"),
            "sprite" : arcade.Sprite("assets/abilities/shield_bubble.png", scale=1.0),
            "ability_time" : 5,
            "cooldown" : 15
        },
        "winter_boss": {
            "name" : "multi_projectiles",
            "texture" : arcade.load_texture("assets/abilities/winter_boss.png"),
            "ability_time" : 4,
            "cooldown" : 15
        },
        "volcano_boss": {
            "name" : "berserk",
            "texture" : arcade.load_texture("assets/abilities/volcano_boss.png"),
            "ability_time" : 3,
            "cooldown" : 15
        },
    }

    @staticmethod
    def get_abilities():
        return AbilitiesResources.abilities