input = "input.txt"


def main():
    columns = get_columns()
    print(part_one(columns))
    print(part_two(columns))


def part_one(columns):
    i = 0
    with open(input, "r") as f:
        for row, line in enumerate(f):
            if row not in (0, lenght_of_row()-1):
                for column in range(len(line.strip())):
                    if column not in (0, len(line.strip())-1):
                        if check_row(line, column) == False or check_column(line, column, row, columns) == False:
                            i+=1
    answer_part1 = i + (lenght_of_row()*2) + ((len(get_columns())*2)-4)
    return(f"answer --- part one: {answer_part1}")


def part_two(columns):
    all_trees_scores = []
    with open(input, "r") as f:
        for row, line in enumerate(f):   
            for column in range(len(line.strip())):
                x = check(row, column, line, columns)
                all_trees_scores.append(x)
    answer_part2 = max(all_trees_scores)
    return(f"answer --- part two: {answer_part2}")      


def check(row, column, line, columns):
    list_right = list(line[column+1:len(line.strip())])
    list_left = list(line[0:column])
    list_left.reverse()
    list_up = list(columns[column][0:row])
    list_up.reverse()
    list_down = columns[column][row+1:len(columns[column])]
    x = how_many_visable(list_right, line[column])
    y = how_many_visable(list_left, line[column])
    z = how_many_visable(list_up, line[column])
    v = how_many_visable(list_down, line[column])
    try:
        score = x*y*z*v
    except TypeError:
        score = 0
    return score


def how_many_visable(list, tree):
    i = 0
    for _ in range(len(list)):
        if tree <= list[_]:
            i+=1
            break
        elif tree > list[_]:
            i+=1
    return i


def get_columns():
    columns = {}
    for column in range(lenght_of_row()):
        columns[column] = []
    with open(input, "r") as f:
        for row, line in enumerate(f):
            for column in range(len(line.strip())):
                x = columns[column]
                x.append(line[column])
                columns[column] = x
    return columns


def lenght_of_row():
    with open(input, "r") as f:
        line = f.readline().strip()
        return len(line)


def check_row(line, column):
    max_left = max(int(x) for x in line[0: column])
    max_right = max(int(x) for x in line[column+1: len(line.strip())])
    if int(line[column]) <= max_left and int(line[column]) <= max_right:
        return True
    else:
        return False


def check_column(line, column, row, columns):
    max_up = max(int(x) for x in columns[column][0: row])
    max_down = max(int(x) for x in columns[column][row+1: len(columns[column])])
    if int(line[column]) <= max_up and int(line[column]) <= max_down:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
