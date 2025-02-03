import datetime, json
from datetime import datetime, timedelta


class Exam:
    LEN_TIME = 120
    EXAM_RESULT = 'data.json'

    def __init__(self, teacher, student_group, subject, ticket_group):
        self.teacher = teacher
        self.student_group = student_group
        self.subject = subject
        self.ticket_group = ticket_group
        self.end_time = None
        self.student_and_marks = {}
        self.exam_running = False

    def start_exam(self, len_time=LEN_TIME):
        self.exam_running = True
        current_datetime = datetime.now()
        self.end_time = current_datetime + timedelta(minutes=len_time)

    def is_exam_running(self):
        return datetime.now() < self.end_time and self.exam_running

    def __contains__(self, item):
        if item == self.teacher.teacher_name:
            return item in self.student_group.teacher.teacher_name
        elif item == self.subject.subject_name:
            return item in self.teacher.teacher_subjects
        return False

    def end_exam(self):
        self.exam_running = False

    def teacher_set_marks(self, student_name, subject, mark):
        if not self.is_exam_running():
            return None
        self.student_group.set_mark_to_student_from_group(student_name, subject, mark)
        if student_name not in self.student_and_marks:
            self.student_and_marks.update({student_name: [mark]})
        else:
            self.student_and_marks[student_name].append(mark)

    def student_get_random_ticket(self):
        for _ in self.ticket_group:
            if self.is_exam_running():
                ticket = self.ticket_group.get_random_ticket()
                yield ticket

    def get_exam_result(self):
        self.student_and_marks.update({"Teacher:": self.teacher.teacher_name, "Subject:": self.subject.subject_name})
        with open(self.EXAM_RESULT, 'w', encoding='utf-8') as f:
            json.dump(self.student_and_marks, f, ensure_ascii=False, indent=2)
        return self.student_and_marks
