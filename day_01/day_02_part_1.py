# X for Rock, Y for Paper, and Z for Scissors
# A for Rock, B for Paper, and C for Scissors
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

def main():
    score = []
    with open("Strategy_guide.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            round_score = outcome[line.replace(" ", "").strip()]
            choice_score = choice_points[line.replace(" ", "").strip()[1]]
            score.append(round_score)
            score.append(choice_score)
    print(f"total score: {sum(score)}")

if __name__ == "__main__":
    main()
