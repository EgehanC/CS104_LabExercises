# Exercise 1
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def report(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


egehan = Student("Egehan", 19, "A")
efe = Student("Efe", 15, "B+")


def main1():
    egehan.report()
    efe.report()


# main1()

# Exercise 2
def new_student_attr():
    attr = []
    new_name = input("Name: ")
    new_age = int(input("Age: "))
    new_grade = input("Grade: ")
    while not 0 < new_age < 100:
        new_age = int(input("Please enter a valid age: "))
    return new_name, new_age, new_grade


def add_students():
    myStudentList = []
    add_new = True
    while add_new:
        new_student = new_student_attr()
        myStudentList.append(Student(new_student[0], new_student[1], new_student[2]))
        add_new = input("Add another student? y/n\n")
        if add_new != "y":
            add_new = False
    return myStudentList


def get_student(student_list):
    print(f"\nNumber of students: {len(student_list)}")
    wanted_student = int(input("Retrieve nth student: n = "))
    while not 1 <= wanted_student <= len(student_list):
        wanted_student = int(input("Please enter a valid index: "))
    student_list[wanted_student-1].report()


get_student(add_students())
