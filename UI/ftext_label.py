
from UI.area import Area
import pygame as pg

class TextLabel(Area):
     def __init__(self, pos : pg.Vector2,
                       size: pg.Vector2,
                       color: pg.Color = None,
                       border_width: float = None,
                       border_color: pg.Color = None):
          super().__init__(pos, size, color, border_width, border_color)
          self._text: str
          self._font_size:int = 25
          self._text_color: pg.Color = pg.Color(0,0,0)
          self._font_family = None 
          self._font_render()
          self._text_render()
     
     def text(self, text: str):
          self._text = text
          self._text_render()

     def text_color(self):
          ...
     
     def font_size(self):
          ...
     
     def font_family(self):
          ...
     

     def _font_render(self):
          self._font = pg.font.Font(self._font_family, self._font_size)

     def _text_render(self):
          self.surface = self._font.render(self._text, self._text_color)
