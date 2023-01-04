input = "input.txt"

class motion:
    def __init__(self, axel, value):
        self.axel = axel
        self.value = value


    def get_value(self):
        return self.value


    def get_axel(self):
        if self.axel == "R" or self.axel == "L":
            self.axel = "0"
        elif self.axel == "U" or self.axel =="D":
            self.axel = "1"
        else:
            raise ValueError("wrong input / axel(name)")
        return self.axel


    def get_vector(self):
        if self.axel == "R" or self.axel == "U":
            self.axel = "+"
        elif self.axel == "L" or self.axel =="D":
            self.axel = "-"
        else:
            raise ValueError("wrong input / axel(name)")
        return self.axel


def main():
    h_position = [0, 0]
    t_position = [0, 0]
    h_visited = []
    h_visited.append(list(h_position))
    t_visited = []
    t_visited.append(list(t_position))
      
    with open(input, "r") as f:
        lines = f.readlines()
        for line in lines:
            i = 0
# get H motion (axel, vector and value)
            axel = int(motion((line.strip().split()[0]), (line.strip().split()[1])).get_axel())
            vector = motion((line.strip().split()[0]), (line.strip().split()[1])).get_vector()
            value = int(motion((line.strip().split()[0]), (line.strip().split()[1])).get_value())
            
# while i != value of H
#       move H by 1 position, and update visited positions
            while i != value:
                x = h_position[axel]
                if vector == "+":
                    x = x + 1
                elif vector == "-":
                    x = x - 1
                h_position[axel]=x
                i+=1
                h_visited.append(list(h_position))

#       get T position
#       chech if T is further than 1 position from H
#       if FALSE -> PASS
#       else -> move T to last H position -> add new T position to T_visited
                if t_position[0] == h_position[0]+2 or t_position[0] == h_position[0]-2:
                    t_position = h_visited[-2]
                    if not h_visited[-2] in t_visited:
                        t_visited.append(h_visited[-2])
                if t_position[1] == h_position[1]+2 or t_position[1] == h_position[1]-2:
                    t_position = h_visited[-2]
                    if not h_visited[-2] in t_visited:
                        t_visited.append(h_visited[-2])
 
    print(len(t_visited))
if __name__ == "__main__":
    main()

    



# i = 0
# T_visited = set
# get H motion (axel, vector and value)
# while i != value of H
#       move H 1 position
#--------------------------------------------------------------------------------
#       get T position
#       chech if T is further than 1 position from H
#       if FALSE -> PASS
#       else -> move T to last H position -> add new T position to T_visited 
#       i+=1

""" 
R 4     H(0,0) -> (0,4), T(0,0) -> (0,3)
U 4     H(0,4) -> (4,4), T(0,0) -> (0,3)
L 3
D 1
R 4
D 1
L 5
R 2


"""