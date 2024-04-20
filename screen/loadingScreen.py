import main

surface_image = main.scaled_studio
fade_surface = main.game.Surface((main.width, main.height))
fade_in = True
fade_out = False
fade_alpha = 255
fade_count = 0

# 加载界面
def loading_screen(window):
    global surface_image, fade_surface, fade_in, fade_out, fade_alpha, fade_count
    if main.game_first_loading:
        if fade_count == 0:
            surface_image = main.scaled_studio
        else:
            surface_image = main.scaled_background
            
        window.blit(surface_image, (0, 0))
        window.blit(fade_surface, (0, 0))

        # 渐入效果
        if fade_in:
            fade_surface.set_alpha(fade_alpha)  # 设置透明度
            fade_alpha -= 1  # 逐渐减小透明度S
            if fade_alpha <= 0:  # 当透明度为0时，停止渐入效果
                fade_in = False
                if fade_count == 0:
                    fade_out = True
                else:
                    main.game_first_loading = False
                    print("main.game_first_loading ="+ str(main.game_first_loading))
                    
        # 渐出效果
        if fade_out:
            fade_surface.set_alpha(fade_alpha)  # 设置透明度
            fade_alpha += 1  # 逐渐增大透明度
            if fade_alpha >= 255:  # 当透明度为255时，停止渐出效果
                fade_out = False
                if fade_count == 0:
                    fade_count = 1
                    fade_in = True
        main.game.display.flip()