import random
import pygame
from pygame.locals import *
from maze import Maze
from data import *


class Item:

    def __init__(self, image, name, level):
        self.item_id = name
        self.level = level
        self.draw = 1
        self.position_x, self.position_y = self.random_position()
        self.x = self.position_x * sprite_size
        self.y = self.position_y * sprite_size
        self.sprite = pygame.image.load(image).convert_alpha()
        self.sprite = pygame.transform.scale((self.sprite), (sprite_size, sprite_size))

        
    def random_position(self):

        self.position_y = 0
        self.position_x = 0

        while self.level.structure[self.position_y][self.position_x] != "O":
            self.position_x = random.randrange(0, (sprite_nb - 1))
            self.position_y = random.randrange(0, (sprite_nb - 1))
        self.level.structure[self.position_y][self.position_x] = self.item_id
        return self.position_x, self.position_y



    def display(self, screen):
 
        if self.draw == 1:
            screen.blit(self.sprite, (self.x, self.y))

    
    def remove_item(self):
        self.draw -= 1
        self.level.structure[self.position_y][self.position_x] = "O"

   
