import random
import pygame
from game import Game


class Maze:


    def __init__(self, level):
        self.level = level
        self.structure = 0

        
    def generate(self):

        with open(self.level, "r") as level:
            structure_level = []

        for line in level:
            print(lines)
            lines_level = []
                for sprite in line:
                    print(sprite)
                    for i in enumerate(line)
                        if spirtes == "O"
                            floor_available.append(i) 
                structure_level.append(lines_level)     
        self.structure = structure_level 


     def display(self, screen)

        spirtes_x = 0
        for line in self.strucutre:
            spirtes_y = 0
            for sprites in line:
                x = spirtes_x * sprite_size
                y = spirtes_y * sprite_size
                if sprite == "x":
                    screen.blit("wall_image", (x,y))
                elif spirtes == "O"
                    screen.blit("floor_image", (x, y))
            spirtes_y = spirtes_y + 1
        spirtes_x = spirtes_x + 1    
                    
        
                    
    
            


