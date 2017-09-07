import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):
        super().__init__()
        self.ai_settings =ai_settings
        self.screen = screen
        self.ship = ship
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
              ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top =ship.rect.top

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        self.rect_y = float(self.rect.y)

    def update(self):
            self.rect_y -= self.speed_factor
            self.rect.y = self.rect_y

    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.rect)