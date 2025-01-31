class StudentGroup:

    def __init__(self, teacher, *group):
        self.teacher = teacher
        self.group = [*group]

    def add_to_group(self, student):
        self.group.append(student)

    def remove_from_group(self, student):
        self.group.remove(student)

    def change_teacher(self, teacher):
        self.teacher = teacher

    def get_mark_to_student_from_group(self, student_name, subject, mark):
        for student in self.group:
            if student.student_name == student_name:
                student.get_mark(subject, mark)
                break

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.group):
            student = self.group[self.index]
            self.index += 1
            return student
        raise StopIteration
