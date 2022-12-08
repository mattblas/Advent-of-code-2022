def main():
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. 
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # A for Rock, B for Paper, and C for Scissors
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

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
        #Paper
        "BX": 0,
        "BY": 3,
        "BZ": 6,
        #Sci
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

    print(f"total score: {sum(score)}")            


if __name__ == "__main__":
    main()
