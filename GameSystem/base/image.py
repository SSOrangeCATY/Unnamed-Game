import pygame as GAME


class Image:
    def __init__(self, image:GAME.Surface):
        self.image = image
    
    def get(self):
        return self.image
    
    def get_fullscreen_image(self) -> GAME.Surface:
        return GAME.transform.scale(self.image, (1280, 720))

    def get_scaled_image(self, width, height) -> GAME.Surface:
            return GAME.transform.scale(self.image, (width, height))
    
    def get_image_by_pos(self, x, y, width, height) -> GAME.Surface:
        return self.image.subsurface((x, y, width, height))