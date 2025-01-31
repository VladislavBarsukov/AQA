class Teacher:
    DEFAULT_RANK = 'Professor'
    DEFAULT_PAYMENT = 40000
    DEFAULT_WORK_HOURS = 160
    def __init__(self, teacher_name, teacher_subject,
                 rank=DEFAULT_RANK, payment=DEFAULT_PAYMENT, work_hours=DEFAULT_WORK_HOURS):
        self.teacher_name = teacher_name
        self.teacher_subjects = [teacher_subject]
        self.payment = payment
        self.rank = rank
        self.work_hours = work_hours

    def __len__(self):
        return len(self.teacher_name)

    def add_teachers_subject(self, subject):
        self.teacher_subjects.append(subject)

    def add_payment(self, payment):
        self.payment += payment

    def teacher_teach(self, teach_hours):
        self.work_hours -= teach_hours