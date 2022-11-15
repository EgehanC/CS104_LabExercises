### Exercise 1


# finds divisors of n using quadrativ sieve
def divisor_gen(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            if i != n / i:
                divisors.insert(0, n / i)
    for div in divisors:
        yield div


def divisors(n):
    return [d for d in divisor_gen(n)]



# Categorizes the number given a number
def isPerfect(n):
    divs = divisors(n)
    # removing the last divisor (itself)
    divs.pop(-1)
    
    # Summing it's divisors
    sum_of_divs = 0
    for divisor in divs:
        sum_of_divs += divisor
    
    # Categorizing the number
    if sum_of_divs == n:
        perfect_list.append(n)
    elif sum_of_divs > n:
        abundant_list.append(n)
    else:
        deficient_list.append(n)


# İnitializing the lists
perfect_list = [] 
abundant_list = []
deficient_list = []


def main():
    n = int(input("I want to check numbers up to n, n = "))
    for n in range(2, n+1):
        isPerfect(n)
    print(f"\nPerfect numbers are {perfect_list} \n")
    print(f"Abundant nubmers are {abundant_list} \n")
    print(f"Deficient numbers are {deficient_list} \n")


main()

### Exercise 2

fib_nums = [0, 1]


def fibs(n):
    index = 0
    while len(fib_nums) < n:
        new_fib = fib_nums[index] + fib_nums[index + 1]
        fib_nums.append(new_fib)
        index += 1
    print(f"\nFibonacci sequence = {fib_nums}")
    print(f"Fib({n}) = {fib_nums[-1]}\n")


def main():
    n = int(input("\nCalculate n fibonacci numbers. \nn = "))
    fibs(n)


main()