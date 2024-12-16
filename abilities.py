import arcade.gui
from game_resources import AbilitiesResources

class Abilities(arcade.gui.UIWidget):
    def __init__(self, max_slots, cell_size, spacing, screen_width, screen_height):
        super().__init__()

        self.cell_size = cell_size
        self.spacing = spacing
        self.max_slots = max_slots

        ability_inventory_height = max_slots * cell_size + (max_slots + 1) * spacing

        self.start_x = screen_width - (cell_size + 2 * spacing)
        self.start_y = (screen_height - ability_inventory_height) // 2

        self.background = arcade.gui.UISpace(
            self.start_x - spacing,
            self.start_y - spacing,
            cell_size + 2 * spacing,
            ability_inventory_height,
            (70, 130, 180, 255)
        )
        self.add(self.background)

        self.index = 0

        self.slot_elements = []
        self.abilities = [None] * max_slots

        for i in range(max_slots):
            slot_x = self.start_x
            slot_y = self.start_y + i * (cell_size + spacing)
            slot = arcade.gui.UISpace(slot_x, slot_y, cell_size, cell_size, (0, 0, 0, 0))
            self.slot_elements.append(slot)
            self.add(slot)

        self.update_abilities()

    def update_abilities(self):
        for child in list(self.children):
            if isinstance(child, arcade.gui.UISpriteWidget):
                self.remove(child)

        for child in list(self.children):
            if isinstance(child, arcade.gui.UISpace) and child.color == (255, 0, 0, 255):
                self.remove(child)

        for i, slot in enumerate(self.slot_elements):
            if i == self.index:
                border_x = slot.x - self.spacing
                border_y = slot.y - self.spacing
                border_width = self.cell_size + 2 * self.spacing
                border_height = self.cell_size + 2 * self.spacing

                red_border = arcade.gui.UISpace(
                    x=border_x,
                    y=border_y,
                    width=border_width,
                    height=border_height,
                    color=(255, 0, 0, 255)
                )
                self.add(red_border)
                self.add(slot)

        for i, ability_name in enumerate(self.abilities):
            if ability_name:
                ability_texture = AbilitiesResources.get_abilities()[ability_name]["texture"]
                slot_x = self.start_x + self.cell_size // 2
                slot_y = self.start_y + i * (self.cell_size + self.spacing) + self.cell_size // 2

                sprite = arcade.Sprite(center_x=slot_x, center_y=slot_y, texture=ability_texture, scale=0.5)
                sprite.scale = self.cell_size / ability_texture.width

                sprite_widget = arcade.gui.UISpriteWidget(
                    x=slot_x - self.cell_size // 2,
                    y=slot_y - self.cell_size // 2,
                    width=self.cell_size,
                    height=self.cell_size,
                    sprite=sprite
                )
                self.add(sprite_widget)

    def learn_ability(self, ability_name):
        for i in range(self.max_slots):
            if self.abilities[i] is None:
                self.abilities[i] = ability_name
                self.update_abilities()
                return

    def select_ability(self, index):
        self.index = index
        self.update_abilities()