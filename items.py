import random
import pygame
from pygame.locals import *
from maze import Maze
from data import *


class Item:

    def __init__(self, image, letter, level):
        self.item_id = letter
        self.level = level
        self.draw = 1
        self.position_x, self.position_y = self.get_random_position()
        self.x = self.position_x * sprite_size
        self.y = self.position_y * sprite_size
        self.sprite = pygame.image.load(image).convert_alpha()
        self.sprite = pygame.transform.scale((self.sprite), (sprite_size, sprite_size))

    

    def get_random_position(self):

        pos_y = 0
        pos_x = 0

        while self.level.structure[pos_y][pos_x] != "O":
            pos_x = random.randrange(0, (sprite_nb - 1))
            pos_y = random.randrange(0, (sprite_nb - 1))
        self.level.structure[pos_y][pos_x] = self.item_id
        return pos_x, pos_y


    def display(self, screen):
 
        if self.draw == 1:
            screen.blit(self.sprite, (self.x, self.y))

    
    def remove_item(self):
        self.draw -= 1
        self.level.structure[self.position_y][self.position_x] = "O"

   
