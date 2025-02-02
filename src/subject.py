from enum import StrEnum


class AvailableSubjects(StrEnum):
    MATH = "math"
    LANGUAGE = "language"
    CHEMISTRY = "chemistry"
    PHYSIC = "physic"
    HISTORY = "history"
    GEOMETRY = "geometry"


class Subject:

    def __init__(self, subject_name, subject_hours, teacher_name):
        self.subject_name = AvailableSubjects(subject_name)
        self.subject_teachers = [teacher_name]
        self.subject_hours = subject_hours

    def add_teacher_to_subject(self, subject_name):
        self.subject_teachers.append(subject_name)

    def add_hours(self, hours):
        self.subject_hours += hours
