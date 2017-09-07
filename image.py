import pygame

class Image():

    def __init__(self,screen,path,rect):
        self.screen = screen
        self.image = pygame.image.load(path)
        self.rect = rect

    def draw(self):
        self.screen.blit(self.image,self.rect)