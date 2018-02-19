"""defines item class"""

import random
import pygame
from pygame.locals import *
from maze import Maze
from constants import *


class Item:
    """class to create an item"""
    def __init__(self, image, letter, level):
        self.item_id = letter
        self.level = level
        self.draw = 1
        self.position_x, self.position_y = self.get_random_position()
        self.case_x = self.position_x * sprite_size
        self.case_y = self.position_y * sprite_size
        self.sprite = pygame.image.load(image)
        self.sprite = pygame.transform.scale((self.sprite), (sprite_size, sprite_size))


    def get_random_position(self):
        """method to place randomly an item on the map"""
        pos_y = 0
        pos_x = -1

        while self.level.structure[pos_y][pos_x] != "O":
            pos_x = random.randrange(0, (sprite_nb - 1))
            pos_y = random.randrange(0, (sprite_nb - 1))
        self.level.structure[pos_y][pos_x] = self.item_id
        return pos_x, pos_y


    def display(self, screen):
        """method to display an item"""     
        if self.draw == 1:
            screen.blit(self.sprite, (self.case_x, self.case_y))


    def remove_item(self):
        """remove an item when the character picks it up"""
        self.draw -= 1
        self.level.structure[self.position_y][self.position_x] = "O"