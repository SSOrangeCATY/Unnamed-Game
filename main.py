import system
import config
import pygame as GAME
import gameSystem.displaySystem
import gameSystem.soundSystem
import resources

audio_bgm =resources.resources_system.get_audio(resources.audio_bgm)

def main():
    while config.running:
    # 处理事件
        for event in GAME.event.get():
            if event.type == GAME.QUIT:
                config.running = False  # 停止游戏循环
                return
            gameSystem.displaySystem.screen_display_logic(None,event)
        gameSystem.displaySystem.screen_display_logic(system.window,None)
        
        if gameSystem.soundSystem.check_music_end():
            resources.resources_system.get_audio(resources.audio_bgm).for_muisc_play()
                     
main()
# 退出pygame
GAME.quit()