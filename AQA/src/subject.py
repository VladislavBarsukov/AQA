class Subject:
    available_subjects = ['math', 'language', 'chemistry',
                          'physic', 'history', 'geometry']

    def __init__(self, subject, subject_hours, teacher_name):
        if subject not in self.available_subjects:
            raise ValueError('Предмет недоступен. Доступные предметы: math, '
                             'language, chemistry, physic, history, geometry')
        self.subject_name = subject
        self.subject_teachers = [teacher_name]
        self.subject_hours = subject_hours

    def add_teacher_to_subject(self, subject_name):
        self.subject_teachers.append(subject_name)

    def add_hours(self, hours):
        self.subject_hours += hours
