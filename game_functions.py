import sys
from random import uniform
import pygame
from bullet import Bullet
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from heart import Heart
from time import sleep
from button import Button
from message import Message
from image import Image
from boss import Boss

def check_keydown_events(flag,event,ship,start_button,):
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        flag['add_bullet_flag'] = True

def check_keyup_events(flag,event,ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_SPACE:
        flag['add_bullet_flag'] = False

def check_events(flag,ai_settings,screen,game_stats,ship,start_button,aliens,bullets,hearts):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(flag,event,ship,start_button,)
        elif event.type == pygame.KEYUP:
            check_keyup_events(flag,event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_start_button(ai_settings,screen,game_stats, start_button, mouse_x, mouse_y,ship,
                       aliens,bullets,hearts)

def check_start_button(ai_settings,screen,game_stats,start_button,mouse_x,mouse_y,ship,aliens,bullets,hearts):
    #start
    if start_button.rect.collidepoint(mouse_x,mouse_y) and not game_stats.game_active:
        start(ai_settings, screen, game_stats,ship, aliens, bullets, hearts)

def start(ai_settings,screen,game_stats,ship,aliens,bullets,hearts):
    pygame.mouse.set_visible(False)

    game_stats.reset_stats()
    game_stats.game_active = True
    ship.center_ship()
    aliens.empty()
    bullets.empty()
    while len(hearts):
        hearts.pop()
    create_fleet(ai_settings, screen, aliens, game_stats)
    create_hearts(ai_settings, screen, hearts)

def update_bullets(flag,bullets,ai_settings, screen, ship,aliens,game_stats,bg_image):
    bullets.update()
    check_bullets_aligns_collisions(ai_settings, screen, bullets, aliens,game_stats,bg_image,ship)
    add_bullets(flag,bullets,ai_settings, screen, ship)
    del_bullets(flag,bullets,ai_settings, screen, ship)

def check_bullets_aligns_collisions(ai_settings,screen,bullets,aliens,game_stats,bg_image,ship):
    level = game_stats.level
    collision = None
    if level != 10 :
         collision =pygame.sprite.groupcollide(bullets, aliens, True, True)
         if len(aliens) == 0:
             next_level(ai_settings, screen, aliens, bullets, bg_image, game_stats,ship)
    else:
        #boss guan
        collision = pygame.sprite.groupcollide(bullets, aliens, True, False)
        if collision:
            for boss in aliens:
                boss.heart -= 1
                if boss.heart <= 0:
                    # win
                    show_win(game_stats)
    if collision:
        add_score(game_stats, level)

def add_score(game_stats,level):
    game_stats.score += level

def next_level(ai_settings, screen, aliens,bullets,bg_image,game_stats,ship):
    game_stats.level += 1
    bullets.empty()
    create_fleet(ai_settings, screen, aliens, game_stats)
    bg_image = Image(screen,"images/level_1.jpg",screen.get_rect())

def show_win(game_stats):
    game_stats.game_active = False
    game_stats.game_over = True
    game_stats.game_win = True

def add_bullets(flag,bullets,ai_settings, screen, ship):
    if flag['add_bullet_flag'] == True:
        flag['add_bullet_interval'] -= 1
        if flag['add_bullet_interval'] == 0 :
            flag['add_bullet_interval'] = ai_settings.add_bullet_interval
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def del_bullets(flag,bullets,ai_settings, screen, ship):
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ai_settings,screen,ship,bullets,aliens,hearts,bg_image,game_stats):
    #清空屏幕并填充背景
    screen_rect = screen.get_rect()

    show_bgimage(bg_image)
    show_score(screen, game_stats)
    show_level(screen, game_stats)

    ship.blitme()
    for bullet in bullets:
        bullet.draw()
    for alien in aliens:
        alien.blitme()
    for heart in hearts:
        heart.blitme()

    pygame.display.flip()

def show_bgimage(bg_image):
    bg_image.draw()

def show_score(screen,game_stats):
    #显示分数
    score = game_stats.score
    score_image = Message(screen,"score:"+str(score),30,(255,0,0),200,15)
    score_image.draw()

def show_level(screen,game_stats):
    level = game_stats.level
    level_image = Message(screen, "level:" + str(level), 30, (0, 255, 0), 50, 15)
    level_image.draw()

def get_alien_number_each_line(ai_settings,screen,aliens,level):
    alien_width = Alien(ai_settings, screen, level).rect.width
    alien_line_number = int(ai_settings.screen_width / (2 * alien_width))
    return alien_line_number

def create_aliens_line(ai_settings, screen,aliens, game_stats,alien_line_number,rect_y):
    level = game_stats.level
    for alien_number in range(alien_line_number):
        alien = Alien(ai_settings, screen, level)

        alien.move_l_or_r = int(uniform(0,2))

        alien.rect_x = alien.rect.x = uniform(1.5,2) * alien.rect.width * alien_number
        alien.rect_y = alien.rect.y = uniform(1.5,2)*rect_y*alien.rect.height

        alien.xspeed_factor = uniform(0.5,1.5)*ai_settings.alien_speed[level - 1][0]
        alien.yspeed_factor = uniform(0.5,1.5)*ai_settings.alien_speed[level - 1][1]

        aliens.add(alien)

def create_fleet(ai_settings,screen,aliens,game_stats):
    level = game_stats.level
    if level == 10:
        create_boss(ai_settings,screen,aliens,level)
    else:
        alien_number_each_line=get_alien_number_each_line(ai_settings,screen,aliens,level)
        alien_line=ai_settings.alien_lines_by_level[level-1]
        for rect_y in range(alien_line):
            create_aliens_line(ai_settings, screen, aliens, game_stats, alien_number_each_line,rect_y)

def create_boss(ai_settings,screen,aliens,level):
    boss = Boss(ai_settings,screen,level)

    boss.rect_x = boss.rect.x = screen.get_rect().centerx
    boss.rect_y = boss.rect.y = 0

    boss.xspeed_factor = uniform(1, 1.5) * ai_settings.alien_speed[level - 1][0]
    boss.yspeed_factor = uniform(1, 1.5) * ai_settings.alien_speed[level - 1][1]

    move_l_or_r = int(uniform(0, 2))

    aliens.add(boss)

def update_aliens(ai_settings,screen,aliens,ship,game_stats,hearts):
    if len(aliens) :
        change_aliens_direction(ai_settings, aliens)
        aliens.update()
        ship_hit(screen, ship, aliens, hearts, game_stats)

def ship_hit(screen,ship,aliens,hearts,game_stats):
    if pygame.sprite.spritecollideany(ship, aliens):
        if ship.invincible == True:
            return
        else:
            game_stats.ships_left -= 1
            if game_stats.ships_left >= 0:
                revive(ship, screen, hearts)
            else:
                #lose
                show_lose(game_stats)

def show_lose(game_stats):
    game_stats.game_active = False
    game_stats.game_over = True
    game_stats.game_win = False

def revive(ship,screen,hearts):
    print("revive")
    hearts.pop()
    ship.center_ship()
    ship.invincible = True
    sleep(0.5)

def game_over(ai_settings,screen,game_stats,start_button,ship,bullets,aliens,hearts,bg_image):
    pygame.mouse.set_visible(True)

    screen_rect =screen.get_rect()

    ship.rect_centerx = screen_rect.centerx
    ship.rect_centery = screen_rect.centery

    aliens.empty()
    bullets.empty()

    update_screen(ai_settings,screen,ship,bullets,aliens,hearts,bg_image,game_stats)
    sleep(0.3)

    show_over_image(ai_settings, screen)
    show_over_score(screen, game_stats)
    show_win_or_lose(game_stats, screen)
    start_button.draw()

    pygame.display.flip()
    game_stats.game_over = False

def show_over_image(ai_settings,screen):
    screen_rect = screen.get_rect()
    over_image = pygame.image.load(ai_settings.game_over_image_path)
    screen.blit(over_image, screen_rect)

def show_over_score(screen,game_stats):
    screen_rect = screen.get_rect()
    score = Message(screen, "score:" + str(game_stats.score),
                    40, (255, 0, 0), screen_rect.centerx, screen_rect.centery / 2)
    score.draw()

def show_win_or_lose(game_stats,screen):
    screen_rect = screen.get_rect()
    if game_stats.game_win == True:
        str_win = Message(screen, 'you win !',
                    60, (255, 255, 0), screen_rect.centerx, screen_rect.centery / 4)
        str_win.draw()
    else :
        str_lose = Message(screen, 'have a good game ',
                    50, (255, 255, 0), screen_rect.centerx, screen_rect.centery / 4)
        str_lose.draw()

def change_aliens_direction(ai_settings,aliens):
    for alien in aliens:
        if alien.rect.right >= ai_settings.screen_width :
            alien.move_l_or_r = 0
        elif alien.rect.left <= 0 :
            alien.move_l_or_r = 1

        if alien.rect.top <= 0:
            alien.move_t_or_b = 1
        elif alien.rect.bottom >= ai_settings.screen_height:
            alien.move_t_or_b = 0

def create_hearts(ai_settings,screen,hearts):
    for heart_index in range(ai_settings.ship_limit):
        heart = Heart(screen)
        heart.rect.x =ai_settings.screen_width - \
            1.2*heart.rect.width*(ai_settings.ship_limit-heart_index)
        hearts.append(heart)


