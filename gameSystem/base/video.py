from moviepy.editor import VideoFileClip

import pygame as GAME

class Video:
    def __init__(self, video:VideoFileClip):
        self.clip = video
        
    def get_frame(self, t:int):
        return self.clip.get_frame(t)

    def get_duration(self):
        return self.clip.duration
    
    def get_fullscreen_video(self,t:int) -> GAME.Surface:
            return GAME.transform.scale(GAME.image.fromstring(self.clip.get_frame(t).tostring(), self.clip.get_frame(t).shape[1::-1], 'RGB'), (1280, 720))

    def get_scaled_video(self, width:int, height:int, t:int) -> GAME.Surface:
            return GAME.transform.scale(GAME.image.fromstring(self.clip.get_frame(t).tostring(), self.clip.get_frame(t).shape[1::-1], 'RGB'), (width, height))