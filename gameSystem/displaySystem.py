from gameSystem.base.screen.base.screen import GameScreens
import config
import pygame as GAME

class DisplaySystem:
    def __init__(self):
        self.widght = config.VIDEO_WIDGHT
        self.height = config.VIDEO_HEIGHT
        self.screens = GameScreens()
        self.registryScreen()
        config.current_screen = "LoadingScreen"
        self.current_screen = self.screens.get_screen(config.current_screen)
    
    def set_window_title(self,title:str):
        GAME.display.set_caption(title)

    def display_update(self):
        if config.running is True:
           GAME.display.update()

    def disply_flip(self):
        if config.running is True:
           GAME.display.flip()
       
    def screen_display_logic(self, window, event, dt):
        if str(self.current_screen) != config.current_screen:
           self.current_screen = self.screens.get_screen(config.current_screen)
        self.current_screen.display(window, dt)
        self.current_screen.event(event)
        self.display_update()

    def registryScreen(self):
        from gameSystem.base.screen.loadingScreen import LoadingScreen
        from gameSystem.base.screen.mainTitle import MainTitle
        from gameSystem.base.screen.gameScreen import GameScreen
    
        self.screens.add_screen(LoadingScreen())
        self.screens.add_screen(MainTitle())
        self.screens.add_screen(GameScreen())