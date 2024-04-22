from pygame import Surface
from screen.screen import Screen
from screen.button import ColorButton
import main
class MainTitle(Screen):
    def __init__(self):
        # 加载视频
        self.scaled_background = main.scaled_background
        self.button_width = 300
        self.button_height = 50
        self.button_x = main.WIDTH / 2 - self.button_width / 2
        self.start_button_y = main.HEIGHT / 2 - self.button_height / 2 + 150
        self.quit_button_y = self.start_button_y + self.button_height + 30
        self.start_button = ColorButton(self.button_x, self.start_button_y, self.button_width, self.button_height,'start', (255,255,255),(98,115,58),(49,56,23))
        self.quit_button = ColorButton(self.button_x, self.quit_button_y, self.button_width, self.button_height,'quit',(255,255,255),(98,115,58), (49,56,23))
    
    def display(self,window:Surface=None,event=None):
        if(event is not None):
            self.button_event(event)
        if window is not None:
            # 获取当前时间（秒），并取模视频的持续时间以实现循环播放
            t = (main.GAME.time.get_ticks() / 1000) % main.main_video.duration
            # 获取当前帧并显示
            frame = main.main_video.get_frame(t)
            frame_image = main.GAME.image.fromstring(frame.tostring(), frame.shape[1::-1], 'RGB')
            window.blit(main.GAME.transform.scale(frame_image, (1280, 720)), (0, 0))
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
           pass
        if self.quit_button.handle_event(event):
           # 在这里处理退出按钮被点击的事件
           main.GAME.quit()