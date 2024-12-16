import arcade
from game_resources import MapResources, ItemResources, EnemyResources

from drop_sprite import DropSprite
from island_status_ui import IslandStatusUI

from melee_enemy import MeleeEnemy
from ranger_enemy import RangerEnemy

from cave_boss import CaveBoss
from winter_boss import WinterBoss
from volcano_boss import VolcanoBoss

class IslandScene(arcade.Scene):
    def __init__(self, island_name, is_lobby):
        super().__init__()

        tile_map = arcade.load_tilemap(f"assets/maps/{island_name}.tmx")
        for name, sprite_list in tile_map.sprite_lists.items():
            self.add_sprite_list(name=name, sprite_list=sprite_list)

        self.map_width = tile_map.width * tile_map.tile_width
        self.map_height = tile_map.height * tile_map.tile_height

        self.collision_layers = arcade.SpriteList(use_spatial_hash=True)
        self.collision_layers.extend(self["Collision Layer"])
        self.collision_layers.extend(self["Collision Layer 2"])
        self.collision_layers.extend(self["Collision Layer 3"])

        self.add_sprite_list_after("Drops", "Collision Layer 3")
        self.add_sprite_list_after("Enemies", "Drops")
        self.add_sprite_list_after("Player", "Enemies")
        self.add_sprite_list_after("Projectiles", "Player")
        self.add_sprite_list_after("Boss", "Top Layer")
        self.add_sprite_list_after("Ability", "Boss")

        hidden_bow_info = MapResources.get_hidden_bows_info(island_name)
        if hidden_bow_info:
            pos_x = hidden_bow_info[0]
            pos_y = hidden_bow_info[1]
            name = hidden_bow_info[2]

            self["Drops"].append(DropSprite(name, ItemResources.get_weapons()[name]["texture"], pos_x, pos_y, self, True))

        self.island_name = island_name
        self.is_lobby = is_lobby
        self.spawned_boss = False
        self.boss_incoming_countdown = 3

        if self.is_lobby:
            self.island_status = None
            self["Drops"].append(DropSprite("cave_sword1", ItemResources.get_weapons()["cave_sword1"]["texture"], 500, 500, self, True))
            return

        # enemies_info = MapResources.get_enemies_info(island_name)
        # for enemy_info in enemies_info:
        #     pos_x = enemy_info[0]
        #     pos_y = enemy_info[1]
        #     enemy_type = enemy_info[2]

        #     enemy_stats = EnemyResources.get_enemy_stats(enemy_type)
        #     attack_type = enemy_stats[0]
        #     weapon_name = enemy_stats[1]
        #     speed = enemy_stats[2]
        #     health = enemy_stats[3]
        #     attack_time = enemy_stats[4]
        #     attack_cooldown = enemy_stats[5]
        #     vision_radius = enemy_stats[6]
        #     drops = enemy_stats[7]

        #     if attack_type == "melee":
        #         self["Enemies"].append(
        #             MeleeEnemy(
        #                 enemy_type,
        #                 weapon_name,
        #                 pos_x,
        #                 pos_y,
        #                 speed,
        #                 health,
        #                 attack_time,
        #                 attack_cooldown,
        #                 vision_radius,
        #                 drops,
        #                 self,
        #                 self.collision_layers
        #             )
        #         )
        #     elif attack_type == "ranger":
        #         self["Enemies"].append(
        #             RangerEnemy(
        #                 enemy_type,
        #                 weapon_name,
        #                 pos_x,
        #                 pos_y,
        #                 speed,
        #                 health,
        #                 attack_time,
        #                 attack_cooldown,
        #                 vision_radius,
        #                 drops,
        #                 self,
        #                 self.collision_layers
        #             )
        #         )

        self.island_status = IslandStatusUI(len(self["Enemies"]))

    def set_up_scene(self, scene):
        self.up = scene

    def set_down_scene(self, scene):
        self.down = scene

    def set_left_scene(self, scene):
        self.left = scene

    def set_right_scene(self, scene):
        self.right = scene

    def get_up_scene(self):
        return self.up

    def get_down_scene(self):
        return self.down

    def get_left_scene(self):
        return self.left

    def get_right_scene(self):
        return self.right

    def on_update(self, delta_time):
        super().on_update(delta_time)

        if not self.is_lobby:
            self.island_status.update(len(self["Enemies"]), delta_time)

        if not self.is_lobby and not self.spawned_boss and len(self["Enemies"]) == 0:
            self.boss_incoming_countdown -= delta_time
            if self.boss_incoming_countdown <= 0:
                if self.island_name == "crystal_cave":
                    self["Boss"].append(CaveBoss(640, 500, self))
                elif self.island_name == "snowy_plains":
                    self["Boss"].append(WinterBoss(624, 656, self))
                elif self.island_name == "volcano_island":
                    self["Boss"].append(VolcanoBoss(1424, 656, self))

                self.spawned_boss = True

    def get_collision_layers(self):
        return self.collision_layers

    def on_draw(self):
        self.draw()