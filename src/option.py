import pygame
from globals import *
from tool import *

class Option:
    logo = None
    def __init__(self, screen):
        self.screen      = screen
        if not self.logo:
            self.logo    = load_image("logo")
        self.selection   = 0
        self.option      = ()
        self.refresh()
        self.soud_select = load_sound("select")
    
    
    def refresh(self):
        self.option = ("Musica :"+(Options.music and "Activado" or "Desactivado"),
                       "Sonido :"+(Options.sound and "Activado" or "Desactivado"),
                       "Nombre :"+(Options.playername))
    
    def run(self):
        flag = True
        while flag:
            self.screen.blit(load_image("background"), self.screen.get_rect())
            for i in xrange(len(self.option)):
                self.render(i)
            rect = self.logo.get_rect()
            rect.centerx = self.screen.get_rect().centerx
            rect.top = 0
            self.screen.blit(self.logo, rect)
            pygame.display.flip()                  
            for event in pygame.event.get():
                if event.type == QUIT:
                    flag = False
                    if Options.sound == True:
                        self.soud_select.play()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        flag = False  
                        if Options.sound == True:
                            self.soud_select.play() 
                    elif event.key == K_UP:
                        self.move_up()
                    elif event.key == K_DOWN:
                        self.move_down()
                    elif event.key == K_LEFT:
                        self.change()
                    elif event.key == K_RIGHT:
                        self.change()
                    elif self.selection == 2:
                        if event.key == K_BACKSPACE:
                            if len(Options.playername) != 0:
                                Options.playername = Options.playername[:-1]
                                self.refresh()
                        elif event.key == K_SPACE or event.unicode != " " and event.unicode>=u' ':
                            if len(Options.playername) < 30:
                                Options.playername += event.unicode
                            self.refresh()                        
                    elif event.key == K_SPACE or event.key == K_RETURN:
                        self.change()        
                        
                                 
    def change(self):
        if Options.sound == True:
            self.soud_select.play()
        if self.selection == 1:
            Options.sound = not Options.sound
        elif self.selection == 0:
            Options.music = not Options.music
            try:
                if Options.music:
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.stop()
            except:
                pass
        self.refresh()

    def move_down(self):
        if Options.sound == True:
            self.soud_select.play()
        self.selection += 1
        if self.selection >= len(self.option):
            self.selection = len(self.option) - 1

    def move_up(self):
        if Options.sound == True:
            self.soud_select.play()
        self.selection -= 1
        if self.selection < 0:
            self.selection = 0

    def render(self, i):
        color = GRIS
        if self.selection == i:
            color = RED
        title = self.option[i]
        image = smallfont.render(title, True, color)
        rect = image.get_rect()
        rect.centerx = self.screen.get_rect().centerx
        rect.top = self.logo.get_height() + i * rect.height * 1.1
        self.screen.blit(image, rect)