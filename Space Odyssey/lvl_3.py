import pygame
import random
import time
import Sp_class
import add_Sp
import W_L
import comments
import Exception_file

def Level_3 (level_2_score):
    pygame.init()
    comments.level_3_welcome()
    size = [900,730]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Space Odyssey. Level 3")
    done = False
    clock = pygame.time.Clock()

    black      = (  0,   0,   0)
    white      = (255, 255, 255)
    orange     = (255,  69,   0)
    pressed = False
    image_evol = 0
    x_s_pos = 0
    y_s_pos = 0
    x1_s_pos = 0
    y1_s_pos = 0
    x_w_pos = 0
    y_w_pos = 0
    image_prot = 0
    shield_count = 0
    block_list = pygame.sprite.Group()
    block1_list = pygame.sprite.Group()
    block2_list = pygame.sprite.Group()
    shield1_list = pygame.sprite.Group()
    shield2_list = pygame.sprite.Group()
    explosion_list = pygame.sprite.Group()
    destruction_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    crystal_list = pygame.sprite.Group()
    weapon_list = pygame.sprite.Group()
    for i in range(11):
        add_Sp.Create_M_1(size, all_sprites_list, block_list, block1_list)
        add_Sp.Create_M_2(size, all_sprites_list, block_list, block2_list)
    shield1 = Sp_class.Shield(x_s_pos, y_s_pos)
    shield1_list.add(shield1)
    shield2 = Sp_class.Shield(x1_s_pos, y1_s_pos)
    shield2_list.add(shield2)
    explosion = Sp_class.Explosion(x_s_pos, y_s_pos)
    explosion_list.add(explosion)
    weapon = Sp_class.Weapon()
    weapon_list.add(weapon)
    destruction = Sp_class.Explosion(x_w_pos, y_w_pos)
    destruction_list.add(destruction)
    player = Sp_class.Player()
    all_sprites_list.add(player)
    add_Sp.Create_C(size, crystal_list)
    rect_x = 380
    x_speed = 0
    time_up = 5040
    lleft = 7
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
    ready_ch = 0
    mistake = 0
    wep_engage = False
    destruct_im = 0
    collision = False
    recharge = 185
    text_output = False
    collision_c = False
    bonus_s = 0
    try:
        click_sound = pygame.mixer.Sound("rocket1.wav")
        parade_sound = pygame.mixer.Sound("jet_airplane.wav")
        ready_sound = pygame.mixer.Sound("sound42.wav")
        prot_sound = pygame.mixer.Sound("buzz.wav")
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
                    x_speed = 10
                if event.key == pygame.K_ESCAPE and lleft == 0:
                    done = True
                if event.key == pygame.K_SPACE and recharge == 185:
                    wep_engage = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_speed = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_speed = 0
                if event.key == pygame.K_SPACE:
                    pass
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
            weapon_list.update(wep_engage, win_image, rect_x)
            crystal_list.update()
            font = pygame.font.Font(None, 35)
            if len(block1_list) < 11:
                add_Sp.Create_M_1(size, all_sprites_list, block_list, block1_list)
            if len(block2_list) < 11:
                add_Sp.Create_M_2(size, all_sprites_list, block_list, block2_list)
            if len(crystal_list) < 1 and timeF%840 == 0:
                add_Sp.Create_C(size, crystal_list)
            rect_x += x_speed
            timeF += 1
            if timeF >= time_up and lleft != 0:
                click_sound.stop()
                prot_sound.stop()
                all_sprites_list.empty()
                crystal_list.empty()
                if parade == 0:
                    parade_sound.play()
                    comments.level_3_complete()
                    parade += 1
                screen.blit(win_image, [x_w,y_w])
                win_image.set_colorkey(black)
                y_w -= 4
                if y_w <= -size[1] - win_image.get_height() - 7:
                    done = True
            if rect_x > size[0] - win_image.get_width()//2:
                rect_x = 0
            if rect_x < 0:
                rect_x = size[0] - win_image.get_width()//2
            player.rect.x = rect_x
            player.rect.y = size[1] - win_image.get_height()
            crystal_hit_list = pygame.sprite.spritecollide(player, crystal_list, True)
            x_s_pos = rect_x
            y_s_pos = size[1] - win_image.get_height()
            x1_s_pos = rect_x + win_image.get_width() - 25
            y1_s_pos = size[1] - win_image.get_height()
            for crystal in crystal_hit_list:
                protection = True
                count_prot = 480
                counter = 8
                prot_sound.play()
            if protection == True and timeF < time_up:
                count_prot -= 1
                count_time += 1
                image_prot += 1
                if shield_count == 0:
                    shield1_list.update(x_s_pos, y_s_pos, image_prot)
                    shield1_list.draw(screen)
                if shield_count == 1:
                    shield2_list.update(x1_s_pos, y1_s_pos, image_prot)
                    shield2_list.draw(screen)
                if count_time >= 60:
                    counter -= 1
                    count_time = 0
                if image_prot >= 26 and shield_count == 0:
                    image_prot = 0
                    shield_count += 1
                if image_prot >= 26 and shield_count == 1:
                    image_prot = 0
                    shield_count = 0
                text_prot_2 = font.render(str(counter), True, orange)
                text_prot_1 = font.render('Shield falls in: ', True, orange) 
                screen.blit(text_prot_1, [680, 80])
                screen.blit(text_prot_2, [860, 80])
            if count_prot < 1:
                protection = False
                image_prot = 0
            blocks1_hit_list = pygame.sprite.spritecollide(player, block1_list, True)
            for block in blocks1_hit_list:
                if protection == True:
                    pass
                if protection == False:
                    pressed = True
                    if lleft <= 0 or timeF >= time_up:
                        pass
                    else:
                        lleft -= 2
                        click_sound.play()
            blocks2_hit_list = pygame.sprite.spritecollide(player, block2_list, True)
            for block in blocks2_hit_list:
                if protection == True:
                    pass
                if protection == False:
                    pressed = True
                    if lleft <= 0 or timeF >= time_up:
                        pass
                    else:
                        lleft -= 1
                        click_sound.play()
            if pressed == True and lleft != 0 and timeF < time_up:
                image_evol += 1
                explosion_list.update(x_s_pos, y_s_pos, image_evol)
                explosion_list.draw(screen)
                if image_evol >= 26:
                    pressed = False
                    image_evol = 0
            if lleft == 0:
                screen.blit(loose_image, [210,250])
                loose_image.set_colorkey(black)
                if l_ch == 0:
                    crystal_list.empty()
                    all_sprites_list.remove(player)
                    comments.loose_conf()
                    l_ch += 1
            if lleft <= 0:
                lleft = 0
            timer += 1
            if timer == 60:
                score += 10
                timer = 0
            if wep_engage == True:
                text_output = True
                weapon_list.draw(screen)
            if text_output == True:
                recharge -= 1
                text1_recharge = font.render ("Battery recharge in: ", True, white)
                text2_recharge = font.render (str(recharge//60), True, white)
                screen.blit(text1_recharge,[600, 110])
                screen.blit(text2_recharge,[860, 110])
                if recharge <= 59:
                    text_output = False
                    recharge = 185
            if weapon.rect.y <= 0:
                wep_engage = False
            weapon_hit_list = pygame.sprite.spritecollide(weapon, block_list, True)
            for block in weapon_hit_list:
                click_sound.play()
                bonus_s += 1
                wep_engage = False
                collision = True
            weapon_c_hit_list = pygame.sprite.spritecollide(weapon, crystal_list, True)
            for crystal in weapon_c_hit_list:
                bonus_s -= 1
                wep_engage = False
                collision_c = True
                click_sound.play()
            if collision == True:
                destruct_im += 1
                explosion_list.update(block.rect.x, block.rect.y, destruct_im)
                explosion_list.draw(screen)
                if destruct_im >= 26:
                    collision = False
                    destruct_im = 0
            if collision_c == True:
                destruct_im += 1
                explosion_list.update(crystal.rect.x, crystal.rect.y, destruct_im)
                explosion_list.draw(screen)
                if destruct_im >= 26:
                    collision_c = False
                    destruct_im = 0
            all_sprites_list.draw(screen)
            crystal_list.draw(screen)
            text = font.render ("Lives left: ", True, white)
            text1 = font.render(str(lleft), True, white)
            screen.blit(text1,[810, 50])
            screen.blit(text, [680,50])
        else:
            pass
        pygame.display.flip()
        clock.tick(60)
    if lleft == 0:
        final_l_score = level_2_score + score + bonus_s*10
        W_L.Loose(final_l_score, white, black)
    if timeF < 5000:
        final_l_score = level_2_score + score + bonus_s*10
        W_L.Win(final_l_score, white, black)
    elif timeF >= 5000 and lleft != 0:
        final_w_score = level_2_score + score*lleft + bonus_s*10
        W_L.Win(final_w_score, white, black)
    pygame.quit ()
