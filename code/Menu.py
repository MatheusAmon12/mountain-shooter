import pygame.image
from pygame.font import FontType
from pygame.rect import RectType
from pygame.surface import SurfaceType

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    def __init__(self, window: SurfaceType):
        self.window = window
        self.surf = pygame.image.load("./assets/MenuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load("./assets/Menu.mp3")
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120))

            for option in range(len(MENU_OPTION)):
                if option == menu_option:
                    self.menu_text(20, MENU_OPTION[option], C_YELLOW, ((WIN_WIDTH / 2), 180 + 25 * option))
                else:
                    self.menu_text(20, MENU_OPTION[option], C_WHITE, ((WIN_WIDTH / 2), 180 + 25 * option))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple[int, int, int, int] = (255, 255, 255), text_center_position: tuple[float, float] = (0, 0)):
        text_font: FontType = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: SurfaceType = text_font.render(text, True, text_color)
        text_rect: RectType = text_surf.get_rect(center=text_center_position)

        self.window.blit(source=text_surf, dest=text_rect)
