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
        self.visible_object = YsortcameraGroup()
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
        self.visible_object.custom_draw(self.player)
        self.visible_object.update()
        #debug(self.player.direction)
        debug(self.player.rect)
        #debug(self.player.dash)
        
class YsortcameraGroup(pygame.sprite.Group):
    def __init__(self) :
        
        #Generel setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2 
        self.half_height = self.display_surface.get_size()[1] // 2 
        self.offset = pygame.math.Vector2()

    def custom_draw(self,player):
        
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
  
    
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft-self.offset
            self.display_surface.blit(sprite.image,offset_pos)