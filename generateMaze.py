# generateMaze.py
# By Leland Jansen and Michael Steer

# Generate maze using recursive backtracking
# Sources:
#  http://www.jamisbuck.org/presentations/rubyconf2011/index.html

# Please note that cairo is required for this python script to run
# For Unix systems: This should be already installed if python 3.xx is installed
# For Windows systems: Please follow the instructions on how to install CairoCFFI
# Detailed in the readme


import random
import pygame
from pygame.locals import *

nodeSize = 32   # Size of a node in pixels
wallSize = 2    # Thickness of walls in pixels, must be even

class Maze:
    '''Maze class. Contains an undirected graph that contains the maze.
       The maze is stored in the form of a dictionary of tuples that specify
       each nodes location in space, along with what each nodes neighbors are.
       The class also contains functions for generating the maze, printing
       out a list of each node and its neighbors, and a function for rasterizing
       the maze into an image for use with the game
    '''
    def __init__(self, sizex, sizey):
        self.sizex = sizex
        self.sizey = sizey
        self.maze = None




    # Generate a Maze
    # Create maze using modified DFS to create random
    def generateMaze(self, startx=0, starty=0):
        #
        # Input
        #   startx  x starting coordinate
        #   starty  y starting coordinate
        #
        # Output
        #   Maze class containing generated maze as undirected graph
        #
        # Runtime
        #   = O(xy+2xy-1)
        #   = O(3xy-1)
        #  ~= O(xy)          (see runtime analysis for nested functions)
        #
        # Note
        #   A "perfect" maze is created meaning there is a unique path to each
        #   node in the graph and there is no discernible pattern or bias in the
        #   generated maze.
        #

        # Generate rectangular maze nodes
        # Runtime: O(xy)
        maze = {}
        for i in range(self.sizex):
            for j in range(self.sizey):
                maze[(i,j)] = []

        # Recursively generate maze path using DFS
        def generatePath(x, y):
            #
            # Begin at start node and choose random path at each node. "Carve" a
            #  path if the node has not yet been rached. Do this recursively
            # until all nodes have been reached.
            #
            # Runtime
            #   = O(n+e)     n = number of nodes, e = number of edges
            #   = O(A+(A-1)  A = maze area (xy),  A-1 = xy-1
            #   = O(2xy-1)
            #  ~= O(xy)
            #

            # decide on random direction to create path
            #              left    right    down     up
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            random.shuffle(directions)

            # Loop through each random direction
            for d in directions:
                dx, dy = x + d[0], y + d[1]

                # Check that the node is in the bounds of the graph
                if -1 < dx and dx < self.sizex and -1 < dy and dy < self.sizey:
                    if maze[(dx,dy)] == []:
                        # If it is possible to create a path to the random
                        #  adjacent node, do so reccursively
                        maze[(x,y)].append((dx,dy))
                        maze[(dx,dy)].append((x,y)) # undirected graph
                        generatePath(dx,dy)


        generatePath(startx, starty)

        # Return maze class
        self.maze = maze




    # Print the maze to the screen
    def printMaze(self):
        for node in self.maze:
            print(str(node) + ": " + str(self.maze[node]))

    # Return the graph that stores the maze
    def graph(self):
        return self.maze

    # Export the maze to an image file
    def exportMaze(self, screen, path=[],filename="maze.png", aifilename="mazeAI.png"):

        # Fill the screen black
        pygame.draw.rect( screen, (0,0,0), \
                          (0, 0, self.sizex*32, self.sizey*32) )

        # Go through each node in the maze
        for node in self.maze:

            # Wall flags for this node.
            top = False
            bottom = False
            left = False
            right = False

            x = node[0]
            y = node[1]

            # Get the nodes neighbors
            neighbors = self.maze[node]



            # Go through each of the nodes neighbors
            for neighbor in neighbors:

                dx = neighbor[0]-x
                dy = neighbor[1]-y

                # Determine what direction the nodes neighbors are in and
                # flag those edges to not have walls
                if dx == 0 and dy == 1:
                    top = True
                if dx == 0 and dy == -1:
                    bottom = True
                if dx == 1 and dy == 0:
                    right = True
                if dx == -1 and dy == 0:
                    left = True

            # Draw the walls that are along edges without neighbors
            if not top:
                pygame.draw.line( screen, (255,255,255), \
                                  (x*nodeSize,y*nodeSize+nodeSize), \
                                  (x*nodeSize+nodeSize,y*nodeSize+nodeSize), \
                                  wallSize)

            if not bottom:
                pygame.draw.line( screen, (255,255,255), \
                                  (x*nodeSize,y*nodeSize), \
                                  (x*nodeSize+nodeSize,y*nodeSize), \
                                  wallSize )
            if not left:
                pygame.draw.line( screen, (255,255,255), \
                                  (x*nodeSize,y*nodeSize), \
                                  (x*nodeSize,y*nodeSize+nodeSize), \
                                  wallSize )
            if not right:
                pygame.draw.line( screen, (255,255,255), \
                                  (x*nodeSize+nodeSize,y*nodeSize), \
                                  (x*nodeSize+nodeSize,y*nodeSize+nodeSize), \
                                  wallSize )

        pygame.image.save(screen, filename)

        # Draw the ai's path if its specified
        if path != list():
            changeamnt = float(255)/float(len(path))
            r = 255
            b = 0
            skipFirst = True

            # Go through the path
            for node in path:

                # Skip the first node
                if skipFirst:
                    skipFirst = False
                    curNode = node

                else:
                    prevNode = curNode
                    curNode = node
                    pygame.draw.line(screen, (r,0,b), \
                                     (curNode[0]*32+16, curNode[1]*32+16), \
                                     (prevNode[0]*32+16, prevNode[1]*32+16) )

                # Change the line color slightly
                r -= changeamnt
                b += changeamnt

                pygame.image.save(screen, aifilename)


    # Return the dimensions of the maze in terms of number of nodes
    def get_sizex(self):
        return self.sizex
    def get_sizey(self):
        return self.sizey
