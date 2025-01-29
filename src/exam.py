import datetime, json
from datetime import datetime, timedelta


class Exam:
    def __init__(self, teacher, student_group, subject, ticket_group):
        self.teacher = teacher
        self.student_group = student_group
        self.subject = subject
        self.ticket_group = ticket_group
        self.end_time = None
        self.teacher_and_subject = {"Teacher:": teacher, "Subject:": subject}
        self.student_and_marks = {}
        self.exam_running = False

    def start_exam(self, len_time=120):
        self.exam_running = True
        current_time = datetime.now().time()
        current_datetime = datetime.now()
        self.end_time = datetime.combine(current_datetime.date(), current_time) + timedelta(minutes=len_time)

    def is_exam_running(self):
        if datetime.now().time() < self.end_time.time() and self.exam_running == True:
            return True
        else:
            return False

    def end_exam(self):
        self.exam_running = False
        return 'Экзамен закончен'

    def teacher_set_marks(self, student_name, subject, mark):
        if self.is_exam_running():
            self.student_group.student_from_group_get_mark(student_name, subject, mark)
            if student_name not in self.student_and_marks:
                self.student_and_marks.update({student_name: [mark]})
            else:
                self.student_and_marks[student_name].append(mark)

    def student_get_random_ticket(self):
        if self.is_exam_running():
            ticket = self.ticket_group.get_random_ticket()
            return ticket

    def get_exam_result(self):
        self.teacher_and_subject.update(self.student_and_marks)
        with open('data.json', 'w') as f:
            json.dump(self.teacher_and_subject, f)
        return self.student_and_marks
