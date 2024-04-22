import os
import pygame
import system.screenSystem
from screen.screen import GameScreens
from moviepy.editor import VideoFileClip

# CORE 别改！！
GAME = pygame
GAME.init()
GAME.font.init()

# Video settings
WIDTH = 1280
HEIGHT = 720
button_font = GAME.font.Font(None, 30)
current_screen = None
screens:GameScreens = None #FIANL
clock = GAME.time.Clock()

# Audio settings
audio_volume = 0.5
background_music_cycle = True
GAME.mixer.music.set_volume(audio_volume)

# Game directory and Resources
GAME_DIR = os.path.dirname(os.path.abspath(__file__))
# Load images
background_image = GAME.image.load(os.path.join(GAME_DIR, 'rescouces',"image", 'bg1.png'))
studio_image = GAME.image.load(os.path.join(GAME_DIR, 'rescouces',"image", 'studio.png'))
scaled_studio = GAME.transform.scale(studio_image, (WIDTH, HEIGHT))
scaled_background = GAME.transform.scale(background_image, (WIDTH, HEIGHT))

# Load music
main_music = os.path.join(GAME_DIR, 'rescouces',"audio", 'music.ogg')
main_video_path = os.path.join(GAME_DIR, 'rescouces',"video", 'video.mp4')
main_video = VideoFileClip(main_video_path)

# Core variables
running = True
window = GAME.display.set_mode((WIDTH, HEIGHT))
game_first_loading = True

       
# Core Methods
# music
def play_music(music_path):
    GAME.mixer.music.load(music_path)
    GAME.mixer.music.play(-1)
    
def stop_music():
    GAME.mixer.music.stop()

def set_music_volume(volume):
    if volume > 1:
        volume = 1
    audio_volume = volume
    GAME.mixer.music.set_volume(audio_volume)
    
# 检测音乐是否播放完
def check_music_end():
    if GAME.mixer.music.get_busy() == 0:
        return True
    return False

# display
def set_window_title(title):
    GAME.display.set_caption(title)

def display_update():
    if running is True:
       GAME.display.update()

def disply_flip():
    if running is True:
       GAME.display.flip()
       
# 游戏循环
while running:
    # 处理事件
    for event in GAME.event.get():
        if event.type == GAME.QUIT:
            running = False  # 停止游戏循环
            break
        system.screenSystem.screen_display_logic(None,event)
    system.screenSystem.screen_display_logic(window,None)

    if check_music_end():
        play_music(main_music)
    
# 退出pygame
GAME.quit()