class GameScreens:
    def __init__(self):
        self.screens = {}
        
    def add_screen(self, screen):
        self.screens[screen.__class__.__name__] = screen
    
    def get_screen(self, screen_name):
        return self.screens[screen_name]

class Screen:
    def __init__(self):
        pass 
           
    def display(self, window, event):
        raise NotImplementedError("Subclasses must implement the display method.")
    
    def draw(self, window):
        pass
    
    def init_button(self, window):
        pass
    
    def disable_button(self):
        pass
    
    def button_event(self, event):
        pass

def registryScreen():
    from screen.loadingScreen import LoadingScreen
    from screen.mainTitle import MainTitle
    screens = GameScreens()
    screens.add_screen(LoadingScreen())
    screens.add_screen(MainTitle())
    return screens
