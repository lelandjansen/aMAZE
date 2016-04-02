import pygame
import sys
from pygame.locals import *
from generateMaze import Maze
from sprites import Player
def game_state(maze, mapSize):

    # Setup the PyGame window
    pygame.init()
    screen = pygame.display.set_mode((32*maze.get_sizex(), 32*maze.get_sizey()))
    pygame.display.set_caption('aMAZE - The best game ever')

    # Setup sprites
    maze_spr = pygame.image.load("maze.png")
    user = Player(1 , 1 , (0,255,0))
    #

    # Set an FPS limit so PyGame doesn't destroy the CPU and create a singularity
    FPS = 60
    clock = pygame.time.Clock()

    while True: # main game loop

        # Python Window events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Render
        user.move_to_node((5,1))
        screen.blit(maze_spr,(0,0))
        user.render(screen)
        pygame.display.update()
        clock.tick(FPS)
