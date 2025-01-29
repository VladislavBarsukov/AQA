class Ticket:

    def __init__(self, subject, question, subscribed=False):
        self.subject = subject
        self.questions = {'1': question}
        self.subscribed = subscribed

    def add_question_to_ticket(self, question):
        self.questions[len(self.questions) + 1] = question

    def change_question_in_ticket(self, number, question):
        self.questions[number] = question

    def subscribe_ticket(self):
        self.subscribed = True

    def show_ticket(self):
        return {"Тема:": self.subject,
                "Вопросы:": self.questions}
