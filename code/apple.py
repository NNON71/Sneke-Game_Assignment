import pygame,random
from setting import *

class Apple(pygame.sprite.Sprite):
    def __init__(self,pos,group,obstacles_object,score):
        super().__init__(group)
        
        self.image = pygame.image.load('graphic/realappleaa.png').convert_alpha()
        self.display_surface = pygame.display.get_surface()
        self.rect = self.image.get_rect(center = pos)
        self.obstacles_object = obstacles_object
        
        self.stats = {'health':5}
        self.health = self.stats['health']
        
        self.score = score
    
    def apple_check(self):
        if self.health <= 0:
            print('apple death')
            

        
    

        