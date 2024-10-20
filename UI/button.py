
from typing import Callable
from UI.text_label import TextLabel
from event_container import Event
from game_object import GameObject
import pygame as pg

class TextButton(TextLabel):
    def __init__(self, pos : pg.Vector2,
                   size: pg.Vector2,
                   color: pg.Color = None,
                   border_width: float = None,
                   border_color: pg.Color = None,
                   text : str = None,
                   id:str = None,
                   parent: GameObject = None):
        super().__init__(pos,size,color,border_width,
                         border_color,text,
                         id,parent)
        self._event = Event(pg.MOUSEBUTTONDOWN)
        self._clicked = Event(f"Clicked{hash(self.id)}")

        self._event.subscribe(self.onCollide)
    def onCollide(self, pos:pg.Vector2, **kwargs):
        if self.checkCollide(pos):
            self._clicked.invoke()

    @property
    def clicked(self):
        return self._clicked
    
    def update(self):
        return super().update()
              

        
 
        


