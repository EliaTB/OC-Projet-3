import pygame
from pygame.locals import *
from maze import Maze
from char import Char
from item import Item
from constants import *



class Game:

    def __init__(self):

        pygame.font.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("The amazing MacGyver !")


        self.level = None
        self.level = Maze("level.txt")
        self.level.generate()
        self.level.display(self.screen)

        self.macgyver = Char(macgyver_icon, self.level)


        self.needle = Item(img_needle, "N", self.level)
        self.needle.display(self.screen)
        self.ether = Item(img_ether, "E", self.level)
        self.ether.display(self.screen)
        self.tube = Item(img_tube, "T", self.level)
        self.tube.display(self.screen)

        self.start()

    def start(self):

        win_img = pygame.image.load("images/win.png")
        lose_img = pygame.image.load("images/lose.png")

        pygame.init()

        running = True
        while running:

            for event in pygame.event.get():

                if event.type == QUIT:
                    running = False
                    pygame.quit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        pygame.quit()

                    if event.key == K_UP:
                        self.macgyver.move_up()
                    elif event.key == K_DOWN:
                        self.macgyver.move_down()
                    elif event.key == K_RIGHT:
                        self.macgyver.move_right()
                    elif event.key == K_LEFT:
                        self.macgyver.move_left()

            if self.level.structure[self.macgyver.position_y][self.macgyver.position_x] == self.needle.item_id:
                self.needle.remove_item()
                self.macgyver.get_item()

            if self.level.structure[self.macgyver.position_y][self.macgyver.position_x] == self.ether.item_id:
                self.ether.remove_item()
                self.macgyver.get_item()

            if self.level.structure[self.macgyver.position_y][self.macgyver.position_x] == self.tube.item_id:
                self.tube.remove_item()
                self.macgyver.get_item()

            #meet the guard

            if self.level.structure[self.macgyver.position_y][self.macgyver.position_x] == "G":
                if self.macgyver.item_counter >= 3:
                    win = True
                    while win:
                        self.screen.blit(win_img, (0, 0))
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                running = False
                                pygame.quit()

                            if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    running = False
                                    pygame.quit()
                                if event.key == K_RETURN:
                                    win = False
                                    Game()
                        pygame.display.flip()


                else:
                    lose = 1
                    while lose:
                        self.screen.blit(lose_img, (0, 0))
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                running = False
                                pygame.quit()

                            if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    running = False
                                    pygame.quit()
                                if event.key == K_RETURN:
                                    lose = False
                                    Game()
                        pygame.display.flip()


            self.level.display(self.screen)
            self.screen.blit(self.macgyver.sprite, (self.macgyver.x, self.macgyver.y))
            pygame.display.flip()

Game()
