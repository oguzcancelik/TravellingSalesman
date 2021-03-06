import math
from random import randint
from matplotlib import pyplot as plt


def findClosest(i, data):
    dist = []
    global visited, totalDist, min, shiftVal
    visited.append(data[i][0])
    for j in range(len(data)):
        dist.append([j, round(
            math.sqrt(math.pow(data[i][1] - data[j][1], 2) + math.pow(data[i][2] - data[j][2], 2)))])
    dist = sorted(dist, key=lambda row: row[1])
    data.pop(i)
    totalDist += dist[1][1]
    if min > dist[1][1]:
        min = dist[1][1]
        shiftVal = len(visited)
    if dist[1][0] > i:
        return dist[1][0] - 1
    return dist[1][0]


def plot():
    global visited
    XX = []
    YY = []
    for k in range(len(visited)):
        XX.append(d2[visited[k]][1])
        YY.append(d2[visited[k]][2])
    plt.plot(XX, YY)
    plt.show()


data = [[]]
visited = []
totalDist = 0
input = input('Type name of the input file: ') + '.txt'
with open(input) as file:
    lines = file.readlines()
file.close()

randNum = randint(0, len(lines) - 1)
par = randNum

for i in range(len(lines)):
    temp = [int(j) for j in lines[i].split()]
    data.insert(i, temp)
data.pop()
d2 = list(data)

min = round(math.sqrt(math.pow(data[0][1] - data[1][1], 2) + math.pow(data[0][2] - data[1][2], 2)))
shiftVal = 0

while len(data) != 1:
    par = findClosest(par, data)

totalDist += round(math.sqrt(math.pow(d2[randNum][1] - data[0][1], 2) + math.pow(d2[randNum][2] - data[0][2], 2)))
visited.append(data[0][0])

for i in range(shiftVal):
    visited.append(visited.pop(0))

visited.append(visited[0])

while 1:
    oldTotalDist = totalDist
    for i in range(len(visited) - 1):
        for j in range(0, len(visited) - 1):
            if i == j or j == i + 1:
                continue
            # print('i,j: ', i, ', ', j)
            calc = round(math.sqrt(math.pow(d2[visited[i]][1] - d2[visited[i + 1]][1], 2) + math.pow(
                d2[visited[i]][2] - d2[visited[i + 1]][2], 2))) + \
                   round(math.sqrt(math.pow(d2[visited[j - 1]][1] - d2[visited[j]][1], 2) + math.pow(
                       d2[visited[j - 1]][2] - d2[visited[j]][2], 2))) + \
                   round(math.sqrt(math.pow(d2[visited[j + 1]][1] - d2[visited[j]][1], 2) + math.pow(
                       d2[visited[j + 1]][2] - d2[visited[j]][2], 2))) - \
                   round(math.sqrt(math.pow(d2[visited[j]][1] - d2[visited[i]][1], 2) + math.pow(
                       d2[visited[j]][2] - d2[visited[i]][2], 2))) - \
                   round(math.sqrt(math.pow(d2[visited[j]][1] - d2[visited[i + 1]][1], 2) + math.pow(
                       d2[visited[j]][2] - d2[visited[i + 1]][2], 2))) - \
                   round(math.sqrt(math.pow(d2[visited[j - 1]][1] - d2[visited[j + 1]][1], 2) + math.pow(
                       d2[visited[j - 1]][2] - d2[visited[j + 1]][2], 2)))
            if calc > 0:
                visited.insert(i + 1, visited[j])
                totalDist -= calc
                if i > j:
                    del visited[j]
                else:
                    del visited[j + 1]
                i = 0
                break
    if totalDist == oldTotalDist:
        break

# plot()
visited.pop()
visited.insert(0, totalDist)

output = "text" + input
file = open(output, 'w')

for i in visited:
    file.write("%s\n" % i)
file.close()

print(totalDist)