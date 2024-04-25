import pygame
from gameSystem.base.animation import Animation, AnimationList

class AnimationManager:
    def __init__(self, animtions:AnimationList):
        self.animations = animtions
        self.currentFrame = 0
        self.currentAnimation:Animation = Animation()
        
    def set_current_animation(self, animation_name:str):
        self.currentAnimation = self.animations[animation_name]
        
    def get_current_frame(self) -> pygame.Surface:
        return self.currentAnimation.play()
        