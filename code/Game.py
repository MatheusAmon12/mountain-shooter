import pygame as app

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu


class Game:
    def __init__(self):
        app.init()
        self.window = app.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_response = menu.run()

            if menu_response == MENU_OPTION[0]:
                pass
            elif menu_response == MENU_OPTION[1]:
                pass
            elif menu_response == MENU_OPTION[2]:
                pass
            elif menu_response == MENU_OPTION[3]:
                pass
            else:
                app.quit()
                quit()