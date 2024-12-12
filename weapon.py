import arcade
from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, damage):
        self.damage = damage

    @abstractmethod
    def update(self, owner, looking_dir_x, looking_dir_y):
        pass