input = "input.txt"

def main():
    paths = []
    path = []
    for i in clean_terminal_output():
        if "cd " in i:
            if "cd .." not in i:
                path.append(i)
            elif "cd .." in i:
                paths.append(path)
                print(paths)
                path.pop()


def clean_terminal_output():
    terminal_output = []
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            terminal_output.append(line.strip().replace("$ ", ""))
    return terminal_output
    

if __name__ == "__main__":
    main()
