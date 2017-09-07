from random import uniform

import pygame
from pygame.sprite import Sprite

class Boss(Sprite):

    def __init__(self,ai_settings,screen,level):
        super().__init__()

        self.ai_settings =ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        image_path = 'images/boss.png'
        self.image = pygame.image.load(image_path)

        self.xspeed_factor = ai_settings.alien_speed[level-1][0]
        self.yspeed_factor = ai_settings.alien_speed[level-1][1]

        self.rect = self.image.get_rect()
        self.rect_x = float(self.rect.x)
        self.rect_y = float(self.rect.y)

        self.move_l_or_r = 1
        self.move_t_or_b = 1

        self.heart = ai_settings.boss_heart

    def update(self):
        if self.move_l_or_r:
            self.rect_x += self.xspeed_factor
        else :
            self.rect_x -= self.xspeed_factor
        self.rect.x = self.rect_x

        if self.move_t_or_b:
             self.rect_y += self.yspeed_factor
        else:
             self.rect_y -= self.yspeed_factor
        self.rect.y = self.rect_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)