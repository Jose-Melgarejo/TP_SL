import pygame
from globals import *
from tool import *

class Menu:
    logo = None

    def __init__(self, screen, menu, selection = 0):
        self.screen = screen
        if not self.logo:
            self.logo = load_image("logo")
        self.menu = menu
        self.selection = selection
        self.soud_select= load_sound("select")

    def run(self):
        done = True
        while done:
            self.screen.blit(load_image("background"), self.screen.get_rect())
            for i in range(len(self.menu)):
                self.render(i)
            
            rect = self.logo.get_rect()
            rect.centerx = self.screen.get_rect().centerx
            rect.top = 0
            self.screen.blit(self.logo, rect)
            pygame.display.flip()
            pygame.event.post(pygame.event.wait())
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.selection = 6
                    done = False
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.move_up()
                    elif event.key == K_DOWN:
                        self.move_down()
                    elif event.key == K_SPACE or event.key == K_RETURN :
                        done = False
                    elif event.key == K_ESCAPE:
                        self.selection = 6
                        done = False
        return self.selection
    


    def move_down(self):
        if Options.sound == True:
            self.soud_select.play()
        self.selection += 1
        if self.selection >= len(self.menu):
            self.selection = len(self.menu) - 1

    def move_up(self):
        if Options.sound == True:
            self.soud_select.play()
        self.selection -= 1
        if self.selection < 0:
            self.selection = 0

    def render(self, i):
        colour =  GRIS
        if self.selection == i:
            colour = RED
        title = self.menu[i]
        image = font.render(title,True,colour)
        rect = image.get_rect()
        rect.centerx = self.screen.get_rect().centerx
        rect.top = self.logo.get_height() + i * rect.height * 1.1
        self.screen.blit(image, rect)