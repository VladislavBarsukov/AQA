import random


class NoTicketsException(Exception):
    """Исключение для случая, когда в группе нет билетов."""
    pass


class TicketCollection:

    def __init__(self, *tickets):
        self.ticket_group = list(tickets)
        self.full_ticket_group = list(tickets)

    def show_group(self):
        for i in range(len(self.ticket_group)):
            print(self.ticket_group[i].subject)
            print(self.ticket_group[i].questions)

    def remove_from_group(self, ticket):
        self.ticket_group.remove(ticket)

    def add_to_group(self, ticket):
        self.ticket_group.append(ticket)

    def get_random_ticket(self):
        if not self.ticket_group:
            raise NoTicketsException("В группе нет билетов.")
        random_index = random.randint(0, len(self.ticket_group) - 1)
        ticket = self.ticket_group[random_index]
        ticket_show = ticket.show_ticket()
        self.ticket_group.remove(ticket)
        return ticket_show