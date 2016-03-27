# generateMaze.py

# Generate maze using recursive backtracking
# Sources:
#  http://www.jamisbuck.org/presentations/rubyconf2011/index.html
#  http://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking



import random

def generateMaze(sizex, sizey, startx, starty):

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

    generatePath(startx, starty)

    return maze


def printMaze(maze):
    for node in maze:
        print(str(node) + ": " + str(maze[node]))




# That's all folks!
