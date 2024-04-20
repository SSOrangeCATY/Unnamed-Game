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
button_font = game.font.Font(None, 30)

# Game directory and Resources
game_dir = os.path.dirname(os.path.abspath(__file__))
background_image = game.image.load(os.path.join(game_dir, 'rescouces', 'bg.png'))
studio_image = game.image.load(os.path.join(game_dir, 'rescouces', 'studio.png'))
scaled_studio = game.transform.scale(studio_image, (width, height))
scaled_background = game.transform.scale(background_image, (width, height))

# Core variables
running = True
window = game.display.set_mode((width, height))
game_first_loading = True


# 游戏循环
while running:
    # 处理事件
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False  # 停止游戏循环
            break
            
    gameSystem.ScreenSystem.screen_display_logic(window)
    
# 退出pygame
game.quit()