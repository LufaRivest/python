import time
import _thread

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from heart import Heart
from button import Button
from image import  Image

class MainGame():

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Alien Invasion")

        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width,
               self.ai_settings.screen_height))
        self.screen_rect =self.screen.get_rect()
        self.bg_image = Image(self.screen,"images/level_1.jpg",self.screen_rect)

        self.start_button = Button(self.screen,"start",120,50,
               self.screen_rect.centerx,self.screen_rect.height*3/5)
        self.init_draw()

        self.game_stats=GameStats(self.ai_settings)
        self.ship = Ship(self.ai_settings, self.screen)
        self.bullets = Group()
        self.aliens = Group()

        self.hearts = []

        self.flag = {'add_bullet_flag': False,
                 'add_bullet_interval':self.ai_settings.add_bullet_interval}

    def run_game(self):
        while True:
            self.check_events()
           # print(len(self.hearts))
            if self.game_stats.game_active == True:
                self.ship.update()
                gf.update_bullets(self.flag,self.bullets,self.ai_settings, self.screen,
                    self.ship,self.aliens,self.game_stats,self.bg_image)
                gf.update_aliens(self.ai_settings,self.screen,self.aliens,self.ship,
                    self.game_stats,self.hearts)
                gf.update_screen(self.ai_settings,self.screen,self.ship,self.bullets,
                    self.aliens,self.hearts,self.bg_image,self.game_stats)

            if self.game_stats.game_over == True:
                gf.game_over(self.ai_settings,self.screen,self.game_stats,self.start_button,
                         self.ship,self.bullets,self.aliens,self.hearts,self.bg_image)

    def check_events(self):
        gf.check_events(self.flag,self.ai_settings,
            self.screen,self.game_stats, self.ship,self.start_button,
                self.aliens,self.bullets,self.hearts)

    def init_draw(self):
        init_image=pygame.image.load(self.ai_settings.init_image_path)
        rect=self.screen.get_rect()
        self.screen.blit(init_image,rect)
        self.start_button.draw()
        pygame.display.flip()

game = MainGame()
game.run_game()









