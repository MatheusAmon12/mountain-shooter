import pygame as app

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        app.init()
        self.window = app.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_response = menu.run()

            if menu_response in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]
                level = Level(self.window, "Level1", menu_response, player_score)
                level_response = level.run(player_score)

                if level_response:
                    level_2 = Level(self.window, "Level2", level_response, player_score)
                    level_2.run(player_score)
            elif menu_response == MENU_OPTION[3]:
                pass
            else:
                app.quit()
                quit()