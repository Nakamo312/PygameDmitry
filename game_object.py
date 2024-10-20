import inspect
from typing import Callable
import pygame as pg
import logging

from event_container import Event, EventService


class GameObject():  
    counter = 0  

    def __init__(self, id: str = None, parent : "GameObject" = None):
        self.id = id if id else f"GameObject{GameObject.counter}"
        GameObject.counter += 1
        self.parent = parent
        self.children: dict[str, GameObject] = dict()
        self._event: Event = Event(-1)
        if parent:
            parent.add_child(self)

    @staticmethod
    def direct_bypass(func:Callable) -> Callable:
        def wrapper(*args):
            func(*args)
            for child in args[0].children.values():
                child.direct_bypass(func)(child)
        return wrapper
    
    @staticmethod
    def reverse_bypass(func:Callable) -> Callable:
        def wrapper(*args):
            for child in args[0].children.values():
                child.reverse_bypass(func)(child)
            return func(*args)
        return wrapper

    @reverse_bypass
    def clear(self):
        del self

    @direct_bypass
    def search(self, id: str) -> "GameObject":
        if self.id == id:
            return self
        
        
    def add_child(self, obj: "GameObject"):
        i = 0
        tmp_id = obj.id
        while obj.id in self.children:
            obj.id = f"{tmp_id}{i}"
            i += 1
        
        self.children[obj.id] = obj

    def remove_child(self, id: str):
        if self.id == id:
            del self

    @direct_bypass
    def events_handlle(self, service: EventService):
        if self._event.uid != -1:
            service.register_event(self._event.uid, self._event)
            

    @direct_bypass
    def update(self):
        ...

    @direct_bypass
    def draw(self, screen: pg.Surface):
        ...
    
    @direct_bypass
    def print(self):
        print(self.id)

