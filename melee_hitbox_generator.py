import arcade
from abc import ABC, abstractmethod

class MeleeHitboxGenerator(ABC):
    def __init__(self, owner):
        self.owner = owner

    @abstractmethod
    def generate_melee_hitbox(self, facing_dir):
        pass