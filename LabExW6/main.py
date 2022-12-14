# Exercise 1

def ask_number():
    number = 0
    sum = 0
    while number >= 0:
        sum += number
        number = float(input("Give me a number: "))
    print(sum)


ask_number()


# Exercise 2

def isPrimeNumber(n):
    dividers_of_x = [1, n]
    if n % 2 == 0:
        while n % 2 == 0:
            n /= 2
        dividers_of_x.append(2)
    for i in range(3, round(n ** 1 / 2)):
        if n % i == 0:
            dividers_of_x.append(i)

    if len(dividers_of_x) > 2:
        return False
    elif len(dividers_of_x) <= 2:
        return True


prime_list = []


def prime():
    n = 2
    while len(prime_list) < 20:
        if isPrimeNumber(n):
            prime_list.append(n)
        n += 1
    print(f"The first 20 prime numbers are {prime_list}")


prime()

# Exercise 3

from random import randint


def guess_game():
    num = randint(1, 101)
    guess = 0
    while guess != num:
        guess = int(input("Guess: "))
        if guess == num:
            print("Congrats! You found it.")
        elif guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")


guess_game()


# Exercise 4

def isPalindrome():
    word = str(input("Which word would you like to check? "))
    lc_word = word.lower()

    first_index = 0
    last_index = len(lc_word) - 1

    r = False
    while last_index >= len(lc_word) / 2:
        if lc_word[first_index] == lc_word[last_index]:
            r = True
        else:
            r = False
        first_index += 1
        last_index -= 1

    if r:
        print(f"{word} is a Palindrome!")
    else:
        print(f"{word} is not a Palindrome.")


isPalindrome()
