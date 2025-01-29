MIN_MARK = 2
MAX_MARK = 5

class Student:

    def __init__(self, student_name, subject):
        self.student_name = student_name
        self.student_marks = {subject: []}

    def student_get_mark(self, subject, mark):
        if MIN_MARK <= mark <= MAX_MARK:
            self.student_marks[subject].append(mark)
        else:
            raise ValueError('Невалидная оценка')

    def student_add_subject(self, subject):
        self.student_marks.update({subject: []})

    def show_student_name(self):
        print(self.student_name)
        return self.student_name

    def show_student_marks(self):
        print(self.student_marks)
        return self.student_marks


class PaymentStudent(Student):
    def __init__(self, student_name, subject, year_pay):
        super().__init__(student_name, subject)
        self.year_pay = year_pay

    def add_pay(self, new_year_pay):
        self.year_pay = new_year_pay
