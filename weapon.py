import arcade
from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, damage):
        self.damage = damage

    @abstractmethod
    def update(self, facing_dir, scene, hit_layer_name):
        pass

    @abstractmethod
    def stop_update():
        pass