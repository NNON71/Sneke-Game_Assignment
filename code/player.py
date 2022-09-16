from tkinter import W
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
            
        self.rect.center += self.direction * speed
        
    def conllision(self,direction):
        
    
    def update(self):
        self.input()
        self.move(self.speed)