import pygame
from pygame.locals import *
from maze import *
from char import *



WIDTH = sprite_nb * sprite_size
HEIGHT = sprite_nb * sprite_size

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
