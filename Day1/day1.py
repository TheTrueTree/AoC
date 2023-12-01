def isThereNumber(numebrsih):
    for y in range(0, len(validList)):
        if (validList[y] in numebrsih):
            return validListDict[validList[y]]
    return 0

def grabInt(got):
    shenanigans = list(got)
    numbersList = []
    letterList = []
    for x in range(0, len(shenanigans)):
        try:
            numbersList.append(int(shenanigans[x]))
        except:
            letterList.append(shenanigans[x])
            letNum = isThereNumber(''.join(letterList))
            if letNum != 0:
                numbersList.append(letNum)
                letterList = [letterList[len(letterList)-1]]
            else:
                None
    return (numbersList[0]*10 + numbersList[(len(numbersList)-1)])

import fileinput

validList = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
validListDict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
answer = 0

for line in fileinput.input(files= 'Day1/input.txt'):
    answer += grabInt(line)

print(answer)
