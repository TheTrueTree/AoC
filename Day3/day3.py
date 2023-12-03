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

def check(inp):
    newL = []
    for x in range(0, len(inp)):
        if(x != len(inp) - 1):
            if(inp[x] == inp[x+1]):
                continue
            else:
                newL.append(inp[x])
        else:
            newL.append(inp[x])
    
    return newL
        
def getList(cord):
    mx = 0
    my = 0
    ax = 0
    ay = 0

    minBound = (0,0)
    maxBound = (0,0)


    if(cord[0] == 0):
        mx = cord[0]
    else:
        mx = cord[0] - 1

    if(cord[0] == len(lookup)):
        my = cord[0]
    else:
        my = cord[0] + 1

    if(cord[1] == 0):
        ax = cord[1]
    else:
        ax = cord[1] - 1

    if(cord[1] == len(lookup[0])):
        ay = cord[1]
    else:
        ay = cord[1] + 1

    minBound = (mx, ax)
    maxBound = (my, ay)
    lister = []
    
    for th in range(minBound[0], maxBound[0]+1):
        for at in range(minBound[1], maxBound[1]+1):
            if(re.findall("[0-9]", lookup[th][at])):
                if((at + 1) <= maxBound[1]):
                    if(lookup[th][at+1] == lookup[th][at]):
                        continue
                    else:
                        lister.append(lookup[th][at])
                else:
                    lister.append(lookup[th][at])

    
    return lister


import fileinput, re

answer = []
lookup = []
buffer = []

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


        curr = ' '.join(thisCon)
        curr = re.sub("[.]", '', curr)
        test = curr.split(' ')
        
        curr = []
        for l in range(0, len(test)):
            if(re.findall("[0-9]", test[l])):
                curr.append(test[l])
        curr = check(curr)
        if(lookup[x][y] == '*'):
            buffer.append((x, y))
            if(len(curr) == 2):
                a = int(curr[0])
                b = int(curr[1])
                ab = a*b
                answer.append(str(ab))
        
thisA = 0
for x in range(0, len(buffer)):
    thi = getList(buffer[x])
    if(len(thi) == 2):
        a = int(thi[0])
        b = int(thi[1])
        thisA += a*b


print(thisA)