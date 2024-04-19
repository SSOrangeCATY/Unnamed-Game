import os
import pygame
from _main_ import width, height, scaled_studio, scaled_background

game_first_loading = True

surface_image = scaled_studio

fade_surface = pygame.Surface((width, height))

def loading_screen(window):
    global game_first_loading, surface_image, scaled_studio, scaled_background, width, height
    fade_in = True
    fade_out = False
    fade_alpha = 255
    fade_count = 0
    while game_first_loading:
        if fade_count == 0:
            surface_image = scaled_studio
        else:
            surface_image = scaled_background
            
        window.blit(surface_image, (0, 0))
        window.blit(fade_surface, (0, 0))

        # 渐入效果
        if fade_in:
            fade_surface.set_alpha(fade_alpha)  # 设置透明度
            fade_alpha -= 1  # 逐渐减小透明度S
            if fade_alpha <= 0:  # 当透明度为0时，停止渐入效果
                fade_in = False
                if fade_count == 0:
                    fade_out = True
                else:
                    game_first_loading = False
                    
        # 渐出效果
        if fade_out:
            fade_surface.set_alpha(fade_alpha)  # 设置透明度
            fade_alpha += 1  # 逐渐增大透明度
            if fade_alpha >= 255:  # 当透明度为255时，停止渐出效果
                fade_out = False
                if fade_count == 0:
                    fade_count += 1
                    fade_in = True
        pygame.display.update()