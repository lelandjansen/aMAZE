# search.py

# Search maze graph for path
# Sources:
#  Referenced search algorithms written in class
#  https://www.python.org/doc/essays/graphhs/

import sys
import random

from generateMaze import generateMaze
from generateMaze import printMaze

recursionLimit = 1000000
sys.setrecursionlimit(recursionLimit)


# "Smart" AI
def find_path(graph, start, end, path=[]):
    # Source:
    #  https://www.python.org/doc/essays/graphhs/

    if start not in graph or end not in graph:
        return None

    path = path + [start]
    if start == end:
        return path
    # if not start in graph:
    #     return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


# "Silly" AI
# AI has 5000 tries to reach end
# If it is not successful, it retraces its steps to the start,
# then uses find_path to find a way out
def randomSearch(graph, start, end, path=[]):

    if start not in graph or end not in graph:
        return None

    path = [start]
    for i in range(5000):
        path.append(random.choice(graph[path[-1]]))
        if path[-1] == end:
            break

    if path[-1] is not end:
        path += path[::-1]
        path += find_path(graph, start, end)

    return path



# myMaze = generateMaze(20, 20, 0, 0)
# print("Shortest path:")
# print(find_path(myMaze, (0,0), (4,4)))
# print()
# print()
# print("Random path:")
# print(randomSearch(myMaze, (0,0), (4,4)))

# That's all folks!
