from maze import Maze
from data import *

class Char:
    
    def __init__(self, level):
        self.position_x = 0
        self.position_y = 0
        self.x = 0
        self.y = 0
        self.level = level
        self.item_count = 0

    # @property
    # def calculate_x_and_y(self):
    # 	self.x = self.position_x * sprite_size
    # 	self.y = self.position_y * sprite_size

    def move_up(self):

        if self.level.structure[self.position_y - 1][self.position_x] != "X" :
            if self.position_y > 0 :
                self.position_y -= 1
                self.y = self.position_y * sprite_size
                
         
    def move_down(self):
         
       if self.level.structure[self.position_y + 1][self.position_x] != "X" :
            if self.position_y < sprite_nb - 1 :       
                self.position_y += 1
                self.y = self.position_y * sprite_size
                
           
    def move_right(self):
           
        if self.level.structure[self.position_y][self.position_x + 1] != "X" :
            if self.position_x < sprite_nb - 1 :
                self.position_x += 1
                self.x = self.position_x * sprite_size
                   

    def move_left(self):
    
    	if self.level.structure[self.position_y][self.position_x - 1] != "X" :
            if self.position_x > 0 :
                self.position_x -= 1
                self.x = self.position_x * sprite_size
                

    def item_counter(self, item):
    
        self.item_count += 1

	
