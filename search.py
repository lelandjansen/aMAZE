# search.py

# Search maze graph for path
# Sources:
#  Referenced search algorithms written in class
#  https://www.python.org/doc/essays/graphhs/

import sys
import random
# random.seed(0) # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DELETE THIS

# from generateMaze import Maze
from generateMaze import Maze

recursionLimit = 1000000
sys.setrecursionlimit(recursionLimit)


# "Smart" AI
def find_path(graph, start, end, path=[]):
    # Source:
    #  https://www.python.org/doc/essays/graphhs/

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


# "Kinda smart" AI
def dfs_path(graph, start, end):

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
        random.shuffle(nextNode)
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


# "A bit sillier smart" AI
# Objective: Choose the path that will take the AI furthest from the goal
def dfs_path_silly(graph, start, end):
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

        nextNode.sort(key=lambda x: abs(x[0]-start[0]) + abs(x[1]-start[1]) )
        # print(nextNode)

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








# "A bit sillier smart" AI
# Objective: Choose the path that will take the AI furthest from the goal
def dfs_path_smart(graph, start, end):
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

        nextNode.sort(key=lambda x: abs(x[0]-end[0]) + abs(x[1]-end[1]) )
        # print(nextNode)

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
def randomSearch(graph, start, end, path=[]):

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




def ai(intelligence, graph, start, end):
    if intelligence is 1:
        return randomSearch(graph, start, end)
    elif intelligence is 2:
        return dfs_path(graph, start, end)
    elif intelligence is 3:
        return find_path(graph, start, end)
    elif intelligence is 4:
        return aStar(graph, start, end)
    else:
        raise ValueError("Intelligence level " + str(intelligence)
                            + " does not exist")




mazeSize = 16
startCoord = (0,0)
endCoord = (mazeSize-1,mazeSize-1)


myMaze = Maze(mazeSize,mazeSize)
myMaze.generateMaze()
myGraph = myMaze.graph()



print("Smart AI:")
print(len(find_path(myGraph, startCoord, endCoord)))

print()
print("Kinda Smart Smarter AI:")
print(len(dfs_path_smart(myGraph, startCoord, endCoord)))

print()
print("Kinda Smart AI:")
print(len(dfs_path(myGraph, startCoord, endCoord)))

print()
print("Kinda Smart Sillier AI:")
print(len(dfs_path_silly(myGraph, startCoord, endCoord)))



# print()
# print()
# print("Silly AI:")
# print(randomSearch(myMaze, (0,0), (80,90)))

# That's all folks!
