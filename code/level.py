import pygame,random,copy
from setting import *
from tile import Tile
from player import Player
from apple import Apple
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
        self.trail_group = pygame.sprite.Group()
        self.snake_trail_group = pygame.sprite.Group()
        
        #attack
        self.current_attack = None 
        self.attack_sprites = pygame.sprite.Group()
        self.attackale_sprites = pygame.sprite.Group()
        
        #object setup
        self.create_map()
                
        #user interface
        self.ui = UI()
        self.count =0
        
        #self.apple.score = self.ui.score_calculate
        
        self.gameover = pygame.font.SysFont(UI_FONT,100)
        
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP): #นับแถวเก็บไว้ในrow_index
            for col_index,col in enumerate(row): 
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_object,self.obstacles_object])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_object],self.obstacles_object,self.trail_group,5)
                    self.apple = Apple((random.uniform(3,16)*64,random.uniform(3,10)*64),[self.visible_object],self.obstacles_object,0)
                if col == 's':
                    self.snake = Enemy('snake_head',(x,y),[self.visible_object,self.attackale_sprites],self.obstacles_object,self.damage_player,self.damage_apple,self.snake_trail_group)
                # if col == 'sb':
                #     self.snake_body = Enemy('snake_body',(x,y),[self.visible_object,self.attackale_sprites],self.obstacles_object,self.damage_player,self.damage_apple)   
                
                
    # def create_attack(self):
    #     self.
        
    def run(self):
        #self.create_apple.draw_apple()
        self.visible_object.custom_draw(self.player)
        self.trail_group.update()
        self.snake_trail_group.update()
        self.ui.display(self.player)
        if self.paused or self.player.game_over_stats :
            #print(self.ui.score)
            self.display_surface.fill('black')
            self.ui.game_over_screen()
        else:
            self.visible_object.enemy_update(self.player,self.apple)
            #self.visible_object.enemybody_update(self.snake)
            self.get_apple()
            self.visible_object.update()
            self.ui.show_score(self.apple.score)
            self.player.death_check()
            self.collison_tail()
            
        #debug(self.player.direction)
        #debug(self.snake.rect)
        #debug(self.player.dash)
    
    def damage_player(self,amount):
        self.player.kill()
        if self.player.vulnerable:
            self.player.health -= amount
            self.player = Player((random.uniform(3,16)*64,random.uniform(3,8)*64),[self.visible_object],self.obstacles_object,self.trail_group,self.player.health)
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
                      
    def collison_tail(self):
        for tail in self.snake_trail_group:
            if tail.rect.colliderect(self.player.rect):
                self.player.vulnerable = True
                self.damage_player(1)
    
    def damage_apple(self,amount):
        self.count += 1
        print(self.count)
        self.snake.eatapple = True
        if self.snake.long < 0.2 :
            self.snake.long = 0.1
        else :
            self.snake.long -= 0.05
        self.snake.snake_range += 100
        self.snake.cdapple = pygame.time.get_ticks()
        self.apple.health  -= amount
        self.apple.apple_check()
        if self.snake.speed < 6:
            self.snake.speed += 0.1
        elif self.snake.speed > 6:
            self.snake.speed = 6
        self.apple = Apple((random.uniform(3,17)*64,random.uniform(3,10)*64),[self.visible_object],self.obstacles_object,self.apple.score) 

    def get_apple(self):
        if self.player.rect.colliderect(self.apple):
            self.apple.kill()
            self.get_player_point()
        
    def get_player_point(self):
        self.apple.score  += 150
        #self.snake.speed -= 0.1
        if self.player.health >= 5:
            self.player.health += 0
        else :
            self.player.health += 1
        # self.player.dash.x += 1
        # self.player.dash.y += 1
        #self.player.speed += 0.1
        #print(self.apple.score)
        #print(type(self.ui.score_calculate))
        self.apple = Apple((random.uniform(3,17)*64,random.uniform(3,10)*64),[self.visible_object],self.obstacles_object,self.apple.score) 
    
    def game_pause(self):
        self.paused = not self.paused
           
         
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
        if target.rect.bottom > self.camera_rect.bottom and self.camera_rect.bottom <= 550:
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
        
    def enemy_update(self,player,apple):
        enemy_sprite = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprite:
            enemy.enemy_update(player,apple)

    
    # def enemybody_update(self,snake):
    #     enemy_sprite = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
    #     for enemy in enemy_sprite:
    #         enemy.enemybody_update(snake)