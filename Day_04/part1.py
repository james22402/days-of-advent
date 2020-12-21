with open("passports.txt", "r") as f:
    content = f.read()
content = content.split("\n\n")
content = [x.strip().replace('\n'," ") for x in content ]
#print(content)

fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]

def check_passport(passport):
    for field in fields:
        if passport.find(field) == -1:
            if field == "cid":
                continue
            else:
                return False
    return True

count = 0

for passport in content:
    if check_passport(passport):
        count+=1
print(count)