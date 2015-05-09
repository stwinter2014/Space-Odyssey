import pygame
import random
import time
import Sp_class
import add_Sp
import W_L
import comments

def Level_1 ():
    pygame.init()
    #comments.level_2_welcome()
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
    all_sprites_list = pygame.sprite.Group()
    for i in range(8):
        add_Sp.Create_M_1(size, all_sprites_list, block_list, block1_list)
        add_Sp.Create_M_2(size, all_sprites_list, block_list, block2_list)
    player = Sp_class.Player()
    all_sprites_list.add(player)
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
    ready_ch = 0
    click_sound = pygame.mixer.Sound("rocket1.wav")
    parade_sound = pygame.mixer.Sound("jet_airplane.wav")
    ready_sound = pygame.mixer.Sound("sound42.wav")
    background_image = pygame.image.load("zvezdy.jpg").convert()
    loose_image = pygame.image.load("Game_Over.jpg").convert()
    win_image = pygame.image.load("player.png").convert()
    ready_image = pygame.image.load("Ready.png").convert()
    set_image = pygame.image.load("Set.png").convert()
    go_image = pygame.image.load("Go.png").convert()
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:   
                if event.key == pygame.K_LEFT:
                    x_speed = -10
                if event.key == pygame.K_RIGHT:
                    x_speed=10
                if event.key == pygame.K_ESCAPE and lleft == 0:
                    done = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = 0
        screen.blit(background_image, [0,0])
        if timeF == 0:
            ready_ch += 1
        if ready_ch <= 60:
            screen.blit(ready_image, [340, 270])
            ready_image.set_colorkey(black)
            if ready_ch % 50 == 0:
                ready_sound.play()
        elif ready_ch <= 120 and ready_ch > 60:
            screen.blit(set_image, [350, 270])
            set_image.set_colorkey(black)
            if ready_ch % 110 == 0:
                ready_sound.play()
        elif ready_ch <= 180 and ready_ch>120:
            screen.blit(go_image, [350, 270])
            go_image.set_colorkey(black)
            if ready_ch % 170 == 0:
                ready_sound.play()
        elif ready_ch > 180:  
            block_list.update()
            font = pygame.font.Font(None, 35)
            if len(block1_list) < 8:
                add_Sp.Create_M_1(size, all_sprites_list, block_list, block1_list)
            if len(block2_list) < 8:
                add_Sp.Create_M_2(size, all_sprites_list, block_list, block2_list)
            rect_x += x_speed
            timeF += 1
            if timeF >= time_up and lleft != 0:
                click_sound.stop()
                all_sprites_list.empty()
                if parade == 0:
                    parade_sound.play()
                    parade += 1
                screen.blit(win_image, [x_w,y_w])
                win_image.set_colorkey(black)
                y_w -= 4
                if y_w <= -86:
                    done = True
                    print('Level is complete!')
            if rect_x > size[0]:
                rect_x = 0
            if rect_x < 0:
                rect_x = size[0]
            player.rect.x = rect_x
            player.rect.y = size[1]-85
            blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
            for block in blocks_hit_list:
                if lleft<=0:
                    pass
                else:
                    lleft -= 1
                    click_sound.play()
            if lleft == 0:
                screen.blit(loose_image, [210,250])
                loose_image.set_colorkey(black)
                if l_ch == 0:
                    all_sprites_list.remove(player)
                    comments.loose_conf()
                    l_ch += 1
            timer += 1
            if timer == 60:
                score += 10
                timer = 0
            all_sprites_list.draw(screen)
            text = font.render ("Lives left: ", True, white)
            text1 = font.render(str(lleft), True, white)
            screen.blit(text1,[810, 50])
            screen.blit(text, [680,50])
        else:
            pass
        pygame.display.flip()
        clock.tick(60)
    if lleft == 0:
        W_L.Loose(score, white, black)
    elif timeF >= 5000 and lleft != 0:
        W_L.Win(lleft, score, white, black)
    pygame.quit ()
Level_1()
