import pygame.image
from pygame.font import FontType
from pygame.rect import RectType
from pygame.surface import SurfaceType

from code.Const import WIN_WIDTH, MENU_TITLE_COLOR, MENU_OPTION, MENU_TEXT_COLOR


class Menu:
    def __init__(self, window: SurfaceType):
        self.window = window
        self.surf = pygame.image.load("./assets/MenuBg.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load("./assets/Menu.mp3")
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", MENU_TITLE_COLOR, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", MENU_TITLE_COLOR, ((WIN_WIDTH / 2), 120))

            for menu_option in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[menu_option], MENU_TEXT_COLOR, ((WIN_WIDTH / 2), 180 + 25 * menu_option) )

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pass

    def menu_text(self, text_size: int, text: str, text_color: tuple[int, int, int, int] = (255, 255, 255), text_center_position: tuple[float, float] = (0, 0)):
        text_font: FontType = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: SurfaceType = text_font.render(text, True, text_color)
        text_rect: RectType = text_surf.get_rect(center=text_center_position)

        self.window.blit(source=text_surf, dest=text_rect)
