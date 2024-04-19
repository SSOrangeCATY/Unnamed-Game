import pygame
from screen.loadingScreen import loading_screen , game_first_loading
from screen.mainTitle import main_title

def open_screen_by_id(screen_id):
    if screen_id == 0:
        loading_screen()
    else:
        print("Screen not found")
        
def screen_display_logic(window):
    if game_first_loading: 
        loading_screen(window)
    else:
        main_title(window)
        pygame.display.update()