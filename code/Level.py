import random

import pygame
from pygame.font import FontType
from pygame.rect import RectType
from pygame.surface import SurfaceType

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, TIMEOUT_LEVEL, \
    TIMEOUT_EVENT, TIMEOUT_STEP
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: SurfaceType, name: str, game_mode: str, player_score: list[int]):
        self.timeout: int = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.player_score = player_score
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(entity_name=self.name + "Bg"))

        player = EntityFactory.get_entity(entity_name="Player1")
        player.score = self.player_score[0]

        self.entity_list.append(player)

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player_2 = EntityFactory.get_entity(entity_name="Player2")
            player_2.score = self.player_score[1]

            self.entity_list.append(player_2)

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(TIMEOUT_EVENT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
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
                    self.level_text(
                            14, f'Player1 - Health: {entity.health} | Score: {entity.score}', C_GREEN,
                            (10, 25)
                    )

                if entity.name == "Player2":
                    self.level_text(14, f'Player2 - Health: {entity.health} | Score: {entity.score}', C_CYAN, (10, 45))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(entity_name=choice))

                if event.type == TIMEOUT_EVENT:
                    self.timeout -= TIMEOUT_STEP

                    if self.timeout == 0:
                        for entity in self.entity_list:
                            if isinstance(entity, Player) and entity.name == "Player1":
                                player_score[0] = entity.score

                            if isinstance(entity, Player) and entity.name == "Player2":
                                player_score[1] = entity.score

                        return True

                found_player = False
                for entity in self.entity_list:
                    if isinstance(entity, Player):
                        found_player = True

                if not found_player:
                    return False

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple[int, int, int, int] = (255, 255, 255),
                   text_position: tuple[float, float] = (0, 0)
                   ):
        text_font: FontType = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: SurfaceType = text_font.render(text, True, text_color).convert_alpha()
        text_rect: RectType = text_surf.get_rect(left=text_position[0], top=text_position[1])

        self.window.blit(source=text_surf, dest=text_rect)
