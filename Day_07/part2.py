import re
with open("c:\\Users\\madri\\Documents\\Advent of Code\\Day_07\\rules.txt", "r") as f:
    content = f.read()
content = content.split("\n")
bag_pattern = r"([0-9]*?) (.*) bag.*$"
bag_rules = {}

def create_rules_map(rules):
    for rule in rules:
        rule = rule.split(' bags contain ')
        hashValue = rule[1].split(',')
        for i in range(0,len(hashValue)):
            hashValue[i] = hashValue[i].strip()
            bag_color = re.search(bag_pattern,hashValue[i])
            if bag_color == None:
                hashValue[i] = None
            else:
                hashValue[i] = {bag_color.group(2): bag_color.group(1)}
        bag_rules[rule[0]] = hashValue

bag_list = ["shiny gold"]

create_rules_map(content)
#print(bag_rules)
bag_count = 0
for bag in bag_list:
    for rule in bag_rules:
        for bag_amounts in bag_rules[rule]:
            if bag in bag_amounts.keys():
                if rule not in bag_list:
                    bag_list.append(rule)
print(len(bag_list)-1)
#print(bag_list)


print(count_bags(bag_list,0,len(bag_list)-1))
print(bag_rules)
print(bag_count)