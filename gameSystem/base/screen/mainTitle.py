import pygame
from gameSystem.base.screen.base.screen import Screen
from gameSystem.base.screen.base.button import ColorButton
from resources import resources_system , res_video_mainTitle
import config
class MainTitle(Screen):
    def __init__(self,width=1280,height=720):
        # 加载视频
        self.video = resources_system.get_video(res_video_mainTitle)
        self.video_druation = self.video.get_duration()
        self.button_width = 300
        self.button_height = 50
        self.button_x = width / 2 - self.button_width / 2
        self.start_button_y = height / 2 - self.button_height / 2 + 150
        self.quit_button_y = self.start_button_y + self.button_height + 30
        self.start_button = ColorButton(self.button_x, self.start_button_y, self.button_width, self.button_height,'start', (255,255,255),(98,115,58),(49,56,23))
        self.quit_button = ColorButton(self.button_x, self.quit_button_y, self.button_width, self.button_height,'quit',(255,255,255),(98,115,58), (49,56,23))
            
    def draw(self, window,dt):
        t = pygame.time.get_ticks() / 1000 % self.video_druation
        # 获取当前帧并显示
        window.blit(self.video.get_fullscreen_video(t), (0, 0))
        self.init_button(window)
            
    def init_button(self, window):
        self.start_button.draw(window)
        self.quit_button.draw(window)
    
    def disable_button(self):
        self.start_button.disable()
        self.quit_button.disable()
        
    def button_event(self, event):
        if self.start_button.handle_event(event):
            # 在这里处理开始按钮被点击的事件
           config.current_screen = "GameScreen"
        if self.quit_button.handle_event(event):
           # 在这里处理退出按钮被点击的事件
           config.running = False