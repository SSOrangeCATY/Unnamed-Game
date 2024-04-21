#写一个控制游戏全局音效 音乐的系统
#根据当前界面的音效音乐设置来播放音效和音乐
#音效音乐的设置在界面py的变量中
#音效音乐的播放在game.image.load(os.path.join(game_dir, 'rescouces',"audio")文件中

import os
import main

def audio_system():
    if main.game_first_loading is True:
        main.game.mixer.music.load(os.path.join(main.game_dir, 'rescouces',"audio", 'bgm.mp3'))
        main.game.mixer.music.play(-1)
        main.game_first_loading = False
    else:
        pass
    return None