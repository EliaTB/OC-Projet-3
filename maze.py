import random 
import pygame
from pygame.locals import *
from data import *


class Maze:

    def __init__(self, level_file):
        self.level_file = level_file
        self.structure = None

        
    def generate(self):

        with open(self.level_file) as level_file:
            structure_level = []
            for line in level_file:
                line_level = []
                for sprite in line:
#                   if sprite == "O":
#                       floor_available.append(i)
                    if sprite != "\n":
                        line_level.append(sprite)
                structure_level.append(line_level)     
            self.structure = structure_level 


    def display(self, screen):

        wall = pygame.image.load("images/wall.png").convert()
        wall = pygame.transform.scale(wall, (sprite_size, sprite_size))
        floor = pygame.image.load("images/floor.png").convert()
        floor = pygame.transform.scale(floor, (sprite_size, sprite_size))
        guard = pygame.image.load("images/Gardien.png").convert()
        guard = pygame.transform.scale(guard, (sprite_size, sprite_size))

        line_nb = 0
        for line in self.structure:
            case_nb = 0
            for sprite in line:
                x = case_nb * sprite_size
                y = line_nb * sprite_size
                if sprite == "X":
                    screen.blit(wall, (x,y))
                elif sprite == "O":
                    screen.blit(floor, (x,y))
                elif sprite == "G":
                    screen.blit(guard, (x,y))    
                case_nb = case_nb + 1
            line_nb = line_nb + 1    
                    
        
                    
    
            


