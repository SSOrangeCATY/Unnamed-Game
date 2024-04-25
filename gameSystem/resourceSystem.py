from enum import Enum
import os
from typing import Union
from moviepy.editor import VideoFileClip
import pygame as GAME
from gameSystem.base.audio import Audio
from config import GAME_DIR
from gameSystem.base.video import Video
from gameSystem.base.image import Image
from gameSystem.base.animation import Animation


class ResourceType(Enum):
    Image = "image"
    Audio = "audio"
    Video = "video"
    Animation = "animations"

class Resource:
    def __init__(self,type:ResourceType,name:str,loaction:str=None):
        self.type = type
        self.name = name
        self.location = loaction if type != ResourceType.Animation else GAME_DIR + "\\resources\\animations\\" + name 
    def getType(self) -> ResourceType:
        return self.type
    def getName(self) -> str:
        return self.name
    def getLocation(self) -> str:
        return self.location
    def registry(self,list:"ResourceList"):
        list.add(self)
        return self
    def __str__(self):
        return self.type.value + ":" + self.name

class ResourceList:
    def __init__(self):
        self.resources = {}

    def add(self, resource: Resource ,preload:bool = True):
        key = resource.getType()
        if key not in self.resources:
            self.resources[key] = []
        for r in self.resources[key]:
            if r.getName() == resource.getName():
                print("Resource already exists: " + key + ":" + resource.getName())
                return
        self.resources[key].append(resource)
        if preload is True : print("Preload resource added: " + key.value + ":" + resource.getName())

    def get(self, type: ResourceType, name: str) -> Resource:
        key = type.value
        if key in self.resources:
            for resource in self.resources[key]:
                if resource.getName() == name:
                    return resource
        print("Resource not found: " + key + ":" + name)
        return None
    
    def __str__(self) -> str:
        result = ""
        for key in self.resources:
            result += key.value + ":\n"
            for resource in self.resources[key]:
                result += "  " + str(resource) + "\n"
        return result
    
class GameResourcesList:
    def __init__(self):
        self.loaded_resources = {}
    
    def try_load(self, resource: Resource):
        if resource.getName() not in self.loaded_resources:
            if resource.getType() == ResourceType.Image:
                try:
                    if resource.getLocation() is not None:
                        self.loaded_resources[str(resource)] = Image(GAME.image.load(resource.getLocation()))
                    else:
                        self.loaded_resources[str(resource)] = Image(GAME.image.load(os.path.join(GAME_DIR, 'resources', resource.type.value, resource.getName())))
                    print("Resource loaded: " + str(resource))
                    return True
                except Exception as e:
                    print("Error loading image:", e)
                    return False
            elif resource.getType() == ResourceType.Audio:
                try:
                    if resource.getLocation() is not None:
                        self.loaded_resources[str(resource)] = Audio(GAME.mixer.Sound(resource.getLocation()),resource.getLocation())
                    else:
                        path = os.path.join(GAME_DIR, 'resources',resource.type.value, resource.getName())
                        self.loaded_resources[str(resource)] = Audio(GAME.mixer.Sound(path),path)
                    print("Resource loaded: " + str(resource))
                    return True
                except Exception as e:
                    print("Error loading audio:", e)
                    return False
            elif resource.getType() == ResourceType.Video: 
                try:
                    if resource.getLocation() is not None:
                        self.loaded_resources[str(resource)] = Video(VideoFileClip(resource.getLocation()))
                    else:
                        self.loaded_resources[str(resource)] = Video(VideoFileClip(os.path.join(GAME_DIR, 'resources',resource.type.value, resource.getName())))
                    print("Resource loaded: " + str(resource))
                    return True
                except Exception as e:
                    print("Error loading video:", e)
                    return False
            elif resource.getType() == ResourceType.Animation:
                surface_list = []
                for _, __, animation_files in os.walk(resource.getLocation()):
                    for animation_file in animation_files:
                        surface_list.append(GAME.image.load(os.path.join(resource.getLocation(), animation_file)).convert_alpha())
                        print("Resource " + str(resource) + " load: " + animation_file)
                self.loaded_resources[str(resource)] = Animation(resource.getName(),surface_list)
                print("Resource loaded: " + str(resource))
        else:
            print("Resource already loaded: " + resource.getName())
            return False
        
    def registry(self, resource: Resource):
        return self.try_load(resource)
        
    def _registry_all(self, preLoad_resourceList: ResourceList):
        for key in preLoad_resourceList.resources:
            for resource in preLoad_resourceList.resources[key]:
               self.registry(resource) 
        return self
    
    def get(self, name: str):
        if name in self.loaded_resources:
            return self.loaded_resources[name]
        print("Resource not found: " + name)
        return None
        
    def __str__(self) -> str:
        result = ""
        for key in self.loaded_resources:
            result += str(key) + ":\n"
        return result

class ResourceSystem:
    def __init__(self,preLoad_resourceList:ResourceList):
        self.preLoad_resourceList = preLoad_resourceList
        self.loaded_resourceList = GameResourcesList()._registry_all(preLoad_resourceList)

    def get_resource(self, name: str) -> Union[Image, Audio, Video]:
        return self.loaded_resourceList.get(name)

    def get_load_resource_list(self):
        return self.loaded_resourceList
    
    def get_image(self,image:Resource) -> Image:
        if image.getType() == ResourceType.Image:
            return self.get_resource(str(image))
        else:
            print("Resource is not an image: " + str(image))
            return None
        
    def get_video(self,video:Resource) -> Video:
        if video.getType() == ResourceType.Video:
            return self.get_resource(str(video))
        else:
            print("Resource is not a video: " + str(video))
            return None

    def get_audio(self,audio:Resource) -> Audio:
        if audio.getType() == ResourceType.Audio:
            return self.get_resource(str(audio))
        else:
            print("Resource is not an audio: " + str(audio))
            return None

    def __str__(self):
        return str(self.loaded_resourceList)