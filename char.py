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

        if direction == "up" :
            if self.position_y > 0 :
                position_y -= 1
                self.y = self.position_y * sprite_size
                if structure_level[position_y][position_x] == "X" :
                    pass
         
    def move_down(self)
         
       if direction == "down" :
            if self.position_y < sprite_nb :       
                position_y += 1
                self.y = self.position_y * spirte_size
                if structure_level[position_y][position_x] == "X" :
                    pass
           
    def move_right(self)
           
        if direction == "right" :
            if self.position_x > 0 :
                position_x += 1
                self.x = self.position_x * sprite_size
                if structure_level[position_y][position_x] == "X" :
                    pass    

    def move_left(self)
    
    	if direction == "left" :
            if self.position_x < sprite_nb :
                position_x -= 1
                self.x = self.position_x * sprite_size
                if structure_level[position_y][position_x] == "X" :
                    pass

    def item_counter(self, item)
    
        self.inventory.append(item)
	
