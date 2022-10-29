import pygame
from entity import Entity
from setting import *
from entity import Entity

class Player(Entity):
    def __init__(self,pos,group,obstacles_object):
        super().__init__(group)
        self.image = pygame.image.load('graphic/player/testad.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(0,0)
        
        self.speed = 10
        
        self.dashing = False
        self.dash_time = None
        self.dash_cooldown = 1000
         
        self.obstacles_object = obstacles_object
                
    def input(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_w]:
            self.direction.y = -1
        elif key[pygame.K_s]:
            self.direction.y = 1
        else :
            self.direction.y = 0 
        
        if key[pygame.K_a]:
            self.direction.x = -1
        elif key[pygame.K_d]:
            self.direction.x = 1
        else :
            self.direction.x = 0 
        
        if key[pygame.K_SPACE] and self.dashing == False:
            
            self.dashing = True
            self.dash_time = pygame.time.get_ticks()
            
            if self.direction.x == -1 and self.hitbox.x > 80:
                self.dash.x = -100
            elif self.direction.x == 1 and self.hitbox.x < 1170 :
                self.dash.x = 100

                         
            if self.direction.y == -1 and self.hitbox.y > 80:
                self.dash.y = -100
            elif self.direction.y == 1 and self.hitbox.y < 1170:
                self.dash.y = 100

        else :
                self.dash.y = 0 
                self.dash.x = 0 
                            
    def cooldown(self):
        current_time = pygame.time.get_ticks()

        if self.dashing == True:
            if current_time - self.dash_time >= self.dash_cooldown:
                self.dashing = False
                         
    def update(self):
        self.input()
        self.cooldown()
        self.move(self.speed,self.dash)