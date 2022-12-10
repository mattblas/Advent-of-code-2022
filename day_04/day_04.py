def main():
        print(f"Part one. In {fully_contains()} assignment pairs one range fully contain the other.")
        print(f"Part two. In {ranges_overlap()} assignment pairs one range overlap the other.")


def fully_contains():
    fully_contains = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            section = line.strip().split(",")
            a = int(section[0].split("-")[0]) 
            b = int(section[0].split("-")[1])
            c = int(section[1].split("-")[0])
            d = int(section[1].split("-")[1])
            if a in range(c, (d+1)) and b in range(c, (d+1)):
                fully_contains.append(1)
            elif c in range(a, (b+1)) and d in range(a, (b+1)):
                fully_contains.append(1)
    return sum(fully_contains)


def ranges_overlap():
    ranges_overlap = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            section = line.strip().split(",")
            a = int(section[0].split("-")[0]) 
            b = int(section[0].split("-")[1])
            c = int(section[1].split("-")[0])
            d = int(section[1].split("-")[1])
            if a in range(c, (d+1)) or b in range(c, (d+1)):
                ranges_overlap.append(1)
            elif c in range(a, (b+1)) or d in range(a, (b+1)):
                ranges_overlap.append(1)
    return sum(ranges_overlap)


if __name__ == "__main__":
    main()
