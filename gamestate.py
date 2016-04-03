import pygame
import sys
import os
import random

from pygame.locals import *

import generateMaze
import search

from generateMaze import Maze
from sprites import Player
from aMAZE import aiDifficulty
from aMAZE import aiSpeed
maze = None
endpoint = None
startpoint = None
score = 0

# Updates the console with the score
def update_console(rounds=0):
    #os.system("clear")
    print("===========================")
    print("=          aMAZE          =")
    print("===========================")
    print("  Score: || " + str(rounds))

# Generates a new maze, a new start and end point, a new AI path
def new_round(mapSize):

    global maze
    global endpoint
    global startpoint
    maze = Maze(mapSize, mapSize)
    maze.generateMaze()
    maze.exportMaze()
    #endpoint = (random.choice([mapSize-1,mapSize-2, 1, 0]),random.choice([mapSize-1,mapSize-2, 1, 0]))
    endpoint = (0,0)
    startpoint = (mapSize-1, mapSize-1)
    #startpoint = (random.choice([int(mapSize/2),int(mapSize/2)+1,int(mapSize/2)-1]), \
                  #random.choice([int(mapSize/2),int(mapSize/2)+1,int(mapSize/2)-1]))
    aiPath = search.dfsPath(maze, endpoint, startpoint, 100)
    generateMaze.display_ai(maze, aiPath)

    for i in range(len(aiPath)-2):
        if abs(aiPath[i][0] - aiPath[i+1][0]) and abs(aiPath[i][1] - aiPath[i+1][1]):
            print("wtf is happening")

# The actual game state where all the magic happens
def game_state(mapSize, aiSpeed, aiDifficulty):

    global maze
    global endpoint
    global startpoint
    global score

    score = 0

    new_round(mapSize)

    # Running flag
    running = True

    # Setup the PyGame window
    pygame.init()
    screen = pygame.display.set_mode((32*maze.get_sizex(), 32*maze.get_sizey()))
    pygame.display.set_caption('aMAZE - The best game ever')

    # Setup sprites
    user = Player(startpoint[0], startpoint[1] , (0,255,0), 4)
    maze_spr = pygame.image.load("maze.png")

    # Set an FPS limit so PyGame doesn't destroy the CPU and create a singularity
    FPS = 60
    clock = pygame.time.Clock()

    update_console()
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
        pygame.draw.rect(screen, (0, 255, 255), (endpoint[0]*32+8,endpoint[1]*32+8,16,16), 0)
        user.render(screen)
        pygame.display.update()

        # Check to see if the user won the round
        if user.atNode(endpoint):
            score += aiSpeed*aiDifficulty + mapSize/4
            update_console(score)
            new_round(mapSize)
            user.jump(startpoint)
            maze_spr = pygame.image.load("maze.png")


        # Limit the framerate
        clock.tick(FPS)

        # Quit the application if the user presses q
        if keys[K_q]:
            pygame.quit()
            os.system("clear")
            running = False

    return '0'
