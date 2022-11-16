import pygame
from setting import *
from button import Button

class Menu:
    def __init__(self) :
        self.display_surface = pygame.display.get_surface()
         #button 
        self.stat_img = pygame.image.load('graphic/Button.png').convert_alpha()
        self.scoreboard_img = pygame.image.load("graphic/Button.png").convert_alpha()
        self.continute_img = pygame.image.load("graphic/Button.png").convert_alpha()
        self.quit_img = pygame.image.load("graphic/Button.png").convert_alpha()
        self.back_img = pygame.image.load('graphic/Button.png').convert_alpha()
               
        self.menustats = "main"
        
        self.stamp = None
        self.pause_time = 0
        self.continute_time = 0
                        
    def consolebutton(self,menustatus):
        self.start_button = Button(600, 250, self.stat_img, 0.25,0.25)
        self.scoreboard_button = Button(600,400,self.scoreboard_img,0.25,0.25)
        self.continute_button = Button(700,400,self.continute_img,0.25,0.25)
        self.quit_button = Button(600, 550, self.quit_img,0.25,0.25)
        self.back_button = Button(1000, 600, self.back_img, 0.25,0.25)
        
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

        if self.menustats == "scoreboard":
            if self.back_button.draw(self.display_surface):
                self.menustats = "main"
        
        # if self.menustats == "pause":
        #     # self.pause_time = pygame.time.get_ticks()
        #     if self.continute_button.draw(self.display_surface):
        #         self.menustats = "continue"
                        
        # if self.menustats == "continue":
        #     self.continute_time = pygame.time.get_ticks()
                
        if self.menustats == "over" :
            #self.menustats = "over"
            if self.back_button.draw(self.display_surface):
                 self.menustats = "main"
        
        #     if self.quit_button.draw(self.display_surface):
        #         self.menustats = "main"
    
