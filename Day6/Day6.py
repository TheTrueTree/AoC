import fileinput, re, math

record = [[],[],[1]]
count, splitter  = 0, ' '
pt2 = False
if (pt2):
    splitter = ':'
for line in fileinput.input("Day6/input.txt"):
    if(pt2):
        line = (line.replace(' ', ''))
    line = (line.replace('\n', '')).split(splitter)
    for thing in line:
        if(re.findall("\d", thing)):
            record[count].append(int(thing))
    count += 1

for z in range(0, len(record[0])):
    bounda = math.floor(-0.5 * (-record[0][z] + math.sqrt((record[0][z]**2)-4*record[1][z])) + 1)
    boundb = math.ceil(-0.5 * (-record[0][z] - math.sqrt((record[0][z]**2)-4*record[1][z])) - 1)
    record[2][0] *= (boundb - bounda + 1)

print(record[2][0])