import pygame
import sys
import os
from pygame.locals import *
from generateMaze import Maze
from sprites import Player
def game_state(maze, mapSize):

    # Running flag
    running = True

    # Setup the PyGame window
    pygame.init()
    screen = pygame.display.set_mode((32*maze.get_sizex(), 32*maze.get_sizey()))
    pygame.display.set_caption('aMAZE - The best game ever')

    # Setup sprites
    maze_spr = pygame.image.load("maze.png")
    user = Player(1 , 1 , (0,255,0), 1)

    # Set an FPS limit so PyGame doesn't destroy the CPU and create a singularity
    FPS = 60
    clock = pygame.time.Clock()

    # main game loop
    while running:

        # Python Window events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update keystates
        keys = pygame.key.get_pressed()

        # Update the users position
        if (  keys[K_LEFT] or keys[K_RIGHT] or \
              keys[K_UP]   or keys[K_DOWN]  ) and user.isMoving() == False:

            # Get the users location in the graph and its neighbors
            node = user.getNode()
            neighbors = maze.graph()[user.getNode()]

            dx = 0
            dy = 0

            # Determine what node the user will end up on
            if keys[K_LEFT]:
                dx = -1
            elif keys[K_RIGHT]:
                dx = 1
            elif keys[K_UP]:
                dy = -1
            elif keys[K_DOWN]:
                dy = 1

            nextNode = (node[0]+dx, node[1]+dy)

            # Determine if this is an acceptable node
            if nextNode in neighbors:
                user.setNodes([nextNode])

        user.move()

        # Render the scene
        screen.blit(maze_spr,(0,0))
        user.render(screen)
        pygame.display.update()

        # Limit the framerate
        clock.tick(FPS)

        # Quit the application if the user presses q
        if keys[K_q]:
            pygame.quit()
            os.system("clear")
            running = False

    return '0'
