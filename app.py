import pygame as pg

from game_manager import GameManager
from scene import Scene
from window import Window

class App():
    MAX_FPS = 240
    def __init__(self):
        self.__init()
        self.__max_fps: int
        self.__clock = pg.time.Clock()
        self.__is_running = True
        self.game_manager = GameManager()
        #подписки
        self.game_manager.event_service.sytem_handlle(pg.QUIT, self.stop)
    def set_screen(self, size: pg.Vector2):
        self.screen = Window(size)

    def start(self):
        self.__is_running = True

    def stop(self):
        self.__is_running = False

    def set_fps(self, fps: int):
        if fps >= App.MAX_FPS:
            raise Exception("Too much frames per seconds")
        self.__max_fps = fps

    def __init(self):
        pg.init()


    def main_loop(self):
        while self.__is_running:
            self.game_manager.update()
            self.__clock.tick(self.__max_fps)


