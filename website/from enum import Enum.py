from enum import Enum

class GenderEnum(Enum):
    Male = "Male"
    Female = "Female"

class Student:
    def _init_(self, name, age, is_enrolled, gpa, gender):
        self.name = name
        self.age = age
        self.is_enrolled = is_enrolled
        self.gpa = gpa
        self.gender = gender

    def display_student_info(self):
        print(f"{self.name}, {self.age} years old")
        self.display_enrollment_status()
        self.display_gender_pronoun()
        print(f"He/She has achieved a GPA of {self.gpa} in the last semester")

    def display_enrollment_status(self):
        enrollment_status = "enrolled" if self.is_enrolled else "not enrolled"
        print(f"{'' if self.is_enrolled else 'not '}{'yes' if self.is_enrolled else 'no'} {self.gender.value} is {enrollment_status}")

    def display_gender_pronoun(self):
        pronoun = "he" if self.gender == GenderEnum.Male else "she"
        print(f"{pronoun.capitalize()}")


def get_user_input():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    is_enrolled = input("Is the student enrolled? (yes/no): ").lower() == 'yes'
    gpa = float(input("Enter student GPA: "))
    gender = get_gender_input()
    
    return Student(name, age, is_enrolled, gpa, gender)

def get_gender_input():
    gender_input = input("Enter student gender (Male/Female): ").capitalize()
    return GenderEnum[gender_input]

def main():
    student = get_user_input()
    student.display_student_info()

if _'name_' == main:
    main()