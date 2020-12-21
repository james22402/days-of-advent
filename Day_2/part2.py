# Part Two

with open("passwords.txt", "r") as f:
    content = f.readlines()
content = [x.strip() for x in content]
valid = 0
for item in content:
    colonIndex = item.index(':')
    passRange = item[0: colonIndex-2:]
    spotOne = int(passRange[0: passRange.index('-'):])
    spotTwo = int(passRange[passRange.index('-')+1: len(passRange):])
    letter = item[colonIndex-1: colonIndex:]
    password = item[colonIndex+2: len(item):]
    print(item)
    doneA = False
    doneB = False
    if spotOne-1 < len(password):
        if password[spotOne-1] == letter:
            print("true")
            doneA = True
    if spotTwo-1 < len(password):
        if password[spotTwo-1] == letter:
            print("true")
            doneB = True
    if doneA and not doneB or doneB and not doneA:
        valid += 1
print(valid)