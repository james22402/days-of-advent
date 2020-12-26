import copy
with open("c:\\Users\\madri\\Documents\\Advent of Code\\Day_08\\boot_code.txt", "r") as f:
    insts = f.read()
insts = insts.split("\n")
insts = [command.split(' ') for command in insts]
insts = [[command[0], int(command[1]), False] for command in insts]
#print(content)


def is_infinite_loop(content):
    try:
        i = 0
        accumulator = 0
        while i < len(content):
            if content[i][2] != True:
                if content[i][0] == "nop":
                    content[i][2] = True
                    i+=1
                elif content[i][0] == "acc":
                    accumulator += content[i][1]
                    content[i][2] = True
                    i+=1
                elif content[i][0] == "jmp":
                    content[i][2] = True
                    i += content[i][1]
                else:
                    print("Something bad happened - here's some info: #" + str(i))
                    print(content[i])
            else:
                return (True, i, content[i], accumulator)
        return (False, i, content[i], accumulator)
    except Exception:
        print("nope #" + str(i) + " " + str(accumulator))

j = 0

while j < len(insts):
    modded = copy.deepcopy(insts)
    #print(modded)
    #print(modded[j])
    if insts[j][0] == "jmp":
        modded[j][0] = "nop"
        #print(modded[j])
        try:
            print(is_infinite_loop(modded))
        except IndexError:
            print(insts[j])
            print(str(j))
    elif insts[j][0] == "nop":
        modded[j][0] = "jmp"
        #print(modded[j])
        try:
            print(is_infinite_loop(modded))
        except IndexError:
            print(insts[j])
            print(str(j))
    j += 1