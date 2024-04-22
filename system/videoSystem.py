import os
import pygame
import main
from moviepy.editor import VideoFileClip

pygame.init()

# 设置窗口标题和大小
pygame.display.set_caption("Video Player")
screen = pygame.display.set_mode((1280, 720))

# 加载视频
clip = VideoFileClip(os.path.join(main.GAME_DIR, "video.mp4"))

# 创建一个时钟对象来控制帧率
clock = pygame.time.Clock()

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取当前时间（秒）
    t = pygame.time.get_ticks() / 1000

    # 如果视频没有结束，获取当前帧并显示
    if t < clip.duration:
        frame = clip.get_frame(t)
        frame_image = pygame.image.fromstring(frame.tostring(), frame.shape[1::-1], 'RGB')
        screen.blit(pygame.transform.scale(frame_image, (1280, 720)), (0, 0))
    else:
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()