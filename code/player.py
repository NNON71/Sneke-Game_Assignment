import pygame
from entity import Entity
from menu import Menu
from particle import Trail
from support import import_folder
from setting import *

class Player(Entity):
    def __init__(self,pos,group,obstacles_object,trail_group,HP):
        super().__init__(group)
        
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,100)
        
        self.image = pygame.image.load('graphic/player/now.png').convert_alpha()
        #self.rect = self.image.fill('black')
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(0,0)
        
        self.menu = Menu()
        
        self.dashing = False
        self.dash_time = None
        self.dash_cooldown = 1000
        
        self.game_over_stats = False
         
        self.obstacles_object = obstacles_object
        self.trail_group = trail_group
        
        #graphic setting
        self.import_player_assert() 
        self.status = 'right'
        self.frame_index = 0
        self.animation_speed = 0.15
        
        #stats
        self.stats = {'health':5,'speed':5}
        self.health = HP#self.stats['health']
        self.speed = self.stats['speed']
        
        #damage timer
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration =  500
        
        #import sound
        self.dash_sound = pygame.mixer.Sound('audio/dash.wav')
        self.dash_sound.set_volume(0.4)
        
    def import_player_assert(self):
        character_path = 'graphic/player/'
        self.animations = {'left':[],'left_idle':[],'right':[],'right_idle':[]}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
       # print(self.animations)          
            
    def input(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_w]:
            if self.status == 'left_idle':
                self.status = 'left'
            elif self.status == 'right_idle':
                self.status = 'right'              
            self.direction.y = -1
            
        elif key[pygame.K_s]:
            if self.status == 'left_idle':
                self.status = 'left'
            elif self.status == 'right_idle':
                self.status = 'right'
            self.direction.y = 1
        else :
            self.direction.y = 0 
        
        if key[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
            
        elif key[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
        else :
            self.direction.x = 0 
        
        if key[pygame.K_SPACE] and self.dashing == False:
            self.dash_sound.play()
            if self.health > 1 :
                self.health -= 1
            else:
                self.health == 1
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
    
    def get_status(self):
        #print(self.status)
        #idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status:
                self.status = self.status + '_idle'
                           
    def cooldown(self):
        current_time = pygame.time.get_ticks()

        if self.dashing == True:
            t =Trail(self.rect.center,(255,0,0))
            self.trail_group.add(t)
            if current_time - self.dash_time >= self.dash_cooldown:
                self.dashing = False
                
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True
        else :
            self.image.set_alpha(255)
                
    def death_check(self):
        if self.health <= 0:
            #self.menu.consolebutton()
            self.game_over_stats = True
            #self.menu.menustats = "over"
              
    def animate(self):
        animation = self.animations[self.status]      
        
        #loop over the frame
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0      

        #set image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
        
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)
            
    def update(self):
        self.input()
        self.death_check()
        self.get_status()
        self.animate()
        self.cooldown()
        self.move(self.speed,self.dash)