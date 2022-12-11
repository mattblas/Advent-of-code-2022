input = "test_input.txt"


def main():
    total_lines = get_total_lines()
    empty_line = get_empty_line()
    index = get_index()
    get_instructions(empty_line)
    crates = get_crates(index, empty_line)
    print(crates)


def get_crates(index, empty_line):
    crates = {}
    with open(input, "r") as f:
        lines = f.readlines()
        for i in range(len(index)):
            temp = []
            crate = index[i]
            for line in range(empty_line-1):
                if str(lines[line])[crate-1] != " ":
                    temp.insert(0, str(lines[line])[crate-1])
            crates[i+1] = temp
    return crates


def get_instructions(empty_line):
    instructions = []
    with open(input, "r") as f:
        lines = f.readlines()
        for i in range(empty_line +1, len(lines)):
            instructions.append(lines[i].strip().replace(" ", "").replace("move", "").replace("from", "").replace("to", ""))
    return(instructions)


def get_index():    
    index = []
    with open(input, "r") as f:
        lines = f.readlines()
        i = 0
        for char in lines[3].replace("\n", ""):
            i+=1
            if char != " ":
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
