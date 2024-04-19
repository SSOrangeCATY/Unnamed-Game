#写出游戏的主标题界面
import pygame
from _main_ import scaled_background

    
# 使用main中的变量定义一个方法用于显示主标题界面
def main_title(window):
    # 加载主标题图像
    window.blit(scaled_background, (0, 0))