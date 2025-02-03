class Student:
    MIN_MARK = 2
    MAX_MARK = 5

    def __init__(self, student_name, subject):
        self.student_name = student_name
        self.student_marks = {subject: []}

    def set_mark(self, subject, mark):
        if mark < self.MIN_MARK or mark > self.MAX_MARK:
            raise ValueError('Невалидная оценка. Доступные оценки: 2, 3, 4, 5')
        self.student_marks[subject].append(mark)

    def student_add_subject(self, subject):
        self.student_marks.update({subject: []})

    def get_student_name(self):
        return self.student_name

    def get_student_marks(self):
        return self.student_marks
