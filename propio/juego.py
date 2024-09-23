import pygame
from personaje import Cubo

#pip install pygame
# en caso de que no nos deje isntalar pygame desde terminal se debe revisar que 
# las carpetas de direccion de python y de script de python esten en el PATH de nuestro WINDOWS
# para estos de debe ingresar a variables de entorno y añadir las dos direcciones

# si aun corrigiendo esos errores sigue sin dar, ir a 
# View -> Comannd Palette -> select interpreter -> interatar uno que este ahi

ANCHO = 900
ALTO = 500
VENTANA = pygame.display.set_mode([ANCHO,ALTO])

jugando = True

cubo = Cubo(50, 50)

while jugando:
    eventos = pygame.event.get()

    for evento in eventos :
        if evento.type == pygame.QUIT:
            jugando = False
    
    cubo.dibujar(VENTANA)

    pygame.display.update()
quit()