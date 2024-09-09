import pygame

#pip install pygame
# en caso de que no nos deje isntalar pygame desde terminal se debe revisar que 
# las carpetas de direccion de python y de script de python esten en el PATH de nuestro WINDOWS
# para estos de debe ingresar a variables de entorno y añadir las dos direcciones

ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode
([ANCHO,ALTO])

jugando = True
while jugando:
    eventos = pygame.event.get()

    for evento in eventos :
        if evento.type == pygame.QUIT:
            jugando = False

    pygame.display.update()
quit()