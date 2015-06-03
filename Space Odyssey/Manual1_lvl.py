import pygame
import Sp_class
import add_Sp
import lvl_1
import comments
"""Manual level.
Here is a description of how the game (1st level)
works shown in interactive way to the gamer"""
def Manual_1 ():
    pygame.init()
    size = [900,730]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Space Odyssey")
    done = False
    clock = pygame.time.Clock()
    """necessary colors"""
    black      = (  0,   0,   0)
    white      = (255, 255, 255)
    orange     = (255,  69,   0)
    """special objects for axplosion animation"""
    pressed = False
    image_evol = 0
    exp1_pos = 0
    exp2_pos = 0
    """sprite lists"""
    block1_list = pygame.sprite.Group()
    block2_list = pygame.sprite.Group()
    player_list = pygame.sprite.Group()
    explosion_list = pygame.sprite.Group()
    """sprites creation"""
    for i in range(1):
        add_Sp.Create_MM_1(size, block1_list)
        add_Sp.Create_MM_2(size, block2_list)
    player = Sp_class.Player()
    player_list.add(player)
    explosion = Sp_class.Explosion(exp1_pos, exp2_pos)
    explosion_list.add(explosion)
    """strings with all the necessary messages"""
    manual_wel_f = 'Welcome to Space Odyssey!'
    manual_wel_s = 'Complete all 3 levels to return to your home planet.'
    manual1_wel = 'Your main goal during the game is to avoid meteors and to'
    manual2_wel = 'go through the levels loosing lives as less as possible.'
    manual_move = 'Press arrow keys RIGHT and LEFT to move your starship.'
    manual_try_move = 'Press'
    manual1_look = 'Impact with smaller meteors will take one of your lives.'
    manual01_look = 'Impact with bigger meteors will take two of your lives.'
    manual02_look = 'Be careful, big meteors move faster, than the smaller ones.'
    manual_finish = 'Now your are ready for your journey!'
    manual_skip = 'Press SPACE to continue'
    x_speed = 0
    lleft = 7
    x_w = 380
    y_w = 730
    parade = 0
    skip = 0
    ready = 0
    move_count = 5
    _seen = 0
    stop_moment = 0
    manual_complete = 0
    """sounds and images assignment"""
    click_sound = pygame.mixer.Sound("rocket1.wav")
    parade_sound = pygame.mixer.Sound("jet_airplane.wav")
    background_image = pygame.image.load("zvezdy.jpg").convert()
    win_image = pygame.image.load("player.png").convert()
    arrow_image = pygame.image.load("arrow_keys.png").convert()
    wasd_image = pygame.image.load('wasd_keys.png').convert()
    rect_x = 450 - win_image.get_width()//2
    """main cycle of the game"""
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:   
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_speed = -10
                    if stop_moment == 1:
                        move_count -= 1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_speed = 10
                    if stop_moment == 1:
                        move_count -= 1
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_SPACE and _seen != 3:
                    skip = 0
                    ready += 1
                if event.key == pygame.K_SPACE and _seen == 3:
                    skip = 0
                    stop_moment = 1 
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
            _seen = 1
            skip += 1
            text_f = font_f.render(manual_wel_f, True, white)
            screen.blit(text_f,(450 - text_f.get_width()//2, 365 - text_f.get_height()//2))
            text_s = font.render(manual_wel_s, True, white)
            screen.blit(text_s, (450 - text_s.get_width()//2, 420 - text_s.get_height()//2))
        if ready == 1:
            _seen = 2
            skip += 1
            text1 = font1.render(manual1_wel, True, white)
            text2 = font1.render(manual2_wel, True, white)
            screen.blit(text1, (450 - text1.get_width()//2, 365 - text1.get_height()//2))
            screen.blit(text2, (450 - text2.get_width()//2, 415 - text2.get_height()//2))
        if ready == 2:
            _seen = 3
            skip += 1
            text_m = font.render(manual_move, True, white)
            screen.blit(text_m, (450 - text_m.get_width()//2, 365 - text_m.get_height()//2))
            player_list.draw(screen)
            if rect_x > size[0]:
                rect_x = 0
            if rect_x < 0:
                rect_x = size[0]
            rect_x += x_speed
            player.rect.x = rect_x
            player.rect.y = size[1] - win_image.get_height()
            if stop_moment == 1:
                text_t_m = font_f.render(manual_try_move, True, white)
                screen.blit(text_t_m, (450 - text_t_m.get_width()//2, 370 + text_t_m.get_height()//2))
                screen.blit(arrow_image, [400 - arrow_image.get_width(), 500])
                arrow_image.set_colorkey(black)
                screen.blit(wasd_image, [400 + wasd_image.get_width(), 500])
                wasd_image.set_colorkey(white)
            if move_count < 3:
                stop_moment = 0
                _seen += 1
        if ready == 3:
            skip += 1
            block2_list.update()
            text1_look = font.render(manual1_look, True, white)
            screen.blit(text1_look, (450 - text1_look.get_width()//2, 365 - text1_look.get_height()//2))
            player_list.draw(screen)
            block2_list.draw(screen)
            text_l = font1.render ("Lives left: ", True, white)
            text1_l = font1.render(str(lleft), True, white)
            screen.blit(text1_l,[810, 50])
            screen.blit(text_l, [680,50])
            player.rect.x = size[0]//2 - win_image.get_width()//2
            player.rect.y = size[1] - win_image.get_height()
            blocks_hit_list = pygame.sprite.spritecollide(player, block2_list, True)
            for block in blocks_hit_list:
                pressed = True
                exp1_pos = player.rect.x
                exp2_pos = player.rect.y
                lleft -= 1
                click_sound.play()
        if ready == 4:
            skip += 1
            block1_list.update()
            text01_look = font.render(manual01_look, True, white)
            screen.blit(text01_look, (450 - text01_look.get_width()//2, 365 - text01_look.get_height()//2))
            text02_look = font.render(manual02_look, True, white)
            screen.blit(text02_look, (450 - text02_look.get_width()//2, 370 + text02_look.get_height()//2))
            player_list.draw(screen)
            block1_list.draw(screen)
            player.rect.x = size[0]//2 - win_image.get_width()//2
            player.rect.y = size[1] - win_image.get_height()
            blocks_hit_list = pygame.sprite.spritecollide(player, block1_list, True)
            text_l = font1.render ("Lives left: ", True, white)
            text1_l = font1.render(str(lleft), True, white)
            screen.blit(text1_l,[810, 50])
            screen.blit(text_l, [680,50])
            for block in blocks_hit_list:
                pressed = True
                exp1_pos = player.rect.x
                exp2_pos = player.rect.y
                lleft -= 2
                click_sound.play()
        if ready == 5:
            click_sound.stop()
            if parade == 0:
                parade_sound.play()
                parade += 1
            screen.blit(win_image, [x_w,y_w])
            win_image.set_colorkey(black)
            y_w -= 4
            text_finish = font_f.render(manual_finish, True, white)
            screen.blit(text_finish, (450 - text_finish.get_width()//2, 365 - text_finish.get_height()//2))
            if y_w < -win_image.get_height() - 7:
                done = True
                manual_complete += 1
        if pressed == True:
            image_evol += 1
            explosion_list.update(exp1_pos, exp2_pos, image_evol)
            explosion_list.draw(screen)
            if image_evol >= 45:
                pressed = False
                image_evol = 0
        if skip > 240 and stop_moment != 1:
            text_skip = font.render(manual_skip, True, white)
            screen.blit(text_skip, (size[0] - text_skip.get_width(), 640 + text_skip.get_height()//2))
        pygame.display.flip()
        clock.tick(60)
    if manual_complete == 1:
        lvl_1.Level_1()
    pygame.quit ()
