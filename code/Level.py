import pygame
from pygame.font import FontType
from pygame.rect import RectType
from pygame.surface import SurfaceType

from code.Const import MENU_TEXT_COLOR, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window: SurfaceType, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(entity_name="Level1Bg"))
        self.timeout: int = 20000

    def run(self):
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', MENU_TEXT_COLOR, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps() :.0f}', MENU_TEXT_COLOR, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', MENU_TEXT_COLOR, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple[int, int, int, int] = (255, 255, 255), text_position: tuple[float, float] = (0, 0)):
        text_font: FontType = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: SurfaceType = text_font.render(text, True, text_color).convert_alpha()
        text_rect: RectType = text_surf.get_rect(left=text_position[0], top=text_position[1])

        self.window.blit(source=text_surf, dest=text_rect)
