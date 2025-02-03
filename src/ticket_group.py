import random


class NoTicketsException(ValueError):
    """Исключение для случая, когда в группе нет билетов."""
    pass


class TicketCollection:

    def __init__(self, *tickets):
        self.ticket_group = list(tickets)
        self.full_ticket_group = list(tickets)

    def get_group(self):
        return self.ticket_group

    def __len__(self):
        return len(self.ticket_group)

    def __str__(self):
        result = "Список билетов:\n"
        for i in range(len(self.ticket_group)):
            result += f"Предмет: {self.ticket_group[i].subject}\nВопросы: {self.ticket_group[i].questions}\n"
        return result

    def remove_from_group(self, ticket):
        self.ticket_group.remove(ticket)

    def add_to_group(self, ticket):
        self.ticket_group.append(ticket)

    def get_random_ticket(self):
        if not self.ticket_group:
            raise NoTicketsException("В группе нет билетов.")
        ticket = random.choice(self.ticket_group)
        ticket_show = ticket.show_ticket()
        self.ticket_group.remove(ticket)
        return ticket_show
