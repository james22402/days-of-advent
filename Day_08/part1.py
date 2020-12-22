with open("c:\\Users\\madri\\Documents\\Advent of Code\\Day_08\\boot_code.txt", "r") as f:
    content = f.read()
content = content.split("\n")
content = [command.split(' ') for command in content]
content = [[command[0], int(command[1]), False] for command in content]
#print(content)

accumulator = 0
i=0
while i < len(content):
    val = content[i]
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
        print(accumulator)
        break