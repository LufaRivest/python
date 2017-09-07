import pygame

class Button():

    def __init__(self,screen,msg,width,height,centerx,centery):
        self.screen = screen
        self.secreen_rect =screen.get_rect()
        self.msg = msg

        self.text_color = (255,0,0)
        self.font = pygame.font.SysFont(None,48)

        self.button_color = (0,255,255)
        self.width ,self.height= width,height
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.centerx = centerx
        self.rect.centery = centery

        self.prep_msg()

    def prep_msg(self):
        self.msg_image = self.font.render(self.msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

