import pygame as GAME

class Audio:
    def __init__(self, audio:GAME.mixer.Sound,path:str):
        self.audio = audio
        self.path = path
        self.is_music = False
        
    def get(self) -> GAME.mixer.Sound:
        return self.audio
    
    def get_path(self) -> str:
        return self.path
    
    def for_sound_play(self):
        self.is_music = False
        self.audio.play()
        
    def stop(self):
        if self.is_music:
            GAME.mixer.music.stop()
        else:
            self.audio.stop()
            
    def set_volume(self,volume):
        if volume > 1:
            volume = 1
        audio_volume = volume
        if self.is_music:
            GAME.mixer.music.set_volume(audio_volume)
        else:
            self.audio.set_volume(audio_volume)
    
    def for_muisc_play(self):
        self.is_music = True
        GAME.mixer.music.load(self.path)
        GAME.mixer.music.play()