# # Egehan Ceylan - CS104 - Lab5 exercises

# ### Exercise 1:

# Inceasing amount of stars
def up():
    counter1 = 1
    counter2 = 4
    for _ in range(0, 5):
        print(" "*counter2+"*"*counter1)
        counter1 += 2
        counter2 -= 1

# Reducing amount of stars
def down():
    counter1 = 9
    counter2 = 0
    for _ in range(0, 5):
        print(" "*counter2+"*"*counter1)
        counter1 -= 2
        counter2 += 1

# Calling the functions
up()
down()


# ### Exercise 2

def sym_num_pat():
    counter = 5
    for i in range(counter, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(j-1, 0, -1):
            print(j, end=" ")
        print()

sym_num_pat()


# ### Exercise 3

def factorial(n):
    result = 1
    for _ in range(0, n):
        result *= n
        n -= 1
    print(result)

n = int(input("Number: "))
factorial(n)


# ### Exercise 4

def isPrimeNumber(n):
    dividers_of_x = [1, n]
    if n % 2 == 0:
        while n % 2 == 0:
            n /= 2
        dividers_of_x.append(2)
    for i in range(3, round(n**1/2)):
        if n % i == 0:
            dividers_of_x.append(i)

    if len(dividers_of_x) > 2:
        print(f"{n} is not a prime number.")
    elif len(dividers_of_x) <= 2:
        print(f"{n} is a prime number!")

n = int(input("What number would you like to check? "))
isPrimeNumber(n)




