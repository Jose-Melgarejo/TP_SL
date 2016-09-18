import pygame
from globals import *

pygame.font.init()
font = pygame.font.Font("data/font/myfont.ttf", 70)
smallfont = pygame.font.Font("data/font/text.ttf", 30)

def load_image(name):
    # devuelve la imagen 
    image = pygame.image.load("data/image/" + name + ".png").convert_alpha()
    return image

def load_sound(name):
    # devuelve el archivo de sonido 
    return pygame.mixer.Sound("data/sound/" + name + ".ogg")

def load_music(name):
    # devuelve el archivo de sonido de fondo
    pygame.mixer.music.load("data/music/" + name + ".mp3")
    
def load_file(name):
    file = open("data/file/"+name+".txt","r")
    array_file = []
    for i in file.readlines():
        i = i.replace("\n", "")
        array_file.append(i)
    return array_file
def str_to_bool(text):
    ltext = text.lower().strip()
    if ltext in ("on", "true", "yes"):
        return True
    else:
        return False