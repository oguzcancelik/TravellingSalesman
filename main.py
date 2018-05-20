import math
import matplotlib.pyplot as plt
from numpy import array


def findClosest():
    global totalDist, curX, city
    min = 500000
    next = 0
    noc = len(city)
    for a in range(noc):
        dist = int(round(math.sqrt(math.pow(curX - int(x[a]), 2) + math.pow(curY - int(y[a]), 2))))
        if dist < min:
            min = dist
            next = a
    totalDist += min
    # visited.append(min)
    return next


city = []
x = []
y = []
visited = []
totalDist = 0
curX = 0
curY = 0

with open('text1.txt') as f:
    lines = f.readlines()
nol = len(lines)  ##number of lines

for i in range(nol):
    temp = lines[i].split()
    city.append(temp[0])
    x.append(temp[1])
    y.append(temp[2])
    # print(city[i], x[i], y[i])

count = 0
val = 0
while (count < nol - 1):
    visited.append(city[val])
    curX = int(x[val])
    curY = int(y[val])
    del city[val]
    del x[val]
    del y[val]
    val = findClosest()
    count += 1
dist = int(round(math.sqrt(math.pow(int(x[0]) - int(x[val]), 2) + math.pow(int(y[0]) - int(y[val]), 2))))
totalDist += dist
visited.append(city[val])
# visited.append(dist)
visited.append(totalDist)

thefile = open('output1.txt', 'w')
for item in visited:
    thefile.write("%s\n" % item)
