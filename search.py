# search.py

# Search maze graph for path
# Sources:
#  Referenced search algorithms written in class
#  https://www.python.org/doc/essays/graphhs/

import sys
import random
random.seed(0) # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DELETE THIS

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


    path = [start]
    visited = set(start)
    found = False

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

    dfs.path = path
    dfs.visited = visited
    dfs.found = found
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

myMaze = Maze(16,16)
myMaze.generateMaze()
myGraph = myMaze.graph()


print("Smart AI:")
print(find_path(myGraph, (0,0), (15,15)))
print()
print("Kinda Smart AI:")
print(dfs_path(myGraph, (0,0), (15,15)))
# dfs_path(myGraph, (12,12), (31,31))

# print()
# print()
# print("Silly AI:")
# print(randomSearch(myMaze, (0,0), (80,90)))

# That's all folks!
