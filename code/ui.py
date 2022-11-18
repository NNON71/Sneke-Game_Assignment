import pygame
from setting import *
from menu import Menu  

class UI:
    def __init__(self):
        
        self.menu = Menu()
        #general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
        self.font_Name = pygame.font.Font(UI_FONT,100)
        self.font_score = pygame.font.Font(UI_FONT,50)
        self.score_text_font = pygame.font.Font(UI_FONT,70)
        
        #bar setup
        self.health_bar_rect = pygame.Rect(100,20,HEALTH_BAR_WIDTH,BAR_HEIGHT)
        self.bar_rect = pygame.Rect(0,0,1280,60)
        
    def show_bar(self,current,max_amount,bg_rect,color):
        #draw bg
        pygame.draw.rect(self.display_surface,'black',self.bar_rect)
        pygame.draw.rect(self.display_surface,'white',bg_rect)
        pygame.draw.rect(self.display_surface,'black',bg_rect,3)
        
        #coverting stat to pixel
        ratio = current/max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width
        
        #drawing the bar
        pygame.draw.rect(self.display_surface,color,current_rect)
        pygame.draw.rect(self.display_surface,'black',current_rect,3)
 
    
    def display(self,player):
        self.show_bar(player.health,player.stats['health'],self.health_bar_rect,HEALTH_COLOR)
        
    
    def show_score(self,apple_score,time,pause,con):
        self.stamee = time
        self.pause_time = pause
        self.con_time = con
        self.run_time = pygame.time.get_ticks()
        self.menu.consolebutton(self.menu.menustats)
        #print(self.menu.stamp)
        if self.con_time >= self.pause_time and self.menu.menustats == "start":
            self.counting_time = self.run_time-self.stamee-(self.con_time-self.pause_time)
        if self.counting_time < 0:
            self.counting_time = 0
        #print(str("UI ")+str(self.run_time)+str(" menu ")+str(self.stamee)+str(" menu continue ")+str(self.con_time)+str(" menu pause ")+str(self.pause_time)+str(" count ")+str(self.counting_time))
        self.score_calculate =  (self.counting_time*25//10000)+apple_score
        self.second_count = (self.counting_time%60000)//1000
        self.minute_count = self.counting_time//60000
        # change milliseconds into minutes, seconds, milliseconds
        counting_minutes = str(self.minute_count).zfill(2)
        counting_seconds = str(self.second_count).zfill(2)
        self.score = str(self.score_calculate)
        counting_string= "%s:%s" % (counting_minutes, counting_seconds)
        score_string = "%s" %  self.score

        counting_text = self.font.render(str("time:")+str(counting_string), 1,'white')
        score_text = self.font.render(str("score:")+str(score_string), 1,'white')
        
        counting_rect = counting_text.get_rect(center = (1180,30))
        score_rect = score_text.get_rect(center = (900,30))
        pygame.draw.rect(self.display_surface,'Black',counting_rect)
        self.display_surface.blit(counting_text, counting_rect)
        pygame.draw.rect(self.display_surface,'Black',score_rect)
        self.display_surface.blit(score_text, score_rect)
    
    def main_screen(self):
        Sneke_text = self.font_Name.render(str("Sneke"),True,'white')
        self.display_surface.blit(Sneke_text,(440,80))    
        
    def score_screen(self):
        with open("data.txt","r") as f :
            data = f.readlines()
            name = []
            score = []
            num = 0
            a = ''
            b = ''
            for line in data:
                a = ''
                b = ''
                num += 1
                for i in line:
                    if i.isalpha() == True:
                        a +=  i
                    if i.isdigit() == True:
                        b += i
                name.append(a)
                score.append(b)
                # print(name)
                # print(score)
            f.close()
        x = 260
        score_font = pygame.font.Font(UI_FONT,60)
        score_text = score_font.render(str("Score board"),True,'white')
        self.display_surface.blit(score_text,(380,40))
        sub_font = pygame.font.Font(UI_FONT,30)
        bg_score = pygame.Rect(260,160,760,480)
        pygame.draw.rect(self.display_surface,'black',bg_score)
        name_word = sub_font.render(str("NAME"),True,'red')
        score_word = sub_font.render(str("score"),True,'red')
        self.display_surface.blit(name_word,(370,180))
        self.display_surface.blit(score_word,(790,180))
        if num > 5:
            num = 5
        for i in range(0,num,1):
            name_text  = sub_font.render(str(name[i]),True,'white')
            name_rect = name_text.get_rect(center = (420,x))
            self.display_surface.blit(name_text,name_rect)
            scorep_text = sub_font.render(str(score[i]),True,'white')
            scorep_rect = scorep_text.get_rect(center = (850,x))
            self.display_surface.blit(scorep_text,scorep_rect)
            x += 80
            
    def pause_screen(self):
        pause_font = pygame.font.Font(UI_FONT,60)
        pasue_text = pause_font.render(str("PAUSE"),True,'red')
        pause_rect = pasue_text.get_rect(center = (640,360))
        #pygame.draw.rect(self.display_surface,'white',pause_rect)
        self.display_surface.blit(pasue_text,pause_rect)
    
    def game_over_screen(self):
        score_surd = self.score_text_font.render(str("SCORE"),True,'white')
        self.display_surface.blit(score_surd,(500,60))
        score_cal_sur = self.font_score.render(str(self.score_calculate),True,'white')
        if self.score_calculate < 10 : 
            self.display_surface.blit(score_cal_sur,(620,210))
        if self.score_calculate < 100 and self.score_calculate >= 10 : 
            self.display_surface.blit(score_cal_sur,(600,210))
        if self.score_calculate < 1000 and self.score_calculate >= 100: 
            self.display_surface.blit(score_cal_sur,(580,210))
        if self.score_calculate < 10000 and self.score_calculate >= 1000: 
            self.display_surface.blit(score_cal_sur,(560,210))
        if self.score_calculate < 100000 and self.score_calculate >= 10000: 
            self.display_surface.blit(score_cal_sur,(540,210))
        