import math


# This function calculates the area of a sphere
def sphere_area(r):
    a = 4 * math.pi * r ** 2
    print(a)


# This function calculates the volume of a sphere
def sphere_volume(r):
    v = 4 / 3 * math.pi * r ** 3
    print(v)


# testing code
sphere_area(2.5)
sphere_volume(2.5)


# This function prints n'th number in a number sequence
def sequence(n):
    y = 2 * n / 3 ** (n - 1)
    print(y)


# testing code for 5, 8 and 11
for _ in range(5, 14, 3):
    sequence(_)


district_rents_and_contributions = {
    'tasdelen': {'rent': 2600, 'contribution': 10},
    'cekmekoy': {'rent': 3000, 'contribution': 10},
    'uskudar': {'rent': 3600, 'contribution': 10},
    'kadikoy': {'rent': 4000, 'contribution': 10},
    'atasehir': {'rent': 5000, 'contribution': 20},
    'beykoz': {'rent': 4500, 'contribution': 15}
}


# This function calculates rents with contribution and prints the amount each person should pay
def calc_rents_with_cont():
    district_rents_with_aidat = {}
    for district in district_rents_and_contributions:
        rent = district_rents_and_contributions[district]['rent']
        rent += rent * district_rents_and_contributions[district]['contribution'] / 100
        district_rents_with_aidat[district] = rent

    # printing results
    for district in district_rents_with_aidat:
        each_person = district_rents_with_aidat[district] / 3
        print(f"{district}: {each_person}")


# calling the function
calc_rents_with_cont()

grades = {
    'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
    'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D': 1.0, 'F': 0
}
term_results = {
    'ali': {
        'cs101': {'grade': "A", "credit": 5},
        'eng101': {'grade': "B", "credit": 4},
        'mat103': {'grade': "C-", "credit": 6},
        'phys101': {'grade': "D+", "credit": 7},
        'tll101': {'grade': "A-", "credit": 4}
    },
    'cenk': {
        'cs101': {'grade': "B+", "credit": 5},
        'eng101': {'grade': "C+", "credit": 4},
        'mat103': {'grade': "A-", "credit": 6},
        'phys101': {'grade': "D", "credit": 7},
        'tll101': {'grade': "F", "credit": 4}
    }
}


# This function converts letter grades to number grades
def conv_letter_to_grade():
    for name in term_results:
        for course in term_results[name]:
            letter_grade = term_results[name][course]['grade']
            for grade in grades:
                if letter_grade == grade:
                    term_results[name][course]['grade'] = grades[grade]


# This function calculates the GPA for each person and printing the result
def calculateGPA():
    for name in term_results:
        total_points = 0
        total_credit = 0
        for course in term_results[name]:
            total_points += term_results[name][course]['grade'] * term_results[name][course]['credit']
            total_credit += term_results[name][course]['credit']
        GPA = total_points / total_credit
        print(f"{name}'s GPA is {GPA}")


# calling the functions
conv_letter_to_grade()
calculateGPA()