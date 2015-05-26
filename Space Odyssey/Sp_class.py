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
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load("explosion5.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
    def update (self, x_pos, y_pos, count):
        if (count >= 3 and count < 6) or (count >= 21 and count < 23):
            self.image = pygame.image.load("explosion4.png").convert()
        if (count >= 6 and count < 9) or (count >= 18 and count < 21):
            self.image = pygame.image.load("explosion3.png").convert()
        if (count >= 9 and count < 12) or (count >= 15 and count < 18):
            self.image = pygame.image.load("explosion2.png").convert()
        if count >= 12 and count < 15:
            self.image = pygame.image.load("explosion1.png").convert()
        if count >= 23 and count < 26:
            self.image = pygame.image.load("explosion5.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
