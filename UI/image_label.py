import pygame as pg
from UI.area import Area
from game_object import GameObject


class ImageLabel(Area):
    def __init__(self, pos : pg.Vector2,
                       size: pg.Vector2,
                       color: pg.Color = None,
                       border_width: float = None,
                       border_color: pg.Color = None,
                       img : pg.Surface = None,
                       id:str = None,
                       parent: GameObject = None):
        super().__init__(pos, size, color, border_color, border_width,id, parent)
        self.img  = img.convert_alpha()
        self.__buffer_img = img.copy()
        coeff = size[0]/self.img.get_size()[0]
        self._image_render()
        self.scale(coeff)

    def _image_render(self):
        x,y = self.rect.x, self.rect.y
        self.surface = self.img.convert_alpha()
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = x,y

    def set_size(self, size: pg.Vector2):
        self.img = pg.transform.scale(self.__buffer_img, size)
        self._image_render()
        
    def scale(self, coeff: float):
        new_size = pg.Vector2(self.rect.width * coeff, self.rect.height * coeff)
        self.set_size(new_size)
    
    @GameObject.direct_bypass
    def resize(self, scale_factor: float):
        size = self.rect.width * scale_factor
        self.set_size(size)


        