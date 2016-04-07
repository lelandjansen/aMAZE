# search.py

# Search maze graph for path
# Sources:
#  Referenced dfs search algorithms written in class
#  and https://www.python.org/doc/essays/graphs/

import sys
import time
import random
from queue import deque

from generateMaze import Maze

recursionLimit = 1000000
sys.setrecursionlimit(recursionLimit)

# Computes variable-difficulty AI bias point based on difficulty
def getBiasPoint(maze, end, difficulty):
    #
    # Input
    #   maze        Maze class
    #   end         End node (tuple)
    #   difficulty  Integer between 0 and 100 (inclusive)
    #
    # Output
    #   A random point on the maze with score biasScore
    #
    # Runtime
    #   O(n) (linear with respect to maze size)
    #   Worst case  O( 4*(mazeSizeX + mazeSizeY) )
    #
    # Note
    #   Score is the manhattan distance away from the end point
    #


    # Validate input
    if end not in maze.graph():
        KeyError("End point " + str(end) + " not in maze.")
    if difficulty < 0 or 100 < difficulty:
        ValueError("Difficulty must be between 0 and 100 (inclusive).")

    # Maze size
    size = (maze.get_sizex(), maze.get_sizey())

    # Compute max score
    maxScore = size[0] - 2*(size[0]//2 - end[0]//2) + \
               size[1] - 2*(size[1]//2 - end[1]//2)

    # Compute AI bias score based on difficulty
    biasScore = maxScore - (difficulty * maxScore) // 100

    if biasScore is 0:
        return end

    # List of all nodes on the maze with score biasScore
    points = []

    # Find all points on maze with score biasScore and add to points list
    # Traverse in diamond pattern
    # Only add point if it is in the maze
    p = [-biasScore, 0]
    for i in range(4*biasScore):
        x, y = p[0] + end[0], p[1] + end[1]
        if 0 <= x and x < maze.get_sizex() and 0 <= y and y < maze.get_sizey():
            points.append((x, y))
        case = i//biasScore
        if case is 0:
            p[0] += 1
            p[1] += 1
        elif case is 1:
            p[0] += 1
            p[1] -= 1
        elif case is 2:
            p[0] -= 1
            p[1] -= 1
        elif case is 3:
            p[0] -= 1
            p[1] += 1

    # Return random point in points
    return random.choice(points)





# An alternate algorithm for getBiasPoint that is more time and space efficient,
#  however, the bias points are not computed with equal probability
# Runtime: O(sizex + sizey) (worst case)
#
# def getBiasPoint(maze, end, difficulty):
#     # maze: Maze class
#     # end: Tuple containing end point
#     # difficulty: Integer between 0 and 100
#
#     if end not in maze.graph():
#         KeyError("End point " + str(end) + " not in maze.")
#     if difficulty < 0 or 100 < difficulty:
#         ValueError("Difficulty must be between 0 and 100 (inclusive).")
#
#     size = (maze.get_sizex(), maze.get_sizey())
#
#     farthestPointScore = size[0] - 2*(size[0]//2 - end[0]//2) + \
#                          size[1] - 2*(size[1]//2 - end[1]//2)
#
#     # Compute AI bias score based on difficulty
#     biasScore = farthestPointScore - (difficulty * farthestPointScore) // 100
#
#     if biasScore is 0:
#         return end
#
#     biasPoint = [0, 0]
#
#     # Runtime: O(farthestPointScore) worst case
#     stepsRemaining = biasScore
#     while stepsRemaining:
#         i = random.choice([0, 1])
#         bound = end[i] if stepsRemaining > end[i] else stepsRemaining
#         steps = random.randint(1, bound)
#         biasPoint[i] += steps
#         stepsRemaining -= steps
#
#     reflections = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
#     random.shuffle(reflections)
#     for r in reflections:
#         x, y = end[0] + r[0]*biasPoint[0], end[1] + r[1]*biasPoint[1]
#         if 0 <= x and x < maze.get_sizex() and 0 <= y and y < maze.get_sizey():
#            return (x, y)










# Variable intelligence AI
def mazeAI(maze, start, end, difficulty):
    #
    # Input
    #   maze        Maze class
    #   start       Start node (tuple)
    #   end         End node (tuple)
    #   difficulty  Integer between -1 and 101 (inclusive)
    #
    # Output
    #   path        List containing AI path nodes
    #
    # Runtime
    #   = O(n+e)     n = number of nodes, e = number of edges
    #   = O(A+(A-1)  A = maze area (xy),  A-1 = xy-1
    #   = O(2xy-1)
    #  ~= O(xy)
    #
    # For 32x32 grid with start at (0, 0) and end at (31, 31), as difficulty
    #  was increased from 0 to 100, the path length decreased by approximately
    #  11.23 units per one unit change in difficulty. (Average of six randomly
    #  generated mazes. Path length for each difficulty is average of 1000
    #  path length computations).
    #  length is average of 1000 samples).
    #  (13.359+8.483+8.4551+12.846+12.846+11.387)/6 ~= 11.23
    #  See test results graph for detailed analysis of path length vs difficulty
    #

    # Get undirected graph from maze class
    graph = maze.graph()

    # Validate input
    if start not in graph:
        KeyError("Start node " + str(start) + " not in maze.")
    if end not in graph:
        KeyError("End node "   + str(end)   + " not in maze.")
    if difficulty < -1 or 101 < difficulty:
        ValueError("Difficulty must be between 0 and 100 (inclusive).")


    # Depth-first search to find variable-difficulty AI path
    def dfsPath(node, end):
        # Add node to set of visited nodes
        visited.add(node)
        # If end has not been found, add node to path
        if not dfsPath.found:
            dfsPath.path += [node]

        # Get neighbors of current node
        nextNode = graph[node]

        # Shuffle neighbors if random difficulty is selected
        if difficulty is -1:
            random.shuffle(nextNode)
        # Sort by proximity to bias point if variable-difficulty is selected
        # Runtime
        #   O(n log(n)), however, n is at most 3 so runtime is
        #    effectively constant
        else:
            nextNode.sort(key=lambda n: \
                          abs(n[0]-biasPoint[0]) + abs(n[1]-biasPoint[1]) )

        # Loop through each neighbor in the order determined above
        for succ in nextNode:
            # If the end has been found
            if succ == end:
                dfsPath.found = True
                dfsPath.path += [end]
            # If the end has not been found and
            #  the node has not yet been reached
            elif succ not in visited:
                # Recursively perform a search on
                dfsPath(succ, end)
                # If end has not been found, add node to path
                #  (we want to add the backtracking to the AI path)
                if not dfsPath.found:
                    dfsPath.path += [node]


    # Find shortest path using breadth-first search
    def shortestPath(start, end):
        # Intialize queue of paths to process
        #  Append start node
        queue = deque([[start]])
        visited = set()

        # While there are still items in the queue to process
        while queue:
            # Get the next path list
            path = queue.popleft()
            # Get the last node from the path
            node = path[-1]

            # If the end node is encountered
            if node == end:
                return path
            # If the node has not yet been visited
            elif node not in visited:
                # Add the node to the visited set
                visited.add(node)

                # Get neighbors of current node
                nextNode = graph[node]
                # Sort by proximity to bias point if variable-difficulty is selected
                # Runtime
                #   O(n log(n)), however, n is at most 3 so runtime is
                #    effectively constant
                nextNode.sort(key=lambda n: \
                              abs(n[0]-biasPoint[0]) + abs(n[1]-biasPoint[1]) )

                # Iterate through the neighbors of the current in sorted ordrer
                for succ in nextNode:
                    # Create new path containing path to the neighboring node
                    #  + the neighboring node
                    newPath = list(path)
                    newPath.append(succ)
                    # Add the new path to the queue to process
                    queue.append(newPath)

        # Return AI path (list of nodes)
        return path


    # Initialize empty set (global within function) that will conain
    #  visited nodes
    visited = set()

    # Compute bias point if difficulty is not set to random
    if difficulty is not -1:
        biasPoint = getBiasPoint(maze, end, difficulty)

    # If difficulty is not set to shortest path (101)
    if difficulty < 101:
        # Intialize variables that are global within the function
        found   = dfsPath.found = False
        path    = dfsPath.path  = []
        # Compute the AI path
        dfsPath(start, end) # modifies path
    # If the difficulty is set to shortest path
    else:
        # Find the shortest path out
        path = shortestPath(start, end)

    # Return path if maze is solvable, None otherwise
    return path if path else None


# That's all folks!
