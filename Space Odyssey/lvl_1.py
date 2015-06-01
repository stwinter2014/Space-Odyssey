import pygame
import Sp_class
import add_Sp
import W_L
import comments
import Exception_file
import lvl_2
def Level_1 ():
    pygame.init()
    comments.level_1_welcome()
    size = [900,730]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Space Odyssey")
    done = False
    clock = pygame.time.Clock()

    black      = (  0,   0,   0)
    white      = (255, 255, 255)
    pressed = False
    image_evol = 0
    exp1_pos = 0
    exp2_pos = 0
    block_list = pygame.sprite.Group()
    block1_list = pygame.sprite.Group()
    block2_list = pygame.sprite.Group()
    explosion_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    for i in range(8):
        add_Sp.Create_M_1(size, all_sprites_list, block_list, block1_list)
        add_Sp.Create_M_2(size, all_sprites_list, block_list, block2_list)
    player = Sp_class.Player()
    all_sprites_list.add(player)
    explosion = Sp_class.Explosion(exp1_pos, exp2_pos)
    explosion_list.add(explosion)
    f_level_score = 0
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
    mistake = 0
    try:
        click_sound = pygame.mixer.Sound("rocket1.wav")
        parade_sound = pygame.mixer.Sound("jet_airplane.wav")
        ready_sound = pygame.mixer.Sound("sound42.wav")
    except pygame.error:
        print("Unable to find one of the sounds.")
        done = True
    try:
        background_image = pygame.image.load("zvezdy.jpg").convert()
        if background_image.get_width() < 900:
            raise Exception_file.Pic_Size_Error("Background picture is not big enough. Try another one!")
    except pygame.error:
        print("Unable to find the background picture.")
        done = True
    except Exception_file.Pic_Size_Error:
        print(Exception_file.Pic_Size_Error.txt)
        mistake = 1
    try:
        loose_image = pygame.image.load("Game_Over.jpg").convert()
        win_image = pygame.image.load("player.png").convert()
        ready_image = pygame.image.load("Ready.png").convert()
        set_image = pygame.image.load("Set.png").convert()
        go_image = pygame.image.load("Go.png").convert()
    except pygame.error:
        print('Unable to open one of the supporting pictures')
        done = True
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_speed = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_speed = 0
        if mistake == 0:
            screen.blit(background_image, [0,0])
        elif mistake == 1:
            screen.fill(black)
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
            if timeF > time_up and lleft != 0:
                click_sound.stop()
                all_sprites_list.empty()
                if parade == 0:
                    parade_sound.play()
                    comments.level_1_complete()
                    parade += 1
                screen.blit(win_image, [x_w,y_w])
                win_image.set_colorkey(black)
                y_w -= 4
                if y_w <= -win_image.get_height():
                    done = True
            if rect_x > size[0] - win_image.get_width()//2:
                rect_x = 0
            if rect_x < 0:
                rect_x = size[0] - win_image.get_width()//2
            player.rect.x = rect_x
            player.rect.y = size[1] - win_image.get_height()
            blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
            for block in blocks_hit_list:
                pressed = True
                exp1_pos = rect_x
                exp2_pos = size[1] - win_image.get_height()
                if lleft <= 0:
                    pass
                else:
                    lleft -= 1
                    click_sound.play()
            if pressed == True and lleft != 0 and timeF < time_up:
                image_evol += 1
                explosion_list.update(exp1_pos, exp2_pos, image_evol)
                explosion_list.draw(screen)
                if image_evol >= 26:
                    pressed = False
                    image_evol = 0
            if lleft == 0:
                screen.blit(loose_image, [210,250])
                loose_image.set_colorkey(black)
                all_sprites_list.remove(player)
                if l_ch == 0:                    
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
        f_level_score = lleft*score
        lvl_2.Level_2(f_level_score)
    pygame.quit ()
