import pygame
import random
import time
import Sp_class
import add_Sp
import comments

def Manual_1 ():
    pygame.init()
    size = [900,730]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Space Odyssey")
    done = False
    clock = pygame.time.Clock()
    
    black      = (  0,   0,   0)
    white      = (255, 255, 255)
    orange     = (255,  69,   0)
    
    block_list = pygame.sprite.Group()
    block1_list = pygame.sprite.Group()
    block2_list = pygame.sprite.Group()
    player_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    for i in range(1):
        add_Sp.Create_M_1(size, all_sprites_list, block_list, block1_list)
        add_Sp.Create_M_2(size, all_sprites_list, block_list, block2_list)
    player = Sp_class.Player()
    player_list.add(player)
    all_sprites_list.add(player)
    manual_wel_f = 'Welcome to Space Odyssey!'
    manual_wel_s = 'Complete all 3 levels to return to your home planet.'
    manual1_wel = 'Your main goal during the game is to avoid meteors and to'
    manual2_wel = 'go through the levels loosing lives as less as possible.'
    manual_move = 'Press arrow keys RIGHT and LEFT to move your starship.'
    rect_x = 380
    x_speed = 0
    time_up = 5000
    lleft = 5
    timer = 0
    score = 0
    timeF = 0
    x_w = 380
    y_w = 730
    parade = 0
    l_ch = 0
    count_time = 0
    ready = 0
    click_sound = pygame.mixer.Sound("rocket1.wav")
    parade_sound = pygame.mixer.Sound("jet_airplane.wav")
    background_image = pygame.image.load("zvezdy.jpg").convert()
    loose_image = pygame.image.load("Game_Over.jpg").convert()
    win_image = pygame.image.load("player.png").convert()
    arrow_image = pygame.image.load("k.png").convert()
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:   
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_speed = -10
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_speed=10
                if event.key == pygame.K_ESCAPE and lleft == 0:
                    done = True
                if event.key == pygame.K_SPACE:
                    ready += 1
                    print('yeah')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_speed = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_speed = 0
        screen.blit(background_image, [0,0])
        font1 = pygame.font.Font(None, 35)
        font_f = pygame.font.Font(None, 55)
        font = pygame.font.Font(None, 45)
        if ready == 0:
            text_f = font_f.render(manual_wel_f, True, white)
            screen.blit(text_f,(450 - text_f.get_width()//2, 365 - text_f.get_height()//2))
            text_s = font.render(manual_wel_s, True, white)
            screen.blit(text_s, (450 - text_s.get_width()//2, 420 - text_s.get_height()//2))
        if ready == 1:
            text1 = font1.render(manual1_wel, True, white)
            text2 = font1.render(manual2_wel, True, white)
            screen.blit(text1, (450 - text1.get_width()//2, 365 - text1.get_height()//2))
            screen.blit(text2, (450 - text2.get_width()//2, 415 - text2.get_height()//2))
        if ready == 2:
            text_m = font.render(manual_move, True, white)
            screen.blit(text_m, (450 - text_m.get_width()//2, 365 - text_m.get_height()//2))
            screen.blit(arrow_image, [200,500])
            arrow_image.set_colorkey(black)
            player_list.draw(screen)
        if ready == 3:
            player_list.draw(screen)
            
        player.rect.x = rect_x
        player.rect.y = size[1]-85
        if rect_x > size[0]:
            rect_x = 0
        if rect_x < 0:
            rect_x = size[0]
        rect_x += x_speed
        text_l = font1.render ("Lives left: ", True, white)
        text1_l = font1.render(str(lleft), True, white)
        screen.blit(text1_l,[810, 50])
        screen.blit(text_l, [680,50])
        pygame.display.flip()
        clock.tick(60)
    if lleft == 0:
        W_L.Loose(score, white, black)
    elif timeF >= 5000 and lleft != 0:
        W_L.Win(lleft, score, white, black)
    pygame.quit ()
Manual_1()
