import pygame,random
from setting import *
from tile import Tile
from player import Player
#from apple import Apple
from debug import debug
from enemy import Enemy
from ui import UI

class Level:
    def __init__(self):
        
        self.paused = False
        #get the display surface
        self.display_surface = pygame.display.get_surface()
        #self.randomize()
        
        #object
        self.visible_object = YsortcameraGroup()
        self.obstacles_object = pygame.sprite.Group()
        
        #attack
        self.current_attack = None 
        self.attack_sprites = pygame.sprite.Group()
        self.attackale_sprites = pygame.sprite.Group()
        
        #object setup
        self.create_map()
        
        #user interface
        self.ui = UI()
        
        self.gameover = pygame.font.SysFont(UI_FONT,100)
        
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
                        self.player = Player((x,y),[self.visible_object],self.obstacles_object,5)
                if col == 's':
                    Enemy('snake_head',(x,y),[self.visible_object,self.attackale_sprites],self.obstacles_object,self.damage_player)
                
    # def create_attack(self):
    #     self.
        
    def run(self):
        #self.create_apple.draw_apple()
        self.visible_object.custom_draw(self.player)
        self.ui.display(self.player)
        if self.paused or self.player.game_over_stats :
            print(self.ui.score)
            #self.img = self.font.render("Game Over",True,'Black')
            #self.text_gameover = self.font.render("GAME OVER",1,'white')
            self.display_surface.fill('black')
            self.ui.game_over_screen()
            #self.display_surface.blit(self.img,(500,500))
            #self.display_surface.blit(self.text_gameover,(280,300))
        else:
            self.visible_object.enemy_update(self.player)
            self.visible_object.update()
            self.ui.show_score()
            self.player.death_check()
        #debug(self.player.direction)
        #debug(self.player.rect,10,10)
        #debug(self.player.dash)
    
    def damage_player(self,amount,attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player = Player((random.uniform(3,15)*64,random.uniform(3,15)*64),[self.visible_object],self.obstacles_object,self.player.health)
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
           
                    
    def game_pause(self):
        self.paused = not self.paused
       
     
            
    # def randomize(self):
    #     self.apple.x = random.randint(96,1184)
    #     self.apple.y = random.randint(96,624)
    #     Apple('apple',(self.apple.x,self.apple.y),True)
    
# class Apple:
# 	def __init__(self):
# 		self.randomize()
  
# 	def draw_apple(self):
# 		fruit_rect = pygame.Rect(int(self.pos.x * TILESIZE),int(self.pos.y * TILESIZE),32,32)
# 		pygame.draw.rect(pygame.display.get_surface(),'red',fruit_rect)
# 		#pygame.draw.rect(screen,(126,166,114),fruit_rect)

# 	def randomize(self):
# 		self.x = random.randint(4,12)
# 		self.y = random.randint(4,12)
# 		self.pos = pygame.math.Vector2(self.x,self.y)
        
        
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