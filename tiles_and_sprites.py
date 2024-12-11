import arcade

map_transitions = {
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

player_walking_textures = {
	"up": [arcade.load_texture("assets/player/walk_up_1.png"),
		arcade.load_texture("assets/player/walk_up_2.png")],
	"down": [arcade.load_texture("assets/player/walk_down_1.png"),
			arcade.load_texture("assets/player/walk_down_2.png")],
	"left": [arcade.load_texture("assets/player/walk_left_1.png"),
			arcade.load_texture("assets/player/walk_left_2.png")],
	"right": [arcade.load_texture("assets/player/walk_right_1.png"),
			arcade.load_texture("assets/player/walk_right_2.png")],
}