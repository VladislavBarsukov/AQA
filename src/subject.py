from enum import Enum

class AvailableSubjects(Enum):
    MATH = "math"
    LANGUAGE = "language"
    CHEMISTRY = "chemistry"
    PHYSIC = "physic"
    HISTORY = "history"
    GEOMETRY = "geometry"

    @classmethod
    def get_all_subjects(cls):
        return [subject.value for subject in cls]

    @classmethod
    def validate_subject(cls, subject):
        if subject not in cls.get_all_subjects():
            raise ValueError(f'Предмет недоступен. Доступные предметы: {", ".join(cls.get_all_subjects())}')
        return subject


class Subject:

    def __init__(self, subject, subject_hours, teacher_name):
        self.subject_name = AvailableSubjects.validate_subject(subject)
        self.subject_teachers = [teacher_name]
        self.subject_hours = subject_hours

    def add_teacher_to_subject(self, subject_name):
        self.subject_teachers.append(subject_name)

    def add_hours(self, hours):
        self.subject_hours += hours