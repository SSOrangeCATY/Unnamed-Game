import pygame
from _main_ import window
from gameSystem.ScreenSystem import screen_display_logic
# 初始化pygame
pygame.init()

# 创建游戏窗口
running = True

# 游戏循环
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # 停止游戏循环
    screen_display_logic(window)
    
# 退出pygame
pygame.quit()