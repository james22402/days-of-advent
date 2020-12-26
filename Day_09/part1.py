import copy
with open("c:\\Users\\madri\\Documents\\Advent of Code\\Day_09\\xmas.txt", "r") as f:
    codes = f.read()
codes = codes.split("\n")
codes = [int(c) for c in codes]

header = codes[0: 25:]
codes = codes[25:]

def is_divisible(code, preamble):
    i = 0
    while i < len(preamble):
        j = 0
        while j < len(preamble):
            num = preamble[i]+preamble[j]
            if num == code:
                return True
            j += 1
        i += 1
    return False

def find_bad_number(preamble, code_list):
    if not is_divisible(code_list[0], preamble=preamble):
        return code_list[0]
    else:
        new_preamble = preamble[1:]
        new_preamble.append(code_list[0])
        return find_bad_number(preamble=new_preamble, code_list=code_list[1:])

print(find_bad_number(preamble=header,code_list=codes))