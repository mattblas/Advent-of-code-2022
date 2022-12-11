input = "input.txt"


def main():
    empty_line = get_empty_line()
    index = get_index()
    crates = get_crates(index, empty_line)
    rearrange_crates(empty_line, crates)


def show_crates(crates):
    for crate in crates:
            print(f"{crate}: {crates[crate]}")


def rearrange_crates(empty_line, crates):
    instruction = get_instructions(empty_line)        
    for i in range(len(get_instructions(empty_line))):
        quantity =  int(instruction[i][0])
        _from =     int(instruction[i][1])
        _to =       int(instruction[i][2])
        temp = []
        for h in range(quantity):
            temp.append(crates[_from][-1])
            crates[_from].pop()
        crates[_to] = crates[_to]+ temp
    print(f"Answer to part one: ", end="")
    for crate in crates: 
        print(f"{crates[crate][-1]}", end="")
    print("")


def get_crates(index, empty_line):
    crates = {}
    with open(input, "r") as f:
        lines = f.readlines()        
        for i in range(len(index)):
            temp = []
            crate = index[i]
            for line in range(empty_line-1):
                if str(lines[line])[crate-1] != " ":
                    # print(str(lines[line])[crate-1])
                    temp.insert(0, str(lines[line])[crate-1])
            crates[i+1] = temp
    return crates


def get_instructions(empty_line):
    instructions = []
    with open(input, "r") as f:
        lines = f.readlines()
        for i in range(empty_line +1, len(lines)):
            instructions.append(lines[i].strip().replace("move", "").replace("from", "").replace("to", "").split())
    
    return(instructions)


def get_index():    
    index = []
    with open(input, "r") as f:
        lines = f.readlines()
        i = 0
        for char in str(lines[get_empty_line()-1]):
            i+=1
            if char.isnumeric():
                index.append(i)
    return(index)


def get_total_lines():
    with open(input, "r") as f:
        for count, line in enumerate(f):
            pass
    return(count + 1)


def get_empty_line():
    with open(input, "r") as f:
        lines = f.readlines()
        empty_line = 0
        for line in lines:
            if len(line.strip()) == 0:
                break
            empty_line+=1
        return(empty_line)
    

if __name__ == "__main__":
    main()
