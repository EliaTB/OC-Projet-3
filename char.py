import pygame
from pygame.locals import *
from maze import Maze


class Char:
    
    def __init__(self,)
        self.position_x = 0
        self.position_y = 0
        self.x = 0
        self.y = 0
        self.inventory = []


    def move_up(self)

        if structure_level[position_y][position_x] == "X" :
            if self.position_y > 0 :
                position_y -= 1
                self.y = self.position_y * sprite_size
                
         
    def move_down(self)
         
       if structure_level[position_y][position_x] == "X" :
            if self.position_y < sprite_nb - 1 :       
                position_y += 1
                self.y = self.position_y * spirte_size
                
           
    def move_right(self)
           
        if structure_level[position_y][position_x] == "X" :
            if self.position_x > 0 :
                position_x += 1
                self.x = self.position_x * sprite_size
                   

    def move_left(self)
    
    	if structure_level[position_y][position_x] == "X" :
            if self.position_x < sprite_nb - 1 :
                position_x -= 1
                self.x = self.position_x * sprite_size
                

    def item_counter(self, item)
    
        self.inventory.append(item)
	
