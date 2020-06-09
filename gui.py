import pygame
from pygame.locals import *
import sys


pygame.init() #encapsula la libreria sdl (entra a la pantalla al teclado, todo el paripe multimedia de nuestra maquina)

pantalla = pygame.display.set_mode((600,400)) #tomar control de la pantalla y tamaño
pygame.display.set_caption("Hola Mundo")

rojo = 0
direccion = 1
juego_activo = True
while juego_activo:
    for event in pygame.event.get():
        if event.type == QUIT: #boton de cierre de ventana
            juego_activo = False
            
    if rojo >= 255:
        direccion= -1

    if rojo <= 0:
        direccion = 1
    if rojo <= 0:
        direccion = 1 

    rojo += direccion

    pantalla.fill((rojo,0,0)) #para colores
    pygame.display.flip() #pinta la pantalla, sin esto no hay color, no se actualiza

    pygame.time.delay(10) #para que se apague, es en milisegundos

pygame.quit()
sys.exit()



