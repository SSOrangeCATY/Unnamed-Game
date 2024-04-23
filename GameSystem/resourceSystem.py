from enum import Enum
import os
from typing import Union
from moviepy.editor import VideoFileClip
import pygame as GAME
from GameSystem.base.audio import Audio
from config import GAME_DIR
from GameSystem.base.video import Video
from GameSystem.base.image import Image

class ResourceType(Enum):
    Image = "image"
    Audio = "audio"
    Video = "video"
    Screen = "screen"

class Resource:
    def __init__(self,type:ResourceType,name:str,loaction:str=None):
        self.type = type
        self.name = name
        self.location = loaction
    def getType(self) -> ResourceType:
        return self.type
    def getName(self) -> str:
        return self.name
    def getLocation(self) -> str:
        return self.location
    def register(self,resource_list: 'ResourceList'):
        resource_list.add(self)
        return self
    def __str__(self):
        return self.type.value + ":" + self.name

class ResourceList:
    def __init__(self):
        self.resources = {}

    def add(self, resource: Resource):
        key = resource.getType()
        if key not in self.resources:
            self.resources[key] = []
        for r in self.resources[key]:
            if r.getName() == resource.getName():
                print("Resource already exists: " + key + ":" + resource.getName())
                return
        self.resources[key].append(resource)

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
            result += key + ":\n"
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
                        self.loaded_resources[str(resource)] = Image(GAME.image.load(os.path.join(GAME_DIR, 'Rescouces',resource.type.value, resource.getName())))
                    return True
                except Exception as e:
                    print("Error loading image:", e)
                    return False
            elif resource.getType() == ResourceType.Audio:
                try:
                    if resource.getLocation() is not None:
                        self.loaded_resources[str(resource)] = Audio(GAME.mixer.Sound(resource.getLocation()),resource.getLocation())
                    else:
                        path = os.path.join(GAME_DIR, 'Rescouces',resource.type.value, resource.getName())
                        self.loaded_resources[str(resource)] = Audio(GAME.mixer.Sound(path),path)
                    return True
                except Exception as e:
                    print("Error loading audio:", e)
                    return False
            elif resource.getType() == ResourceType.Video: 
                try:
                    if resource.getLocation() is not None:
                        self.loaded_resources[str(resource)] = Video(VideoFileClip(resource.getLocation()))
                    else:
                        self.loaded_resources[str(resource)] = Video(VideoFileClip(os.path.join(GAME_DIR, 'Rescouces',resource.type.value, resource.getName())))
                    return True
                except Exception as e:
                    print("Error loading video:", e)
                    return False
            elif resource.getType() == ResourceType.Screen:
                print("Screen resource not supported: " + resource.getName())
                return False
        else:
            print("Resource already loaded: " + resource.getName())
            return False
        
    def registry(self, resource: Resource):
        return self.try_load(resource)
        
    def _registry_all(self, resourceList: ResourceList):
        for key in resourceList.resources:
            for resource in resourceList.resources[key]:
                if self.registry(resource) is True:
                    #删除已经加载的资源
                    resourceList.resources[key].remove(resource)
        return resourceList
    
    def get(self, name: str):
        if name in self.loaded_resources:
            return self.loaded_resources[name]
        print("Resource not found: " + name)
        return None
        
    def __str__(self) -> str:
        result = ""
        for key in self.loaded_resources:
            result += key + ":\n"
        return result

class ResourceSystem:
    def __init__(self,preLoad_resourceList:ResourceList=ResourceList()):
        self.preLoad_resourceList = preLoad_resourceList
        self.failLoad_resourceList = None
        self.loaded_resourceList = GameResourcesList()

    def get_resource(self, name: str) -> Union[GAME.Surface, GAME.mixer.Sound, VideoFileClip]:
        return self.loaded_resourceList.get(name)

    def _load_resource(self):
        self.failLoad_resourceList = self.loaded_resourceList._registry_all(self.preLoad_resourceList)
        return self

    def get_load_resource_list(self):
        return self.loaded_resourceList

    def get_fail_load_resource_list(self):
        return self.failLoad_resourceList
    
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