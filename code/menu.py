import pygame
from setting import *
from button import Button

class Menu:
    def __init__(self) :
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,40)
         #button 
        self.stat_img = pygame.image.load('graphic/button/buttone.png').convert_alpha()
        self.scoreboard_img = pygame.image.load("graphic/button/buttone.png").convert_alpha()
        #self.continute_img = pygame.image.load("graphic/button/start_button.png").convert_alpha()
        self.quit_img = pygame.image.load("graphic/button/buttone.png").convert_alpha()
        self.back_img = pygame.image.load('graphic/button/buttone.png').convert_alpha()
               
        self.menustats = "main"
        
        self.stamp = None
        self.pause_time = 0
        self.continute_time = 0
                        
    def consolebutton(self,menustatus):
        self.start_button = Button(130,310, self.stat_img, 0.80,0.25)
        self.scoreboard_button = Button(130,455,self.scoreboard_img,1.5,0.25)
        self.quit_button = Button(130, 600, self.quit_img,0.68,0.25)
        self.back_button = Button(560, 675, self.back_img, 0.7,0.25)
        
        self.menustats = menustatus
        
        if self.menustats == "main" : #recever
            if self.start_button.draw(self.display_surface) : #sender
                self.stamp = pygame.time.get_ticks()
                #print(str("---------")+str(self.stamp))
                self.menustats = "start"
                
            if self.scoreboard_button.draw(self.display_surface):
                self.menustats = "scoreboard" 
                
            if self.quit_button.draw(self.display_surface):
                self.menustats = "quit"
            start_text = self.font.render("START",True,'white')
            self.display_surface.blit(start_text,(150,310)) 
            score_text = self.font.render("SCOREBOARD",True,'white')
            self.display_surface.blit(score_text,(150,460))   
            exit_text = self.font.render("EXIT",True,'white')
            self.display_surface.blit(exit_text,(150,600))   

        if self.menustats == "scoreboard":
            if self.back_button.draw(self.display_surface):
                self.menustats = "main"
            back_text = self.font.render("BACK",True,'white')
            self.display_surface.blit(back_text,(580,680))   
        
        # if self.menustats == "pause":
        #     # self.pause_time = pygame.time.get_ticks()
        #     if self.continute_button.draw(self.display_surface):
        #         self.menustats = "continue"
                        
        # if self.menustats == "continue":
        #     self.continute_time = pygame.time.get_ticks()
                
        #     if self.quit_button.draw(self.display_surface):
        #         self.menustats = "main"
    
