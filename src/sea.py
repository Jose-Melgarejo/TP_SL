import pygame
import math

from globals import *

class Sea(pygame.sprite.Sprite):
    global_sea = None
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()

       

        self.sea_levels = []
        for i in xrange(self.rect.width):
            self.sea_levels.append(0.0)
        self.t = 0


        self.target_amplitude = self.amplitude = SCREEN_HEIGHT / 200.0
        self.target_wavelength = self.wavelength = 0.001 * SCREEN_WIDTH / 2.0 / math.pi
        self.target_speed = self.speed = 0.1 / math.pi / 2.0 * 100
        self.target_baseheight = self.baseheight = SCREEN_HEIGHT / 24.0 * 3.0
        self.xmul = 2.0 * math.pi / self.wavelength / float(SCREEN_WIDTH)
        self.tmul = math.pi * 2.0 / float(FPS) * self.speed
        self.update()
    
    def update(self):
        self.image.fill((200,210,255,0))
        for x in xrange(self.rect.width):
            h = SCREEN_HEIGHT - (math.sin(x * self.xmul + self.t * self.tmul) * self.amplitude + self.baseheight)
            self.sea_levels[x] = h
            h_float,h_int=math.modf(h)
            pygame.draw.line(self.image, (20, 60, 180,110), (x, h_int+1), (x, SCREEN_HEIGHT))

        if self.target_amplitude != self.amplitude:
            self.amplitude = 0.99 * self.amplitude + 0.01 * self.target_amplitude
        if self.target_wavelength != self.wavelength:
            self.wavelength = 0.99 * self.wavelength + 0.01 * self.target_wavelength
            self.xmul = 2.0 * math.pi / self.wavelength / float(SCREEN_WIDTH)
        if self.target_speed != self.speed:
            self.speed = 0.99 * self.speed + 0.01 * self.target_speed
            self.tmul = math.pi * 2.0 / float(FPS) * self.speed
        if self.target_baseheight != self.baseheight:
            self.baseheight = 0.99 * self.baseheight + 0.01 * self.target_baseheight

        self.t += 1            

    def get_sea_level(self, x):
        if x >= len(self.sea_levels):
            return self.sea_levels[len(self.sea_levels) - 1]
        elif x < 0:
            return self.sea_levels[0]
        return self.sea_levels[int(x)]
