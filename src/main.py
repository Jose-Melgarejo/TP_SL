import pygame
import tool
import os
import sys
from globals import *
from menu import Menu
from text import Text
from option import Option
def main():
    #esto es para centrar la pantalla
    os.environ['SDL_VIDEO_CENTERED'] = "1"
    
    pygame.init()
    #mouse invisible 
    pygame.mouse.set_visible(0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_icon(tool.load_image("skyhaw"))
    pygame.display.set_caption(NAME)
    tool.load_music("music")
    #aca se controla con un if las  opciones de musica on/off
    if Options.music == True:
        pygame.mixer.music.play(-1)
    main_selection = 0
    while True:
        main_selection = Menu(screen, ("Jugar", "Historia","Mejores Puntos", "Opciones", "Ayuda","Creditos","Salir"), main_selection).run()
        if main_selection == 0:
            pass
            #cuando tengamos el modulo de game o arena esta tiene que ir aca... ejemplo game.run()
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
        elif main_selection == 6:
            #salir
            pygame.QUIT()
            sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()
