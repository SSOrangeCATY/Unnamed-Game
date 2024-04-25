from pygame import Surface,time
from gameSystem.base.screen.base.screen import Screen
from resources import resources_system,res_video_mainTitle,res_img_studio
import config

class LoadingScreen(Screen):
    
    def __init__(self):
        self.video = resources_system.get_video(res_video_mainTitle)
        self.video_druation = self.video.get_duration()
        self.surface_image = resources_system.get_image(res_img_studio).get_fullscreen_image()
        self.surface = Surface((1280, 720))
        self.fade_in = True
        self.fade_out = False
        self.fade_alpha = 255
        self.fade_count = 0

    def draw(self, window: Surface,dt=None):
            if self.fade_count == 1:
                # 获取当前时间（秒），并取模视频的持续时间以实现循环播放
                t = time.get_ticks() / 1000 % self.video_druation
                # 获取当前帧并显示
                self.surface_image = self.video.get_fullscreen_video(t)
                
            window.blit(self.surface_image, (0, 0))
            window.blit(self.surface, (0, 0))


            # 渐入效果
            if self.fade_in:
                self.surface.set_alpha(self.fade_alpha)  # 设置透明度
                self.fade_alpha -= 1  # 逐渐减小透明度S
                if self.fade_alpha <= 0:  # 当透明度为0时，停止渐入效果
                    self.fade_in = False
                    if self.fade_count == 0:
                        self.fade_out = True
                    else:
                        config.game_first_loading = False
                        config.current_screen = "MainTitle"
                        #print("main.current_screen ="+ str(main.current_screen))
                        #print("main.game_first_loading ="+ str(main.game_first_loading))
                    
            # 渐出效果
            if self.fade_out:
                self.surface.set_alpha(self.fade_alpha)  # 设置透明度
                self.fade_alpha += 1  # 逐渐增大透明度
                if self.fade_alpha >= 255:  # 当透明度为255时，停止渐出效果
                    self.fade_out = False
                    if self.fade_count == 0:
                        self.fade_count = 1
                        self.fade_in = True