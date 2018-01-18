import pygame
from pygame.locals import *
from maze import Maze
from char import Char
from data import *



class Game:

    def __init__(self): 

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("The amazing MacGyver !" )

        self.level = None
        self.macgyver_icon = None
        self.start()
        

    def start(self):

        self.level = Maze("level.txt")
        self.level.generate()
        self.level.display(self.screen)

        self.macgyver_icon = pygame.image.load("images/McGyver.png")
        self.macgyver_icon = pygame.transform.scale(self.macgyver_icon, (sprite_size, sprite_size))
        self.macgyver = Char(self.level)
      


def main_loop():

    pygame.init()
    game = Game() 
    game.start()

    running = True
    while running: 

        for event in pygame.event.get():

            if event.type == QUIT: 
                running = False
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

                if event.key == K_UP:
                    game.macgyver.move_up()
                elif event.key == K_DOWN:
                    game.macgyver.move_down()
                elif event.key == K_RIGHT:
                    game.macgyver.move_right()       
                elif event.key == K_LEFT:
                    game.macgyver.move_left()


        game.level.display(game.screen)
        game.screen.blit(game.macgyver_icon, (game.macgyver.x, game.macgyver.y))       
        pygame.display.flip()

    
main_loop() 

