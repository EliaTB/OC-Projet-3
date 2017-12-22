import pygame
from pygame.locals import *
from laby import *
from perso import *



WIDTH = 600
HEIGHT = 480

# WHITE = (255, 255, 255)
# SQUARE = pygame.draw.rect(screen, WHITE, (x, y, 10, 10))



def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    mainloop()
    
def mainloop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
    pygame.quit()

main()
