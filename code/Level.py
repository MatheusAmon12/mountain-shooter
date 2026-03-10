import pygame
from pygame.surface import SurfaceType

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window: SurfaceType, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(entity_name="Level1Bg"))

    def run(self):
        while True:
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()

            pygame.display.flip()
