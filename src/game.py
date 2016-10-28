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
from modulos import *

class game:
    def __init__(self, screen):
        self.screen = screen
        self.t = 0
        self.dificultad = 0
        self.sea = Sea.global_sea
        self.sea_sprite = pygame.sprite.Group()
        self.sea_sprite.add(self.sea)
        self.flag = True
        pygame.display.flip()
        self.lista_proyectiles = pygame.sprite.Group();
        self.lista_embarcacion = pygame.sprite.Group();
        self.lista_oceano = pygame.sprite.Group();
        self.lista_avion = pygame.sprite.Group();
###############################
        self.nubeImg = pygame.image.load('data/image/cloud.png')
    def run(self):
        fps,lead = self.definirDificultad(self.dificultad);
        puntuacion = 0
        #DEFINIMOS LOS OBJETOS PRINCIPALES
        avion = Avion(75,132,10,1000);
        oceano = Oceano(0,SCREEN_HEIGHT-27,lead/2);
        managerProyectiles = ManagerProyectiles(SCREEN_WIDTH,140,lead+30);
        ###############################
    
        self.lista_oceano.add(oceano)
        self.lista_avion.add(avion) #Agregamos los objetos anteriores a una lista.
    
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
                    elif event.key == pygame.K_UP:
                        avion.subir()
                    elif event.key == pygame.K_RIGHT:
                        avion.soltarBomba()
                        puntuacion -= 10;
                    elif event.key == pygame.K_DOWN:
                        avion.bajar()
            self.blitImg(self.nubeImg,pos_x_nube,30)
            self.blitImg(self.nubeImg,pos_x_nube2,20)
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

    
            #SE DEFINE CUANDO EMPIEZAN Y TERMINAN LOS ATAQUES NAVALES INGLESES Y CUANDO MOSTRAR LA EMBARCACION ATACANTE
            tiempo_critico = duracion_paz + duracion_hostilidad #En el tiempo critico el ataque se detiene
            
            if (segundos_que_pasaron == duracion_paz and contador == 0):
                managerProyectiles.atacar = True;
            elif (segundos_que_pasaron == tiempo_critico and contador == 10):
                managerProyectiles.atacar = False;
            elif (segundos_que_pasaron == tiempo_critico + 3 and contador == 0):
                avion.configurarModoAtaque()
            elif (segundos_que_pasaron == tiempo_critico + 5 and contador == 0):
                embarcacion = Embarcacion(SCREEN_WIDTH,SCREEN_HEIGHT,lead+30,1000); #original
                self.lista_embarcacion.add(embarcacion);
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
                list_barco_impacto = pygame.sprite.spritecollide(avion.bomba_avion, self.lista_embarcacion, False)
                if (len(list_barco_impacto) == 1):
                    print "The Ship was hit!"
                    barco_impactado = True;
                    avion.bomba_avion.kill();
                    avion.bomba_avion = None;
                    puntuacion += 110
                    
            ###############################
    
            #UPDATEO Y DIBUJO LOS GRUPOS DE SPRITES
            self.updateAndDrawFromList(managerProyectiles.lista_proyectiles)
            self.updateAndDrawFromList(avion.lista_bombas)
            self.updateAndDrawFromList(self.lista_avion)
            self.updateAndDrawFromList(self.lista_oceano)
            self.updateAndDrawFromList(self.lista_embarcacion)
            ###############################
            
            pygame.display.update();
            clock.tick(fps);
    
            if (salir_del_juego):
                puntuacion = puntuacion - (10 * impactos_recibidos)
                avion.kill();
                managerProyectiles.destruirProyectiles()
        
        return  puntuacion      
            
    def draw(self):
        self.sea_sprite.draw(self.screen)
    def updateAndDrawFromList(self,lista):
        lista.update();
        lista.draw(self.screen)   

    def definirDificultad(self,valor):
        if (valor <= 0): return 14,25 #CADETE
        if (valor == 1): return 22,20 #CAPITAN
        if (valor >= 2): return 25,18 #HALCON

    def blitImg(self,img,x,y):
        self.screen.blit(img,(x,y));
  
