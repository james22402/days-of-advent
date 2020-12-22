with open("c:\\Users\\madri\\Documents\\Advent of Code\\Day_05\\boarding_passes.txt", "r") as f:
    content = f.read()
content = content.split("\n")
#print(content)

def get_row_num(boarding_pass,i,min,max):
    if i == 7:
        return min
    elif boarding_pass[0] == 'F':
        return get_row_num(boarding_pass=boarding_pass[1:], i=i+1, min=min, max=max-(max-min)/2)
    elif boarding_pass[0] == 'B':
        return get_row_num(boarding_pass=boarding_pass[1:], i=i+1, min=min+(max-min)/2, max=max)
    else:
        return "problem " + boarding_pass[0] + " " + str(i) + " " + str(min) + " " + str(max)

def get_col_num(boarding_pass,i,min,max):
    if i == 3:
        return min
    elif boarding_pass[0] == 'L':
        return get_col_num(boarding_pass=boarding_pass[1:], i=i+1, min=min, max=max-(max-min)/2)
    elif boarding_pass[0] == 'R':
        return get_col_num(boarding_pass=boarding_pass[1:], i=i+1, min=min+(max-min)/2, max=max)
    else:
        return "problem " + boarding_pass[0] + " " + str(i) + " " + str(min) + " " + str(max)

ID_List = []

for boarding_pass in content:
    ID_List.append(int(get_row_num(boarding_pass,0,0,128))*8+int(get_col_num(boarding_pass[7:],0,0,8)))

print(max(ID_List))
