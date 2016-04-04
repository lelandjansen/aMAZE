# search.py

# Search maze graph for path
# Sources:
#  Referenced dfs search algorithms written in class
#  and https://www.python.org/doc/essays/graphs/

import sys
import random
# random.seed(8)
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
    # Output
    #   path        List containing AI path nodes
    #
    # Runtime
    #   O(nodes + edges)
    #   Variable-difficulty runtime: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #
    # Note
    #   See test results for detailed analysis of path length vs difficulty
    #

    graph = maze.graph()


    if start not in graph:
        KeyError("Start node " + str(start) + " not in maze.")
    if end not in graph:
        KeyError("End node "   + str(end)   + " not in maze.")
    if difficulty < -1 or 101 < difficulty:
        ValueError("Difficulty must be between 0 and 100 (inclusive).")


    def dfsPath(node, end):

        visited.add(node)
        if not dfsPath.found:
            dfsPath.path += [node]

        nextNode = graph[node]

        if difficulty is -1:
            random.shuffle(nextNode)
        else:
            nextNode.sort(key=lambda n: \
                          abs(n[0]-biasPoint[0]) + abs(n[1]-biasPoint[1]) )

        for succ in nextNode:
            if succ == end:
                dfsPath.found = True
                dfsPath.path += [end]
            elif succ not in visited:
                dfsPath(succ, end)
                if not dfsPath.found:
                    dfsPath.path += [node]


    # find shortest path using breadth-first search
    def shortestPath(start, end):
        queue = deque([[start]])
        visited = set()

        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == end:
                return path
            elif node not in visited:
                visited.add(node)
                nextNode = graph[node]
                nextNode.sort(key=lambda n: \
                              abs(n[0]-biasPoint[0]) + abs(n[1]-biasPoint[1]) )
                for succ in nextNode:
                    newPath = list(path)
                    newPath.append(succ)
                    queue.append(newPath)

        return path



    visited = set()
    if difficulty is not -1:
        biasPoint = getBiasPoint(maze, end, difficulty)

    if difficulty < 101:
        found   = dfsPath.found = False
        path    = dfsPath.path  = []
        dfsPath(start, end) # modifies path
    else:
        path = shortestPath(start, end)

    # Return path if maze is solvable, None otherwise
    return path if path else None


# That's all folks!
