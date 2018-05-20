import math
from random import randint
import numpy as np
from matplotlib import pyplot as plt


def findClosest(i, data):
    dist = []
    global visited
    for j in data:
        x = [x for x in data if i in x][0]
        x = data.index(x)
        dist.append([j[0], round(
            math.sqrt(math.pow(data[x][1] - j[1], 2) + math.pow(data[x][2] - j[2], 2)))])
    visited.append(data[x][0])
    dist = sorted(dist, key=lambda row: row[1])
    if len(data) == 1:
        return 0
    # if len(data) == 2:
    #     return dist[0][1] + findClosest(dist[0][0], list(data))
    # if len(data) == 3:
    #     return min(dist[0][1] + findClosest(dist[0][0], list(data)),
    #                dist[1][1] + findClosest(dist[1][0], list(data)))

    data.pop(x)
    dist.pop(0)

    # print(i, dist[0][1])
    # print(i, dist[0][0])
    # print(i, dist[1][1])
    # print(i, dist[1][0])
    # print(i, dist[2][1])
    # print(i, dist[2][0])
    #
    # return dist[0][1] + findClosest(dist[0][0], list(data))
    return dist[0][1] + findClosest(dist[0][0], list(data))
    # x1 = dist[0][1] + findClosest(dist[0][0], list(data))
    # x2 = dist[1][1] + findClosest(dist[1][0], list(data))
    # # x3 = dist[2][1] + findClosest(dist[2][0], list(data))
    # return min(x1, x2)


data = [[]]
visited = []

with open('text1.txt') as file:
    lines = file.readlines()
for i in range(len(lines)):
    temp = [int(j) for j in lines[i].split()]
    data.insert(i, temp)
data.pop()
#
# x, y = np.array([[[i[1], i[2]] for i in data]]).T
# plt.scatter(x, y)
# plt.show

# randNum = randint(0, len(lines) - 1)
randNum = 0
temp = data[randNum]

totalDist = findClosest(randNum, data)
# totalDist += round(math.sqrt(
#     math.pow(temp[1] - data[0][1], 2) + math.pow(temp[2] - data[0][1], 2)))

visited.insert(0, totalDist)

file = open('output.txt', 'w')
for i in visited:
    print(i)
    file.write("%s\n" % i)
