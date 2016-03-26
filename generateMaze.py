# maze.py

import random

# Maze grid size
sizex = 5
sizey = 5



def generateMaze(sizex, sizey):

    # Generate maze
    # Runtime: O(x*y)
    maze = {}
    for i in range(sizex):
        for j in range(sizey):
            maze[(i,j)] = []


    # Type a clever description
    # Runtime: O(?????????????????)
    def generatePath(x, y):

        #              left    right    down     up
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)

        for d in directions:
            dx, dy = x + d[0], y + d[1]

            # Check that the node is in the bounds of the graph
            if -1 < dx and dx < sizex and -1 < dy and dy < sizey:
                if maze[(dx,dy)] == []:
                    maze[(x,y)].append((dx,dy))
                    maze[(dx,dy)].append((x,y)) # undirected graph
                    generatePath(dx,dy)


    startx, starty = 0, 0
    # Alternately:
    # Choose random starting position
    # startx, starty = random.randint(0, sizex-1), random.randint(0, sizey-1)

    generatePath(startx, starty)

    return maze



myMaze = generateMaze(4,4)
for node in myMaze:
    print(str(node) + ": " + str(myMaze[node]))



# That's all folks!
