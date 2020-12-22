with open("c:\\Users\\madri\\Documents\\Advent of Code\\Day_06\\responses.txt", "r") as f:
    content = f.read()
content = content.split("\n\n")
content = [x.strip().replace('\n',"") for x in content ]

def remove_dup_answers(responses):
    for i in range(0,len(responses)):
        responses[i] = "".join(set(responses[i]))

def sum_responses(responses):
    count = 0
    for response in responses:
        count += len(response)
    return count

remove_dup_answers(content)
print(sum_responses(content))