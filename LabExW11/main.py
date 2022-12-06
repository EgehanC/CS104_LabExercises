# Exercise 1
# Egehan Ceylan S034206
# CS104 Lab Exercises Week 11


def bin_search_names(name_list, name):
    low = 0
    high = len(name_list) - 1
    index = high - low // 2
    if len(name_list) < 1:
        return False
    elif name == name_list[index]:
        return True
    elif name > name_list[index]:
        return bin_search_names(name_list[index:high], name)
    elif name < name_list[index]:
        return bin_search_names(name_list[low:index], name)


def main1():
    print("----------------------------------")
    name = input("Name you want to find: ")
    ordered_name_list = ['ayla', 'ben', 'can', 'david', 'eliz', 'fatma', 'gene',
                         'huseyin', 'kemal', 'ken', 'liam', 'matt', 'zach']
    print(bin_search_names(ordered_name_list, name))
    print("----------------------------------")


main1()

# Exercise 2
count = 0


def hanoi(n, S, T, A):
    global count
    count += 1
    if n == 1:
        print('Move disk from', S, 'to', T)
        return
    hanoi(n - 1, S, A, T)  # move n-1 disks from S to A
    print('Move disk from', S, 'to', T)
    hanoi(n - 1, A, T, S)  # move n-1 disks from A to T


def main2():
    n = int(input("Number of discs: "))
    print("----------------MOVES---------------")
    hanoi(n, "S", "T", "A")
    print("------------------------------------")
    print(f'Moves required to complete: {count}')


main2()















