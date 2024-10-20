import pygame as pg

from game_object import GameObject


class Area(GameObject):
    def __init__(self, pos : pg.Vector2,
                       size: pg.Vector2,
                       color: pg.Color = None,
                       border_width: float = None,
                       border_color: pg.Color = None,
                       id:str = None,
                       parent: GameObject = None):
        super().__init__(id, parent)
        self.rect = pg.Rect(pos,size) 
        self.color = color if color else pg.Color(255,255,255) 
        self.border_width = border_width if border_width else 0
        self.border_color = border_color if border_color else self.color
        self.surface = pg.Surface(self.rect.size).convert_alpha()
        self._buffer_surface = self.surface.copy() 
        self.background = True
        self.is_active = True
        
    def draw(self, surface : pg.Surface):
        if self.is_active:
            if self.background:
                pg.draw.rect(surface, self.color,self.rect)
            surface.blit(self.surface, self.rect)
            if self.border_width > 0:
                pg.draw.rect(surface, self.border_color, self.rect, self.border_width)
            super().draw(surface)

    def checkCollide(self, pos: pg.Vector2) -> bool:
        if (self.rect.x < pos[0] < self.rect.x + self.rect.width):
            if ((self.rect.y < pos[1] < self.rect.y + self.rect.height)):
                return True
        return False

    def update(self):
        if not self.is_active:
            return
        super().update()

    def move(self, pos: pg.Vector2):
        x = pos.x - self.rect.x
        y = pos.y - self.rect.y
        self.__move_delta(delta= pg.Vector2(x,y))

    @GameObject.direct_bypass
    def __move_delta(self, delta: pg.Vector2):
        self.rect.x += delta.x
        self.rect.y += delta.y
    
    def set_size(self, size: pg.Vector2):
        self.rect.width = size.x
        self.rect.height = size.y
        self.surface = pg.transform.scale(self._buffer_surface, self.rect.size)
    
    @GameObject.direct_bypass
    def resize(self, scale_factor: float):
        size = self.rect.width * scale_factor
        self.set_size(size)
    