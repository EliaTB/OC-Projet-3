import pygame
from pygame.locals import *
from maze import Maze
from char import Char


class Game:


    def __init__(self):
        self.sprite_nb = 15
        self.sprite_size = 50
        self.WIDTH = sprite_nb * sprite_size
        self.HEIGHT = sprite_nb * sprite_size
    	self.size = WIDTH, HEIGHT
    	self.screen = pygame.display.set_mode((size))
        game_start()
  

    def game_start():
    	running = True
    	while running:
            for event in pygame.event.get():
            	if event.type == QUIT:
                running = False      
    	pygame.quit()

    def movement_event(char)
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.key == K_UP:
                char.movement("up")
            elif event.key == K_DOWN:
                char.movement("down")
            elif event.key == K_RIGHT:
                char.movement("right")        
            elif event.key == K_LEFT:
                char.movement("left")
        
