import pygame as pg

class Window():
    def __init__(self, size: pg.Vector2 = None):
        self.__init()
        self.size = size if size else pg.Vector2(500,500)
        self.screen = pg.display.set_mode(self.size)
    
    def __init(self):
        self.display = pg.display
        self.display.init()

    def update(self):
        self.display.update()