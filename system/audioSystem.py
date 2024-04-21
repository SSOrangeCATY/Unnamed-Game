#根据当前界面的音效音乐设置来播放音效和音乐
#音效音乐的设置在界面py的变量中
#音效音乐的播放在game.image.load(os.path.join(game_dir, 'rescouces',"audio")文件中

import os
import main

class AudioSystem:
    def __init__(self):
        self.audio_volume = 1
        self.music_volume = 1
        self.audio_path = os.path.join(main.GAME_DIR, 'rescouces',"audio")
        self.current_music = None
        self.current_

    def play_music(self, music_path):
        self.current_music = main.GAME.mixer.music.load(os.path.join(self.audio_path, music_path))
        main.GAME.mixer.music.play(-1)
        self.music_playing = True

    def stop_music(self):
        main.GAME.mixer.music.stop()
        self.music_playing = False

    def set_music_volume(self, volume):
        if volume > 1:
            volume = 1
        self.music_volume = volume
        main.GAME.mixer.music.set_volume(self.music_volume)

    def check_music_end(self):
        if main.GAME.mixer.music.get_busy() == 0:
            return True
        return False

class GameAudios:
    def __init__(self):
        self.audios = {}
        
    def add_audio(self, audio):
        self.audios[audio.__class__.__name__] = audio
    
    def get_audio(self, audio_name):
        return self.audios[audio_name]