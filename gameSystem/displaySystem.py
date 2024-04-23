from gameSystem.base.screen.base.screen import GameScreens
import config
import system
 
def set_window_title(title:str):
    system.GAME.display.set_caption(title)

def display_update():
    if config.running is True:
       system.GAME.display.update()

def disply_flip():
    if config.running is True:
       system.GAME.display.flip()
       
def screen_display_logic(window=None, event=None):
    if config.game_first_loading is True: 
        system.current_screen = system.screens.get_screen("LoadingScreen")
    else :
        system.current_screen = system.screens.get_screen("MainTitle")
    system.current_screen.display(window,event)
    display_update()

def registryScreen():
    from gameSystem.base.screen.loadingScreen import LoadingScreen
    from gameSystem.base.screen.mainTitle import MainTitle
    screens = GameScreens()
    screens.add_screen(LoadingScreen())
    screens.add_screen(MainTitle())
    return screens