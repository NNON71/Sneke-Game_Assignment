import pygame,random
from debug import debug
from setting import *
from entity import Entity

class Enemy(Entity):
    def __init__(self,monster_name,pos,groups,obstacles_object,damage_player):

        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'
        
        #graphic setup
        # self.import_grapgics(monster_name)
        self.image = pygame.image.load('graphic/snake.png').convert_alpha()
        self.status = 'idle'
        
        #move
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,0)
        self.obstacles_object = obstacles_object
        
        #stats
        self.monster_name = monster_name
        monster_info = enemy_data[self.monster_name]
        self.health = monster_info['health']
        self.damage = monster_info['damage']
        self.speed = monster_info['speed']
        self.attack_type = monster_info['attack_type']
        self.attack_player = monster_info['attack_player']
        self.attack_apple = monster_info['attack_apple']
        self.notice_radius = monster_info['notice_radius']    
        
        #player interact
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 500
        self.damage_player = damage_player
        
        #invicibility timer
        self.vulnerable = True
        self.hit_time = None
        self.invicibility_duration = 300
        
    # def import_grachic(self,name):
    #     self.animation =
    
    def get_player_distance_direction(self,player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        y_diff = player_vec[1]-enemy_vec[1]
        x_diff = player_vec[0]-enemy_vec[0]
        direction = pygame.math.Vector2()
        
        if distance > 0:
            #direction = (player_vec - enemy_vec).normalize() #ทำเป็นเวกเตอร์หนึ่งหน่วย ทีทิศทาง
            if y_diff == -1 or y_diff == 2 or y_diff == 1 or y_diff == -2 or y_diff == 0:
                if x_diff <= 0 :
                    direction.x = -1
                elif x_diff >= 0 :
                    direction.x = 1
            else:
                if y_diff < 0 and y_diff != -1 and y_diff != 2 and y_diff != 1 and y_diff != -2:
                    direction.y = -1
                elif y_diff > 0 and y_diff != -1 and y_diff != 2 and y_diff != 1 and y_diff != -2:
                    direction.y = 1
                elif y_diff == -1 or y_diff == 2 or y_diff == 1 or y_diff == -2 or y_diff == 0:
                    direction.y = 0
        
        else:
            direction = pygame.math.Vector2()

        return (distance,direction)
    
    def get_status(self,player):
        distance = self.get_player_distance_direction(player)[0]
        
        if distance <= self.attack_player and self.can_attack:
            self.status = 'attack_player'
       
        elif distance <= self.notice_radius:
            self.status = 'move'
        else :
            self.status = 'idle'
    
    def actions(self,player):
        if self.status == 'attack_player':
            #print('attack')
            player.kill()
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.damage,self.attack_type)
            self.can_attack = False
            
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()
    
    def cooldown(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True 
       
    def update(self):
        # self.input()
        self.move(self.speed,self.dash)
        self.cooldown()


    def enemy_update(self,player):
        self.get_status(player)
        self.actions(player)