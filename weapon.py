import arcade
from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, damage):
        self.damage = damage

    @abstractmethod
    def update(self, owner, facing_dir, scene, hit_layer_name):
        pass

    @abstractmethod
    def stop_update(self):
        pass