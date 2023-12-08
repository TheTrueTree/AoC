def getNew(l1, l2):
    toSort = []
    for x in range(0, len(l1)):
        for y in range(0, len(l2)):
            if((l1[x][0] < l2[y][1]) & (l1[x][1] >= l2[y][0])):
                if((l1[x][0] == l2[y][0]) & (l1[x][1] < l2[y][1])):
                    toSort.append([l1[x][0], l1[x][1], (l1[x][2] + l2[y][2])])
                elif((l1[x][0] > l2[y][0]) & (l1[x][1] > l2[y][1])):
                    toSort.append([l1[x][0], l2[y][1], (l1[x][2] + l2[y][2])])
                elif((l1[x][0] < l2[y][0]) & (l1[x][1] <= l2[y][1])):
                    toSort.append([l2[y][0], l2[y][1], (l1[x][2] + l2[y][2])])
    return toSort

def getLocation(number, mode):
    if (mode == 7):
        return number
    for x in range(0, len(direct[mode+1])):
        if((number >= direct[mode+1][x][0]) & (number <= direct[mode+1][x][1])):
            return getLocation(number+direct[mode+1][x][2], mode+1)
    return getLocation(number, mode+1)

def getBroadLocation(lower, upper):
    for x in range(0, len(direct[1])):
        if((lower >= direct[1][x][0]) & (lower <= direct[1][x][1])):
            lowerScore = getLocation(lower, 1)
            if((upper >= direct[1][x][0]) & (upper <= direct[1][x][1])):
                upperScore = getLocation(upper, 1)
                if(lowerScore < upperScore):
                    return lowerScore
                return upperScore
            else:
                furtherBound = getBroadLocation(direct[1][x][1]+1, upper)
                upperScore = getLocation(direct[1][x][1], 1)
                if(lowerScore < upperScore):
                    if(lowerScore < furtherBound):
                        return lowerScore
                else:
                    if(upperScore < furtherBound):
                        return upperScore
                return furtherBound

import fileinput, re, math

mode, direct = 0, [[],[],[],[],[],[],[],[]]
for line in fileinput.input("Day5/input.txt"):
    if(line == '\n'):
        mode += 1
        continue
    line = (line.replace('\n', '')).split(' ')
    if(line[0] == "seeds:"):
        for seed in range(1,len(line), 2):
            direct[0].append((int(line[seed]), int(line[seed+1])))
    if(re.findall("\d", line[0])):
        line = [int(line[0]), int(line[1]), int(line[2])]
        direct[mode].append([line[1], (line[1] + line[2] - 1), (line[0] - line[1])])

for y in range(1, 7):
    for a in range(0, len(direct[y])):
        minimum = a
        for b in range(a+1, len(direct[y])):
            if direct[y][b][0] < direct[y][minimum][0]:
                minimum = b
        
        temp = direct[y][a]
        direct[y][a] = direct[y][minimum]
        direct[y][minimum] = temp


midMaps = []
for a in range(1, len(direct)):
    for b in range(0, len(direct[a])):
        midMaps.append(direct[a][b])

for c in range(1, len(direct)):
    for a in range(0, len(direct[c])):
        minimum = a
        for b in range(a+1, len(direct[c])):
            if (direct[c][b][0] + direct[c][b][1]) < direct[c][minimum][0]:
                minimum = b
        
        temp = direct[c][a]
        direct[c][a] = direct[c][minimum]
        direct[c][minimum] = temp

print(getNew(direct[1], direct[2]))