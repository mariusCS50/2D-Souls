import arcade
from abc import ABC, abstractmethod

class MeleeHitboxGenerator(ABC):
    @abstractmethod
    def generate(self, owner, facing_dir):
        pass