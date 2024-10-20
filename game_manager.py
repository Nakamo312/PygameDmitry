
import logging
from UI.button import TextButton
from event_container import EventService
from game_object import GameObject
from scene_service import SceneService
from window import Window
import pygame as pg

class GameManager():
    def __init__(self, window_size: pg.Vector2 = None):
        #инициализация сервисов
        self.main_window = Window(window_size) if window_size else Window()
        self.scene_service = SceneService()
        self.event_service = EventService()
        self.start()

    def start(self):

        logging.basicConfig(filename='game_manager.log', level=logging.INFO)
        
        self.scene_service.create_scene("start_menu")
        self.scene_service.set_active_scene("start_menu")

        btn = TextButton(pg.Vector2(10,100),pg.Vector2(100,50),
                         id="TestButton")
        btn.text = "Test1"

        btn2 = TextButton(pg.Vector2(70,100),pg.Vector2(100,50),
                         id="TestButton")
        btn2.text = "Test2"
        
        btn.clicked.subscribe(lambda **kwargs: print("Button1 Clicked"))
        btn2.clicked.subscribe(lambda **kwargs: print("Button2 Clicked"))

        self.scene_service.scenes["start_menu"].add(btn)
        self.scene_service.scenes["start_menu"].add(btn2)

        self.__events_handlle()

    def __events_handlle(self):
        self.scene_service.curent_scene.events_handlle(self.event_service)

    def set_screen(self, size: pg.Vector2):
        self.main_window.size = size

    def set_active_scene(self, id: str):
        self.scene_service.set_active_scene(id)
        self.__events_handlle()

    def add_scene(self, id: str):
        self.scene_service.create_scene(id)

    def add_object(self, obj: GameObject, scene_id: str):
        if scene_id in self.scene_service.scenes:
            self.scene_service.scenes[scene_id].add(obj)

    def update(self):
        self.scene_service.curent_scene.update()
        self.scene_service.curent_scene.draw(self.main_window.screen)
        self.main_window.update()
        self.event_service.procces_system_events()