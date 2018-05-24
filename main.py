import math
from random import randint
from matplotlib import pyplot as plt

def plot():
    global visited
    XX = []
    YY = []
    for k in range(len(visited) - 1):
        XX.append(d2[visited[k]][1])
        YY.append(d2[visited[k]][2])
    # XX.append(d2[0][1])
    # YY.append(d2[0][2])
    plt.plot(XX, YY)
    plt.show()


def random(data, d2):
    global visited, totalDist
    while len(data) != 1:
        randNum = randint(0, len(data) - 2)
        visited.append(data[randNum][0])
        data.pop(randNum)
    visited.append(data[0][0])
    # print(visited)
    totalDist = 0
    for i in range(len(visited) - 2):
        totalDist += round(math.sqrt(math.pow(d2[visited[i]][1] - d2[visited[i + 1]][1], 2) + math.pow(
            d2[visited[i]][2] - d2[visited[i + 1]][2], 2)))
    totalDist += round(
        math.sqrt(math.pow(d2[visited[i]][1] - data[0][1], 2) + math.pow(d2[visited[i]][2] - data[0][2], 2)))


data = [[]]
visited = []
totalDist = 0
with open('text1.txt') as file:
    lines = file.readlines()
file.close()

for i in range(len(lines)):
    temp = [int(j) for j in lines[i].split()]
    data.insert(i, temp)
data.pop()
d2 = list(data)

random(data,d2)
for k in range(4):
    for i in range(len(visited)):
        for j in range(i + 2, len(visited) - 2):
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
                del visited[j + 1]
                totalDist -= calc
    print(totalDist)


visited.pop()
visited.insert(0, totalDist)
print(totalDist)
file = open('output.txt', 'w')
for i in visited:
    file.write("%s\n" % i)
file.close()
del visited[0]
plot()