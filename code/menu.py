import pygame
from setting import *

class menu:
    def __init__(self) :
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
        self.font_gameover = pygame.font.Font(UI_FONT,100)
        self.font_score = pygame.font.Font(UI_FONT,60)
        
    def start(self):
        pass