import main
from pygame import Surface
import screen.screen

class LoadingScreen(screen.screen.Screen):
    def __init__(self, ):
        self.surface_image = main.scaled_studio
        self.fade_surface = main.GAME.Surface((main.WIDTH, main.HEIGHT))
        self.fade_in = True
        self.fade_out = False
        self.fade_alpha = 255
        self.fade_count = 0

    def display(self, window, event):
        if window is not None:
            self.draw(window)
    
    def draw(self, window: Surface):
        if main.game_first_loading:
            if self.fade_count == 0:
                self.surface_image = main.scaled_studio
            else:
                # 获取当前时间（秒），并取模视频的持续时间以实现循环播放
                t = (main.GAME.time.get_ticks() / 1000) % main.main_video.duration
                # 获取当前帧并显示
                frame = main.main_video.get_frame(t)
                self.surface_image = main.GAME.image.fromstring(frame.tostring(), frame.shape[1::-1], 'RGB')
            window.blit(main.GAME.transform.scale(self.surface_image, (1280, 720)), (0, 0))
            window.blit(self.fade_surface, (0, 0))


            # 渐入效果
            if self.fade_in:
                self.fade_surface.set_alpha(self.fade_alpha)  # 设置透明度
                self.fade_alpha -= 1  # 逐渐减小透明度S
                if self.fade_alpha <= 0:  # 当透明度为0时，停止渐入效果
                    self.fade_in = False
                    if self.fade_count == 0:
                        self.fade_out = True
                    else:
                        main.game_first_loading = False
                        main.current_screen = main.screens.get_screen("MainTitle")
                        #print("main.current_screen ="+ str(main.current_screen))
                        #print("main.game_first_loading ="+ str(main.game_first_loading))
                    
            # 渐出效果
            if self.fade_out:
                self.fade_surface.set_alpha(self.fade_alpha)  # 设置透明度
                self.fade_alpha += 1  # 逐渐增大透明度
                if self.fade_alpha >= 255:  # 当透明度为255时，停止渐出效果
                    self.fade_out = False
                    if self.fade_count == 0:
                        self.fade_count = 1
                        self.fade_in = True