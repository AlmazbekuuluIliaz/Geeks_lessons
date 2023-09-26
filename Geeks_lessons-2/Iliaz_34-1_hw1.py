class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"fullname: {self.fullname}, age: {self.age}, married: {self.is_married}")

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        total_marks = sum(self.marks.values())
        num_subjects = len(self.marks)
        return total_marks / num_subjects

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, base_salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus_percentage = max(0, (self.experience - 3) * 5)
        bonus = (bonus_percentage / 100) * self.base_salary
        return self.base_salary + bonus

def create_students():
    stud1 = Student("Ильяз", 18, False, {"Мат": 90, "Англ": 85, "Гео": 78})
    stud2 = Student("Ислам", 17, False, {"Мат": 88, "Англ": 92, "Гео": 76})
    stud3 = Student("Ибадат", 19, False, {"Мат": 94, "Англ": 89, "Гео": 80})
    studs = [stud1, stud2, stud3]
    return studs

students_list = create_students()
for student in students_list:
    student.introduce_myself()
    print(f"Marks: {student.marks}")
    avg_mark = student.calculate_average_mark()
    print(f"Average Mark: {avg_mark:.2f}\n")

teacher = Teacher("Жанара эжеке", 45, True, 5, 50000)

teacher.introduce_myself()
print(f"Experience: {teacher.experience} years")
print(f"Base Salary: ${teacher.base_salary}")
salary = teacher.calculate_salary()
print(f"Calculated Salary: ${salary:.2f}")
