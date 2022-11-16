import pygame,sys
from setting import *
from level import Level


class Game:
    def __init__(self):
        
        #general setup
        pygame.init()
        self.font = pygame.font.SysFont(UI_FONT, 40)
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Sneke')
        self.clock = pygame.time.Clock()
        
        self.level = Level()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.level.out == True:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and (self.level.statusmenu == "start" or self.level.statusmenu == "pause"):
                        self.level.game_pause()
  
            self.screen.fill('white')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
    