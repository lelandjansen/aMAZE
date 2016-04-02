import pygame
import sys
from pygame.locals import *

PLAYER_RADIUS = 10
PLAYER_SPEED = 10
class Player:

    def __init__(self, nodex, nodey, color):
        self.nodex = nodex
        self.nodey = nodey
        self.x = (nodex)*32+16
        self.y = (nodey)*32+16
        self.color = color
        self.moving = False
        self.activeNode = True

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_to_node(self, node):
        if not self.moving:
            self.activeNode = node
            self.moving = True
        elif self.x == self.activeNode[0]*32 + 16 and self.y == self.activeNode[1]*32 + 16 and self.moving:
            self.moving = False
            pass
        else:
            if self.x < self.activeNode[0]*32 + 16:
                self.x += 1
            else:
                self.x -= 1

            if self.y < self.activeNode[1]*32 + 16:
                self.y += 1
            else:
                self.y -= 1

    def isMoving(self):
        return self.moving

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), PLAYER_RADIUS, 0)
