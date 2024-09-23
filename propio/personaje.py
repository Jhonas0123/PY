import pygame

class Cubo: 
    def _init_(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto =50
        self.velocidad =1
        self.color = "red"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
    

    def dibujar(self, ventana):
        pygame.draw.rect(ventana,self.color, self.rect)