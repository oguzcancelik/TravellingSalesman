import math
from random import randint


def findClosest(i, data):
    dist = []
    global visited
    x = data.index([x for x in data if i in x][0])
    visited.append(data[x][0])
    # visited.append('x:  ' + str(x))
    for j in data:
        dist.append([j[0], round(
            math.sqrt(math.pow(data[x][1] - j[1], 2) + math.pow(data[x][2] - j[2], 2)))])
    dist = sorted(dist, key=lambda row: row[1])
    if len(data) == 1:
        return 0
    data.pop(x)
    return dist[1][1] + findClosest(dist[1][0], data)


data = [[]]
visited = []

with open('text3.txt') as file:
    lines = file.readlines()
file.close()
for i in range(len(lines)):
    temp = [int(j) for j in lines[i].split()]
    data.insert(i, temp)
data.pop()

randNum = randint(0, len(lines) - 1)
# randNum = 0
temp = data[randNum]
counter = 0
totalDist = findClosest(randNum, data) + round(
    math.sqrt(math.pow(temp[1] - data[0][1], 2) + math.pow(temp[2] - data[0][2], 2)))

visited.insert(0, totalDist)

file = open('output.txt', 'w')
print(visited[0])
for i in visited:
    file.write("%s\n" % i)
file.close()
