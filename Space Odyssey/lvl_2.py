import pygame
import random
import time
import Sp_class
import add_Sp
import W_L
import comments

def Level_2 ():
    pygame.init()
    comments.level_2_welcome()
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
    crystal_list = pygame.sprite.Group()
    for i in range(8):
        add_Sp.Create_M_1(size, all_sprites_list, block_list, block1_list)
        add_Sp.Create_M_2(size, all_sprites_list, block_list, block2_list)
    player = Sp_class.Player()
    all_sprites_list.add(player)
    for i in range(2):
        add_Sp.Create_C(size, crystal_list)
    rect_x = 0
    x_speed = 0
    lleft = 5
    timer = 0
    score = 0
    timeF = 0
    x_w = 380
    y_w = 730
    parade = 0
    protection = False
    count_prot = 0
    l_ch = 0
    count_time = 0
    click_sound = pygame.mixer.Sound("rocket1.wav")
    prot_sound = pygame.mixer.Sound("buzz.wav")
    parade_sound = pygame.mixer.Sound("jet_airplane.wav")
    background_image = pygame.image.load("zvezdy.jpg").convert()
    loose_image = pygame.image.load("Game_Over.jpg").convert()
    win_image = pygame.image.load("player.png").convert()
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
        block_list.update()
        crystal_list.update()
        screen.fill(white)
        screen.blit(background_image, [0,0])
        font = pygame.font.Font(None, 35)
        if len(block1_list) < 8:
            add_Sp.Create_M_1(size, all_sprites_list, block_list, block1_list)
        if len(block2_list) < 8:
            add_Sp.Create_M_2(size, all_sprites_list, block_list, block2_list)
        if len(crystal_list)<2 and lleft > 0:
            add_Sp.Create_C(size, crystal_list)
        rect_x += x_speed
        timeF += 1
        if timeF >= 5000 and lleft != 0:
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
        crystal_hit_list = pygame.sprite.spritecollide(player, crystal_list, True)
        for crystal in crystal_hit_list:
            protection = True
            count_prot = 480
            counter = 8
            prot_sound.play()
        if protection == True:
            count_prot -= 1
            count_time += 1
            if count_time >= 60:
                counter -= 1
                count_time = 0
            text_prot_2 = font.render(str(counter), True, orange)
            text_prot_1 = font.render('Shield falls in: ', True, orange) 
            screen.blit(text_prot_1, [680, 80])
            screen.blit(text_prot_2, [860, 80])
        if count_prot < 1:
            protection = False
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
        for block in blocks_hit_list:
            if protection == True:
                pass
            if protection == False:
                if lleft<=0:
                    pass
                else:
                    lleft -= 1
                    click_sound.play()
        if lleft == 0:
            screen.blit(loose_image, [210,250])
            loose_image.set_colorkey(black)
            if l_ch == 0:
                crystal_list.empty()
                all_sprites_list.remove(player)
                comments.loose_conf()
                l_ch += 1
        timer += 1
        if timer == 60:
            score += 10
            timer = 0
        all_sprites_list.draw(screen)
        crystal_list.draw(screen)
        text = font.render ("Lives left: ", True, white)
        text1 = font.render(str(lleft), True, white)
        screen.blit(text1,[810, 50])
        screen.blit(text, [680,50])
        pygame.display.flip()
        clock.tick(60)
    if lleft == 0:
        W_L.Loose(score, white, black)
    elif timeF >= 500 and lleft != 0:
        W_L.Win(lleft, score, white, black)
    pygame.quit ()
Level_2()