import datetime, time
from faker import Faker

from src.student import Student, PaymentStudent
from src.subject import Subject
from src.teacher import Teacher
from src.student_group import StudentGroup
from src.exam import Exam
from src.ticket import Ticket
from src.ticket_group import TicketCollection

if __name__ == '__main__':

    fake = Faker("ru_RU")

    teacher_1 = Teacher(fake.name(), 'math')
    teacher_31 = Teacher(fake.name(), 'math')
    print(teacher_1.teacher_name, teacher_1.teacher_subjects,
          teacher_1.work_hours, teacher_1.payment)
    teacher_1.add_teachers_subject('geometry')
    teacher_1.teacher_teach(40)
    teacher_1.add_payment(5000)
    print(teacher_1.teacher_name, teacher_1.teacher_subjects,
          teacher_1.work_hours, teacher_1.payment)

    print()
    subject_math = Subject('math', 40, teacher_1.teacher_name)
    new_subject = Subject('geometry', 40, teacher_1.teacher_name)
    print(new_subject.subject_teachers, new_subject.subject_hours,
          new_subject.subject_name)
    new_subject.add_teacher_to_subject(fake.name_female())
    new_subject.add_hours(5)
    print(new_subject.subject_teachers, new_subject.subject_hours,
          new_subject.subject_name)

    print()

    student_1 = Student(fake.name(), 'math')
    print(student_1.student_name, student_1.student_marks)
    student_1.student_add_subject('physic')
    student_1.get_mark('math', 5)
    student_1.get_mark('math', 2)
    student_1.get_mark('physic', 3)
    print(student_1.student_name, student_1.student_marks)

    print()

    student_2 = PaymentStudent(fake.name_male(), new_subject.subject_name, 100000)
    print(student_2.student_name, student_2.student_marks, student_2.year_pay)
    student_2.student_add_subject(new_subject.subject_name)
    student_2.get_mark(new_subject.subject_name, 4)
    student_2.add_pay(104990)
    print(student_2.student_name, student_2.student_marks, student_2.year_pay)

    print()

    stud_1 = Student('Mark', 'math')
    stud_2 = Student('Ben', 'math')
    student_group = StudentGroup(teacher_1, stud_1, stud_2)
    print('++++++++++++++++++++++++++++++++++++++++++')
    for student in student_group:
        print(f"Студент: {student.student_name}")
    print('++++++++++++++++++++++++++++++++++++++++++')

    a = Ticket('math', '2*4')
    b = Ticket('math', "7/0")
    b2 = Ticket('math', "2-4")
    b3 = Ticket('math', "2+2")
    b4 = Ticket('math', "3+5")
    b5 = Ticket('math', "3+5")
    ticket_group = TicketCollection(a, b, b2, b3, b4)
    print('---------------------')
    print(ticket_group.get_random_ticket())
    print(ticket_group.get_random_ticket())
    print(ticket_group.get_random_ticket())
    print(ticket_group.get_random_ticket())
    print(ticket_group.get_random_ticket())
    #print(ticket_group.get_random_ticket())
    #print(ticket_group.get_random_ticket())

    print('---------------------')
    n = Exam(teacher_1.teacher_name, student_group, subject_math.subject_name, ticket_group)
    print('---------------------')
    n.start_exam()
    for i in range(3):
        time.sleep(1)
        print(n.is_exam_running())
        print(datetime.datetime.now())
        print(n.end_time)

    n.teacher_set_marks("Mark", "math", 3)
    n.teacher_set_marks("Mark", "math", 3)
    n.teacher_set_marks("Ben", "math", 5)
    n.teacher_set_marks("Ben", "math", 5)
    n.teacher_set_marks("Ben", "math", 5)
    stud_1.show_student_marks()
    stud_2.show_student_marks()
    print(n.student_and_marks)
    n.get_exam_result()

    for i in student_group:
        print(i.student_name)