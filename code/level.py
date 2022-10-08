import pygame
from setting import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):
        
        #get the display surface
        self.display_surface = pygame.display.get_surface()
        
        #object
        self.visible_object = pygame.sprite.Group()
        self.obstacles_object = pygame.sprite.Group()
        
        #object setup
        self.create_map()
        
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index,col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_object,self.obstacles_object])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_object],self.obstacles_object)
        
    def run(self):
        self.visible_object.draw(self.display_surface)
        self.visible_object.update()
        debug(self.player.direction)