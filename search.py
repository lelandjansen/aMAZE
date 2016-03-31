# search.py

# Search maze graph for path
# Sources:
#  Referenced search algorithms written in class
#  https://www.python.org/doc/essays/graphhs/

import sys
import random
random.seed(0) # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DELETE THIS

from generateMaze import generateMaze
from generateMaze import printMaze

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
def dfs_path(graph, start, end, path=[]):

    if start not in graph:
        KeyError("Start node " + str(start) + " not in maze.")
    if end not in graph:
        KeyError("End node " + str(end) + " not in maze.")


    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            path = path + find_path(graph, node, end, path)

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



myMaze = generateMaze(9000, 9000, 0, 0)
print("Smart AI:")
print(len(find_path(myMaze, (0,0), (700,700))))
print()
print()
print("Kinda Smart AI:")
print(len(dfs_path(myMaze, (0,0), (700,700))))
# print()
# print()
# print("Silly AI:")
# print(randomSearch(myMaze, (0,0), (80,90)))

# That's all folks!
