# X for Rock, Y for Paper, and Z for Scissors
# A for Rock, B for Paper, and C for Scissors


def main():
    print(f"Total score (part one): {part_one()}")
    print(f"Total score (part two): {part_two()}")


def part_one():
    choice_points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    outcome = {
        "AX": 3,
        "AY": 6,
        "AZ": 0,
        "BX": 0,
        "BY": 3,
        "BZ": 6,
        "CX": 6,
        "CY": 0,
        "CZ": 3,
    }   

    score = []
    with open("Strategy_guide.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            round_score = outcome[line.replace(" ", "").strip()]
            choice_score = choice_points[line.replace(" ", "").strip()[1]]
            score.append(round_score)
            score.append(choice_score)
    return sum(score)


def part_two():
    choice = {
        #Rock
        "AX": 3, #Sci lose
        "AY": 1, #Rock draw
        "AZ": 2, #Paper win
        #Paper
        "BX": 1, #Rock lose
        "BY": 2, #Paper draw
        "BZ": 3, #Sci win
        #Sci
        "CX": 2, #Paper lose
        "CY": 3, #Sci draw
        "CZ": 1, #Rock win
    }

    outcome = {
        #Rock
        "AX": 0, 
        "AY": 3,
        "AZ": 6,
        "BX": 0,
        "BY": 3,
        "BZ": 6,
        "CX": 0,
        "CY": 3,
        "CZ": 6,
    }

    score = []
    with open("Strategy_guide.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            round_result = outcome[line.strip().replace(" ", "")] 
            choice_results = choice[line.strip().replace(" ", "")]
            score.append(round_result)
            score.append(choice_results)
    return sum(score)         


if __name__ == "__main__":
    main()
