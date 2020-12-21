# Part One

with open("passwords.txt", "r") as f:
    content = f.readlines()
content = [x.strip() for x in content]
valid = 0
for item in content:
    colonIndex = item.index(':')
    passRange = item[0: colonIndex-2:]
    lowEnd = int(passRange[0: passRange.index('-'):])
    highEnd = int(passRange[passRange.index('-')+1: len(passRange):])
    letter = item[colonIndex-1: colonIndex:]
    password = item[colonIndex+2: len(item):]
    charCount = password.count(letter)
    print(item)
    print(charCount)
    if charCount >= lowEnd and charCount <= highEnd:
        print("true")
        valid+=1
print(valid)