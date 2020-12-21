#import math
with open("trees.txt", "r") as f:
    content = f.readlines()
map_basis = [x.strip() for x in content]
##Right 3 down by 1
##y = -1/3x
height = len(content)
##height = -1/3x
##soooo height *3? for total width...
width = len(content[0])
maxWidth = height * 3
##print(height)
#print(width)
##print(maxWidth)
##print(maxWidth/width)
i = 0
j = 0
trees = 0
while i < height:
    element = content[i][j%31]
#    print("POS:" + str(i) + " " + str(pos+3) + " " + element)
    if element == '#':
        trees += 1
    i += 1
    j += 3
print(trees)