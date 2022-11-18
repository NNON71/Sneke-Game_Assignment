import pygame,random
from debug import debug
from particle import SnakeTail
from setting import *
from entity import Entity

class Enemy(Entity):
    def __init__(self,monster_name,pos,groups,obstacles_object,damage_player,damage_apple,tail_group):

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
        self.attack_player = monster_info['attack_player']
        self.attack_apple = monster_info['attack_apple']
        self.notice_radius = monster_info['notice_radius']    
        self.apple_radius = monster_info['apple_radius']
        
        #player interact
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 500
        self.damage_player = damage_player
        self.damage_apple = damage_apple
        
        #invicibility timer
        self.vulnerable = True
        self.hit_time = None
        self.invicibility_duration = 300
        #snake eatapple
        self.snake_trail_group = tail_group
        self.long = 2
        self.eatapple = False
        self.cdapple = None
        self.snake_range = 200
        
    # def import_grachic(self,name):
    #     self.animation =
    
    def get_player_distance_direction(self,player,apple):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        apple_vec = pygame.math.Vector2(apple.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        distance_apple = (apple_vec-enemy_vec).magnitude()
        y_diff = player_vec[1]-enemy_vec[1]
        x_diff = player_vec[0]-enemy_vec[0]
        direction = pygame.math.Vector2()

        #print(str("x ")+str(x_diff)+str(" y ")+str(y_diff))
        
        if distance > 0:
            #direction = (player_vec - enemy_vec).normalize() #ทำเป็นเวกเตอร์หนึ่งหน่วย ทีทิศทาง
            if y_diff == -1 or y_diff == 2 or y_diff == 1 or y_diff == -2 or y_diff == 0 or y_diff == -3 or y_diff == 3:
                if x_diff <= 0 :
                    direction.x = -1
                elif x_diff >= 0 :
                    direction.x = 1
            else:
                if y_diff < 0 and y_diff != -1 and y_diff != 2 and y_diff != 1 and y_diff != -2 and y_diff != -3 and y_diff != 3:
                    direction.y = -1
                elif y_diff > 0 and y_diff != -1 and y_diff != 2 and y_diff != 1 and y_diff != -2 and y_diff != -3 and y_diff != 3:
                    direction.y = 1
                elif y_diff == -1 or y_diff == 2 or y_diff == 1 or y_diff == -2 or y_diff == 0 or y_diff == -3 or y_diff == 3:
                    direction.y = 0
        
        if distance_apple > 0:
            direction_apple = (apple_vec-enemy_vec).normalize()
        
        # else:
        #     direction = pygame.math.Vector2()

        return (distance,direction,distance_apple,direction_apple)
    
    def get_status(self,player,apple):
        distance = self.get_player_distance_direction(player,apple)[0]
        distance_apple = self.get_player_distance_direction(player,apple)[2]
        
        if distance <= self.attack_player and self.can_attack:
            self.status = 'attack_player'
            
        elif distance_apple <= self.attack_apple :
            self.status = 'attack_apple'
       
        elif distance < distance_apple :#distance <= self.notice_radius and  distance_apple <= distance:
            self.status = 'move'
            
        elif distance > distance_apple :#distance_apple <= self.apple_radius :
            self.status = 'move_to_apple'    
        else :
            self.status = 'move_to_apple'
        
    def actions(self,player,apple):
        if self.status == 'attack_player' :
            #print('attack')
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.damage)
            self.can_attack = False
        
        elif self.status == 'attack_apple':
            #print('attack apple')
            apple.kill()
            self.damage_apple(self.damage)
            
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player,apple)[1]
            
        elif self.status == 'move_to_apple':
            self.direction = self.get_player_distance_direction(player,apple)[3]
            
        else:
            self.direction = pygame.math.Vector2()
    
    def cooldown(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True
        if self.eatapple == True:
            if self.long < 0:
                self.long = 0.1
            t =SnakeTail(self.rect.center,self.long)
            self.snake_trail_group.add(t)
            current_time = pygame.time.get_ticks()
            if current_time - self.cdapple >= self.snake_range:
                self.can_attack = True
       
    def update(self):
        # self.input()
        self.move(self.speed,self.dash)
        self.cooldown()
        #print(self.status)
         
    def enemy_update(self,player,apple):
        self.get_status(player,apple)
        self.actions(player,apple)
        
