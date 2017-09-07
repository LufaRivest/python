import pygame
from pygame.sprite import  Sprite

class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.center_ship()
        self.rect_centerx = float(self.rect.centerx)
        self.rect_centery = float(self.rect.centery)

        self.moving_left=False
        self.moving_right=False
        self.moving_up=False
        self.moving_down=False

        self.invincible = False
        self.invincible_time = self.ai_settings.ship_invincible_time


    def update(self):
        if self.invincible == True:
            self.invincible_time -= 1
            if self.invincible_time == 0 :
                self.invincible = False
                self.invincible_time = self.ai_settings.ship_invincible_time

        if self.moving_left==True and self.rect.left > self.screen_rect.left:
            self.rect_centerx -= self.ai_settings.ship_speed_factor
        if self.moving_right==True and self.rect.right < self.screen_rect.right:
            self.rect_centerx += self.ai_settings.ship_speed_factor
        if self.moving_up==True and self.rect.top > 0:
            self.rect_centery -= self.ai_settings.ship_speed_factor
        if self.moving_down==True and self.rect.bottom < self.screen_rect.bottom:
            self.rect_centery += self.ai_settings.ship_speed_factor

        self.rect.centerx =self.rect_centerx
        self.rect.centery =self.rect_centery

    def center_ship(self):
        self.rect_centerx = self.screen_rect.centerx
        self.rect_centery = self.screen_rect.height * 4 / 5

    def blitme(self):
        self.screen.blit(self.image,self.rect)