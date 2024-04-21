from pygame import Surface
from screen.Screen import Screen
from screen.button import ColorButton
import main
class MainTitle(Screen):
    def __init__(self):
        self.scaled_background = main.scaled_background
        self.button_width = 300
        self.button_height = 50
        self.button_x = main.WIDTH / 2 - self.button_width / 2
        self.start_button_y = main.HEIGHT / 2 - self.button_height / 2 + 150
        self.quit_button_y = self.start_button_y + self.button_height + 30
        self.start_button = ColorButton(self.button_x, self.start_button_y, self.button_width, self.button_height,'start', (125,125,125),(52,134,206),(32,114,186))
        self.quit_button = ColorButton(self.button_x, self.quit_button_y, self.button_width, self.button_height,'quit',(52,134,206), (32,114,186))
    
    def display(self,window:Surface=None,event=None):
        if(event is not None):
            self.button_event(event)
        if window is not None:
            window.blit(self.scaled_background, (0, 0))
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