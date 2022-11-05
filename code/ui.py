import pygame
from setting import *

class UI:
    def __init__(self):
        
        #general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
        self.font_gameover = pygame.font.Font(UI_FONT,100)
        
        #bar setup
        self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
        #self.bar_rect = pygame.Rect(0,0,1280,60)
        
    def show_bar(self,current,max_amount,bg_rect,color):
        #draw bg
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
        
        #coverting stat to pixel
        ratio = current/max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width
        
        #drawing the bar
        #pygame.draw.rect(self.display_surface,'black',self.bar_rect)
        pygame.draw.rect(self.display_surface,color,current_rect)
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,current_rect,3)
 
    
    def display(self,player):
        self.show_bar(player.health,player.stats['health'],self.health_bar_rect,HEALTH_COLOR)
        
    def show_score(self):
        counting_time = pygame.time.get_ticks() 
        # change milliseconds into minutes, seconds, milliseconds
        counting_minutes = str(counting_time//60000).zfill(2)
        counting_seconds = str((counting_time%60000)//1000 ).zfill(2)
        self.score = str((counting_time)*25//1000)
        counting_string = "%s:%s" % (counting_minutes, counting_seconds)
        score_string = "%s" %  self.score

        counting_text = self.font.render(str("time:")+str(counting_string), 1,'white')
        score_text = self.font.render(str("score:")+str(score_string), 1,'white')
        
        counting_rect = counting_text.get_rect(center = (1200,30))
        score_rect = score_text.get_rect(center = (900,30))
        pygame.draw.rect(self.display_surface,'Black',counting_rect)
        self.display_surface.blit(counting_text, counting_rect)
        pygame.draw.rect(self.display_surface,'Black',score_rect)
        self.display_surface.blit(score_text, score_rect)
    
    def game_over_screen(self):
        text_surf =  self.font_gameover.render(str("GAME OVER"),True,'white')
        self.display_surface.blit(text_surf,(280,300))    