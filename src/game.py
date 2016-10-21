import pygame
import pygame
import math
import random
import sys
import os
from pygame.locals import *
from sea import Sea
from globals import *
from tool import *

class game:
    def __init__(self, screen):
        self.screen = screen
        self.t = 0

        self.sea = Sea.global_sea
        self.sea_sprite = pygame.sprite.Group()
        self.sea_sprite.add(self.sea)
        self.flag = True
        pygame.display.flip()
    def run(self):
        while self.flag:
            pygame.display.flip()
            self.screen.blit(load_image("background2"), self.screen.get_rect())
            self.sea.update()
            self.draw()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.selection = 6
                    self.flag = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE or event.key == K_RETURN :
                        self.flag = False
                    elif event.key == K_ESCAPE:
                        self.selection = 6
                        self.flag = False
            
            pygame.display.update()
            
            
    def draw(self):
        self.sea_sprite.draw(self.screen)

  
