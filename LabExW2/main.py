# Question 1
name = input("What's your name?: ")
print(" /\_/\ ")
print("/ o o \ ")
print("\  ~  /")
print(f"Hello {name}!")

# Question 2
s0 = float(input("s0= "))
v0 = float(input("v0= "))
a = float(input("a= "))
t = float(input("t= "))
S = s0 + (v0 * t) + (1 / 2 * a * (t ** 2))
print(f"Result is {S}")

# Question 3
district_rents = {
    'tasdelen': 2600,
    'cekmekoy': 3000,
    'uskudar': 3600,
    'kadikoy': 4000
}

# calculating rents with aidat
district_rents_with_aidat = {}
for district in district_rents:
    rent = district_rents[district]
    new_rent = rent + rent / 10
    district_rents_with_aidat[district] = new_rent

# printing results
for district in district_rents_with_aidat:
    each_person = district_rents_with_aidat[district] / 3
    print(f"{district}: {each_person}")

# Question 4
grades = {
    'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
    'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D': 1.0, 'F': 0
}
term_results = {
    'canan': {
        'cs101': {'grade': "A", "credit": 6},
        'eng101': {'grade': "B-", "credit": 4},
        'mat103': {'grade': "C+", "credit": 6},
        'phys101': {'grade': "D+", "credit": 8},
        'tll101': {'grade': "A-", "credit": 4}
    },
    'akin': {
        'cs101': {'grade': "B+", "credit": 6},
        'eng101': {'grade': "C", "credit": 4},
        'mat103': {'grade': "A-", "credit": 6},
        'phys101': {'grade': "D", "credit": 8},
        'tll101': {'grade': "A", "credit": 4}
    }
}

# convert letter grades to values
for name in term_results:
    for course in term_results[name]:
        letter_grade = term_results[name][course]['grade']
        for grade in grades:
            if letter_grade == grade:
                term_results[name][course]['grade'] = grades[grade]
# calculating GPA for each person and printing the result
for name in term_results:
    total_points = 0
    total_credit = 0
    GPA = 0
    for course in term_results[name]:
        total_points += term_results[name][course]['grade'] * term_results[name][course]['credit']
        total_credit += term_results[name][course]['credit']
    GPA = total_points / total_credit
    print(f"{name}'s GPA is {GPA}")
