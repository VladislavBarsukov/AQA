from .student import Student


class PaymentStudent(Student):
    def __init__(self, student_name, subject, year_pay):
        super().__init__(student_name, subject)
        self.year_pay = year_pay

    def add_pay(self, new_year_pay):
        self.year_pay = new_year_pay
