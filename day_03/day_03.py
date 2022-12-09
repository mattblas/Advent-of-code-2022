def main():
    items = []
    rucksacks = separate_compartments()    
    for rucksack in rucksacks:
        items.append(chech_for_item(rucksack))
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
        # print(f"{item}, ({value})")
    return sum(value_list)

if __name__ == "__main__":
    main()