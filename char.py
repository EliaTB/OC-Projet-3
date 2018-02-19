"""defines char class"""

import pygame
from pygame.locals import *
from maze import Maze
from constants import *

class Char:
    """class to create a character"""
    def __init__(self, image, level):
        self.level = level
        self.position_x, self.position_y = self.get_initial_position(self.level)
        self.case_x = self.position_x * sprite_size
        self.case_y = self.position_y * sprite_size
        self.item_counter = 0
        self.sprite = pygame.image.load(image)
        self.sprite = pygame.transform.scale((self.sprite), (sprite_size, sprite_size))


    def get_initial_position(self, level):
        """method to find the initial position fo the character"""    
        line_nb = 0
        for line in level.structure:
            column_nb = 0
            for sprite in line:
                if sprite == "M":
                    return (column_nb, line_nb)
                column_nb += 1
            line_nb += 1

    #methods to move the characater in all 4 direction       
    def move_up(self):

        if self.level.structure[self.position_y - 1][self.position_x] != "X":
            if self.position_y > 0:
                self.position_y -= 1
                self.case_y = self.position_y * sprite_size

    def move_down(self):

        if self.position_y < sprite_nb - 1:
            if self.level.structure[self.position_y + 1][self.position_x] != "X":
                self.position_y += 1
                self.case_y = self.position_y * sprite_size

    def move_right(self):

        if self.position_x < sprite_nb - 1:
            if self.level.structure[self.position_y][self.position_x + 1] != "X":
                self.position_x += 1
                self.case_x = self.position_x * sprite_size

    def move_left(self):

    	if self.level.structure[self.position_y][self.position_x - 1] != "X":
            if self.position_x > 0:
                self.position_x -= 1
                self.case_x = self.position_x * sprite_size


    def get_item(self):
        """count the number of items in possesion of the character"""    
        self.item_counter += 1