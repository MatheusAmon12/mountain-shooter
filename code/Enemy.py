import pygame

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY_IN_MS, PLAYER_KEY_SHOOT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY_IN_MS[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1

        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY_IN_MS[self.name]

            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        return None