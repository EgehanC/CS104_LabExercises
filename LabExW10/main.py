data = {}
with open("students.dat") as f:
    f.seek(107)
    for line in f:
        line = line.split()
        for item in line:
            number = int(line[0])
            data[number] = {}
            data[number]["name"] = line[1]
            data[number]["surname"] = line[2]
            data[number]["birth place"] = line[3]
            data[number]["department"] = line[4]
            data[number]["gpa"] = line[5]


def print_name(id):
    if id in data:
        print(data[id]["name"])
    else:
        print("ID do not exist")


def print_surname(id):
    if id in data:
        print(data[id]["surname"])
    else:
        print("ID do not exist")


def print_birth_place(id):
    if id in data:
        print(data[id]["birth place"])
    else:
        print("ID do not exist")


def print_department(id):
    if id in data:
        print(data[id]["department"])
    else:
        print("ID do not exist")


def print_gpa(id):
    if id in data:
        print(data[id]["gpa"])
    else:
        print("ID do not exist")


# print_name(81709043)
# print_surname(81709043)
# print_birth_place(81709043)
# print_department(81709043)
# print_gpa(81709043)


EtoF = {'bread': 'pain', 'wine': 'vin', 'with': 'avec', 'i': 'Je', 'eat': 'mange',
        'drink': 'bois', 'John': 'Jean',
        'friends': 'amis', 'and': 'et', 'of': 'du', 'red': 'rouge'}
FtoE = {'pain': 'bread', 'vin': 'wine', 'avec': 'with', 'Je': 'i',
        'mange': 'eat', 'bois': 'drink', 'Jean': 'John',
        'amis': 'friends', 'et': 'and', 'du': 'of', 'rouge': 'red'}


def translate(sentence, action):
    s = sentence.lower().split()
    translated_words = ""
    for word in s:
        if action == "eng":
            if word in FtoE:
                translated_words += FtoE[word] + " "
            else:
                return "Translation not possible"
        elif action == "fren":
            if word in EtoF:
                translated_words += EtoF[word] + " "
            else:
                return "Translation not possible"
        else:
            return "Please enter a correct language to translate"

    print(translated_words)


# sentence = input("Write your sentence: \n")
# action = input("Which language are you translating to? eng/fren \n")
# translate(sentence, action)


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z"]


def writeNLetters(n):
    f = open("words.txt", "w")
    remainder = len(alphabet) % n
    index = 0
    for i in range((len(alphabet) - remainder) // n):
        for j in range(n):
            f.write(alphabet[index])
            index += 1
        f.write("\n")
    f.close()

# writeNLetters(3)
