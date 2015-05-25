import random
import pygame
pygame.init()
size = [900,730]
black      = (  0,   0,   0)
white      = (255, 255, 255)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

class Meteor_1(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("meteor1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def reset_pos(self):
        self.rect.y = random.randrange(-500,-10)
        self.rect.x = random.randrange(0,size[0]-60)  
    def update(self):
        self.rect.y += 2
        if self.rect.y > size[1]:
            self.reset_pos()

class Meteor_2(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("meteor2.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def reset_pos(self):
        self.rect.y = random.randrange(-500,-10)
        self.rect.x = random.randrange(0,size[0]-40)  
    def update(self):
        self.rect.y += 1
        if self.rect.y > size[1]:
            self.reset_pos()

class Crystal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Crystal.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def reset_pos(self):
        self.rect.y = random.randrange(-500,-10)
        self.rect.x = random.randrange(0,size[0]-40)  
    def update(self):
        self.rect.y += 2
        if self.rect.y > size[1]:
            self.reset_pos()

class Weapon(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        pygame.draw.rect(self.image,color,[0,0,width,height])
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 3
        
class Explosion (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("explosion5.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
    def update(self, count):
        if count >= 5 and count < 10:
            self.image = pygame.image.load("explosion4.png").convert()
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.rect.x = 500
            self.rect.y = 500
        if count >= 10 and count < 15:
            self.image = pygame.image.load("explosion3.png").convert()
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.rect.x = 500
            self.rect.y = 500
        if count >= 15 and count < 20:
            self.image = pygame.image.load("explosion2.png").convert()
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.rect.x = 500
            self.rect.y = 500
        if count >= 20 and count < 25:
            self.image = pygame.image.load("explosion1.png").convert()
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.rect.x = 500
            self.rect.y = 500
        if count >= 25 and count < 30:
            self.image = pygame.image.load("explosion2.png").convert()
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.rect.x = 500
            self.rect.y = 500
        if count >= 30 and count < 35:
            self.image = pygame.image.load("explosion3.png").convert()
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.rect.x = 500
            self.rect.y = 500
        if count >= 35 and count < 40:
            self.image = pygame.image.load("explosion4.png").convert()
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.rect.x = 500
            self.rect.y = 500
        if count >= 40 and count < 45:
            self.image = pygame.image.load("explosion5.png").convert()
            self.image.set_colorkey(black)
            self.rect = self.image.get_rect()
            self.rect.x = 500
            self.rect.y = 500
            
            
