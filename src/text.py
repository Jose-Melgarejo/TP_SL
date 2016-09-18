import pygame
from tool import *
from globals import *
class Text:
    logo = None
    def __init__(self,screen,name):
        self.screen = screen
        self.text = load_file(name)
        if not self.logo:
            self.logo = load_image("logo")
        self.soud_select = load_sound("select")   
    
    def run(self):
        flag = True
        while flag:
            self.screen.blit(load_image("background"), self.screen.get_rect())
            colour =  WHITE
            for i in range(len(self.text)):
                title = self.text[i]
                image = smallfont.render(title,True,colour)
                rect = image.get_rect()
                rect.centerx = self.screen.get_rect().centerx
                rect.top = self.logo.get_height() + i * rect.height * 1.1
                self.screen.blit(image, rect)
            rect = self.logo.get_rect()
            rect.centerx = self.screen.get_rect().centerx
            rect.top = 0
            self.screen.blit(self.logo, rect)
            pygame.display.flip()
            pygame.event.post(pygame.event.wait())
            for event in pygame.event.get():
                if event.type == QUIT:
                    flag = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE or event.key == K_RETURN or event.key == K_ESCAPE:
                        flag = False
                        if Options.sound == True:
                            self.soud_select.play()