# Özyeğin University
# CS 104, Week-7 Lab exercises

# Egehan Ceylan
# S034206

# ### Exercise 1


def fibs():
    fib_nums = [1, 2]
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

def findLCM(n1, n2):
    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)

    def lcm(a, b):
        return (a / gcd(a, b)) * b

    print(lcm(n1, n2))


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
