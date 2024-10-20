import pygame as pg

from event_container import EventService
from game_object import GameObject

class Scene(): 
    counter = 0 
    def __init__(self, _id: str):
        self.id = _id if _id else f"Scene{Scene.counter}"
        self.objects: list[GameObject] = []

    def add(self, object: GameObject):
        i = 0
        for obj in self.objects:
            while obj.id == object.id:
                object.id = f"{obj.id}{i}"
                i += 1
        self.objects.append(object)
    
    def delete(self, id: str):
        for obj in self.objects:
            finded_obj = obj.search(id)
            if finded_obj:
                finded_obj.clear()
                return
            
    def events_handlle(self, service: EventService):
        for obj in self.objects:
            obj.events_handlle(service)

    def update(self):
        for obj in self.objects:
            obj.update()
    
    def draw(self, screen: pg.Surface):
        for obj in self.objects:
            obj.draw(screen) 
    
    def clear(self):
        for obj in self.objects:
            obj.clear()