def main():
# Part one
    print(f"Part one: ", end="")
    items = []
    rucksacks = separate_compartments()    
    for rucksack in rucksacks:
        items.append(chech_for_item(rucksack))
    print(f"Sum of the priorities is: {count_priority_sum(items)}")
# Part two
    print(f"Part two: ", end="")
    groups = separete_groups()
    items= get_common_item(groups)
    print(f"Sum of the priorities is: {count_priority_sum(items)}")


def separate_compartments():
    rucksacks = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            first_compartment = []
            second_compartment = []
            line_len = len(line.strip())
            for i in range(int((line_len)/2)):
                first_compartment.append(line[i])
                i += 1
            for i in range(int((line_len)/2), line_len):
                second_compartment.append(line[i])
                i += 1
            rucksacks.append([first_compartment, second_compartment])
    return rucksacks


def chech_for_item(rucksack):
    item = []
    for i in range(len(rucksack[0])):
        if rucksack[0][i] not in rucksack[1]: 
            i+=1
        elif rucksack[0][i] in rucksack[1]:
            item.append(rucksack[0][i])
            return(item)
    

def count_priority_sum(items):
    value_list = []
    for item in items:
        ascii = ord(item[0])
        if ascii in range(97, 123): #Lower
            value = int(ascii) - 96
        elif ascii in range(65, 91): #Upper
            value = int(ascii) - 38
        value_list.append(value)
    return sum(value_list)


def separete_groups():
    groups = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
        group = []
        for line in lines:
            group.append(line.strip())
            if len(group) == 3:
                groups.append(group)
                group = []
    return groups


def get_common_item(groups):
    items_temp = []
    items = []
    for group in groups:
        item = set()
        for char in group[0]:
            if char in group[1] and char in group[2]:
                item.add(char)
        items_temp.append(item)
    for item in items_temp:
        for i in item:
            items.append(i)
    return items


if __name__ == "__main__":
    main()
