import pygame,random

class Trail(pygame.sprite.Sprite):
    def __init__(self,pos,color):
        super(Trail, self).__init__()   
        self.color = color
        self.display_surface = pygame.display.get_surface()

        self.x, self.y = pos
        #self.y += 10
        self.dx = random.randint(0,50) / 10 - 1
        self.dy = -2
        self.size = 10#random.randint(4,10)

        self.rect = pygame.draw.circle(self.display_surface, self.color, (self.x, self.y), self.size)

    def update(self):
        #self.x -= self.dx
        #self.y -= self.dy
        self.size -= 0.1

        if self.size <= 0:
            self.kill()

        self.rect = pygame.draw.circle(self.display_surface, self.color, (self.x, self.y), self.size)
        
class SnakeTail(pygame.sprite.Sprite):
    def __init__(self,pos,rangeee) :
        super(SnakeTail,self).__init__()
        self.x,self.y = pos
        #self.x += 32
        #self.y += 32
        self.display_surface = pygame.display.get_surface()
        self.size = 16
        self.long = rangeee

        self.rect = pygame.draw.circle(self.display_surface,(2,120,2), (self.x, self.y), self.size)
        #self.rect = pygame.draw.rect(self.display_surface,'blue',(self.x,self.y,self.size,self.size))
    
    def update(self):
        self.size -= self.long
        
        if self.size <= 0 :
            self.kill()
        
        #self.rect = pygame.draw.rect(self.display_surface,'blue',(self.x,self.y,self.size,self.size))
        self.rect = pygame.draw.circle(self.display_surface,(2,120,2), (self.x, self.y), self.size)