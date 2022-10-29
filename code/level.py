import pygame
from setting import *
from tile import Tile
from player import Player
from debug import debug
from enemy import Enemy

class Level:
    def __init__(self):
        
        #get the display surface
        self.display_surface = pygame.display.get_surface()
        
        #object
        self.visible_object = YsortcameraGroup()
        self.obstacles_object = pygame.sprite.Group()
        
        #object setup
        self.create_map()
        
        #spawn apple
        #self.create_apple = Apple() 
        
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP): #นับแถวเก็บไว้ในrow_index
            for col_index,col in enumerate(row): 
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_object,self.obstacles_object])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_object],self.obstacles_object)
                if col == 's':
                    Enemy('snake_head',(x,y),[self.visible_object],self.obstacles_object)
                
        
    def run(self):
        #self.create_apple.draw_apple()
        self.visible_object.custom_draw(self.player)
        self.visible_object.update()
        self.visible_object.enemy_update(self.player)
    
        #debug(self.player.direction)
        #debug(self.player.rect,10,10)
        #debug(self.player.dash)
        
# class Apple:
    
# 	def __init__(self):
# 		self.randomize()

# 	def draw_apple(self):
# 		fruit_rect = pygame.Rect(int(self.pos.x * TILESIZE),int(self.pos.y * TILESIZE),32,32)
# 		pygame.draw.rect(pygame.display.set_mode((WIDTH,HEIGTH)),(126,166,114),fruit_rect)
# 		#pygame.draw.rect(screen,(126,166,114),fruit_rect)

# 	def randomize(self):
# 		self.x = random.randint(1,16)
# 		self.y = random.randint(1,16)
# 		self.pos = Vector2(self.x,self.y)
        
class YsortcameraGroup(pygame.sprite.Group):
    def __init__(self) :
        
        #Generel setup//camera offset
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        
        self.offset = pygame.math.Vector2()
        self.half_width  = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        
        #box setup
        self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surface.get_size()[0]  - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surface.get_size()[1]  - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l,t,w,h)


    def box_target_camera(self,target):

        if target.rect.left < self.camera_rect.left and self.camera_rect.left >= 300:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right and self.camera_rect.right <= 900:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top and self.camera_rect.top >= 120:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom and self.camera_rect.bottom <= 1150:
            self.camera_rect.bottom = target.rect.bottom
    
        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']
            
        
    def custom_draw(self,player):
        
        self.box_target_camera(player)
        
        #self.offset.x = player.rect.centerx - self.half_width
        #self.offset.y = player.rect.centery - self.half_height
  
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
            
        #pygame.draw.rect(self.display_surface,'red',self.camera_rect,5)
        
    def enemy_update(self,player):
        enemy_sprite = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprite:
            enemy.enemy_update(player)