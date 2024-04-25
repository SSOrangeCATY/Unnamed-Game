import config
import pygame as GAME
from gameSystem.displaySystem import DisplaySystem

class Game:
    def __init__(self):
        self.window = GAME.display.set_mode((config.VIDEO_WIDGHT,config.VIDEO_HEIGHT))
        GAME.init()
        self.display = DisplaySystem()
        self.sound = GAME.mixer
        self.clock = GAME.time.Clock()
        self.fps = config.VIDEO_FPS
        
    def quit(self):
        config.running = False
        
    def main(self):
        while config.running:
            self.running = config.running
            for event in GAME.event.get():
                if event.type == GAME.QUIT:
                    self.quit()
                self.display.screen_display_logic(None,event,None)
            dt = self.clock.tick() / 1000
            self.display.screen_display_logic(self.window,None,dt)
            self.display.disply_flip()
        GAME.quit()
        
main = Game()
main.main()
# 退出pygame
GAME.quit()