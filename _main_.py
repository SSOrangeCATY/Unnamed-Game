import os
import pygame

width = 1280
height = 720

game_dir = os.path.dirname(os.path.abspath(__file__))

background_image = pygame.image.load(os.path.join(game_dir, 'rescouces', 'bg.png'))
studio_image = pygame.image.load(os.path.join(game_dir, 'rescouces', 'studio.png'))

scaled_studio = pygame.transform.scale(studio_image, (width, height))
scaled_background = pygame.transform.scale(background_image, (width, height))

window = pygame.display.set_mode((width, height))
