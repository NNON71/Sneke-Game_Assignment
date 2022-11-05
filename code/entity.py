import pygame
from math import sin

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups) :
        super().__init__(groups)
        self.dash = pygame.Vector2()
        self.direction = pygame.Vector2()
        
    def move(self,speed,dash):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * speed + dash.x
        self.conllision('horizontal')
        self.hitbox.y += self.direction.y * speed + dash.y
        self.conllision('vertical')
        self.rect.center = self.hitbox.center
    
    def conllision(self,direction):
        if direction == 'horizontal':
            for object in self.obstacles_object:
                if object.hitbox.colliderect(self.hitbox): #colliderect ทับซ้อน rect = ฟังชันclass object = ตัวแปร//เช็คว่าการคท.แนวนอนมีการทับซ้อนหรือไม่
                    if self.direction.x > 0: # moving right //direction.x = 1 press d
                        self.hitbox.right = object.hitbox.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = object.hitbox.right
                    
        if direction == 'vertical':
            for object in self.obstacles_object: 
                if object.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving up
                        self.hitbox.bottom = object.hitbox.top
                    if self.direction.y < 0: # moving down
                        self.hitbox.top = object.hitbox.bottom  
                        
    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0