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
    def __init__(self, name, age, gender, Id, course):
        super().__init__(name, age, gender)
        self.Student_id = Id
        self.course = course
        self.grades = []
    def set_student_details(self):
        super().set_details()
        self.Student_id = input("What is their id?: ")
        self.course = input("What subject do they study?: ")
    def add_grade(self):
        grade = int(input("What grade are you adding?: "))
        self.grades.append(grade)
    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades)
    def get_student_summary(self):
        super().get_details()
        av = self.calculate_average_grade()
        print(f"""
Student id: {self.Student_id}
student's course: {self.course}
student's grade average: {av}""")
    def get_mentor(self, professor):
        if self.name in professor.teach:
            print(f"{self.name} is getting mentoored by {professor.name}")
        else:
            print(f'{self.name} has no mentoor')

class professor(person):
    def __init__(self, name, age, gender, staff_id, department, salary):
        super().__init__(name, age, gender)
        self.staffid = staff_id
        self.department = department
        self.salary = salary
        self.teach = []
    def set_professor_details(self):
        super().set_details()
        self.staffid = input("What is their id?: ")
        self.department = input("What subject do they teach?: ")
        self.salary = input("What is their salary?: ")
    def give_feedback(self, student, feedback):
        print(f"Feed back for {student}: {feedback}")
    def get_professor_summary(self):
        super().get_details()
        print(f"""
ID: {self.staffid}
DEPARTMENT: {self.department}
salary: {self.salary}""")
    def mentor_student(self, student):
        print(f'Professor {self.name} is now mentooring {student.name} in {student.course}')
        (self.teach).append(student.name)
    def get_mentored_students(self):
        print(self.teach)
    def increase_salary(self):
        new_salary = int(self.salary) * 1.1
        print(f"{self.name}'s salary increased from {self.salary} into {new_salary}")
class administrator(person):
    def __init__(self, name, age, gender, admin_id, office, years_of_service):
        super().__init__(name, age, gender)
        self.adminid = admin_id
        self.office = office
        self.yos = years_of_service
    def set_admin_details(self):
        super().set_details()
        self.adminid = input("What is their id?: ")
        self.office = input("What office are they in: ")
        self.yos = int(input("How many years of service?: "))
    def increment_service_years(self):
        self.yos += 1
        print(f'1 year of service added!!!!!')
    def get_admin_summary(self):
        super().get_details()
        print(f"""
ID: {self.adminid}
office: {self.office}
years of service: {self.yos}""")
        
a = professor('', '', '', '', '', '')
a.set_professor_details()
a.increase_salary()
a.get_professor_summary()
b = Student('', '', '', '', '')
b.set_student_details()
b.add_grade()
b.add_grade()
b.add_grade()
b.get_student_summary()
d = Student('', '', '', '', '')
d.set_student_details()
d.add_grade()
d.add_grade()
d.add_grade()
d.get_student_summary()
a.give_feedback(b.name, 'You need to get better at school buddy')
a.give_feedback(d.name, 'Nerd')
c = administrator('', '', '', '', '', '')
c.set_admin_details()
c.increment_service_years()
c.get_admin_summary()
a.mentor_student(b)
a.mentor_student(d)
b.get_mentor(a)
a.get_mentored_students()