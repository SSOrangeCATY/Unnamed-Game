import pygame as GAME
#class SoundSystem:
        
def check_music_end(audio:GAME.mixer.Channel=None):
    if audio is None:
        if GAME.mixer.music.get_busy() == 0:
            return True
        return False
    else:
        if audio.get_busy() == 0:
            return True
        return False

def stop_music():
    GAME.mixer.music.stop()
    
def set_music_volume(volume):
    if volume > 1:
        volume = 1
    audio_volume = volume
    GAME.mixer.music.set_volume(audio_volume)