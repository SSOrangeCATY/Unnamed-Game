import pygame
from gameSystem.base.screen.base.screen import Screen
from gameSystem.base.player.player import Player

from resources import resources_system , res_img_game_ground , res_img_player
# Initialize pygame

class GameScreen(Screen):
    # Set up the game map
    def __init__(self):
        self.viewport_x = 0
        self.viewport_y = 0
        self.viewport_width = 16*32
        self.viewport_height = 16*16
        self.map_image = resources_system.get_image(res_img_game_ground)
        self.all_sprites = pygame.sprite.Group()
        self.setup()

    def setup(self):
        player_img = resources_system.get_image(res_img_player).get()
        self.player = Player((640,360), player_img, self.all_sprites)
        
    def draw(self, window:pygame.Surface, dt):
        window.fill('black')
        self.all_sprites.draw(window)
        self.all_sprites.update(dt)
    
    def event(self, event:pygame.event=None, keys=pygame.key.get_pressed()):
        pass