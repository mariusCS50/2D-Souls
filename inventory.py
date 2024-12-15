import arcade.gui
from game_resources import ItemResources

class Inventory(arcade.gui.UIWidget):
    def __init__(self, max_slots, cell_size, spacing, screen_width, screen_height):
        super().__init__()

        self.cell_size = cell_size
        self.spacing = spacing
        self.max_slots = max_slots

        inventory_width = max_slots * cell_size + (max_slots + 1) * spacing

        self.start_x = (screen_width - inventory_width) / 2
        self.start_y = 20

        self.background = arcade.gui.UISpace(
            self.start_x - spacing,
            self.start_y - spacing,
            inventory_width,
            cell_size + 2 * spacing,
            (70, 130, 180, 255)
        )
        self.add(self.background)

        self.index = 0

        self.slot_elements = []
        self.items = [None] * max_slots

        for i in range(max_slots):
            slot_x = self.start_x + i * (cell_size + spacing)
            slot_y = self.start_y
            slot = arcade.gui.UISpace(slot_x, slot_y, cell_size, cell_size, (0, 0, 0, 0))
            self.slot_elements.append(slot)
            self.add(slot)

        self.update_inventory()

    def update_inventory(self):
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

        for i, item_name in enumerate(self.items):
            if item_name:
                weapon_texture = ItemResources.get_weapons()[item_name]["texture"]
                slot_x = self.start_x + i * (self.cell_size + self.spacing) + self.cell_size // 2
                slot_y = self.start_y + self.cell_size // 2

                sprite = arcade.Sprite(center_x=slot_x, center_y=slot_y, texture=weapon_texture)
                sprite.scale = self.cell_size / weapon_texture.width

                sprite_widget = arcade.gui.UISpriteWidget(
                    x=slot_x - self.cell_size // 2,
                    y=slot_y - self.cell_size // 2,
                    width=self.cell_size,
                    height=self.cell_size,
                    sprite=sprite
                )
                self.add(sprite_widget)

    def add_item(self, item_name):
        for i in range(self.max_slots):
            if self.items[i] is None:
                self.items[i] = item_name
                self.update_inventory()
                return True
        return False

    def remove_item(self):
        if self.items[self.index] is not None:
            self.items[self.index] = None
            self.update_inventory()

    def select_next(self):
        self.index = (self.index + 1) % self.max_slots
        self.update_inventory()

    def select_previous(self):
        self.index = (self.index - 1) % self.max_slots
        self.update_inventory()