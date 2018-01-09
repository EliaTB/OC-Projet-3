import random
import pygame


# maze = [[X,S,X,X,X,X,X,X,X,X,X,X,X,X],
#         [X,O,X,X,X,X,X,X,X,X,X,X,X,X],
#         [X,O,X,X,X,X,X,X,X,X,X,X,X,X],
#         [X,O,O,O,O,O,O,O,O,O,O,O,X,X],
#         [X,X,X,X,X,X,X,X,X,X,X,O,X,X],
#         [X,X,X,X,X,X,X,X,X,X,X,O,X,X],
#         [X,X,X,X,X,X,X,X,X,X,X,O,X,X],
#         [X,X,X,X,X,X,X,X,X,X,X,O,X,X],
#         [X,X,X,X,X,X,X,X,X,X,X,O,X,X],
#         [X,X,X,X,X,X,X,X,X,X,X,O,X,X],
#         [X,X,X,X,X,X,X,X,X,X,X,O,X,X],
#         [X,X,X,X,X,X,X,X,X,X,X,O,X,X],
#         [X,X,X,X,X,X,X,X,X,X,X,O,X,X],
#         [X,X,X,X,X,X,X,X,X,X,X,E,X,X]]


class Maze:

    def __init__(self, level):
        self.level = level
        self.spirtes_x = 15 
        self.spirtes_y = 15
        self.structure = 0
        
    def generate(self):
        with open(self.level, "r") as level:
            structure_level = []

        for lines in level:
            print(lines)
            lines_level = []
                for sprites in lines
                    print(sprites)
                    for i in enumerate(lines)
                        if spirtes == "O"
                            floor_available.append(i) 
                structure_level.append(lines_level)     
        structure = structure_level 


    # def display(self)

    #     for lines in strucutre:
    #         for sprites in lines:
    #             if sprites == "X"
    #                  draw wall_image
    #             elif spirtes == "O"
    #                 draw floor_image
               
        
                    
    
            


