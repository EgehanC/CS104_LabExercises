### Egehan Ceylan     S034206
### CS 104 - Lab Exercise Week 12

# Exercise 1
import time


def squareRootExhaustive(x, e):
    start = time.time()
    guess = 1
    err = abs((guess ** 2) - x)
    while guess ** 2 < x:
        if err > e:
            guess += e ** 2

    print(f"Approximate: {guess}")
    end = time.time()
    print(f"Time: {end - start}")


# squareRootExhaustive(169, 0.001)


# Exercise 2

def squareRootBinary(x, e):
    start = time.time()
    low = 1
    high = x
    while high - low > e:
        mid = (high + low) / 2
        if mid ** 2 > x:
            high = mid
        else:
            low = mid
    end = time.time()
    print(f"Approximate: {mid}")
    print(f"Time: {end - start}")


# squareRootBinary(169, 0.001)

# Exercise 3
def no_punc_lower(s):
    for c in ".,:;\"\'!&`~@#$%&*_-+=|<>?^+-}{[]()\/":
        s = s.replace(c, "")
    return s.lower()


def turn_to_list(filename):
    word_list = []
    f = open(filename, "r")
    for line in f:
        line = no_punc_lower(line).split()
        for word in line:
            word_list.append(word)
    f.close()
    return word_list


def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


def search(word, list):
    high = len(list) - 1
    low = 0
    while high != low:
        mid = (high + low) // 2
        if list[mid] == word:
            return f"Word: {word}, İndex:  {mid}"
        else:
            if list[mid] < word:
                low = mid
            else:
                high = mid
    return None


def main():
    list = turn_to_list("Alice-in-Wonderland.txt")
    insertion_sort(list)
    word = input("What word would you like to search? (type 'exit' to stop searching)")
    while word != "exit":
        result = search(word, list)
        if result is None:
            print("Word could not be found")
        else:
            print(result)
        word = input("What word would you like to search? (type 'exit' to stop searching)")

    print("Exitted search")


# main()
