import config
import pygame
class Animation():
    def __init__(self,name:str,animaiton:list):
        self.name = name
        self.animations = animaiton
        self.animations_count = len(animaiton)
        self.location = config.GAME_DIR + "/resources/animations/" + self.name
    
    def play(self,index) -> pygame.Surface:
        if index + 1 >= self.animations_count:
            index = 0
        else:
            index += 1
        return self.animations[index]
              
    
    def __str__(self):
        return "aniamtion:" + self.name
    
class AnimationList():
    def __init__(self):
        self.animations = {}
    
    def add(self,animation:Animation):
        self.animations[animation.name] = animation
    
    def get(self,name:str) -> Animation:
        return self.animations[name]
    
    def __str__(self):
        result = ""
        for key in self.animations:
            result += str(self.animations[key]) + "\n"
        return result