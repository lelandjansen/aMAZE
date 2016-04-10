# Gamestate.py
# By: Michael Steer

# Contains the actual game that the user plays

import pygame
import sys
import os
import random

from pygame.locals import *

import aMAZE
import generateMaze
import search

from generateMaze import Maze
from sprites import Player

# Globals
maze = None                 # The maze that the user navigate
endpoint = None             # Where the user and AI end
startpoint = None           # Where the user and AI start
aiPath = None               # The path the AI takes from start to end
score = 0                   # The users score

# Updates the console with the score
def update_console(rounds=0):
    os.system("clear")

    print("===========================")
    print("=          aMAZE          =")
    print("===========================")
    print("  Score: || " + str(rounds))

# Generates a new maze, a new start and end point, a new AI path
def new_round(mapSize, aiDifficulty):

    global maze
    global endpoint
    global startpoint
    global aiPath

    # Generate a new maze
    maze = Maze(mapsize, mapsize)
    maze.generateMaze()
    maze.exportMaze()
    # Set a startpoint and endpoint for the user
    endpoint = (mapSize-1, mapSize-1)
    startpoint = (0,0)

    # Set the path the AI follows
    if aiDifficulty == -2:
        aiPath = [startpoint, endpoint]
    else:
        aiPath = search.mazeAI(maze, startpoint, endpoint, aiDifficulty)

# The actual game state where all the magic happens
def game_state(mapSize, aiSpeed, aiDifficulty):

    global maze
    global endpoint
    global startpoint
    global score

    # Set an FPS limit so PyGame doesn't destroy the CPU and create a singularity
    FPS = 60
    clock = pygame.time.Clock()

    # Start with no score
    score = 0

    # Generate an initial set of conditions
    new_round(mapSize, aiDifficulty)

    # Running flag
    running = True

    # Setup the PyGame window
    pygame.init()
    screen = pygame.display.set_mode((32*maze.get_sizex(), 32*maze.get_sizey()))
    pygame.display.set_caption('aMAZE - The best game ever')

    # Setup the User and the AI
    user = Player(startpoint[0], startpoint[1] , (0,255,0), 4)
    enemy = Player(startpoint[0], startpoint[1], (255,0,0), aiSpeed)
    enemy.setNodes(aiPath)

    # Load the maze
    maze_spr = pygame.image.load("maze.png")

    # Update the console with score information
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

        # Move the user and the AI
        user.move()
        enemy.move()


        # Render the scene
        screen.blit(maze_spr,(0,0))
        pygame.draw.rect(screen, (0, 255, 255), (endpoint[0]*32+8,endpoint[1]*32+8,16,16), 0)

        # Render the user and the AI
        enemy.render(screen)
        user.render(screen)

        # Flip the display buffer
        pygame.display.update()
        # Check to see if the user beat the AI to the end
        if user.atNode(endpoint) and not enemy.atNode(endpoint):

            # Don't increment the Difficulty if its maxed out or a special
            # Variant
            if aiDifficulty in [101, -1, -2]:
                pass
            else:

                # Up the difficulty
                aiDifficulty += 1

            # Increase the users score depending on the difficulty
            score += int(aiDifficulty/100)*aiSpeed + mapSize/4

            # Update the console with this new score
            update_console(score)

            # Generate a new set of conditions
            new_round(mapSize, aiDifficulty)

            # Move the User and player back to the start and update the
            # AI path
            user.jump(startpoint)
            enemy.clearPath()
            enemy.setNodes(aiPath)
            enemy.jump(startpoint)

            # Update the maze
            maze_spr = pygame.image.load("maze.png")

                # Check to see if the AI Beat the user to the end
        elif enemy.atNode(endpoint) and not user.atNode(endpoint):
            # Quit the game and run the gameover State
            pygame.quit()
            os.system("clear")
            running = False
            aMAZE.game_over(score)

        # Limit the framerate
        clock.tick(FPS)

        # Quit the application if the user presses q
        if keys[K_q]:
            pygame.quit()
            os.system("clear")
            running = False
            aMAZE.game_over(score)

    return '0'
