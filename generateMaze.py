# generateMaze.py
# By Leland Jansen and Michael Steer

# Generate maze using recursive backtracking
# Sources:
#  http://www.jamisbuck.org/presentations/rubyconf2011/index.html
#  http://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking

# Please note that cairo is required for this python script to run
# For Unix systems: This should be already installed if python 3.xx is installed
# For Windows systems: Please follow the instructions on how to install CairoCFFI
# Detailed in the readme


import random
import cairo

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
    def generateMaze(self, startx=0, starty=0):

        # Generate maze
        # Runtime: O(x*y)
        maze = {}
        for i in range(self.sizex):
            for j in range(self.sizey):
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
                if -1 < dx and dx < self.sizex and -1 < dy and dy < self.sizey:
                    if maze[(dx,dy)] == []:
                        maze[(x,y)].append((dx,dy))
                        maze[(dx,dy)].append((x,y)) # undirected graph
                        generatePath(dx,dy)

        generatePath(startx, starty)

        self.maze = maze

    # Print the maze to the screen
    def printMaze(self):
        for node in self.maze:
            print(str(node) + ": " + str(self.maze[node]))

    # Return the graph that stores the maze
    def graph(self):
        return self.maze

    # Export the maze to an image file
    def exportMaze(self):

        # Setup the Cairo surface
        MazeSurface = cairo.ImageSurface(cairo.FORMAT_RGB24, nodeSize*self.sizex, nodeSize*self.sizey)
        surfaceHandle = cairo.Context(MazeSurface)

        # Set whole surface black
        surfaceHandle.set_source_rgb(0,0,0)

        # Set the surface up for paining white walls
        surfaceHandle.paint()
        surfaceHandle.set_source_rgb(1,1,1)
        surfaceHandle.set_line_width(wallSize)

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
                surfaceHandle.move_to(x*nodeSize,y*nodeSize+nodeSize)
                surfaceHandle.line_to(x*nodeSize+nodeSize,y*nodeSize+nodeSize)
            if not bottom:
                surfaceHandle.move_to(x*nodeSize,y*nodeSize)
                surfaceHandle.line_to(x*nodeSize+nodeSize,y*nodeSize)
            if not left:
                surfaceHandle.move_to(x*nodeSize,y*nodeSize)
                surfaceHandle.line_to(x*nodeSize,y*nodeSize+nodeSize)
            if not right:
                surfaceHandle.move_to(x*nodeSize+nodeSize,y*nodeSize)
                surfaceHandle.line_to(x*nodeSize+nodeSize,y*nodeSize+nodeSize)

        # Render the walls
        surfaceHandle.stroke()

        # Write the image to a png file
        MazeSurface.write_to_png("maze.png")

    # Return the dimensions of the maze in terms of number of nodes
    def get_sizex(self):
        return self.sizex
    def get_sizey(self):
        return self.sizey

# Temp functions for visualizing the AI path. to be deleted
def display_ai(maze, path=[]):
    MazeSurface = cairo.ImageSurface(cairo.FORMAT_RGB24, nodeSize*maze.sizex, nodeSize*maze.sizey)
    surfaceHandle = cairo.Context(MazeSurface)

    # Set whole surface black
    surfaceHandle.set_source_rgb(0,0,0)

    # Set the surface up for paining white walls
    surfaceHandle.paint()
    surfaceHandle.set_source_rgb(1,1,1)
    surfaceHandle.set_line_width(wallSize)


    for node in maze.maze:
        # Wall flags for this node
        top = False
        bottom = False
        left = False
        right = False

        x = node[0]
        y = node[1]

        neighbors = maze.maze[node]
        for neighbor in neighbors:

            dx = neighbor[0]-x
            dy = neighbor[1]-y

            # Node is above
            if dx == 0 and dy == 1:
                top = True
            if dx == 0 and dy == -1:
                bottom = True
            if dx == 1 and dy == 0:
                right = True
            if dx == -1 and dy == 0:
                left = True

        if not top:

            surfaceHandle.move_to(x*nodeSize,y*nodeSize+nodeSize)
            surfaceHandle.line_to(x*nodeSize+nodeSize,y*nodeSize+nodeSize)

        if not bottom:

            surfaceHandle.move_to(x*nodeSize,y*nodeSize)
            surfaceHandle.line_to(x*nodeSize+nodeSize,y*nodeSize)


        if not left:

            surfaceHandle.move_to(x*nodeSize,y*nodeSize)
            surfaceHandle.line_to(x*nodeSize,y*nodeSize+nodeSize)

        if not right:

            surfaceHandle.move_to(x*nodeSize+nodeSize,y*nodeSize)
            surfaceHandle.line_to(x*nodeSize+nodeSize,y*nodeSize+nodeSize)

    surfaceHandle.stroke()
    changeamnt = float(1)/float(len(path))
    r = 1
    b = 0
    surfaceHandle.set_source_rgb(r, 0, b)
    skipFirst = True
    for node in path:
        surfaceHandle.set_source_rgb(r, 0, b)

        if skipFirst:
            skipFirst = False
            curNode = node
            surfaceHandle.move_to(curNode[0]*32+16, curNode[1]*32+16)
        else:
            prevNode = curNode
            curNode = node
            surfaceHandle.move_to(prevNode[0]*32+16, prevNode[1]*32+16)
            surfaceHandle.line_to(curNode[0]*32+16, curNode[1]*32+16)
            #surfaceHandle.line_to(curNode[0]*32+10, curNode[1]*32+10)
            #surfaceHandle.move_to(curNode[0]*32+16, curNode[1]*32+16)
            surfaceHandle.stroke()

        r -= changeamnt
        b += changeamnt
    MazeSurface.write_to_png("AI.png")

def display_path_process(maze, path=[]):
    filenumber = 0
    MazeSurface = cairo.ImageSurface(cairo.FORMAT_RGB24, nodeSize*maze.sizex, nodeSize*maze.sizey)
    surfaceHandle = cairo.Context(MazeSurface)

    # Set whole surface black
    surfaceHandle.set_source_rgb(0,0,0)

    # Set the surface up for paining white walls
    surfaceHandle.paint()
    surfaceHandle.set_source_rgb(1,1,1)
    surfaceHandle.set_line_width(wallSize)


    for node in maze.maze:
        # Wall flags for this node
        top = False
        bottom = False
        left = False
        right = False

        x = node[0]
        y = node[1]

        neighbors = maze.maze[node]
        for neighbor in neighbors:

            dx = neighbor[0]-x
            dy = neighbor[1]-y

            # Node is above
            if dx == 0 and dy == 1:
                top = True
            if dx == 0 and dy == -1:
                bottom = True
            if dx == 1 and dy == 0:
                right = True
            if dx == -1 and dy == 0:
                left = True

        if not top:

            surfaceHandle.move_to(x*nodeSize,y*nodeSize+nodeSize)
            surfaceHandle.line_to(x*nodeSize+nodeSize,y*nodeSize+nodeSize)

        if not bottom:

            surfaceHandle.move_to(x*nodeSize,y*nodeSize)
            surfaceHandle.line_to(x*nodeSize+nodeSize,y*nodeSize)


        if not left:

            surfaceHandle.move_to(x*nodeSize,y*nodeSize)
            surfaceHandle.line_to(x*nodeSize,y*nodeSize+nodeSize)

        if not right:

            surfaceHandle.move_to(x*nodeSize+nodeSize,y*nodeSize)
            surfaceHandle.line_to(x*nodeSize+nodeSize,y*nodeSize+nodeSize)

    surfaceHandle.stroke()
    changeamnt = float(1)/float(len(path))
    r = 1
    b = 0
    surfaceHandle.set_source_rgb(r, 0, b)
    skipFirst = True
    for node in path:
        surfaceHandle.set_source_rgb(r, 0, b)
        if skipFirst:
            skipFirst = False
            curNode = node
            surfaceHandle.move_to(curNode[0]*32+16, curNode[1]*32+16)
        else:
            prevNode = curNode
            curNode = node
            surfaceHandle.move_to(prevNode[0]*32+16, prevNode[1]*32+16)
            surfaceHandle.line_to(curNode[0]*32+16, curNode[1]*32+16)
            #surfaceHandle.line_to(curNode[0]*32+10, curNode[1]*32+10)
            #surfaceHandle.move_to(curNode[0]*32+16, curNode[1]*32+16)
            surfaceHandle.stroke()
            name = "AI-" + str(filenumber) + ".png"
            print(name)
            MazeSurface.write_to_png(name)
            filenumber += 1

        r -= changeamnt
        b += changeamnt
