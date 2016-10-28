import pygame
import codecs
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
    
"""def write_scores(scores):
    try:
        f = codecs.open("data/file/higscore.txt", "w", "utf_8")
        for i in xrange(5):
            print >> f,scores[i][0]
            print >> f,scores[i][1]
    except:
        print "Error al cargar mejores puntos" 
        return"""

def write_scores(scores,difficult):
    try:
        f = codecs.open("data/file/higscore"+str(difficult)+".txt", "w", "utf_8")
        for i in xrange(5):
            print >> f,scores[i][0]
            print >> f,scores[i][1]
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

    size_of_list = len(score);
    ordered_score = []
    
    for i in range(0,size_of_list):
        ordered_score.append(get_min_value(score));

    ordered_score.reverse();
    return ordered_score;

def get_min_value(scores):
    output = ();
    min_score = 0;
    min_index = -1;
    i = 0;
    for element in scores:
        if (i == 0):
            min_score = element[1];
            min_index = 0;
        else:
            if (element[1] < min_score):
                min_score = element[1];
                min_index = i;
        i+=1;
    output = scores[min_index]
    scores.remove(output);
    return output;

