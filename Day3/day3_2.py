import fileinput, re
Values, numbers, gears = [], [], []

for line in fileinput.input("Day3/input.txt"):
    line = list(line.replace('\n', '')) 
    numLocation = [i for i in range(len(line)) if re.findall("\d", line[i])]
    gearLocation = [i for i in range(len(line)) if re.findall("[*]", line[i])]

    numbers.append(numLocation)
    gears.append(gearLocation)

    digitList, indexList = [], []
    for x in range(0, len(line)):
        if(re.findall('\d', line[x])):
            digitList.append(line[x])
            indexList.append(x)
            if(len(line) - 1 == x):
                for y in range(0, len(indexList)):
                    line[indexList[y]] = ''.join(digitList)
                digitList, indexList = [], []
        elif(x != len(line) - 1):
            if(digitList != []):
                for y in range(0, len(indexList)):
                    line[indexList[y]] = ''.join(digitList)
                digitList, indexList = [], []
    
    Values.append(line)

print(numbers)
                

    
    
