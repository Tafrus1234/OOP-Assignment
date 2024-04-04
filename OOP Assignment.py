class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class Section:
    def __init__(self, section_name):
        self.section_name = section_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print(f"Students in {self.section_name}:")
        for student in self.students:
            print(student)

class Class:
    def __init__(self, class_name):
        self.class_name = class_name
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

    def display_sections(self):
        print(f"Sections in {self.class_name}:")
        for section in self.sections:
            section.display_students()

# Example usage:
student1 = Student("Ali", 15, 10)
student2 = Student("Hadi", 16, 11)
student3 = Student("Ahmad", 14, 9)

section1 = Section("A")
section1.add_student(student1)
section1.add_student(student2)

section2 = Section("B")
section2.add_student(student3)

class1 = Class("Math")
class1.add_section(section1)
class1.add_section(section2)

class1.display_sections()