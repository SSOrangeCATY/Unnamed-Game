from gameSystem.resourceSystem import Resource, ResourceList,ResourceSystem, ResourceType

preLoad_resourceList = ResourceList()

res_img_bg = Resource(ResourceType.Image, 'bg.png').registry(preLoad_resourceList)
res_img_studio = Resource(ResourceType.Image, 'studio.png').registry(preLoad_resourceList)
res_img_player = Resource(ResourceType.Image, 'player.png').registry(preLoad_resourceList)
res_img_game_ground = Resource(ResourceType.Image, 'game_ground.png').registry(preLoad_resourceList)
res_audio_music = Resource(ResourceType.Audio, 'music.ogg').registry(preLoad_resourceList)
res_video_mainTitle = Resource(ResourceType.Video, 'mainTitle.mp4').registry(preLoad_resourceList)

res_anim_player_up = Resource(ResourceType.Animation, 'player\\up').registry(preLoad_resourceList)
res_anim_player_down = Resource(ResourceType.Animation, 'player\\down').registry(preLoad_resourceList)
res_anim_player_left = Resource(ResourceType.Animation, 'player\\left').registry(preLoad_resourceList)
res_anim_player_right = Resource(ResourceType.Animation, 'player\\right').registry(preLoad_resourceList)

resources_system = ResourceSystem(preLoad_resourceList)
