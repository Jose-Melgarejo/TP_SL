import pygame
import tool
import os
import sys

from globals import *
from sea import *
from menu import Menu
from scores import Scores
from text import Text
from game import *
from option import Option
from tool import load_file, str_to_bool, read_scores, write_scores
from main2 import main_loop
import scores
def main():
    #esto es para centrar la pantalla
    os.environ['SDL_VIDEO_CENTERED'] = "1"
    
    pygame.init()
    #mouse invisible 
    pygame.mouse.set_visible(0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_icon(tool.load_image("skyhaw"))
    pygame.display.set_caption(NAME)
    f = load_file("options")
    c = 0
    for value in f:
        c+=1
        if c == 1:
            Options.music = str_to_bool(value)
        if  c == 2:
            Options.sound = str_to_bool(value)
        if  c == 3:
            Options.playername = value      
    tool.load_music("music")
    #aca se controla con un if las  opciones de musica on/off
    if Options.music == True:
        pygame.mixer.music.play(-1)
    main_selection = 0
    Sea.global_sea = Sea()
    while not main_selection == 6:
        main_selection = Menu(screen, ("Jugar", "Historia","Mejores Puntos", "Opciones", "Ayuda","Creditos","Salir"), main_selection).run()
        if main_selection == 0:
            dificultad = 0; 
            dificultad = Menu(screen,("Cadete","Teniente","Halcon"),dificultad).run()
            if (dificultad is not 6):
                screen = pygame.display.set_mode((800, 200))
                puntos = main_loop(dificultad)
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                
                objScores = Scores(screen,dificultad);
                objScores.scores,res = objScores.loadNewScore(Options.playername, puntos, dificultad);
                if (res):
                    objScores.run()
        elif main_selection == 1: 
            Text(screen,"history").run()
            #Historia
        elif main_selection == 2: 
            view = 0
            view = Menu(screen,("Cadete","Teniente","Halcon"),view).run()
            if (view is not 6):
                Scores(screen,view).run() 
            #Mejores Puntos 
        elif main_selection == 3: 
            Option(screen).run()
            #Opciones        
        elif main_selection == 4: 
            Text(screen,"help").run()  
        elif main_selection == 5: 
            Text(screen,"credit").run()
        pygame.display.update()
    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    main()
