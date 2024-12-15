import arcade
from drop_sprite import DropSprite
from game_resources import MapResources
from game_resources import WeaponResources
from melee_enemy import MeleeEnemy
from ranger_enemy import RangerEnemy
from winter_boss import WinterBoss

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

        self.add_sprite_list_after("Player", "Collision Layer 3")
        self.add_sprite_list_after("Projectiles", "Collision Layer 3")
        self.add_sprite_list_after("Enemies", "Collision Layer 3")
        self.add_sprite_list_after("Boss", "Collision Layer 3")
        self.add_sprite_list_after("Drops", "Collision Layer 3")

        hidden_bow_info = MapResources.get_hidden_bows_info(island_name)
        if hidden_bow_info:
            pos_x = hidden_bow_info[0]
            pos_y = hidden_bow_info[1]
            name = hidden_bow_info[2]

            self["Drops"].append(DropSprite(name, WeaponResources.get_weapons()[name]["texture"], pos_x, pos_y, self, True))
   
        # TODO: Add enemies
        # self.enemies = arcade.SpriteList()

        # enemy = RangerEnemy(
        #     enemy_type="cave_slime",
        #     weapon_name="fire_wand",
        #     pos_x=self.map_width / 2,
        #     pos_y=300,
        #     speed=100,
        #     health=20,
        #     shoot_time=0.2,
        #     shoot_cooldown=1.5,
        #     vision_radius=300,
        #     scene=self,
        #     collision_layers=self.collision_layers
        # )

        # enemies.append(enemy)

        # self["Enemies"].extend(enemies)

#         self["Boss"].append(WinterBoss(self.map_width / 2, 500, self))
        
#         enemy = MeleeEnemy(
#             enemy_type="cave_orc",
#             weapon_name="sword",
#             pos_x=self.map_width / 2,
#             pos_y=300,
#             speed=100,
#             health=20,
#            	attack_time=0.2,
#             attack_cooldown=1.5,
#             vision_radius=300,
#             drops = {
#                 "sword": 0.5
#             },
#             scene=self,
#             collision_layers=self.collision_layers
#         )

#         self.enemies.append(enemy)

#         self["Enemies"].extend(self.enemies)

        self.is_lobby = is_lobby
        self.spawned_boss = False

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

        if not self.is_lobby and not self.spawned_boss and len(self["Enemies"]) == 0:
            # TODO: Spawn boss
            self.spawned_boss = True

    def get_collision_layers(self):
        return self.collision_layers

    def on_draw(self):
        self["Collision Layer"].draw()
        self["Collision Layer 2"].draw()
        self["Ground Layer"].draw()
        self["Ground Layer 2"].draw()
        self["Ground Layer 3"].draw()
        self["Collision Layer 3"].draw()
        self["Drops"].draw()

        draw_priority = arcade.SpriteList()
        draw_priority.extend(self["Player"])
        draw_priority.extend(self["Projectiles"])
        draw_priority.extend(self["Enemies"])
        draw_priority.extend(self["Boss"])

        sprite_priority = sorted(draw_priority, key=lambda sprite: sprite.center_y, reverse=True)
        for sprite in sprite_priority:
            sprite.draw()

        self["Top Layer"].draw()