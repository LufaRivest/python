import pygame

class Message():

    def __init__(self,screen,msg,size,color,centerx,centery):
        self.screen = screen
        self.secreen_rect =screen.get_rect()
        self.msg = msg

        self.text_color = color
        self.font = pygame.font.SysFont(None,size)

        self.centerx = centerx
        self.centery = centery
        self.prep_msg()

    def prep_msg(self):
        self.msg_image = self.font.render(self.msg,True,self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.centerx
        self.msg_image_rect.centery = self.centery


    def draw(self):
        self.screen.blit(self.msg_image,self.msg_image_rect)

