import pygame
import codecs
from globals import *

pygame.font.init()
font = pygame.font.Font("data/font/myfont.ttf", 40)
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
def update_option():
    file = open("data/file/options.txt","w")
    array_file = []
    if Options.music==True :
        print>>file,"true"
    else:
        print>>file,"false"
    if Options.sound==True :
        print>>file,"true"
    else:
        print>>file,"false"
    print>>file,Options.playername   
    file.close()
def str_to_bool(text):
    ltext = text.lower().strip()
    if ltext in ("on", "true", "yes"):
        return True
    else:
        return False
    
def write_scores(scores):
    try:
        f = codecs.open("data/file/higscore.txt", "w", "utf_8")
        for i in xrange(10):
            print >> f,scores[i][0]
            print >> f,scores[i][1]
            f.close()
    except:
        print "Error al cargar mejores puntos" 
        return

def read_scores(difficult):
    score = []
    f = codecs.open("data/file/higscore"+str(difficult)+".txt", "r", "utf_8")
    i = 0
    name, point = "", 0
    for line in f:
        if i % 2 == 0:
            name = line.strip()
        else:
            point = int(line)
            score.append((name, point))
        
        i += 1
    return score

