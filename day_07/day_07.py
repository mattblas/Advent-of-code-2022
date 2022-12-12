input = "test_input.txt"

def main():
    terminal_output = []
    with open(input, "r") as f:
        lines = f.readlines()
        for line in lines:
            terminal_output.append(line.replace("\n", "").replace("$ ", ""))

    dir_list = []
    dir_content = {}
    for output in terminal_output:
        # print(output)
        if "dir" in output or "/" in output:
           dir_list.append(output.replace("dir ", "").replace("cd ", ""))
    # print(dir_list)

    for directory in dir_list:
        for _ in range(len(terminal_output)):
            if terminal_output[_] == f"cd {directory}" and terminal_output[_+1] == "ls":
                temp_content = terminal_output[_+2].split(" ")
                i = 2
                temp = []
                try:
                    while ("cd") not in temp_content[0]: 
                        temp_content = terminal_output[_+i].split(" ")
                        if temp_content[0].isnumeric() or "dir" in temp_content[0]:
                            temp.append(temp_content)
                        i+=1
                except IndexError:
                    pass
                dir_content[directory] = temp

    for dir in dir_content:
        for _ in dir_content[dir]:
            for i in _:
                if "dir" in i:
                    print(f"{dir}: {_}")
        print("")
    
    # dir_sum = {}
    # small_dirs = []
    # for directory in dir_list:
    #     dir_sum[directory] = sum(dir_values[directory])
    #     if sum(dir_values[directory]) <= 100_000:
    #         small_dirs.append(sum(dir_values[directory]))

    # for dir in dir_values:
    #     print(f"{dir}: {dir_values[dir]}")


if __name__ == "__main__":
    main()