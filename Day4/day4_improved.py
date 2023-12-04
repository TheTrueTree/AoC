def getScore(count):
    if(count <= 0):
        return count
    return 2**(count-1)

import fileinput

numberMatrix, winnersMatrix, countMatrix = [], [], []
for line in fileinput.input("Day4/input.txt"):
    line = (line.replace('\n', '')).split(' ')
    line = list(filter(lambda a: a != '', line))

    divider = line.index('|')
    numbers = [line[i] for i in range(divider+1, len(line))]
    winners = [line[i] for i in range(2, divider)]
    numberMatrix.append(numbers)
    winnersMatrix.append(winners)
    countMatrix.append(len(list(filter(lambda a: a in winners, [i for i in numbers]))))

multipliers, scratchNum, score = [1] * len(numberMatrix), 0, 0

for x in range(0, len(multipliers)):
    scratchNum += multipliers[x]
    affected = list(filter(lambda i: i < len(multipliers), [i for i in range(x+1, x+1+countMatrix[x])]))
    score += getScore(countMatrix[x])
    for y in affected:
        multipliers[y] += 1*multipliers[x]

print("Score:", score, "Number of Cards:", scratchNum)