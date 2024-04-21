import os
import pygame
import gameSystem.screenSystem
from screen.Screen import GameScreens

# CORE 别改！！
GAME = pygame
GAME.init()
GAME.font.init()

# Video settings
WIDTH = 1280
HEIGHT = 720
button_font = GAME.font.Font(None, 30)
current_screen = None
screens:GameScreens = None #FIANL

# Game directory and Resources
GAME_DIR = os.path.dirname(os.path.abspath(__file__))
background_image = GAME.image.load(os.path.join(GAME_DIR, 'rescouces',"image", 'bg.png'))
studio_image = GAME.image.load(os.path.join(GAME_DIR, 'rescouces',"image", 'studio.png'))
scaled_studio = GAME.transform.scale(studio_image, (WIDTH, HEIGHT))
scaled_background = GAME.transform.scale(background_image, (WIDTH, HEIGHT))
 
# Core variables
running = True
window = GAME.display.set_mode((WIDTH, HEIGHT))
game_first_loading = True

def display_update():
    if running is True:
       GAME.display.update()

def disply_flip():
    if running is True:
       GAME.display.flip()

# 游戏循环
while running:
    # 处理事件
    for event in GAME.event.get():
        if event.type == GAME.QUIT:
            running = False  # 停止游戏循环
            break
        gameSystem.screenSystem.screen_display_logic(None,event)
    gameSystem.screenSystem.screen_display_logic(window,None)
    
# 退出pygame
GAME.quit()