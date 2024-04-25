import pygame

class Screen:
    def __init__(self):
        pass 
           
    def display(self, window=None,dt=None):
        if window is not None:
            self.draw(window,dt)
    
    def draw(self, window):
        pass
    
    def init_button(self, window):
        pass
    
    def button_event(self, event):
        pass
    
    def event(self, event):
        if event != None :
            self.button_event(event)
    
    def __str__(self) -> str:
        return self.__class__.__name__
    
class GameScreens:
    def __init__(self):
        self.screens = {}
        
    def add_screen(self, screen):
        self.screens[screen.__class__.__name__] = screen
    
    def get_screen(self, screen_name:str) -> Screen:
        return self.screens[screen_name]
