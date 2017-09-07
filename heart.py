import pygame

class Heart():

    def __init__(self,screen):
        self.image = pygame.image.load('images/heart.png')
        self.screen = screen
        self.rect=self.image.get_rect()
        self.rect.y = 5

    def blitme(self):
        self.screen.blit(self.image, self.rect)