import pygame,sys
from setting import *
from level import Level


class Game:
    def __init__(self):
        
        #general setup
        pygame.init()
        self.font = pygame.font.SysFont(UI_FONT, 40)
        icon = pygame.image.load('graphic/icon/icon.png')
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Sneke')
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        
        self.level = Level()
        self.name = pygame.image.load('graphic/name.png')
        
        self.bgmain_sound = pygame.mixer.Sound('audio/bg_main.wav')
        self.bgmain_sound.set_volume(0.5)
        
    def run(self):
        self.bgmain_sound.play(loops=-1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.level.out == True:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and (self.level.statusmenu == "start" or self.level.statusmenu == "pause"):
                        self.level.game_pause()
                    if self.level.statusmenu == "over":
                        if event.key == pygame.K_BACKSPACE :
                            self.level.name_input = self.level.name_input[:-1]
                        if event.key == pygame.K_RETURN and self.level.name_input != '':
                            self.level.save_score = True
                        else:
                            self.level.name_input += event.unicode
                            if self.level.name_input.isalpha() == False:
                                self.level.name_input = self.level.name_input[:-1]
                            
            self.screen.fill('white')
            self.level.run()
            sub_font = pygame.font.Font(UI_FONT,20)
            myname = sub_font.render(str("65010971 WASITPHON MALIWAN"),True,'white')
            self.screen.blit(myname,(800,720))
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
    