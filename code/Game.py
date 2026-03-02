import pygame as app

from code.Menu import Menu


class Game:
    def __init__(self):
        app.init()
        self.window = app.display.set_mode(size=(1080, 640))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
