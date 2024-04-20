import os
import pygame
import gameSystem.ScreenSystem

# CORE
game = pygame
game.init()
game.font.init()

# Video settings
width = 1280
height = 720

# Game directory and Resources
game_dir = os.path.dirname(os.path.abspath(__file__))
background_image = pygame.image.load(os.path.join(game_dir, 'rescouces', 'bg.png'))
studio_image = pygame.image.load(os.path.join(game_dir, 'rescouces', 'studio.png'))
scaled_studio = pygame.transform.scale(studio_image, (width, height))
scaled_background = pygame.transform.scale(background_image, (width, height))

# Core variables
running = True
window = pygame.display.set_mode((width, height))
game_first_loading = True


# 游戏循环
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # 停止游戏循环
            break
            
    gameSystem.ScreenSystem.screen_display_logic(window)
    
# 退出pygame
pygame.quit()