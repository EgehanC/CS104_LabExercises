# Özyeğin University
# CS 104, Week-7 Lab exercises

# Egehan Ceylan
# S034206

# ### Exercise 1
fib_nums = [1, 2]


def fibs():
    n = int(input("Calculate n fibonacci numbers. \nn = "))
    index = 0
    while len(fib_nums) < n:
        new_fib = fib_nums[index] + fib_nums[index + 1]
        fib_nums.append(new_fib)
        index += 1
    print(fib_nums)


fibs()

# ### Exercise 2

from random import randint
def dice_sum():
    desired_sum = int(input("What is the desired sum? "))
    while not desired_sum in range(2, 13):
        desired_sum = int(input("Your sum is not possible, please enter a valid sum: "))
    sum = 0
    while sum != desired_sum:
        dice1 = randint(1, 7)
        dice2 = randint(1, 7)
        sum = dice1 + dice2
        print(f"{dice1} + {dice2} = {sum}")
    print("Got it!")

dice_sum()

# ### Exercise 3

prime_factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def findLCM(n1, n2):
    n1_org = n1
    n2_org = n2
    # Calculating prime factor format of the two number
    n1_prime_factors = []
    n2_prime_factors = []
    for i in prime_factors:
        if i < n1_org*n2_org+1:
            if n1 % i == 0:
                while n1 % i == 0:
                    n1_prime_factors.append(i)
                    n1 /= i
            if n2 % i == 0:
                while n2 % i == 0:
                    n2_prime_factors.append(i)
                    n2 /= i
    # Iterating over 2 prime factors
    lcm = 1
    index = 0
    while index < len(n1_prime_factors) and index < len(n2_prime_factors):
        if n1_prime_factors[index] == n2_prime_factors[index]:
            lcm *= n1_prime_factors[index]
        else:
            lcm *= n1_prime_factors[index]
            lcm *= n2_prime_factors[index]
        index += 1
    if index > len(n1_prime_factors):
        while index > len(n1_prime_factors):
            lcm *= n1_prime_factors[index]
            index += 1
    elif index > len(n2_prime_factors):
        while index > len(n2_prime_factors):
            lcm *= n2_prime_factors[index]
            index += 1
    print(f"LCM({n1_org}, {n2_org}) = {lcm}")


n1 = int(input("First Number? "))
n2 = int(input("Second Number? "))
findLCM(n1, n2)

### Exercise 4
def get_row(r):
    for i in range(1, r):
        print(i, end="")
    for j in range(r, 0, -1):
        print(j, end="")


def print_triangle(height):
    space = height - 1
    row = 1
    for r in range(row, height + 1):
        print(space * " ", end="")
        get_row(r)
        print()
        space -= 1

height = int(input("Height = "))
print_triangle(height)
