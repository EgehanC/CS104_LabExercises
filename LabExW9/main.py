def collapse(nl):
    collapsed_list = []
    if len(nl) % 2 == 0:
        for i in range(0, len(nl), 2):
            collapsed_list.append(nl[i] + nl[i + 1])
    else:
        for i in range(0, len(num_list) - 1, 2):
            collapsed_list.append(num_list[i] + num_list[i + 1])
        collapsed_list.append(num_list[-1])
    print(collapsed_list)


num_list = [7, 2, 8, 9, 4, 13, 7, 1, 9, 10]

# collapse(num_list)


# Exercise 2
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v",
            "w", "x", "y", "z"]
letter_counts = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
}


def count_letters(s):
    for i in s:
        for j in alphabet:
            if i == j:
                letter_counts[j] += 1


def fancy_output():
    included_letters = {}
    for i in letter_counts:
        if letter_counts[i] != 0:
            included_letters[i] = letter_counts[i]
    print("| letter 	| frequency 	|")
    print("|--------	|-----------	|")
    for j in included_letters:
        print(f"|    {j}    	|    {included_letters[j]}       	|")


# sentence = input("Enter your sentence here >>> ").lower().replace(" ", "")
# count_letters(sentence)
# fancy_output()


# Exercise 3
from random import randint

simulated_counts = {
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0
}
expected_percents = {
    2: round((1 / 36) * 100, 2),
    3: round((2 / 36) * 100, 2),
    4: round((3 / 36) * 100, 2),
    5: round((4 / 36) * 100, 2),
    6: round((5 / 36) * 100, 2),
    7: round((6 / 36) * 100, 2),
    8: round((5 / 36) * 100, 2),
    9: round((4 / 36) * 100, 2),
    10: round((3 / 36) * 100, 2),
    11: round((2 / 36) * 100, 2),
    12: round((1 / 36) * 100, 2)
}


def roll_dice():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    total = dice1 + dice2
    return total


def main():
    for i in range(0, 1000):
        total = roll_dice()
        simulated_counts[total] += 1

    # output
    print("|  Total	|Simulated Percent  	|  Expected Percent	|")
    print("|---	|---	|---	|")
    for i in simulated_counts:
        print(f"| {i} 	| {simulated_counts[i] / 10} 	| {expected_percents[i]}  |")

# main()
