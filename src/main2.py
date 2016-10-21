import pygame 
from modulos import *
pygame.init();

#RESOLUCION Y TITULO DE VENTANA
width_s, height_s = 800, 180;
pantalla = pygame.display.set_mode((width_s,height_s)); #Sets resolution
pygame.display.set_caption('1982'); #Sets game's name.
###############################

#DEFINIMOS LAS LISTAS DE SPRITES
lista_proyectiles = pygame.sprite.Group();
lista_embarcacion = pygame.sprite.Group();
lista_oceano = pygame.sprite.Group();
lista_avion = pygame.sprite.Group();
###############################

def updateAndDrawFromList(lista):
    lista.update();
    lista.draw(pantalla);   

def definirDificultad(valor):
    if (valor <= 0): return 14,25; #CADETE 
    if (valor == 1): return 22,20; #CAPITAN
    if (valor >= 2): return 25,18; #HALCON

def blitImg(img,x,y):
    pantalla.blit(img,(x,y));

def main_loop():
    #DEFINIMOS LOS OBJETOS PRINCIPALES
    avion = Avion(75,102,50,1000);
    oceano = Oceano(0,height_s-27,lead/2);
    managerProyectiles = ManagerProyectiles(width_s,110,lead+30);
    ###############################

    lista_oceano.add(oceano)
    lista_avion.add(avion) #Agregamos los objetos anteriores a una lista.

    #SETEAMOS VARIABLES DE TIEMPO Y PARA SALIR DEL JUEGO
    contador,segundos_que_pasaron,salir_del_juego,impactos_recibidos = 0,0,0,0;
    aux = 0;
    clock = pygame.time.Clock();
    
    soporte_maximo_disparos = 10;
    duracion_paz = 3;
    duracion_hostilidad = 15;
    ###############################

    while not salir_del_juego:
        pantalla.fill((255,255,255)); #Pintamos de blanco toda la pantalla
        
        if (contador == fps):
            contador = 0;
            segundos_que_pasaron += 1;
        else:
            contador += 1
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                salir_del_juego = 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    avion.subir()
                if event.key == pygame.K_RIGHT:
                    print "key_right"
                    avion.soltarBomba()                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    avion.bajar()

        #SE DEFINE CUANDO EMPIEZAN Y TERMINAN LOS ATAQUES NAVALES INGLESES Y CUANDO MOSTRAR LA EMBARCACION ATACANTE
        tiempo_critico = duracion_paz + duracion_hostilidad #En el tiempo critico el ataque se detiene
        
        if (segundos_que_pasaron == duracion_paz and contador == 0):
            managerProyectiles.atacar = True;
        elif (segundos_que_pasaron == tiempo_critico and contador == 10):
            managerProyectiles.atacar = False;
        elif (segundos_que_pasaron == tiempo_critico + 1 and contador == 0):
            avion.configurarModoAtaque()
        elif (segundos_que_pasaron == tiempo_critico + 3 and contador == 0):
            embarcacion = Embarcacion(width_s,height_s-27-55,lead+30,1000); #original
            lista_embarcacion.add(embarcacion);
        ###############################

        #LOS INGLESES REALIZAN DISPAROS Y SE CHEQUEA SI ALGUNO IMPACTA EN EL AVION ARGENTINO
        if (contador == 4 or contador == 8 or contador == 12 or contador == 16 or contador == 20 or contador == 24):
            managerProyectiles.disparar()
            
        lista_impactos = pygame.sprite.spritecollide(avion, managerProyectiles.lista_proyectiles, True)
        impactos_recibidos += len(lista_impactos);

        if (impactos_recibidos == soporte_maximo_disparos):
            avion.estrellar();
            managerProyectiles.atacar = False;

        if (impactos_recibidos > aux):
            aux = impactos_recibidos

        if avion.bomba_avion is not None:
            list_barco_impacto = pygame.sprite.spritecollide(avion.bomba_avion, lista_embarcacion, True)
            if (len(list_barco_impacto) == 1):
                print "The Ship was hit!"
                
        ###############################

        #UPDATEO Y DIBUJO LOS GRUPOS DE SPRITES
        updateAndDrawFromList(managerProyectiles.lista_proyectiles)
        updateAndDrawFromList(avion.lista_bombas)
        updateAndDrawFromList(lista_avion)
        updateAndDrawFromList(lista_oceano)
        updateAndDrawFromList(lista_embarcacion)
        ###############################
        
        pygame.display.update();
        clock.tick(fps);
        
    pygame.quit()
    quit()

#DEFINIMOS LA DIFICULTAD (0=Normal 1=Dificil 2=Supervivencia)
fps,lead = definirDificultad(1);

#INICIAMOS EL JUEGO
