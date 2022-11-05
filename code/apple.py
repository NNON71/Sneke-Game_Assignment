from this import d
import pygame,random
from setting import *

class Apple:
    def __init__(self,item_name,pos,stats):
        self.image = pygame.image.load('graphic/item.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        
        #item setting
        self.item_name = item_name
        item_info = item_data[self.item_name]
        self.health = item_info['health']
        self.check = stats
        
    
    def draw_apple(self):
        if self.check == True:
            pygame.rect.Rect()
        