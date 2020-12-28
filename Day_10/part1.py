with open("c:\\Users\\madri\\Documents\\Advent of Code\\Day_10\\adapters.txt", "r") as f:
    adapters = f.read()
adapters = adapters.split("\n")
adapters = [int(n) for n in adapters]
laptop_adapter = max(adapters) + 3
#print(laptop_adapter)
adapters.append(0) #Append 0 and laptop adapter because they are start and finish
adapters.append(laptop_adapter)
adapters.sort()
#print(adapters)
i = 0
count_one = 0
count_three = 0
for i in range(0,len(adapters)-1):
    if adapters[i]+3 < adapters[i+1]:
        print("Problem! " + str(adapters[i]) + " " + str(adapters[i+1]))
    elif adapters[i]+1 == adapters[i+1]:
        count_one += 1
    elif adapters[i]+3 == adapters[i+1]:
        count_three += 1
    else:
        print("Problem! " + str(adapters[i]) + " " + str(adapters[i+1]))

print(count_one)
print(count_three)
print(count_one * count_three)