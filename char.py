import pygame
from pygame.locals import *
from maze import Maze
from data import *

class Char:
    
    def __init__(self, image, level):
        self.level = level
        self.position_x, self.position_y = self.get_initial_position(self.level)
        self.x = self.position_x * sprite_size
        self.y = self.position_y * sprite_size
        self.item_counter = 0
        self.sprite = pygame.image.load(image)
        self.sprite = pygame.transform.scale((self.sprite), (sprite_size, sprite_size))


    # @property
    # def sprite_position(self):
    #     self.x = self.position_x * sprite_size
    #     self.y = self.position_y * sprite_size

    #     return (self.x, self.y)

    def get_initial_position(self, level):

        # mcgyver = pygame.image.load(macgyver_icon)
        # mcgyver = pygame.transform.scale(macgyver, (sprite_size, sprite_size))
        
        line_nb = 0
        for line in level.structure:
            column_nb = 0
            for case in line:
                if case == "M":
                    return (column_nb, line_nb)
                column_nb += 1
            line_nb += 1


        # def display(self, screen):
        # screen.blit(self.sprite, (self.x, self.y))
        
        
    def move_up(self):

        if self.level.is_floor(self.position_y - 1, self.position_x):
            if self.position_y > 0 :
                self.position_y -= 1
                self.y = self.position_y * sprite_size
            self.level.structure[self.position_y][self.position_x] = "O"
         
    def move_down(self):
         
        if self.level.is_floor(self.position_y + 1, self.position_x):
            if self.position_y < sprite_nb - 1 :       
                self.position_y += 1
                self.y = self.position_y * sprite_size
            self.level.structure[self.position_y][self.position_x] = "O"
           
    def move_right(self):
           
        if self.level.is_floor(self.position_y, self.position_x + 1):
            if self.position_x < sprite_nb - 1 :
                self.position_x += 1
                self.x = self.position_x * sprite_size
            self.level.structure[self.position_y][self.position_x] = "O"   

    def move_left(self):
    
    	if self.level.is_floor(self.position_y, self.position_x - 1):
            if self.position_x > 0 :
                self.position_x -= 1
                self.x = self.position_x * sprite_size
            self.level.structure[self.position_y][self.position_x] = "O"

    def get_item(self):
    
        self.item_counter += 1

    

	
