import random

import pygame
from pygame.font import FontType
from pygame.rect import RectType
from pygame.surface import SurfaceType

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: SurfaceType, name: str, game_mode: str):
        self.timeout: int = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(entity_name="Level1Bg"))
        self.entity_list.append(EntityFactory.get_entity(entity_name="Player1"))

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity(entity_name="Player2"))

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()

                if isinstance(entity, (Player, Enemy)):
                    shoot = entity.shoot()

                    if shoot is not None:
                        self.entity_list.append(shoot)

                if entity.name == "Player1":
                    self.level_text(14, f'Player1 - Health: {entity.health} | Score: {entity.score}', C_GREEN,
                                    (10, 25))

                if entity.name == "Player2":
                    self.level_text(14, f'Player2 - Health: {entity.health} | Score: {entity.score}', C_CYAN, (10, 45))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(entity_name=choice))

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple[int, int, int, int] = (255, 255, 255),
                   text_position: tuple[float, float] = (0, 0)):
        text_font: FontType = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: SurfaceType = text_font.render(text, True, text_color).convert_alpha()
        text_rect: RectType = text_surf.get_rect(left=text_position[0], top=text_position[1])

        self.window.blit(source=text_surf, dest=text_rect)
