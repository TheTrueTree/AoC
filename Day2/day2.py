def logic(textLine, bounds):
    rgb = [0,0,0,0]
    split = re.split(': |, |; | ', textLine)
    split.pop(0)
    rgb[0] = int(split[0])
    split.pop(0)
    split[len(split)-1]  = split[len(split)-1] .replace("\n", "")

    print(split)

    for x in range (1, len(split), 2):
        cur_ind = direct[split[x]]
        if(int(split[x-1]) > rgb[cur_ind]):
            rgb[cur_ind] = int(split[x-1])

    print(rgb)

    # for y in range(0,3):
    #     if (rgb[y+1] > bounds[y]):
    #         return rgb[0], False    
    
    return rgb, True

import fileinput, re

direct = {"red": 1, "green": 2, "blue": 3}
answer = 0
for line in fileinput.input(files= 'Day2/input.txt'):
    number, whether = logic(line, [12,13,14])
    if(whether):
        answer += number[1] * number[2] * number[3]
        print(answer)

print(answer)