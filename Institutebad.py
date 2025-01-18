from faker import Faker

class Subject:
    available_subjects = ['math', 'language', 'chemistry', 'physic', 'history', 'geometry']

    def __init__(self, subject, subject_hours, teacher_name):
        if subject not in self.available_subjects:
            raise ValueError('Предмет недоступен')
        self.subject_name = subject
        self.subject_teachers = [teacher_name]
        self.subject_hours = subject_hours

    def add_teacher_to_subject(self, subject_name):
        self.subject_teachers.append(subject_name)

    def add_hours(self, hours):
        self.subject_hours += hours


class Teacher:
    def __init__(self, teacher_name, teacher_subject, rank='Professor', payment=40000, work_hours=160):
        self.teacher_name = teacher_name
        self.teacher_subjects = [teacher_subject]
        self.payment = payment
        self.rank = rank
        self.work_hours = work_hours

    def add_teachers_subject(self, subject):
        self.teacher_subjects.append(subject)

    def add_payment(self, payment):
        self.payment+=payment

    def teacher_teach(self, teach_hours):
        self.work_hours -=teach_hours


class Student:
    def __init__(self,  student_name, subject):
        self.student_marks = {student_name: {subject: []}}
        self.student_name = student_name

    def student_get_mark(self, student_name, subject, mark):
        if 2 <= mark <= 5:
            self.student_marks[student_name][subject].append(mark)
        else:
            raise ValueError('Невалидная оценка')

    def student_add_subject(self, student_name, subject):
        self.student_marks[student_name][subject] = []

class PaymentStudent(Student):
    def __init__(self, student_name, subject, year_pay):
        super().__init__(student_name, subject)
        self.year_pay = year_pay

    def add_pay(self, new_year_pay):
        self.year_pay = new_year_pay


fake = Faker("ru_RU")

teacher_1=Teacher(fake.name(), 'math')
print(teacher_1.teacher_name, teacher_1.teacher_subjects, teacher_1.work_hours, teacher_1.payment)
teacher_1.add_teachers_subject('geometry')
teacher_1.teacher_teach(40)
teacher_1.add_payment(5000)
print(teacher_1.teacher_name, teacher_1.teacher_subjects, teacher_1.work_hours, teacher_1.payment)

print()

new_subject = Subject('geometry', 40, teacher_1.teacher_name)
print(new_subject.subject_teachers, new_subject.subject_hours, new_subject.subject_name)
new_subject.add_teacher_to_subject(fake.name_female())
new_subject.add_hours(5)
print(new_subject.subject_teachers, new_subject.subject_hours, new_subject.subject_name)

print()

student_1=Student(fake.name(), 'math')
print(student_1.student_name, student_1.student_marks)
student_1.student_add_subject(student_1.student_name, 'physic')
student_1.student_get_mark(student_1.student_name,'math', 5)
student_1.student_get_mark(student_1.student_name,'math', 2)
student_1.student_get_mark(student_1.student_name,'physic', 3)
print(student_1.student_name, student_1.student_marks)

print()

student_2=PaymentStudent(fake.name_male(), new_subject.subject_name, 100000)
print(student_2.student_name, student_2.student_marks, student_2.year_pay)
student_2.student_add_subject(student_2.student_name, new_subject.subject_name)
student_2.student_get_mark(student_2.student_name,new_subject.subject_name, 4)
student_2.add_pay(104990)
print(student_2.student_name, student_2.student_marks, student_2.year_pay)