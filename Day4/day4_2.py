def getScore(count):
    if(count <= 0):
        return count
    return 2**(count-1)

import fileinput, re

for line in fileinput.input("Day4/input.txt"):
    line = (line.replace('\n', '')).split(' ')
    line = list(filter(lambda a: a != '', line))
    winners, numbers = [], []

    print(line)