import pygame
import random

class Avion(pygame.sprite.Sprite):
    lista_bombas = pygame.sprite.Group()
    modo_ataque = False;
    ataque_realizado = False;
    bomba_avion = None;
    
    def __init__(self, p_posx, p_posy, p_bloque, puntos_resistencia):
        # Llama al constructor de la clase padre (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('imagenes/skyhawkb.gif');
        self.rect = self.image.get_rect();
        self.rect.width = self.rect.width * .9
        self.rect.x = p_posx;
        self.rect.y = p_posy;
        self.bloque = p_bloque;
        self.puntos_resistencia = puntos_resistencia;
        self.estrellarse = False;

    def configurarModoAtaque(self):
        if not (self.estrellarse):
            self.rect.y = 82
            self.modo_ataque = True;

    def subir(self):
        if not (self.estrellarse) and not (self.modo_ataque) and not (self.ataque_realizado):
            self.rect.y -= self.bloque;

    def bajar(self):
        if not (self.estrellarse) and not (self.modo_ataque) and not (self.ataque_realizado):
            self.rect.y += self.bloque;

    def soltarBomba(self):
        if (self.modo_ataque):
            print "atacando"
            self.bomba_avion = Bomba(self.rect.x+3,self.rect.y,self.bloque)
            self.lista_bombas.add(self.bomba_avion)
            self.modo_ataque = False;
            self.ataque_realizado = True

    def estrellar(self):
        self.estrellarse = True;

    def update(self):
        if (self.estrellarse):
            self.rect.y += (self.bloque * 0.1);
            self.rect.x -= (self.bloque * 0.05);
            self.image = pygame.transform.rotate(self.image, -0.1)
            if (self.rect.y > 200):
                self.kill();

class Bomba(pygame.sprite.Sprite):
    velocidad_caida = 0.05
    
    def __init__(self, p_posx, p_posy, p_bloque):
        # Llama al constructor de la clase padre (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('imagenes/a4_bomb.png');
        self.rect = self.image.get_rect();
        self.rect.height = self.rect.height * .005
        self.rect.x = p_posx;
        self.rect.y = p_posy;
        self.bloque = p_bloque;

    def update(self):
        self.rect.y += (self.bloque * self.velocidad_caida);
        self.rect.x -= (self.bloque * 0.01);
        self.velocidad_caida *= 1.05
        if (self.rect.y > 200):
            self.kill();        

class Embarcacion(pygame.sprite.Sprite):
    def __init__(self, p_posx, p_posy, p_bloque, puntos_resistencia):
        # Llama al constructor de la clase padre (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('imagenes/coventry_c.png');
        self.rect = self.image.get_rect();
        #self.rect.height = self.rect.height * .1
        self.rect.x = p_posx;
        self.rect.y = p_posy;
        self.bloque = p_bloque;
        self.puntos_resistencia = puntos_resistencia;

    def update(self):
        self.rect.x -= self.bloque;
        if (self.rect.x < -self.rect.width):
            self.kill();

class Oceano(pygame.sprite.Sprite):
    def __init__(self, p_posx, p_posy, p_bloque):
        # Llama al constructor de la clase padre (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('imagenes/ocean.png');
        self.rect = self.image.get_rect();
        self.rect.x = p_posx;
        self.rect.y = p_posy;
        self.bloque = p_bloque;

    def update(self):
        if (self.rect.x == -self.bloque):
            self.rect.x = 0;
        else:
            self.rect.x -= self.bloque;

class ManagerProyectiles():
    lista_proyectiles = pygame.sprite.Group()
    atacar = False;

    def __init__(self, p_posx, p_posy, p_bloque):
        self.posx = p_posx;
        self.posy = p_posy;
        self.bloque = p_bloque;
    
    def disparar(self):
        if (self.atacar):
            aux = self.posy;
            if (random.randint(1, 2) == 2):
                aux = self.posy - self.bloque;
            proyectil = Proyectil(self.posx,aux,self.bloque)
            self.lista_proyectiles.add(proyectil)

    def destruirProyectiles(self):
        self.lista_proyectiles.empty()

    #def update(self):
    #    for proyectil in lista_proyectiles:
            

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, p_posx, p_posy, p_bloque):
        # Llama al constructor de la clase padre (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('imagenes/municion_naval.png');
        self.rect = self.image.get_rect();
        self.rect.width = self.rect.width * .9
        self.rect.x = p_posx;
        self.rect.y = p_posy;
        self.bloque = p_bloque;

    def update(self):
        self.rect.x -= self.bloque;
        if (self.rect.x < 0):
            self.kill();

    

    
        
        
        

    
