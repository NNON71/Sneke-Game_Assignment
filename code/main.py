import pygame,sys
from setting import *
from level import Level


class Game:
    def __init__(self):
        
        #general setup
        pygame.init()
        self.font = pygame.font.SysFont(None, 40)
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Sneke')
        self.clock = pygame.time.Clock()
        
        self.level = Level()
        
        self.paused  = False
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                 
            if self.paused == False:
                    
                counting_time = pygame.time.get_ticks() 

                # change milliseconds into minutes, seconds, milliseconds
                counting_minutes = str(counting_time//60000).zfill(2)
                counting_seconds = str((counting_time%60000)//1000 ).zfill(2)
                score = str((counting_time)*25//1000)
                counting_string = "%s:%s" % (counting_minutes, counting_seconds)
                score_string = "%s" % score

                counting_text = self.font.render(str(counting_string), 1,'white')
                score_text = self.font.render(str(score_string), 1,'white')
                
                counting_rect = counting_text.get_rect(center = (1200,30))
                score_rect = score_text.get_rect(center = (900,30))

            self.screen.fill((255,255,255))
            self.level.run()
            pygame.draw.rect(self.screen,'Black',counting_rect)
            self.screen.blit(counting_text, counting_rect)
            pygame.draw.rect(self.screen,'Black',score_rect)
            self.screen.blit(score_text, score_rect)
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
    
    #50.28