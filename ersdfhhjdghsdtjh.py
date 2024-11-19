class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_details(self):#
        self.name = input("What is their name: ")
        self.age = input("How old are they: ")
        self.gender = input("What gender do they identify as: ")
    
    def get_details(self):
        print(f"""
Name: {self.name}
Age: {self.age}
gender: {self.gender}""")

class Student(person):
    def __init__(self, name, age, gender, Id, course, grades):
        super().__init__(self, name, age, gender)
        self.Student_id = Id
        self.course = course
        self.grades = []
    def set_student_details(self):
        super().set_details()
        self.Student_id = input("What is their id?: ")
        self.course = input("What subject do they study?: ")
    def add_grade(self):
        grade = input("What grade are you adding?: ")
        self.grades.append(grade)
    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades)
    def get_student_summary(self):
        super().get_details()
        av = self.calculate_average_grade()
        print(f"""
Student id: {self.Student_id}
student's course: {self.course}
student's grade average: {av}""" )








