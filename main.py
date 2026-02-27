import pygame as app

app.init()

screen = app.display.set_mode(size=(1080, 640))


while True:
    # check for all events
    for event in app.event.get():
        if event.type == app.QUIT:
            app.quit() # close window
            quit()  # close pygame
