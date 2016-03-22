# maze.py

import random

maze = {}

mazeNodes = list(range(8))

while len(mazeNodes) > 2:
    leftChild  = random.choice(mazeNodes)
    mazeNodes.remove(leftChild)
    rightChild = random.choice(mazeNodes)
    mazeNodes.remove(rightChild)
    parent = random.choice(mazeNodes)
    mazeNodes.remove(parent)
    maze[parent] = [leftChild, rightChild]

for i in maze:
    print(str(i) + ": " + str(maze[i]))


# That's all folks!
