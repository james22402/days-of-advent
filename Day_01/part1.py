with open("numbers.txt", "r") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [int(x) for x in content]

i = 0
j = 0
while i < len(content):
    try:
        while j < len(content):
            try:
                if content[i] + content[j] == 2020:
                    print(str(content[i]) + " " + str(content[j]))
                    print(content[i]*content[j])
                elif content[i] + content[j] != 2020:
                    continue
            finally:
                j += 1
    finally:
        i += 1
        j = 0
