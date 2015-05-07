import pygame
class Loose():
    def __init__(self, score, color, color1):
        loose_sound = pygame.mixer.Sound("boo.wav")
        clock=pygame.time.Clock()
        screen=pygame.display.set_mode([300,200])
        done=False
        loose = 0
        while done==False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
            screen.fill(color)
            if loose == 0:
                loose_sound.play()
                loose +=1
            font = pygame.font.Font(None, 35)
            text = font.render ("Total score: ", True, color1)
            text1 = font.render(str(score),True, color1)
            screen.blit(text1,[185, 50])
            screen.blit(text, [40,50])
            pygame.display.flip()
            clock.tick(60)

class Win():
    def __init__(self, lives_left, score, color, color1):
        win_sound = pygame.mixer.Sound("cheer1.wav")
        clock=pygame.time.Clock()
        size=[300,200]
        screen=pygame.display.set_mode(size)
        win = 0
        done = False
        while done==False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
            screen.fill(color)
            if win == 0:
                win_sound.play()
                win +=1
            Finish = score*lives_left
            font = pygame.font.Font(None, 35)
            text = font.render ("Total score: ", True, color1)
            text1 = font.render(str(Finish),True, color1)
            screen.blit(text1,[185, 50])
            screen.blit(text, [40,50])
            pygame.display.flip()
            clock.tick(60)
