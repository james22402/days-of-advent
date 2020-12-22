import re
with open("c:\\Users\\madri\\Documents\\Advent of Code\\Day_04\\passports.txt", "r") as f:
    content = f.read()
content = content.split("\n\n")
content = [x.strip().replace('\n'," ") for x in content ]
#print(content)

fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]

def data_check_valid_passport(passport):
    hair_color_regex = re.compile(r"^\#[0-9a-f]{6}$")
    pid_regex = re.compile(r"^[0-9]{9}$")
    passportElements = passport.split(' ')
    passportDict = {key:value for (key, value) in [element.split(':') for element in passportElements]}
    #Checks
    if len(passportDict['byr']) != 4 or int(passportDict['byr']) < 1920 or int(passportDict['byr']) > 2002:
        return False
    if len(passportDict['iyr']) != 4 or int(passportDict['iyr']) < 2010 or int(passportDict['iyr']) > 2020:
        return False
    if len(passportDict['eyr']) != 4 or int(passportDict['eyr']) < 2020 or int(passportDict['eyr']) > 2030:
        return False
    if passportDict['hgt'].find('cm') != -1:
        height = int(passportDict['hgt'].replace('cm',''))
        if height < 150 or height > 193:
            return False
    elif passportDict['hgt'].find('in') != -1:
        height = int(passportDict['hgt'].replace('in',''))
        if height < 59 or height > 76:
            return False
    else:
        return False
    if not hair_color_regex.match(passportDict['hcl']):
        return False
    if passportDict['ecl'] != "amb" and passportDict['ecl'] != "blu" and passportDict['ecl'] != "brn" and passportDict['ecl'] != "gry" and passportDict['ecl'] != "grn" and passportDict['ecl'] != "hzl" and passportDict['ecl'] != "oth":
        return False
    if not pid_regex.match(passportDict['pid']):
        return False
    return True

def check_passport(passport):
    for field in fields:
        if passport.find(field) == -1:
            if field == "cid":
                continue
            else:
                return False
    return data_check_valid_passport(passport)

count = 0

for passport in content:
    if check_passport(passport):
        count+=1
print(count)