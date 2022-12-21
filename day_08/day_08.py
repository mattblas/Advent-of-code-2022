input = "input.txt"

def main():

    with open(input) as f:
        for row, line in enumerate(f):
            if row not in (0,98):                           #lose top and bottom row
                for column in range(len(line.strip())):
                    if column not in (0, 98):               #lose left and right column
                        #TODO
                        # check left, right, up, down
                        ...

def check_left():
    ...


def check_right():
    ...


def check_up():
    ...


def check_down():
    ...

#tree position == row, column
# rows ---> 0-98
# columns ---> 0-98








if __name__ == "__main__":
    main()