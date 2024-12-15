import arcade
from drop_sprite import DropSprite
from game_resources import MapResources, WeaponResources, EnemyResources
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

        self.is_lobby = is_lobby
        self.spawned_boss = False

        if self.is_lobby:
            self["Drops"].append(DropSprite("cave_sword1", WeaponResources.get_weapons()["cave_sword1"]["texture"], 500, 500, self, True))
            return
        
        enemies_info = MapResources.get_enemies_info(island_name)
        for enemy_info in enemies_info:
            pos_x = enemy_info[0]
            pos_y = enemy_info[1]
            enemy_type = enemy_info[2]

            enemy_stats = EnemyResources.get_enemy_stats(enemy_type)
            attack_type = enemy_stats[0]
            weapon_name = enemy_stats[1]
            speed = enemy_stats[2]
            health = enemy_stats[3]
            attack_time = enemy_stats[4]
            attack_cooldown = enemy_stats[5]
            vision_radius = enemy_stats[6]
            drops = enemy_stats[7]

            if attack_type == "melee":
                self["Enemies"].append(
                    MeleeEnemy(
                        enemy_type,
                        weapon_name,
                        pos_x,
                        pos_y,
                        speed,
                        health,
                        attack_time,
                        attack_cooldown,
                        vision_radius,
                        drops,
                        self,
                        self.collision_layers
                    )
                )
            elif attack_type == "ranger":
                self["Enemies"].append(
                    RangerEnemy(
                        enemy_type,
                        weapon_name,
                        pos_x,
                        pos_y,
                        speed,
                        health,
                        attack_time,
                        attack_cooldown,
                        vision_radius,
                        drops,
                        self,
                        self.collision_layers
                    )
                )
            

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