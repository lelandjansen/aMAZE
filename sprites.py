import pygame
import sys
from pygame.locals import *

PLAYER_RADIUS = 10

# The player class
class Player:

    # Initialization
    def __init__(self, nodex, nodey, color, speed):

        self.nodex = nodex          # The x and y position of the player
        self.nodey = nodey          # with respect to the maze

        self.x = (nodex)*32+16      # The x and y position of the player
        self.y = (nodey)*32+16      # With respect to the window

        self.color = color          # The color of the player (Tuple)

        self.moving = False         # Flag for if the player is moving

        self.nodes = None           # a list of nodes that the player will
                                    # move through

        self.activeNode = None      # The current node the player is moving to

        self.speed = speed          # The speed at which the player can move

    # Returns whether the player is moving or not
    def isMoving(self):
        return self.moving

    # Sets a path for the player to move to, but only if the player is not
    # already moving through a path
    def setNodes(self, nodes):
        if self.nodes is None:
            self.nodes = nodes
            self.activeNode = self.nodes.pop(0)
            self.moving = True

    # Clears the path and stops the Player
    def clearPath(self):
        self.moving = False
        self.activeNode = None
        self.nodes = None

    # returns the node the player is at or is moving away from
    def getNode(self):
        return (self.nodex, self.nodey)

    # returns true or false depending on whether the player is at the
    # specified node on the graph or not
    def atNode(self, node):
        if node[0]*32+16 == self.x and node[1]*32+16 == self.y:
            return True
        else:
            return False

    # Moves the player towards the next node in the path that it has,
    # if this path exists
    def move(self):
        # If the player has a destanation and should be moving
        if self.activeNode is not None and self.moving:

            # Determine what direction the player needs to move
            # based on where the node is
            if self.x > self.activeNode[0]*32+16:
                self.x -= self.speed
            elif self.x < self.activeNode[0]*32+16:
                self.x += self.speed

            if self.y > self.activeNode[1]*32+16:
                self.y -= self.speed
            elif self.y < self.activeNode[1]*32+16:
                self.y += self.speed

            # After moving, determine if the player has reached the node
            if self.atNode(self.activeNode):

                # If it has reached the node and there are no more nodes,
                # stop moving
                if len(self.nodes) == 0:
                    self.moving = False
                    self.nodex = self.activeNode[0]
                    self.nodey = self.activeNode[1]

                    self.activeNode = None
                    self.nodes = None

                # Otherwise get the next node in the list and continue moving
                else:
                    self.activeNode = self.nodes.pop(0)
    # Jumps the player to a specified node
    def jump(self,node):
        self.nodex = node[0]
        self.nodey = node[1]

        self.x = (self.nodex)*32+16
        self.y = (self.nodey)*32+16
    # Draw the player to the screen
    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), PLAYER_RADIUS, 0)
