import math, sys, os
from random import randint
# from matplotlib import pyplot as plt


def findClosest(x, data):
    dist = []
    global visited, totalDist
    visited.append(data[x][0])
    for j in range(len(data)):
        dist.append([j, round(
            math.sqrt(math.pow(data[x][1] - data[j][1], 2) + math.pow(data[x][2] - data[j][2], 2)))])
    dist = sorted(dist, key=lambda row: row[1])
    data.pop(x)
    totalDist += dist[1][1]
    if dist[1][0] > x:
        return dist[1][0] - 1
    return dist[1][0]


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


data = [[]]
visited = []
totalDist = 0
filename = 'g.txt'
with open(filename) as file:
    lines = file.readlines()
file.close()

for i in range(len(lines)):
    temp = [int(j) for j in lines[i].split()]
    data.insert(i, temp)
data.pop()
d2 = list(data)
# randNum = randint(0, len(lines) - 1)
randNum = 0
print('randNum: ', randNum)
temp = data[randNum]
par = randNum

while len(data) != 1:
    par = findClosest(par, data)
    print(par)

totalDist += round(math.sqrt(math.pow(temp[1] - data[0][1], 2) + math.pow(temp[2] - data[0][2], 2)))

visited.append(data[0][0])
visited.append(d2[randNum][0])
print('totalDist: ', totalDist)
# for k in range(5):
# while 1:
#     oldTotalDist = totalDist
for i in range(len(visited)):
    for j in range(i + 2, len(visited) - 1):
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
    print(i)
print('totalDist: ', totalDist)
    # if oldTotalDist == totalDist:
    #     break

visited.pop()

# plot()
visited.insert(0, totalDist)
for i in visited:
    print(i)
outfile = "output"+filename
file = open(outfile, 'w')
for i in visited:
    file.write("%s\n" % i)
file.close()

# sys.exit(totalDist)
# outfile = "python tsp-verifier.py " + filename+ " output"+filename
# os.system(outfile)
# print(outfile)