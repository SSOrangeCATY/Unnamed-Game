import main

# 使用main中的变量定义一个方法用于显示主标题界面
def main_title(window):
    # 加载主标题图像
    window.blit(main.scaled_background, (0, 0))
    init_button(window)
    main.game.display.update()

def init_button(window):
    # 定义按钮的尺寸和位置
    button_width = 100
    button_height = 50
    button_x = main.width / 2 - button_width / 2
    button_y = main.height / 2 - button_height / 2

    # 定义按钮的颜色
    button_color = (255, 0, 0)  # 红色

    # 定义按钮的文本
    button_text = 'Click me!'
    button_font = main.game.font.Font(None, 30)  # 使用默认字体，字号为30
    button_label = button_font.render(button_text, True, (255, 255, 125))  # 白色文本

    # 绘制按钮
    main.game.draw.rect(window, button_color, (button_x, button_y, button_width, button_height))
    window.blit(button_label, (button_x + (button_width - button_label.get_width()) / 2, button_y + (button_height - button_label.get_height()) / 2))