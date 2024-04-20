import main
from screen.button import ColorButton

button_width = 300
button_height = 50

button_x = main.width / 2 - button_width / 2

start_button_y = main.height / 2 - button_height / 2 + 150
quit_button_y = start_button_y + button_height + 30

# 创建按钮实例
start_button = ColorButton(x=button_x, y=start_button_y, width=button_width, height=button_height,text='start', text_color=(125,125,125),color=(52,134,206), click_color=(32,114,186))
quit_button = ColorButton(x=button_x, y=quit_button_y, width=button_width, height=button_height,text='quit',color=(52,134,206), click_color=(32,114,186))

# 使用main中的变量定义一个方法用于显示主标题界面
def main_title(window):
    # 加载主标题图像
    window.blit(main.scaled_background, (0, 0))
    init_button(window)
    main.game.display.update()

def init_button(window):
    # 绘制按钮
    start_button.draw(window)
    quit_button.draw(window)
    
    # 检测鼠标点击事件
    for event in main.game.event.get():
        if start_button.handle_event(event):
            # 在这里处理开始按钮被点击的事件
            pass
        if quit_button.handle_event(event):
            # 在这里处理退出按钮被点击的事件
            main.game.quit()