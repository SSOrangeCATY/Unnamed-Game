import main
button_color = (255, 0, 0)  # 红色
button_width = 300
button_height = 50
button_x = main.width / 2 - button_width / 2
button_y = main.height / 2 - button_height / 2
button_label = main.button_font.render('start', True, (255, 255, 125))  # 白色文本
# 使用main中的变量定义一个方法用于显示主标题界面
def main_title(window):
    # 加载主标题图像
    window.blit(main.scaled_background, (0, 0))
    init_button(window)
    main.game.display.update()

def init_button(window):
    global button_color, button_width, button_height, button_x, button_y, button_label
    # 绘制按钮
    main.game.draw.rect(window, button_color, (button_x, button_y, button_width, button_height))
    window.blit(button_label, (button_x + (button_width - button_label.get_width()) / 2, button_y + (button_height - button_label.get_height()) / 2))
    
    # 检测鼠标点击事件
    mouse_x, mouse_y = main.game.mouse.get_pos()
    if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
        if main.game.mouse.get_pressed()[0]:
            # 点击后 修改按钮的颜色
            button_color = (0, 255, 0)
        else:
            button_color = (255, 0, 0)