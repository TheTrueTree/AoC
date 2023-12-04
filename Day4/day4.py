def getScore(count):
    if(count == 0):
        return 0
    elif(count == 1):
        return 1
    else:
        count -= 1
        points = 1
        while(count != 0):
            points *= 2
            count -=1
        return points

import fileinput, re

numbersTot = []
winningNumbersTot = []
winningNumberCounts = []

for line in fileinput.input("Day4/input.txt"):
    line = (line.replace('\n', '')).split(' ')
    winningNumbers, numbers = [], []
    guardA, guardB = False, False
    for x in range(0, len(line)):
        if(guardA & (line[x] != '')):
            if(guardB):
                numbers.append(line[x])
            elif(line[x] == '|'):
                guardB = True
            else:
                winningNumbers.append(line[x])
        elif(re.findall("[:]", line[x])):
            guardA = True

    winningNumberCount = 0
    for thing in numbers:
        if thing in winningNumbers:
            winningNumberCount += 1
        
    numbersTot.append(numbers)
    winningNumberCounts.append(winningNumberCount)
    winningNumbersTot.append(winningNumbers)

multipliers = [1] * len(winningNumberCounts)
score = 0

for y in range(0, len(multipliers)):
    thisScore = getScore(winningNumberCounts[y])
    for b in range(0, multipliers[y]):
        for z in range(y+1, y+winningNumberCounts[y]+1):
            if(z < len(multipliers)):
                multipliers[z] += 1
    # print(multipliers)
    # print(winningNumbersTot[y], ' | ', numbersTot[y])
    # print(winningNumberCounts[y])
    thisScore *= multipliers[y]
    score += thisScore

scratchcards = 0
for ad in range(0, len(multipliers)):
    scratchcards += int(multipliers[ad])

print(scratchcards)

