import pygame
import os
from loadingScreen import loading_screen , game_first_loading

# 初始化pygame
pygame.init()

# 定义游戏的根目录
game_dir = os.path.dirname(os.path.abspath(__file__))

width = 1280
height = 720

# 创建游戏窗口
window = pygame.display.set_mode((width, height))

# 加载背景图像
background_image = pygame.image.load(os.path.join(game_dir, 'rescouces', 'bg.png'))
studio_image = pygame.image.load(os.path.join(game_dir, 'rescouces', 'studio.png'))

# 将背景图像设置为窗口的表面
window.blit(background_image, (0, 0))

running = True

fade_surface = pygame.Surface((width, height))  # 创建一个新的表面来覆盖窗口
fade_surface.fill((0, 0, 0))  # 填充黑色

scaled_background = pygame.transform.scale(background_image, (width, height))
# 游戏循环
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # 停止游戏循环
    
    if game_first_loading: 
        scaled_studio = pygame.transform.scale(studio_image, (width, height))
        loading_screen(window, fade_surface, scaled_background, scaled_studio)
    else:
        window.blit(scaled_background, (0, 0))
    
    pygame.display.update()
    
# 退出pygame
pygame.quit()