
def main():
    get_input()
    with open("Calories.txt", "r") as f:
        Calories = list(f)[0]
        elves_split = Calories.split("/n/n")
        _ = 1
        dict = {}
        for elv in elves_split:
            item_split = elv.split("/n")
            int_item_split = list(map(int, item_split))
            items_sum = sum(int_item_split)
            dict[_] = items_sum
            _+=1
        Elf_with_max_cal = max(dict, key=dict.get)
        max_cal = dict[Elf_with_max_cal]
        print(f"Elf number {Elf_with_max_cal} is carrying the most Calories, and it's {max_cal} Calories.")


def get_input():
    with open("Calories.txt", "w") as f:
        add_new_item = True
        while add_new_item == True:
            f.write(input("What's the number of calories of the item? "))
            answer = input("(a)dd another item, (n)ext Elf or (e)xit? ").strip().lower()
            while answer not in ("a", "n", "e"):
                answer = input("(a)dd another item, (n)ext Elf or (e)xit?").strip().lower()
            else:
                if answer == "a":
                    f.write("/n")
                    add_new_item = True
                elif answer == "n":
                    f.write("/n/n")
                elif answer == "e":
                    add_new_item = False


if __name__ == "__main__":
    main()
