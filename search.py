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










def getBiasPoint(maze, end, difficulty):
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

    if biasScore is 0:
        return end
    #
    # biasPoint = [0, 0]
    #
    # # Runtime: O(farthestPointScore) worst case
    # stepsRemaining = biasScore
    # while stepsRemaining:
    #     i = random.choice([0, 1])
    #     bound = end[i] if stepsRemaining > end[i] else stepsRemaining
    #     steps = random.randint(1, bound)
    #     biasPoint[i] += steps
    #     stepsRemaining -= steps
    #
    # reflections = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # random.shuffle(reflections)
    # for r in reflections:
    #     x, y = end[0] + r[0]*biasPoint[0], end[1] + r[1]*biasPoint[1]
    #     if 0 <= x and x < maze.get_sizex() and 0 <= y and y < maze.get_sizey():
    #        return (x, y)


    points = []

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

    if not points:
        print("EMPTY")

    return random.choice(points)







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
            newpath = find_path(maze, node, end, path)
            if newpath: return newpath
    return None





def dfsPath(maze, start, end, difficulty):

    # print("difficulty: " + str(difficulty))
    # print("end: " + str(end))

    graph = maze.graph()

    if start not in graph:
        KeyError("Start node " + str(start) + " not in maze.")
    if end not in graph:
        KeyError("End node "   + str(end)   + " not in maze.")

    path    = [start]
    visited = set(start)
    found   = False

    if difficulty is not -1:
        biasPoint = getBiasPoint(maze, end, difficulty)

    def dfs(node, end):
        visited.add(node)
        nextNode = graph[node]

        if difficulty is -1: # random next node
            random.shuffle(nextNode)
        else:
            nextNode.sort(key=lambda n: abs(n[0]-biasPoint[0]) + abs(n[1]-biasPoint[1]))

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

                if abs(path[-1][0] - path[-2][0]) == 1 and abs(path[-1][1] - path[-2][1]) == 1:
                    print("SKIP!!!")

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
        path += find_path(maze, start, end)

    return path




# mazeSize   = (16, 16)
# startCoord = (3,3)
# endCoord   = (12,12)
#
#
# myMaze = Maze(mazeSize[0],mazeSize[1])
# myMaze.generateMaze()
# myGraph = myMaze.graph()
#
#
# scoreList = []
#
# for x in range(mazeSize[0]):
#     scoreList.append([])
#     for y in range(mazeSize[1]):
#         scoreList[x].append(abs((abs(x-endCoord[0]) + abs(y-endCoord[1]))))
#
# scoreList = list(zip(*scoreList))
#
# for i in range(len(scoreList)):
#     for j in range(len(scoreList[i])):
#         number = scoreList[i][j]
#         if number < 10:
#             print(" ", end="")
#         print("   " + str(number), end="")
#     print()
#     print()
#
#
#
#
#
#
#
#
# # n = 100000
# # result = {}
# # for i in range(n):
# #     answer = getBiasPoint(myMaze, endCoord, 50)
# #     if answer in result:
# #         result[answer] += 1
# #     else:
# #         result[answer] = 1
# #
# # print("Expected: " + str(1/len(result)))
# #
# # for r in result:
# #     print(str(r) + ": " + str(result[r]/n))
#
#
# for difficulty in range(0,101):
#     l = []
#     for t in range(1000):
#         l.append(len(dfsPath(myMaze, startCoord, endCoord, difficulty)))
#     # print("Difficulty " + str(difficulty) + ": " + str(sum(l) / len(l)))
#     print(sum(l)/len(l))




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
