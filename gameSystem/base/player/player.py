from typing import Any
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,texture:pygame.Surface,group):
        super().__init__(group)
        self.texture = texture if texture is not None else pygame.Surface(32,64) and self.texture.fill((255,255,255))
        self.image = self.texture
        self.rect = self.texture.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.speed = 200
        self.pos =  pygame.math.Vector2(self.rect.center)
        
        self.select_item = None
        
    def input(self) -> None:
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w] and keys[pygame.K_s]:
            self.direction.y = 0
        elif keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pygame.K_a] and keys[pygame.K_d]:
            self.direction.x = 0
        elif keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        
    def move(self, dt) -> None:
        # normalize the vector
        if self.direction.magnitude() > 0:
           self.direction = self.direction.normalize()
        
        # horizontal and vertical movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
        
    def update(self, dt) -> None:
        self.input()
        self.move(dt)