from tkinter import HORIZONTAL, W
from turtle import speed
from typing import TYPE_CHECKING
import pygame
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group,obstacles_object):
        super().__init__(group)
        self.image = pygame.image.load('graphic/player/apple1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.Vector2()
        self.speed = 20
        
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
    
    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.rect.x += self.direction.x * speed
        self.conllision('horizontal')
        self.rect.y += self.direction.y * speed
        self.conllision('vertical')
        #self.rect.center += self.direction * speed
        
    def conllision(self,direction):
        if direction == 'horizontal':
            for object in self.obstacles_object:
                if object.rect.colliderect(self.rect): #colliderect ทับซ้อน rect = ฟังชันclass object = ตัวแปร//เช็คว่าการคท.แนวนอนมีการทับซ้อนหรือไม่
                    if self.direction.x > 0: # moving right //direction.x = 1 press d
                        self.rect.right = object.rect.left
                    if self.direction.x < 0: # moving left
                        self.rect.left = object.rect.right
                    
        if direction == 'vertical':
            for sprite in self.obstacles_object: 
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # moving up
                        self.rect.bottom = self.rect.top
                    if self.direction.y < 0: # moving down
                        self.rect.top = self.rect.bottom    
    def update(self):
        self.input()
        self.move(self.speed)