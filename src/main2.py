import pygame 
from modulos import *
pygame.init();

#RESOLUCION Y TITULO DE VENTANA
width_s, height_s = 800, 200;
pantalla = pygame.display.set_mode((width_s,height_s)); #Sets resolution
pygame.display.set_caption('1982'); #Sets game's name.
###############################

#DEFINIMOS LAS LISTAS DE SPRITES
lista_proyectiles = pygame.sprite.Group();
lista_embarcacion = pygame.sprite.Group();
lista_oceano = pygame.sprite.Group();
lista_avion = pygame.sprite.Group();
###############################
nubeImg = pygame.image.load('data/image/cloud.png')

def updateAndDrawFromList(lista):
    lista.update();
    lista.draw(pantalla);   

def definirDificultad(valor):
    if (valor <= 0): return 14,25; #CADETE
    if (valor == 1): return 22,20; #CAPITAN
    if (valor >= 2): return 25,18; #HALCON

def blitImg(img,x,y):
    pantalla.blit(img,(x,y));
    
def main_loop(dificultad):
    fps,lead = definirDificultad(dificultad);
    
    #DEFINIMOS LOS OBJETOS PRINCIPALES
    avion = Avion(75,132,50,1000);
    oceano = Oceano(0,height_s-27,lead/2);
    managerProyectiles = ManagerProyectiles(width_s,140,lead+30);
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
    tiempo_al_momento_del_derribo = -1
    barco_impactado = False;
    puntuacion = 100;

    pos_x_nube = 800;
    pos_x_nube2 = 400;


    while not salir_del_juego:
        pantalla.fill((255,255,255)); #Pintamos de blanco toda la pantalla
        blitImg(nubeImg,pos_x_nube,30)
        blitImg(nubeImg,pos_x_nube2,20)
        pos_x_nube -= lead - 10
        pos_x_nube2 -= lead - 10
        if (pos_x_nube < -100):
            pos_x_nube = 800;
        if (pos_x_nube2 < -100):
            pos_x_nube2 = 800;
        
        if (contador == fps):
            contador = 0;
            segundos_que_pasaron += 1;
        else:
            contador += 1
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    avion.subir()
                elif event.key == pygame.K_RIGHT:
                    avion.soltarBomba()
                    puntuacion -= 10;
                elif event.key == pygame.K_ESCAPE:
                    salir_del_juego = True
                    puntuacion = 0;
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    avion.bajar()

        #SE DEFINE CUANDO EMPIEZAN Y TERMINAN LOS ATAQUES NAVALES INGLESES Y CUANDO MOSTRAR LA EMBARCACION ATACANTE
        tiempo_critico = duracion_paz + duracion_hostilidad #En el tiempo critico el ataque se detiene
        
        if (segundos_que_pasaron == duracion_paz and contador == 0):
            managerProyectiles.atacar = True;
        elif (segundos_que_pasaron == tiempo_critico and contador == 10):
            managerProyectiles.atacar = False;
        elif (segundos_que_pasaron == tiempo_critico + 3 and contador == 0):
            avion.configurarModoAtaque()
        elif (segundos_que_pasaron == tiempo_critico + 5 and contador == 0):
            embarcacion = Embarcacion(width_s,height_s-27-40,lead+30,1000); #original
            lista_embarcacion.add(embarcacion);
        elif (segundos_que_pasaron == tiempo_critico + 10 and contador == 0):
            salir_del_juego = True;
        ###############################

        #LOS INGLESES REALIZAN DISPAROS Y SE CHEQUEA SI ALGUNO IMPACTA EN EL AVION ARGENTINO
        if (contador == 4 or contador == 8 or contador == 12 or contador == 16 or contador == 20 or contador == 24):
            managerProyectiles.disparar()
            
        lista_impactos = pygame.sprite.spritecollide(avion, managerProyectiles.lista_proyectiles, True)
        impactos_recibidos += len(lista_impactos);

        #if (segundos_que_pasaron == tiempo_al_momento_del_derribo + 4):
            #salir_del_juego = True;

        if (impactos_recibidos == soporte_maximo_disparos):
            avion.estrellar();
            managerProyectiles.atacar = False;
            tiempo_al_momento_del_derribo = segundos_que_pasaron;
            puntuacion = 0;

        if (impactos_recibidos > aux):
            aux = impactos_recibidos

        if not avion.bomba_avion == None:
            list_barco_impacto = pygame.sprite.spritecollide(avion.bomba_avion, lista_embarcacion, False)
            if (len(list_barco_impacto) == 1):
                print "The Ship was hit!"
                barco_impactado = True;
                avion.bomba_avion.kill();
                avion.bomba_avion = None;
                puntuacion += 110
                
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

        if (salir_del_juego):
            puntuacion = puntuacion - (10 * impactos_recibidos)
            if (puntuacion < 0):
                puntuacion = 0;
            avion.kill();
            managerProyectiles.destruirProyectiles()
        
    return puntuacion;
    #pygame.quit()
    #quit()
