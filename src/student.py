class Student:
    MIN_MARK = 2
    MAX_MARK = 5
    def __init__(self, student_name, subject):
        self.student_name = student_name
        self.student_marks = {subject: []}

    def get_mark(self, subject, mark):
        if mark<self.MIN_MARK or mark>self.MAX_MARK:
            raise ValueError('Невалидная оценка')
        self.student_marks[subject].append(mark)

    def student_add_subject(self, subject):
        self.student_marks.update({subject: []})

    def show_student_name(self):
        return self.student_name

    def show_student_marks(self):
        return self.student_marks


class PaymentStudent(Student):
    def __init__(self, student_name, subject, year_pay):
        super().__init__(student_name, subject)
        self.year_pay = year_pay

    def add_pay(self, new_year_pay):
        self.year_pay = new_year_pay