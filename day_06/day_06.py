input = "input.txt"


def main():

    part_one()
    part_two()


def part_two():
    with open(input, "r") as f:
        line = f.readline()
        for i in range(len(line)):
            temp = set()
            for _ in range(14):
                temp.add(line[i+_]) 
            if len(temp) == 14:
                print(f"Answer to part two: {i+14}")
                break


def part_one():
    with open(input, "r") as f:
        line = f.readline()
        for i in range(len(line)):
            temp = set()
            for _ in range(4):
                temp.add(line[i+_]) 
            if len(temp) == 4:
                print(f"Answer to part two: {i+4}")
                break


if __name__ == "__main__":
    main()
    