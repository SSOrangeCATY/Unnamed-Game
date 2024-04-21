import main
# 创建一个ImageButton实例
# image_button = ImageButton(x=50, y=50, width=100, height=50, idle_image='idle.png', click_image='click.png')

# 创建一个ColorButton实例
# start_button = ColorButton(x=button_x, y=start_button_y, width=button_width, height=button_height,text='start', text_color=(125,125,125),color=(52,134,206), click_color=(32,114,186))

class Button:
    def __init__(self, x, y, width, height, text='', text_color=(255, 255, 125)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_hover = False
        self.text = main.button_font.render(text, True, text_color)  # 文本
        self.enable = True

    def draw(self, window):
        window.blit(self.text, (self.x + (self.width - self.text.get_width()) / 2, self.y + (self.height - self.text.get_height()) / 2))


    def is_over(self, pos):
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            return True
        return False

    def handle_event(self, event):
        pass
    
    def disable(self):
        self.enable = False
        
    def enable(self):
        self.enable = True
        
# 创建一个ImageButton类，继承自Button类
class ImageButton(Button):
    def __init__(self, x, y, width, height, text='',text_color=(255, 255, 125), idle_image=None, click_image=None):
        super().__init__(x, y, width, height, text,text_color)
        self.idle_image = main.GAME.image.load(idle_image) if idle_image else None
        self.click_image = main.GAME.image.load(click_image) if click_image else None
        self.current_image = self.idle_image

    def draw(self, window):
        if self.current_image:
            window.blit(self.current_image, (self.x, self.y, self.width, self.height))
            if self.is_hover is True:
                main.GAME.draw.rect(window, (125, 125, 125), (self.x, self.y, self.width, self.height), 5)
            super().draw(window)

    def handle_event(self, event):
        if not self.enable:
           return False
        if event.type == main.GAME.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_over(main.GAME.mouse.get_pos()):
                if self.click_image:
                    self.current_image = self.click_image
                    self.is_hover = False
                return True
        elif self.is_over(main.GAME.mouse.get_pos()):
            self.is_hover = True
        else:
            if self.idle_image:
                self.current_image = self.idle_image
                self.is_hover = False
        return False


class ColorButton(Button):
    def __init__(self, x, y, width, height, text='', text_color=(255, 255, 125), color=(25,120,25), click_color=(45,100,45)):
        super().__init__(x, y, width, height,text,text_color)
        self.color = color
        self.click_color = click_color
        self.current_color = self.color

    def draw(self, window):
        main.GAME.draw.rect(window, self.current_color, (self.x, self.y, self.width, self.height))
        if self.is_hover is True:
            main.GAME.draw.rect(window, self.click_color, (self.x, self.y, self.width, self.height), 5)
        super().draw(window)

    def handle_event(self, event):
        if not self.enable:
            return False
        if event.type == main.GAME.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_over(main.GAME.mouse.get_pos()):
                self.current_color = self.click_color
                self.is_hover = False
                return True
        elif self.is_over(main.GAME.mouse.get_pos()):
            self.is_hover = True
            self.current_color = self.color
        else:
            self.is_hover = False
            self.current_color = self.color
        return False