from GameSystem.resourceSystem import Resource, ResourceList,ResourceSystem, ResourceType

preLoad_resourceList = ResourceList()

image_bg = Resource(ResourceType.Image, 'bg.png').register(preLoad_resourceList)
image_bg1 = Resource(ResourceType.Image, 'bg1.png').register(preLoad_resourceList)
image_studio = Resource(ResourceType.Image, 'studio.png').register(preLoad_resourceList)
    
audio_bgm = Resource(ResourceType.Audio, 'music.ogg').register(preLoad_resourceList)

video_mainTitle = Resource(ResourceType.Video, 'mainTitle.mp4').register(preLoad_resourceList)

def load_resources() -> ResourceSystem:
    return ResourceSystem(preLoad_resourceList)._load_resource()

resources_system = load_resources()
