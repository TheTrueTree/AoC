def bufferAdd(numBuffer, indexMemory):
    if(numBuffer != []):
        current = ''.join(numBuffer)
        for a in range(0, len(indexMemory)):
            curLine[indexMemory[a]] = current
        numBuffer = []
        indexMemory = []
    return numBuffer, indexMemory

def getLookup(lookup, x, y , xa, ya):
    if(x==0):
        if(y==0):
            return [lookup[x][y+1], lookup[x+1][y], lookup[x+1][y+1]]
        else:
            if(y < (ya-1)):
                return [lookup[x][y-1], lookup[x][y+1], lookup[x+1][y-1], lookup[x+1][y], lookup[x+1][y+1]]
            else:
                return [lookup[x][y-1], lookup[x+1][y-1], lookup[x+1][y]]
    elif(y==0):
        if(x < (xa-1)):
            return [lookup[x-1][y], lookup[x-1][y+1], lookup[x][y+1], lookup[x+1][y], lookup[x+1][y+1]]
        else:
             return [lookup[x-1][y], lookup[x-1][y+1], lookup[x][y+1]]
    else:
        if(x >= (xa-1)):
            if(y >= (ya - 1)):
                return [lookup[x-1][y-1], lookup[x-1][y], lookup[x][y-1]]
            else:
                return [lookup[x-1][y-1], lookup[x-1][y], lookup[x-1][y+1], lookup[x][y-1], lookup[x][y+1]]
        elif(y >= (ya-1)):
            return [lookup[x-1][y-1], lookup[x-1][y], lookup[x][y-1], lookup[x+1][y-1], lookup[x+1][y]]
        else:
            return [lookup[x-1][y-1], lookup[x-1][y], lookup[x-1][y+1], lookup[x][y-1], lookup[x][y+1], lookup[x+1][y-1], lookup[x+1][y], lookup[x+1][y+1]]

import fileinput, re

answer = []
lookup = []

for line in fileinput.input(files= 'Day3/input.txt'):
    curLine = list(line.replace('\n', ''))

    indexMemory = []
    numBuffer = []
    for z in range(0, len(curLine)):
        if (re.findall("[0-9]", curLine[z])):
            indexMemory.append(z)
            numBuffer.append(curLine[z])
            if(z == (len(curLine)-1)):
                numBuffer, indexMemory = bufferAdd(numBuffer,indexMemory)
        else:
            if(numBuffer != []):
                numBuffer, indexMemory = bufferAdd(numBuffer,indexMemory)
    
    lookup.append(curLine)

for x in range(0, len(lookup)):
    guard = 0
    for y in range(0, len(lookup[x])):
        if(guard != 0):
            guard = guard - 1
            continue

        thisCon = getLookup(lookup, x, y, len(lookup), len(lookup[x]))
        if(len(lookup[x][y]) != 1):
            guard = len(lookup[x][y]) - 1
            for z in range(1, len(lookup[x][y])):
                thisCon = thisCon + getLookup(lookup, x, y+z, len(lookup), len(lookup[x]))

        print(thisCon)
        curr = ''.join(thisCon)

        print(curr)
        curr = re.sub("[0-9]", '', curr)
        curr = re.sub("[.]", '', curr)
        curr = re.sub("[0-9]", 'x', curr)

        if(curr != ''):
            if(re.findall("[0-9]", lookup[x][y])):
                answer.append(lookup[x][y])
            elif(re.findall("[*]", lookup[x][y])):
                print(curr)
        
final = 0
for z in range(0, len(answer)):
    final += int(answer[z])

print(final)