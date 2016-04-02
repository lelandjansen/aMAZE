# search.py

# Search maze graph for path
# Sources:
#  Referenced search algorithms written in class
#  https://www.python.org/doc/essays/graphhs/

import sys
import random
# random.seed(0)

from generateMaze import Maze

recursionLimit = 1000000
sys.setrecursionlimit(recursionLimit)


# "Smart" AI
def find_path(maze, start, end, path=[]):
    # Source:
    #  https://www.python.org/doc/essays/graphhs/

    graph = maze.graph()

    if start not in graph:
        KeyError("Start node " + str(start) + " not in maze.")
    if end not in graph:
        KeyError("End node " + str(end) + " not in maze.")

    path = path + [start]
    if start == end:
        return path

    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None





def dfsPath(maze, start, end, mode):

    graph = maze.graph()

    if start not in graph:
        KeyError("Start node " + str(start) + " not in maze.")
    if end not in graph:
        KeyError("End node "   + str(end)   + " not in maze.")

    path    = [start]
    visited = set(start)
    found   = False

    def dfs(node, end):
        visited.add(node)
        nextNode = graph[node]

        if mode is 1: # random next node
            nextNode.sort(key=lambda x: abs(x[0]-start[0]) + abs(x[1]-start[1]))
        elif mode is 2: # "worst" next node
            random.shuffle(nextNode)
        elif mode is 3: # "best" next node
            nextNode.sort(key=lambda x: abs(x[0]-end[0]) + abs(x[1]-end[1]))

        for succ in nextNode:
            if succ == end:
                dfs.found = True
                dfs.path += [end]
                return
            if succ not in visited:
                if not dfs.found:
                    dfs.path += [succ]
                dfs(succ, end)
                if not dfs.found:
                    dfs.path += [succ]

    dfs.path    = path
    dfs.visited = visited
    dfs.found   = found

    dfs(start, end)

    return path



# "Silly" AI
# AI has 5000 tries to reach end
# If it is not successful, it retraces its steps to the start,
# then uses find_path to find a way out
def randomSearch(maze, start, end, path=[]):

    graph = maze.graph()

    if start not in graph:
        KeyError("Start node " + str(start) + " not in maze.")
    if end not in graph:
        KeyError("End node " + str(end) + " not in maze.")

    path = [start]
    for i in range(5000):
        path.append(random.choice(graph[path[-1]]))
        if path[-1] == end:
            break

    if path[-1] is not end:
        path += path[::-1]
        path += find_path(graph, start, end)

    return path




def ai(intelligence, maze, start, end):
    if intelligence is 1:
        return randomSearch(maze, start, end)
    elif intelligence is 2:
        return dfsPath(maze, start, end, 1)
    elif intelligence is 3:
        return dfsPath(maze, start, end, 2)
    elif intelligence is 4:
        return dfsPath(maze, start, end, 3)
    else:
        raise ValueError("AI level " + str(intelligence) + " does not exist.")




mazeSize   = (5, 10)
startCoord = (2,3)
endCoord   = (7,8)


myMaze = Maze(mazeSize[0],mazeSize[1])
myMaze.generateMaze()
myGraph = myMaze.graph()


scoreList = []

for x in range(mazeSize[0]):
    scoreList.append([])
    for y in range(mazeSize[1]):
        scoreList[x].append(abs((abs(x-endCoord[0]) + abs(y-endCoord[1]))))

for i in range(len(scoreList)):
    for j in range(len(scoreList[i])):
        number = scoreList[i][j]
        if number < 10:
            print(" ", end="")
        print("   " + str(number), end="")
    print()
    print()



# To compute farthest point (manhattan)
# (sizeX-2(sizeX//2 - endX//2)) + (sizeY-2(sizeY//2 - endY//2))


def biasPoint(maze, end, difficulty):
    # maze: Maze class
    # end: Tuple containing end point
    # difficulty: Integer between 0 and 100

    if end not in maze.graph():
        KeyError("End point " + str(end) + " not in maze.")
    if difficulty < 0 or 100 < difficulty:
        ValueError("Difficulty must be between 0 and 100 (inclusive).")

    size = (maze.get_sizex(), maze.get_sizey())

    farthestPointScore = size[0] - 2*(size[0]//2 - end[0]//2) + \
                         size[1] - 2*(size[1]//2 - end[1]//2)

    # Compute AI bias score based on difficulty
    biasScore = farthestPointScore - (difficulty * farthestPointScore) // 100

    biasPoint = list(end)

    direction = (random.choice([-1, 1]), random.choice([-1, 1]))

    for d in range(biasScore):
        i = random.choice([0, 1])
        biasPoint[i] += direction[i]
    biasPoint = tuple(biasPoint)
    print(biasPoint)


biasPoint(myMaze, endCoord, 80)


# print()
# myPath = dfsPath(myGraph, startCoord, endCoord, 1)
# print("Worst path DFS:" + str(len(myPath)))
# print(myPath)
#
# print()
# myPath = dfsPath(myGraph, startCoord, endCoord, 2)
# print("Random path DFS: " + str(len(myPath)))
# print(myPath)
#
# print()
# myPath = dfsPath(myGraph, startCoord, endCoord, 3)
# print("Best path DFS: " + str(len(myPath)))
# print(myPath)
#
# print()
# myPath = find_path(myGraph, startCoord, endCoord)
# print("Shortest path: " + str(len(myPath)))
# print(myPath)
#
#
#
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()












# print("Silly AI:")
# print(randomSearch(myMaze, (0,0), (80,90)))

# That's all folks!
