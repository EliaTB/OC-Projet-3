import pygame
from pygame.locals import *
from maze import *


class Char:
    
    def __init__(self,)
        self.position_x = 0
        self.position_y = 0
        self.x = 0
        self.y = 0

       
		
    def movement(self)

        if direction == "up"
            position_y = position_y - 1
            self.y = self.position_y * sprite_size
         
       if direction == "down"
            position_y = position_y + 1
            self.y = self.position_y * spirte_size
           
        if direction == "right"
            position_x = position_x + 1
            self.x = self.position_x * sprite_size    

    	if direction == "left"
            position_x = position_x -1
            self.x = self.position_x * sprite_size


    def movementEvent(self)


    	if event.type == KEYDOWN:
            if event.key == K_UP:
                char.movement("up")
    	if event.type == KEYDOWN:
            if event.key == K_DOWN:
                char.movement("down")
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                char.movement("right")        
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                char.movement("left")
        
