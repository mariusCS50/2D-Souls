import arcade.gui


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
            (50, 50, 50, 200)
        )
        self.add(self.background)

        self.index = 0

        self.slots = [None] * max_slots
        self.slot_elements = []

        for i in range(max_slots):
            slot_x = self.start_x + i * (cell_size + spacing)
            slot_y = self.start_y
            slot = arcade.gui.UISpace(slot_x, slot_y, cell_size, cell_size, (200, 200, 200, 100))
            self.slot_elements.append(slot)
            self.add(slot)

        self.update_inventory()

    def update_inventory(self):
        for i, slot in enumerate(self.slot_elements):
            if i == self.index:
                slot.color = (200, 200, 200, 255)
            else:
                slot.color = (200, 200, 200, 100)

    def add_item(self, weapon_name):
        for i in range(self.max_slots):
            if self.slots[i] is None:
                self.slots[i] = weapon_name
                return True
        return False

    def remove_item(self, index):
        if self.slots[index] is not None:
            self.slots[index] = None

    def select_next(self):
        self.index = (self.index + 1) % self.max_slots
        self.update_inventory()

    def select_previous(self):
        self.index = (self.index - 1) % self.max_slots
        self.update_inventory()