import pygame
import tool
import os
import sys

from globals import *
from sea import *
from menu import Menu
from text import Text
from game import *
from option import Option
from tool import load_file, str_to_bool
from main2 import main_loop
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
            screen = pygame.display.set_mode((800, 200))

            #############Pongo a la fuerza un nivel de dificultad
            dificultad = 0; #va de 0 a 2
            puntos = main_loop(dificultad)   #cuando tengamos el modulo de game o arena esta tiene que ir aca... ejemplo game.run()

            print "puntos: "
            print puntos
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        elif main_selection == 1: 
            Text(screen,"history").run()
            #Historia
        elif main_selection == 2: 
            Text(screen,"highscore").run() 
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
