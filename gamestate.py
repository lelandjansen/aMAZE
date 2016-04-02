import pygame
import sys
from pygame.locals import *
from generateMaze import maze
import aMAZE
def game_state(maze):
    print(mapSize)
    pygame.init()
    screen = pygame.display.set_mode((mapSize*mazeGraph.get_sizex(), mapSize*mazeGraph.get_sizey()))
    pygame.display.set_caption('Hello World!')
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
