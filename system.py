import pygame as GAME
from GameSystem.base.screen.base.screen import GameScreens, Screen
from GameSystem.displaySystem import registryScreen

GAME.init()

window = GAME.display.set_mode((1280, 720))

screens:GameScreens = registryScreen()
current_screen:Screen = screens.get_screen("LoadingScreen")
