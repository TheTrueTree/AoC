#Cases
# |  |         , |   |     ,   |  |   ,    |  |  ,      |   |  , |       | 
#      |    |  ,   |    |  , |      | ,  |   |   , |   |       ,    |   |
def getNewSeeds(seedList, mode):
    newSeeds = []
    for seed in seedList:
        for z in range(0, len(direct[mode])):
            this = direct[mode][z]
            if(seed[1] < this[0]): # Case 1
                newSeeds.append(seed)
                break
            elif((seed[0] < this[0]) and (this[0] <= seed[1] <= this[1])): #case 2
                newSeeds.append((seed[0], this[0] - 1))
                newSeeds.append((this[0] + this[2], this[1] + this[2]))
            elif((seed[0] > this[0]) and (seed[1] < this[1])): #Case 3
                newSeeds.append(((seed[0] + this[2]), (seed[1] + this[2])))
                break
            elif((this[1] > seed[0] >= this[0]) and (seed[1] > this[1])): #Case 4
                newSeeds.append((seed[0] + this[2], this[1] + this[2]))
                newSeeds.append((this[1] + 1, seed[1]))
            elif(seed[0] > this[1]): #Case 5
                if(z == (len(direct[mode]) - 1)):
                    newSeeds.append(seed)
                continue
            elif((seed[0] < this[0]) and (seed[1] > this[1])): #Case 6
                newSeeds.append((seed[0], this[0] - 1))
                newSeeds.append((this[0] + this[2], this[1] + this[2]))
                newSeeds.append((this[1] + 1, seed[1]))
    return(newSeeds)


import fileinput, re

mode, direct = 0, [[],[],[],[],[],[],[],[]]
for line in fileinput.input("Day5/input.txt"):
    if(line == '\n'):
        mode += 1
        continue
    line = (line.replace('\n', '')).split(' ')
    if(line[0] == "seeds:"):
        for seed in range(1,len(line), 2):
            direct[0].append((int(line[seed]), (int(line[seed]) + int(line[seed+1]))))
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

for z in range(1, 2):
    print(direct[0])
    direct[0] = getNewSeeds(direct[0], z)


print(direct[0])